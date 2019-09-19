Array.prototype.Exists = function (v) {
    var b = false;
    for (var i = 0; i < this.length; i++) {
        if (this[i] === v) { b = true; break; }
    }
    return b;
};

const parseJSON = data => {
    let irregularStudent = data.irregular_student;
    let irregularItem = data.irregular_item;
    let boxs = data.boxes;
    let j = 0;
    let temp = "";
    for (let l = 0; l < data.content.length; l++) {
        let stu = Object.keys(data.content[l]).toString()
        j++;
        temp += "<tr>";
        if (irregularStudent.Exists(stu)) {
            temp += "<td  class='irregular-student'>" + stu + "</td>";
        } else {
            temp += "<td  >" + stu + "</td>";
        }

        for (let i = 0; i < data.content[l][stu].length; i++) {
            let class_ = "";

            for (let k = 0; k < boxs.length; k++) {
                if (j > boxs[k]["row_range"][0] && j <= boxs[k]["row_range"][1] + 1) {
                    if (i === boxs[k]["column_range"][0] - 1) {
                        class_ += " border-left";
                    }
                    if (i === boxs[k]["column_range"][1] - 1) {
                        class_ += " border-right";
                    }
                }

                if (i >= boxs[k]["column_range"][0] - 1 && i < boxs[k]["column_range"][1]) {
                    if (j === boxs[k]["row_range"][0] + 1) {
                        class_ += " border-top";
                    }
                    if (j === boxs[k]["row_range"][1] + 1) {
                        class_ += " border-bottom";
                    }
                }
            }

            if (l > 0 && data.content[l][stu][i] > 0 && (i !== data.content[l][stu].length - 1) && (stu !== "total")) {
                class_ += " greater-than-0";
            }
            else if (irregularItem.Exists(data.content[l][stu][i])) {
                class_ += " irregular-item"
            }

            temp += "<td class = \" " + class_ + "\" >" + data.content[l][stu][i] + "</td>";
        }
        temp += "</tr>";
    }
    return temp;
};

const renderLeftPanel = data => {

    const markup = `
        <div class="back-section">
            <a href="./index.html" class="back-link">
                <img src="./assets/back.svg" alt="back-icon">
                <span class="text">Back</span>
            </a>
        </div>
        <div class="export-section">
            <a href=${data.export_url} class="download-link" download>
                <img src="./assets/dl.svg" alt="export-icon">
                <span class="text">Export</span>
            </a>
        </div>
    `;

    document.querySelector('.left-panel').insertAdjacentHTML('afterbegin', markup);
};

/** This function is remained for dynamically render feedbacks in the future */
const renderFeedback = data => {
    const markup = `
        <div class="feedback-container">
            <div class="feedback-header">
                <p>Feedback</p>
            </div>
            <div class="feedback-body">
                <ul class="rule-list">
                    <li>
                        <span>Rule 1</span>
                        <p>Rule 1 says the rubric should be specific.</p>
                    </li>

                    <li>
                        <span>Rule 2</span>
                        <p>Rule 2 says the rubric should be specific.</p>
                    </li>

                    <li>
                        <span>Rule 3</span>
                        <p>Rule 3 says the rubric should be specific.</p>
                    </li>
                </ul>
            </div>
        </div>
    `;
    document.querySelector('.guttman-page-left').insertAdjacentHTML('afterbegin', markup);
};

const renderGuttmanChart = data => {
    const resultMarkup = parseJSON(data);

    document.querySelector('#data').insertAdjacentHTML('beforeend', resultMarkup);
};

export const renderParsedResult = data => {
    renderLeftPanel(data);
    renderFeedback(data);
    renderGuttmanChart(data);
};