const express = require('express');
const bodyParser = require('body-parser');
const spawn = require('child_process').spawn;
const cors = require('cors');


//initializing express application
const app = new express();
const port = 3000;
app.use(express.json());
app.use(cors({
    origin:"http://localhost:3000"
}))


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
       
       res = data.toString()

       response.json({data:JSON.parse(res)})
    })
    
})

app.listen(port,() =>{console.log(`SERVER STARTED ON PORT ${port}`)});
