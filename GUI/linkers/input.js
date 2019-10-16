let {PythonShell} = require('python-shell');
var path = require("path");

function checkSyntax(input){
  //  checks the input to determine if the input is valid
  // if not input

  // if it fits the regex return true
  let re = new RegExp('{((((q([0-9]|[0-9]))|(R|L|Δ| |a|b|c|)),)*)(q([0-9]|[0-9])|(R|L|Δ| |a|b|c))}');
  if (re.test(input)) {
    return true
  }

  else if (input === ""){
    console.log('input is empty');
    alert('Input Empty. please enter a valid input');
    return false
  }

  else{
    alert('Input invalid. please enter a valid input');
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
    array.push("\n[INPUT] - " + input);
    evaluated = eval(message)
    array.push("\n[Parsed Output]: ", evaluated)
    output.innerHTML = array;
  });
}