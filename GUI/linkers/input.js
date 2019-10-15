let {PythonShell} = require('python-shell');
var path = require("path");

function checkSyntax(input){
  //  checks the input to determine if the input is valid

}

function input(){
  let input = document.getElementById("INPUT").value;

  let options = {
    scriptPath : path.join(__dirname, '/../engine/'),
    args : [input]
  };

  let pyshell = new PythonShell('interface.py', options);

  pyshell.on('message', function(message) {
    alert(message);
    let output = document.getElementById('OUTPUT');
    output.innerHTML = message;
  });
}