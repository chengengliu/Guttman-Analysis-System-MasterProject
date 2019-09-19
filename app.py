from flask import Flask, send_from_directory, request
from .model import storage
from werkzeug.utils import secure_filename

app = Flask(__name__, static_url_path='')


@app.route('/export/<int:file_id>')
def export(file_id):
    file_dir, file = storage.get_export_path(file_id)
    return send_from_directory(file_dir, file, as_attachment=True, attachment_filename=file)


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return {'err_msg': 'No file part'}
    file = request.files['file']
    if file.filename == '':
        return {'err_msg': 'No selected file'}
    if file and storage.allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_id, path = storage.make_new_path(filename)
        file.save(path)
        return {
            'file_id': file_id,
            'file_url': '/export/' + str(file_id)
        }


@app.route('/filelist', methods=['GET'])
def file_list():
    return {'file_list': storage.get_file_list()}

