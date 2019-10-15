let {PythonShell} = require('python-shell');
var path = require("path");

function checkSyntax(input){
  //  checks the input to determine if the input is valid
  // if not input
  if (input === ""){
    console.log('input is empty');
    alert('Input Empty. please enter a valid input');
    return false
  }
}

function input(){
  let input = document.getElementById("INPUT").value;

  let syntax = checkSyntax(input);
  if (syntax === false){
    return null
  }

  let options = {
    scriptPath : path.join(__dirname, '/../engine/'),
    args : [input]
  };

  let pyshell = new PythonShell('interface.py', options);

  let output = document.getElementById('OUTPUT');
  var array = [];

  pyshell.on('message', function(message) {
    array.push("[INPUT] - " + input + "\n");
    var evaluated = eval(message);
    for (i = 0; i < evaluated.length; i++) {
      array.push(evaluated[i]);
    }

    output.innerHTML = array;
  });
}