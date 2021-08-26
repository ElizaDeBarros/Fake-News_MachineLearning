/* data route */
const url = "/data/api";
d3.json(url).then(function(response) {
    console.log(response.URLs)
})