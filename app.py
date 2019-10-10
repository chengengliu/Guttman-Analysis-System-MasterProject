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
            data = file_importing.readfile(path)
            data = file_importing.transpose(data)
            file_importing.sort_2d_array_max_mark(data)

            matrix = guttman_analysis.clean_input(data)

            flag = 'Accumulation'  # Similarity, Correlation, Accumulation
            corr_item = guttman_analysis.return_correlation(matrix, False, flag)
            irregular_item = guttman_analysis.return_irregular_index(matrix, False, flag)
            irregular_student = guttman_analysis.return_irregular_index(matrix, True, flag)

            excel = ExcelOutput(data, mod_path)
            excel.write_excel()

            for col in irregular_item:
                excel.highlight_area(0, 0, col + 1, col + 1, '#95e1d3')
            for row in irregular_student:
                excel.highlight_area(row + 1, row + 1, 0, 0, '#f9ed69')

            excel.add_total_score()
            excel.add_correlation(corr_item, 'column')

            boxes = guttman_analysis.irregular_box(matrix)
            boxes_json = []
            for i in boxes:
                col1, col2, rows = i
                row1, row2 = rows
                excel.add_border(row1 + 1, row2 + 1, col1 + 1, col2 + 1)
                boxes_json.append({
                    'row_range': [row1 + 1, row2 + 1],
                    'column_range': [col1 + 1, col2 + 1]
                })

            content_list = []

            for i in range(len(data)):
                tail = "total" if i == 0 else sum(data[i][1:])
                content_list.append({
                    data[i][0]: data[i][1:]
                })
                content_list[i][data[i][0]].append(tail)
            content_list.append({
                'total': guttman_analysis.sumItemScore(matrix)
            })
            odd_cells = guttman_analysis.odd_cells(matrix)
            odd_cells_str_tuple = []
            for (r, c) in odd_cells:
                excel.highlight_area(r + 1, r + 1, c + 1, c + 1, '#b063c5')
                odd_cells_str_tuple.append("(%d, %d)" % (c, r))

            json = {
                'file_id': file_id,
                'file_name': filename,
                'export_url': '/export/' + str(file_id),
                'irregular_student': [data[i + 1][0] for i in irregular_student],
                'irregular_item': [data[0][i + 1] for i in irregular_item],
                'item_performance': corr_item,
                'content': content_list,
                'boxes': boxes_json,
                'odd_cells': odd_cells_str_tuple
            }
            storage.save_result(json, file_id)
            excel.close_workbook()
        except:
            storage.delete_file(file_id)

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
