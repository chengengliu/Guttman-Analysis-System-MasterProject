export const renderPopupWindow = (fileName, flag) => {

    let content;

    switch (flag) {
        case 'INVALID_EXTENSION':
            content = `
                <p class="text">The selected file <span>${fileName}</span> is invalid.</p>
                <p class="text">Please submit <span>.xls</span> or <span>.xlsx</span> file.</p>
            `;
            break;
        case 'INVALID_FORMAT':
            content = `
                <p class="text">The selected file <span>${fileName}</span> is invalid.</p>
                <p class="text">Please submit <span>Guttman Chart format</span> file.</p>
            `;
            break;
        default:
            content = `
                <p class="text">Sorry, upexpected error.</p>
            `;
    }

    const markup = `
        <div class="window">
            <div class="pop-up">
                <div class="pop-up-header">
                    <img src="./assets/warning.svg" alt="alert-icon">
                    <p class="text">WARNING</p>
                </div>
                <div class="pop-up-text">
                    ${content}
                </div>
                <div class="pop-up-button">
                    <button>Okay</button>
                </div>
            </div>
        </div>
    `
    document.querySelector('body').insertAdjacentHTML('afterbegin', markup);

    // close the dialog window
    document.querySelector('.pop-up-button').addEventListener('click', () => clearNode('.window'));
};

export const renderFileProcessing = () => {
    const markup = `
        <div class="file-container processing">
            <div class="loader">
                <img src="./assets/loader.svg" alt="loading-icon">
            </div>
            <img class="black-line" src="./assets/black-line.svg" alt="black-line">
            <div class="form2">
                <span class="text label-process">Processing...</span>
                <img class="processing-delete" src="./assets/close-window.svg" alt="close-icon">
            </div>
        </div>
    `;

    document.querySelector('.right-panel').insertAdjacentHTML('afterbegin', markup);
};


export const renderProcessDone = (fileID, fileName, downloadURL) => {

    const query = `?fileID=${fileID}`;

    const markup = `
        <div data-file-id=${fileID} class="file-container processed">
            <div data-file-id="${fileID}" class="file-description processed">
                <a href="./result.html${query}" class="file-description-link">
                    <h4 class="text">${limitFileName(fileName)}</h4>
                    <br>
                    <span class="text">The file has been processed</span>
                    <br>
                    <span class="text">Click to see results and feedback</span>
                </a>
            </div>
            <img class="black-line" src="./assets/black-line.svg" alt="black-line">
            <div class="form3">
                <a href="${downloadURL}" class="download-link" download>
                    <img class="download" src="./assets/download.svg" alt="download-icon">
                </a>
                <img data-file-id=${fileID} class="delete" src="./assets/close-window.svg" alt="close-icon"> 
            </div>
        </div>
    `;

    document.querySelector('.right-panel').insertAdjacentHTML('afterbegin', markup);
};

export const renderNewFileUpload = () => {
    const markup = `
        <div class="file-container new">
            <form class="form1" enctype="multipart/form-data" method="POST">
                <img class="upload" src="./assets/plus.svg" alt="add-file">
                <br>
                <span class="text label-new">New</span>
                <input class="import" type="file" name="file" accept=".xls, .xlsx" />
            </form>
            <img class="black-line" src="./assets/black-line.svg" alt="black-line">
            <form class="form2" enctype="multipart/form-data" method="POST">
                <img class="upload" src="./assets/upload.svg" alt="upload-file">
                <span class="text label-import">Import</span>
                <input class="import" type="file" name="file" accept=".xls, .xlsx" />
            </form>
        </div>
    `;
    document.querySelector('.right-panel').insertAdjacentHTML('beforeend', markup);
};

export const clearNode = className => {
    const element = document.querySelector(className);

    if (element.parentElement) {
        element.parentElement.removeChild(element);
    }
}

const limitFileName = fileName => {
    if (!fileName) return;

    const len = fileName.length;

    return len > 18 ? `${fileName.substring(0, 10)}.xlsx` : fileName;
};

