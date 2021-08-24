d3.json("http://localhost:5000/data").then(function(data) {
    console.log(data[1][2])
})