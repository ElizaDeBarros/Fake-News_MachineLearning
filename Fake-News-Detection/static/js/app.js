const url = "/data/predictions";

function init() {
    // Use D3 to select the dropdown menu
    var dropdownMenu = d3.select("#selDataset");

    d3.json(url).then(function(data) {

        let uniqueHeadline = [...new Set(data.map(item => item.Headline))];
  
        //bodyList = [];
        //for (var i=0; i < data.length; i++) {
        //    bodyList.push(data[i].index)
        //};
            
        // add the options to the button
        dropdownMenu.selectAll("option")
            .data(uniqueHeadline)
            .enter()
            .append("option")
            .text(a => a)
            .attr('value', a => a);

        answers(uniqueHeadline[0])
    });


};

// On change to the dropdown menu
//d3.selectAll("#selDataset").on("change", optionChanged);

// Function called by DOM changes
function optionChanged() {
    var dropdownMenu = d3.select("#selDataset");
    // Assign the value of the dropdown menu option to a variable
    var newHeadline = dropdownMenu.property("value");
    // Initialize an empty array for the country's data
    answers(newHeadline);
};

function answers(headline) {  
    d3.json(url).then(function(data) {
        console.log(headline)

        answer_dict = {}
        for (var i=0; i < data.length; i++) {
            //console.log(data[i].index)
            if (data[i].Headline === headline) {                
                answer_dict = {"Headline": data[i].Headline,
                 "Logistic_Regression": data[i].Logistic_Regression,
                 "Naive_Bayes": data[i].Naive_Bayes,
                 "Decision_Tree": data[i].Decision_Tree,
                 "Passive_Aggressive_Classifier": data[i].Passive_Aggressive_Classifier
                }
            }
        };
        console.log(answer_dict)
    });
};



init();