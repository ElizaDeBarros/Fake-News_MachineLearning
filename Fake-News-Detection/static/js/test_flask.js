/* data route */
//const url = "/data/api";
const url = "/data/predictions";

d3.json(url).then(function(response) {
    for (var i=0; i < response.length; i++) {
        console.log(response[i])
    };

});