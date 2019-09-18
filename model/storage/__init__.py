import os

if not os.path.exists('upload/'):
    os.mkdir('upload/')

def get_export_path(file_id):
    dir = get_base_dir(file_id) + 'mod/'
    for file in os.listdir(dir):
        if file.endswith(".xls") or file.endswith(".xlsx"):
            return (dir, file)  

def get_base_dir(file_id):
    return 'upload/' + str(file_id) + '/'
    
def make_new_path(name):
    last_id = 0
    for file in os.listdir('upload/'):
        last_id = int(file) if int(file) > last_id else last_id
    new_id = last_id + 1
    os.mkdir('upload/' + str(new_id))
    os.mkdir('upload/' + str(new_id) + '/ori/')
    os.mkdir('upload/' + str(new_id) + '/mod/')
    
    return new_id, 'upload/' + str(new_id) + '/ori/' + name

def allowed_file(name):
    return '.' in name and name.rsplit('.', 1)[1].lower() in ['xls', 'xlsx']
    
def get_file_list():
    list = []
    for dir in os.listdir('upload/'):
        for file in os.listdir('upload/' + dir + '/ori/'):
            if file.endswith(".xls") or file.endswith(".xlsx"):
                list.append({
                    'file_id': int(dir), 
                    'file_name': file,
                    'export_url': '/export/' + dir
                })
    return list