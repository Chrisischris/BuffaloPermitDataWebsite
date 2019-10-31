// path is URI we are sending request
// callback is function to execute once reply received                                                               
function ajaxGetRequest(path, callback) {
    let request = new XMLHttpRequest();
    request.onreadystatechange = function() {
        if (this.readyState===4 && this.status ===200) {
            callback(this.response);
        }
    }
    request.open("GET", path);
    request.send();
}

function showBar(response) {
    let resp = JSON.parse(response);
    var layout = {
        xaxis: {title: 'Month'},
        yaxis: {title: '# of Permits'},
        title: 'Building permits by month, Buffalo NY'
    };
    Plotly.newPlot('bar', resp, layout);
}

function showLine(response) {
    let resp = JSON.parse(response);
    var layout = {
        xaxis: {title: 'Year'},
        yaxis: {title: '# of Permits'},
        title: 'Building permits by year, Buffalo NY'
    };
    Plotly.newPlot('line', resp, layout);
}

function showScatter(response) {
    let resp = JSON.parse(response);
    var layout = {
        xaxis: {title: 'Total Value of Work ($)'},
        yaxis: {title: 'Project Size'},
        title: 'Total Value of Work, by project size and year'
    };
    Plotly.newPlot('scatter', resp, layout);
}

function getData() {
    ajaxGetRequest("/barJSON", showBar);
    ajaxGetRequest("/lineJSON", showLine);
    ajaxGetRequest("/scatterJSON", showScatter);
}