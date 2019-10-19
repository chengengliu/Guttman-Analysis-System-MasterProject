import os
import shutil
import json

if not os.path.exists('upload/'):
    os.mkdir('upload/')


def get_export_path(file_id):
    file_dir = get_base_dir(file_id) + 'mod/'
    for file in os.listdir(file_dir):
        if file.endswith(".xls") or file.endswith(".xlsx"):
            return file_dir, file


def get_base_dir(file_id):
    return 'upload/' + str(file_id) + '/'


def make_new_path(name):
    last_id = 0
    for file in os.listdir('upload/'):
        if file.isnumeric():
            last_id = int(file) if int(file) > last_id else last_id
    new_id = last_id + 1
    os.mkdir('upload/' + str(new_id))
    os.mkdir('upload/' + str(new_id) + '/ori/')
    os.mkdir('upload/' + str(new_id) + '/mod/')
    
    return new_id, 'upload/' + str(new_id) + '/ori/' + name, 'upload/' + str(new_id) + '/mod/' + name


def allowed_file(name):
    return '.' in name and name.rsplit('.', 1)[1].lower() in ['xls', 'xlsx']


def get_file_list():
    file_list = []
    for file_id in os.listdir('upload/'):
        for file in os.listdir('upload/' + file_id + '/ori/'):
            if file.endswith(".xls") or file.endswith(".xlsx"):
                file_list.append(get_result(file_id, 0))
    return file_list


def delete_file(file_id):
    shutil.rmtree('upload/' + str(file_id), ignore_errors=True, onerror=None)


def get_result(file_id, pattern_id):
    with open('upload/' + str(file_id) + '/result_' + str(pattern_id) + '.json', 'r') as json_file:
        return json.load(json_file)


def save_result(json_dict, file_id, pattern_id):
    with open('upload/' + str(file_id) + '/result_' + str(pattern_id) + '.json', 'w') as json_file:
        json.dump(json_dict, json_file)
