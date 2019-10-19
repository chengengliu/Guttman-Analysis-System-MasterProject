import sys

from flask import Flask, send_from_directory, request
from .model.excel_processing.ExcelOutput import ExcelOutput
from .model import storage, file_importing, guttman_analysis
from werkzeug.utils import secure_filename

app = Flask(__name__, static_url_path='')


@app.route('/export/<int:file_id>')
def export(file_id):
    file_dir, file_name = storage.get_export_path(file_id)
    return send_from_directory(file_dir, file_name, as_attachment=True, attachment_filename=file_name)


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return {'err_msg': 'No file part'}
    file_name = request.files['file']
    if file_name.filename == '':
        return {'err_msg': 'No selected file'}
    if file_name and storage.allowed_file(file_name.filename):
        filename = secure_filename(file_name.filename)
        file_id, path, mod_path = storage.make_new_path(filename)
        result = {
            'file_id': file_id,
            'export_url': '/export/' + str(file_id)
        }

        try:
            file_name.save(path)
            data, index = file_importing.readfile(path)
            data = file_importing.transpose(data)
            new_data = file_importing.break_down_marks(data, index)
            file_importing.sort_2d_array_mark(new_data)
            print("This is the new data", new_data)
            matrix = guttman_analysis.clean_input(new_data)
            print(matrix)
            print("this is the matrix !!!!!!!!!!!!!")
            for i in matrix:
                print(i)
            flag = 'Accumulation'  # Similarity, Correlation, Accumulation
            corr_item = guttman_analysis.return_correlation(matrix, False, flag)
            irregular_item = guttman_analysis.return_irregular_index_test2(matrix, False, flag)
            irregular_student = guttman_analysis.return_irregular_index_test2(matrix, True, flag)
            print(new_data)

            excel = ExcelOutput(new_data, mod_path)
            excel.write_excel()
            print("Irregular item list is: ",irregular_item)
            for col in irregular_item:
                print("Column is: ", col)
                excel.highlight_area(0, 0, col + 1, col + 1, '#95e1d3')
            for row in irregular_student:
                print("Row is : ", row)
                excel.highlight_area(row + 2, row + 2, 0, 0, '#f9ed69')
            excel.add_total_score()
            print(corr_item)
            excel.add_correlation(corr_item, 'column')

            boxes = guttman_analysis.irregular_box(matrix)
            boxes_json = []
            for i in boxes:
                col1, col2, rows = i
                row1, row2 = rows
                excel.add_border(row1 + 2, row2 + 2, col1 + 1, col2 + 1)
                boxes_json.append({
                    'row_range': [row1 + 2, row2 + 2],
                    'column_range': [col1 + 1, col2 + 1]
                })

            content_list = []

            for i in range(len(new_data)):
                if i == 0:
                    tail = "total"
                else:
                    tail = "total" if i == 1 else sum(new_data[i][1:])
                content_list.append({
                    new_data[i][0]: new_data[i][1:]
                })
                print(content_list[i], i, new_data[i][0])
                content_list[i][new_data[i][0]].append(tail)
            content_list.append({
                'total': guttman_analysis.sumItemScore(matrix)
            })
            odd_cells = guttman_analysis.odd_cells(matrix)
            odd_cells_str_tuple = []
            for (r, c) in odd_cells:
                excel.highlight_area(r + 2, r + 2, c + 1, c + 1, '#b063c5')
                odd_cells_str_tuple.append("(%d, %d)" % (c, r+1))

            json = {
                'file_id': file_id,
                'file_name': filename,
                'export_url': '/export/' + str(file_id),
                'irregular_student': [new_data[i + 2][0] for i in irregular_student],
                'irregular_item': [new_data[0][i + 1] for i in irregular_item],
                'item_performance': corr_item,
                'content': content_list,
                'boxes': boxes_json,
                'odd_cells': odd_cells_str_tuple
            }
            storage.save_result(json, file_id)
            excel.close_workbook()
        except IOError as e:
            storage.delete_file(file_id)
            return {'err_msg': str(e)}
        return result
    else:
        return {'err_msg': 'Illegal file extension'}


@app.route('/filelist', methods=['GET'])
def file_list():
    return {'file_list': storage.get_file_list()}


@app.route('/delete/<int:file_id>', methods=['GET'])
def delete_file(file_id):
    storage.delete_file(file_id)
    return {}


@app.route('/result/<int:file_id>', methods=['GET'])
def get_result(file_id):
    return storage.get_result(file_id)


@app.route('/')
def index():
    return app.send_static_file('index.html')
