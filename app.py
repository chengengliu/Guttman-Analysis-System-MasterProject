from flask import Flask, send_from_directory, request

from .model.excel_processing.ExcelOutput import ExcelOutput
from .model import storage, file_importing
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
        file_name.save(path)
        result = {
            'file_id': file_id,
            'file_url': '/export/' + str(file_id)
        }
        data = file_importing.readfile(path)
        print(data)
        data = file_importing.transpose(data)
        print(data)
        file_importing.sort_2d_array(data)
        print(data)
        for j in data:
            print(j)

        """
        create an instance of exceloutput class
        """
        excel = ExcelOutput(data, mod_path)
        """
        write 2d array data to 
        """
        excel.write_excel()
        """
        highlight anomaly area by painting the background color
        """
        excel.highlight_area(2, 4, 2, 4, 'lime')
        excel.add_border(2, 4, 2, 4)
        """
        store total score of each row and column to the excel file, note it's not to the array
        """
        excel.add_total_score()
        """
        correlation values should be received from Victor's module
        """
        correlation1 = range(1, 41)
        correlation2 = [11, 12, 13, 14, 15, 16, 17]
        """
        store correlation values to the excel, note it's not to array
        """
        excel.add_correlation(correlation1, 'row')
        excel.add_correlation(correlation2, 'column')
        #####################################################################################
        # the following function is crucial, it's the only way to close the file and export it
        #####################################################################################
        excel.close_workbook()
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


