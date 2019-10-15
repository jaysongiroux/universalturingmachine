let {PythonShell} = require('python-shell');
var path = require("path");

function input(){
  var input = document.getElementById("INPUT").value;

  var options = {
    scriptPath : path.join(__dirname, '/../engine/'),
    args : [input]
  };

  let pyshell = new PythonShell('interface.py', options);


  pyshell.on('message', function(message) {
    alert(message);
  });
}