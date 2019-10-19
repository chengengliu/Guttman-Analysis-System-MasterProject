import * as resultView from './view/resultView.js';

const getProcessedResult = async (fileID, typeID) => {

    // const url = `/result/${fileID}`;

    const url = `/result/${fileID}/pattern/${typeID}`;

    const response = await fetch(url, { method: 'GET' });
    const json = await response.json();

    return json;
};

const renderResult = async () => {

    const query = decodeURIComponent(window.location.search);
    const index1 = query.indexOf('=');
    const index2 = query.indexOf('=', index1 + 1);
    const fileID = query.substring(index1 + 1, index1 + 2);
    const typeID = query.substring(index2 + 1, index2 + 2);

    console.log(`fileID: ${fileID}`);
    console.log(`typeID: ${typeID}`);

    const processedData = await getProcessedResult(fileID, typeID);  // should be a JSON object

    resultView.renderParsedResult(typeID, processedData);
};

document.querySelector('.left-panel').addEventListener('click', e => {
    if (e.target.matches('.other-pattern, .other-pattern *')) {
        renderOtherPattern();
        console.log(`click`);
    }
});

window.onload = renderResult;