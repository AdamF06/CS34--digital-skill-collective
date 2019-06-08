var express = require('express');
var app = express();
var controller = require("./controller/controller.js")
var bodyParser = require('body-parser');

app.use(bodyParser.json()); 
app.use(bodyParser.urlencoded({ extended: true })); 

app.set("view engine","ejs");

// Router 
app.get("/",controller.showHomePage);
app.get("/test",controller.showForm);
app.post('/form',controller.showResult)
app.get("/result",controller.getResult)
app.get("/moreresult",controller.showMore)

app.use(express.static("public"))

app.listen(3000)
console.log("listening on port 3000!")