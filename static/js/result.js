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
    const processedData = await getProcessedResult(fileID);  // should be a JSON object

    resultView.renderParsedResult(processedData);
};

window.onload = renderResult;