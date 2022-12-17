const express = require('express');
const bodyParser = require('body-parser');
const spawn = require('child_process').spawn;

//initializing express application
const app = new express();
const port = process.env.PORT;
app.use(express.json());



let subjectData = [];

//root endpoint
app.get("/",(request,response) =>{
    response.json({message:"working"});
})

//end point to post subjects
app.post("/subjects",(request,response) =>{
    //invokes a python function
    const childProcess = spawn('python',['./public/middleware.py',JSON.stringify(request.body)]);
    childProcess.stdout.on("data",(data) =>{
        console.log(data.toString());
        response.json({status:"data Recieved"});
    })
    
})

app.listen(port,() =>{console.log(`SERVER STARTED ON PORT ${port}`)});