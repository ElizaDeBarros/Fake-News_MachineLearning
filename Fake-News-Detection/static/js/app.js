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
        // Prevent page from refreshing
        
    var dropdownMenu = d3.select("#selDataset");
    var selection = d3.select("#logistic");
    selection.html("");
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
                if(data[i].Logistic_Regression==='0') {
                    var logistics = 'FAKE';
                }
                else {
                    var logistics = 'REAL'
                };
                if(data[i].Naive_Bayes==='0') {
                    var naive = 'FAKE';
                }
                else {
                    var naive = 'REAL'
                };
                if(data[i].Decision_Tree==='0') {
                    var decision = 'FAKE';
                }
                else {
                    var decision = 'REAL'
                };
                if(data[i].Passive_Aggressive_Classifier==='0') {
                    var passive = 'FAKE';
                }
                else {
                    var passive = 'REAL'
                };

                answer_dict = {"Headline": data[i].Headline,
                 "Logistic_Regression": logistics,
                 "Naive_Bayes": naive,
                 "Decision_Tree": decision,
                 "Passive_Aggressive_Classifier": passive
                }
            }
        };
        
    //     console.log(answer_dict.Logistic_Regression);
        // d3.select("#logistic").append(answer_dict.Logistic_Regression);
        
        // document.getElementById("#naive").value="";
        
        // d3.select('#decision').html("");
        // d3.select('#passive').html("");
        d3.select('td').enter.text(answer_dict.Logistic_Regression);
        d3.select('td').enter.text(answer_dict.Naive_Bayes);
        d3.select('#decision').append('td').text(answer_dict.Decision_Tree);
        d3.select('#passive').append('td').text(answer_dict.Passive_Aggressive_Classifier);
    });
};


// function to delete all contents of tbody before adding filtered data
function delete_table() {
    var table = document.getElementById("table-data");
    while(table.rows.length > 0) {
        table.deleteRow(1);
    };
};

init();