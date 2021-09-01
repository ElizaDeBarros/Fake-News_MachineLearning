function init() {
    // Use D3 to select the dropdown menu
    var dropdownMenu = d3.select("#selDataset");
    // 1. Use the D3 library to read in `samples.json`.
    const url = "/data/predictions";

d3.json(url).then(function(data) {
        dataNews = data.news;   
        console.log(data);
        
        // add the options to the button
        dropdownMenu.selectAll("option")
            .data(dataNews)
            .enter()
            .append("option")
            .text(a => a)
            .attr('value', a => a);

    });
};

init();