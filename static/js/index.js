import * as fileView from './view/fileView.js';


// initial query to server asking for processed files
const init = async () => {

    //localStorage.clear();

    const jsonData = await initFetch(); // data should be an array of processed files

    jsonData.file_list.forEach(json => {
        localStorage[json.file_id] = JSON.stringify(json);
    });

    // render inital processed files
    for (let i = 0; i < localStorage.length; i++) {
        const value = localStorage.getItem(localStorage.key(i));
        const json = JSON.parse(value);

        fileView.renderProcessDone(json.file_id, json.file_name, json.export_url);
    }
};

const initFetch = async () => {

    const url = '/filelist';
    const response = await fetch(url, { method: 'GET' });
    const json = await response.json();

    return json;
};

window.onload = init;

const openDialog = () => document.querySelector('.import').click();

const validateFile = element => {
    const filePath = element.value;
    const file = element.files[0];

    // i enables both upper and lowercase
    const allowedExtensions = /(\.xls|\.xlsx)$/i;

    // if not a valid file, popup warning
    if (!allowedExtensions.exec(filePath)) {
        fileView.renderPopupWindow(file.name);
        // close the dialog window
        document.querySelector('.pop-up-button').addEventListener('click', () => fileView.clearNode('.window'));
    } else {
        // send the file to server
        uploadFile(file);
    }
};

const uploadFile = file => {
    /** <-- this should be replaced */
    const url = '/upload';

    const formData = new FormData();
    formData.append('file', file, file.name);

    const xhr = new XMLHttpRequest();

    xhr.upload.onloadstart = () => {
        fileView.clearNode('.file-container.new');
        fileView.renderFileProcessing();
    };

    xhr.onload = () => {
        if (xhr.status >= 200 && xhr.status < 400) {

            const fileID = JSON.parse(xhr.responseText).file_id;
            const downloadURL = JSON.parse(xhr.responseText).export_url;

            fileView.clearNode('.file-container.processing');
            fileView.renderProcessDone(fileID, file.name, downloadURL);
            fileView.renderNewFileUpload();

        } else {
            console.error(`error ${xhr.response}`);
        }
    };

    xhr.onerror = () => {
        console.log(`Network Error`);
    };

    xhr.open('POST', url, true);
    xhr.send(formData);
};

const deleteFile = (fileID, element) => {

    const url = `/delete/${fileID}`;

    fetch(url, { method: 'GET' })
        .then(response => response.json())
        .then(res => console.log(`Delete file: ${fileID} success. ${JSON.stringify(res)}`))
        .catch(error => console.error(`Delete error: ${error}`));

    // remove data and node
    if (localStorage.getItem(fileID)) localStorage.removeItem(fileID);
    if (element.dataset.fileId == fileID) element.remove();
};

document.querySelector('.right-panel').addEventListener('click', e => {

    if (e.target.matches('.upload, .upload *')) {
        openDialog();
    } else if (e.target.matches('.delete')) {
        const fileID = e.target.dataset.fileId;
        const element = e.target.closest('.file-container.processed');

        deleteFile(fileID, element);
    }
});

document.querySelector('.right-panel').addEventListener('change', e => {

    if (e.target.matches('.import, .import *')) validateFile(e.target);
});