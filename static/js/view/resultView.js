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
    let odd_cells = data.odd_cells;
    let j = 0;
    let temp = "";

    let font_size = "";
    if ((data.content.length * data.content[0][Object.keys(data.content[0])].length) < 300) {
        font_size = "24px";
    }
    else {
        font_size = "middle";
    }
    temp += "<table table cellspacing=\"0\" style=\"font-size: " + font_size + "\"width= 90%>\n" +
        "<tbody  class = \"test\">";

    for (let l = 0; l < data.content.length; l++) {
        let stu = Object.keys(data.content[l]).toString();
        j++;
        temp += "<tr>";
        if (irregularStudent.Exists(stu)) {
            temp += "<td  class='irregular-student'>" + stu + "</td>";
        } else {
            temp += "<td  >" + stu + "</td>";
        }

        for (let i = 0; i < data.content[l][stu].length; i++) {
            let class_ = "";
            if(l === 0 || l === 1){
                class_ += " all_border";
            }
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

            let coordinate = ("(" + (i) + ", " + (j - 2) + ")");
            if (l > 0 && data.content[l][stu][i] > 0 && (i !== data.content[l][stu].length - 1) && (stu !== "total")) {
                if (odd_cells.Exists(coordinate)) {
                    class_ += " odd-cells";
                }
                else {
                    class_ += " greater-than-0";
                }
            }
            else if (irregularItem.Exists(data.content[l][stu][i])) {
                class_ += " irregular-item"
            }
            else {
                if (odd_cells.Exists(coordinate)) {
                    class_ += " odd-cells";
                }
            }

            temp += "<td class = \" " + class_ + "\" >" + data.content[l][stu][i] + "</td>";
        }
        temp += "</tr>";
    }
    temp += "</tbody>\n" +
        "</table>";
    return temp;
};

const renderLeftPanel = data => {

    // const query = `?fileID=${fileID}`;
    const query1 = `?fileID=${data.file_id}&typeID=0`;
    const query2 = `?fileID=${data.file_id}&typeID=1`;

    const markup = `
        <div class="back-section">
            <a href="./index.html" class="back-link">
                <img src="./assets/back.svg" alt="back-icon">
                <span class="text">Back</span>
            </a>
        </div>
        <div class="other-pattern">
            <a href="./result.html${query1}" class="pattern-link">
                <span class="text">Show irregular Items</span>
            </a>
        </div>
        <div class="other-pattern">
            <a href="./result.html${query2}" class="pattern-link">
                <span class="text">Show other patterns</span>
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
const renderFeedback = (typeID, data) => {

    let content;
    const irregularStudent = data["irregular_student"];
    const oddCells = data["odd_cells"];
    const irregularItem = data["irregular_item"];
    let irregularStudentStr = Array.isArray(irregularStudent) && irregularStudent.length === 0 ? 'none in this dataset' : irregularStudent;
    let oddCellsStr = Array.isArray(oddCells) && oddCells.length === 0 ? 'none in this dataset' : oddCells;
    let irregularItemStr = Array.isArray(irregularItem) && irregularItem.length === 0 ? 'none in this dataset' : irregularItem;

    if (typeID == 1) {
        content = `
            <li>
                <span>Irregular Students Pattern</span>
                <p>Irregular students are marked with <span class="yellow">yellow</span> color, which are ${irregularStudentStr}.</p>
                <p> An irregular row of ones and zeros indicates that the student has not engaged fully in the assessment.
                    The pattern is a reflection of the student’s attention to the task, rather than their skills. Therefore,
                    it is not possible to identify the student’s point of readiness to learn from the assessment and alternate
                    means must be used.
                </p>
            </li>

            <li>
                <span>Width of Mixture of Ones and Zeros</span>
                <p>Interestring areas are grouped with <span>blue</span> boxes.</p>
                <p>The width of the zone containing a mixture of ones and zeros in an indication of the
                reliability of the assessment. A very wide zone means that there is a lot of ‘noise’ in
                the measure of the students’ abilities. A narrow zone indicates that the assessment is
                a reliability of the students’ abilities in the underlying construct. ‘Noise’ could be due
                to a number of reasons, including the following: that the students were not engaged
                in the task, that the assessment was not administered consistently, that the assessment
                is not of good quality or that the assessment measures more than one underlying
                construct.</p>
            </li>

            <li>
                <span>Odd Cells</span>
                <p>Odd cells are marked with <span class="purple">purple</span> color</p>
                <p>odd cells in this graph are ${oddCellsStr}.</p>
                <p>An unexpected greater-then-zero odd cell after the pattern has broken down
                    should also be disregarded. It is an indication of lucky
                    guessing or an unusual event, not a skill that the student has mastered.
                    This is much more likely if the assessment is a multiple choice test,
                        where the probability of guessing correctly is relatively high.
                        <br />
                        An unusual zero amongst a lot of ones is most likely an
                    indication of a lapse in concentration and not an indication that the student needs to be taught the skill
                    again. We all occasionally made mistakes with something we can do accurately most of the time!
                </p>
            </li>
        `;
    } else if (typeID == 0) {
        content = `
            <li>
                <span>Irregular Items Pattern</span>
                <p>Irregular items are marked with <span class="green">green</span> color, which are ${irregularItemStr}.</p>
                <p>If there is an irregular mixture of ones and zeros within
                    a column, it shows the item is not an indicator of a student’s ability in the underlying construct. This may be
                    due to ambiguity in the item, inconsistent marking, or
                    an item that is not matched to the underlying construct.
                    (Eg: if a maths question is written in difficult language,
                    the question may measure reading ability, not maths
                    ability.) It could also be an indication that the item is too
                    difficult for the students undertaking the assessment.
                    Items which perform like this should be removed from
                    the current analysis, and teachers can use this information to improve their assessment tasks in the future.
                </p>
            </li>
        `;
    }

    const markup = `
        <div class="feedback-container">
            <div class="feedback-header">
                <p>Feedback</p>
            </div>
            <div class="feedback-body">
                <ul class="rule-list">
                    ${content}
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

export const renderParsedResult = (typeID, data) => {
    renderLeftPanel(data);
    renderFeedback(typeID, data);
    renderGuttmanChart(data);
};