function init() {
    // Use D3 to select the dropdown menu
    var dropdownMenu = d3.select("#selDataset");
    // 1. Use the D3 library to read in `samples.json`.
    const url = "/data/predictions";

d3.json(url).then(function(data) {
        dataNews = data.Body;   
        bodyList = [];
        for (var i=0; i < data.length; i++) {
            bodyList.push(data[i].index)
        };
        
        // add the options to the button
        dropdownMenu.selectAll("option")
            .data(bodyList)
            .enter()
            .append("option")
            .text(a => a)
            .attr('value', a => a);

    });
};

init();