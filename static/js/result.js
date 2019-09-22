import * as resultView from './view/resultView.js';

const getProcessedResult = async fileID => {

    const url = `/result/${fileID}`;

    const response = await fetch(url, { method: 'GET' });
    const json = await response.json();

    return json;
};

const renderResult = async () => {

    const query = decodeURIComponent(window.location.search);
    const index = query.indexOf('=');
    const fileID = query.substring(index + 1);
    let processedData;

    // if the request file has not been processed before
    if (!localStorage.getItem(fileID)) {
        processedData = await getProcessedResult(fileID);  // should be a JSON object
        localStorage[fileID] = JSON.stringify(processedData);
    } else {
        processedData = JSON.parse(localStorage.getItem(fileID));
    }

    resultView.renderParsedResult(processedData);
};

window.onload = renderResult;