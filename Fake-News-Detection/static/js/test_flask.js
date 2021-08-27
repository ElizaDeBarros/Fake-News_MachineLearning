/* data route */
const url = "/data/api";
d3.json(url).then(function(response) {
    console.log(response[0].URLs)
})