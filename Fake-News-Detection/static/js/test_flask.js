/* data route */
const url = "/data/api";
d3.json(url).then(function(response) {
    for (var i=0; i < response.length; i++) {
        console.log(response[i].URLs)
    };

});