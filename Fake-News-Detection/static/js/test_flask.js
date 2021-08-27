/* data route */
const url = "/data/api";
d3.json(url).then(function(responses) {
    for (var i=0; i < responses.length; i++) {
        console.log(response[i].URLs)
    };

});