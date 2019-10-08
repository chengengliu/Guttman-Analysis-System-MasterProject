import * as fileView from './view/fileView.js';


const INVALID_EXTENSION = 'INVALID_EXTENSION';
const INVALID_FORMAT = 'INVALID_FORMAT';
const INSTRUCTION = 'INSTRUCTION';

// initial query to server asking for processed files
const init = async () => {

    const jsonData = await initFetch(); // data should be an array of processed files

    // render inital processed files
    jsonData.file_list.forEach(json => {
        fileView.renderProcessDone(json.file_id, json.file_name, json.export_url);
    });

    // render instruction
    fileView.renderPopupWindow(undefined, INSTRUCTION); 
};

const initFetch = async () => {

    const url = '/filelist';
    const response = await fetch(url, { method: 'GET' });
    const json = await response.json();

    return json;
};

window.onload = init;

// const openDialog = () => document.querySelector('.import').click();

const validateFile = element => {
    const filePath = element.value;
    const file = element.files[0];

    // i enables both upper and lowercase
    const allowedExtensions = /(\.xls|\.xlsx)$/i;

    // if not a valid file, popup warning
    if (!allowedExtensions.exec(filePath)) {
        fileView.renderPopupWindow(file.name, INVALID_EXTENSION);
    } else {
        // send the file to server
        uploadFile(file);
    }
};

const uploadFile = file => {

    const url = '/upload';
    const formData = new FormData();
    const xhr = new XMLHttpRequest();

    formData.append('file', file, file.name);

    xhr.upload.onloadstart = () => {
        fileView.clearNode('.file-container.new');
        fileView.renderFileProcessing();

        document.querySelector('.processing-delete').addEventListener('click', () => {
            xhr.abort();
            fileView.clearNode('.file-container.processing');
            fileView.renderNewFileUpload();
        });
    };

    xhr.onload = () => {
        if (xhr.status >= 200 && xhr.status < 400) {

            // const isFormatValid = JSON.parse(xhr.responseText).file_format;   <------- TODO
            const isFormatValid = true;

            // if file format is valid
            if (isFormatValid === true) {
                const fileID = JSON.parse(xhr.responseText).file_id;
                const downloadURL = JSON.parse(xhr.responseText).export_url;
    
                fileView.clearNode('.file-container.processing');
                fileView.renderProcessDone(fileID, file.name, downloadURL);
                fileView.renderNewFileUpload();
            } else {
                fileView.renderPopupWindow(file.name, INVALID_FORMAT);
                fileView.clearNode('.file-container.processing');
                fileView.renderNewFileUpload();
            }
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
    // set the target to empty so that 'change' will fire even select the same file
    e.target.value = '';  
});

const openDialog = () => document.querySelector('.import').click();