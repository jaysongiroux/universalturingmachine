let {PythonShell} = require('python-shell');
var path = require("path");

function checktape(tape){
  // return true for now.
  return true
}

// this is to check syntax for input
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
  let tape = document.getElementById("TAPE").value;

  let syntax = checkSyntax(input);
  if (syntax === false){
    return null
  }

  let tapeSyntax = checktape(tape);
  if (tapeSyntax === false){

  }


  let options = {
    scriptPath : path.join(__dirname, '/../engine/'),
    args : [input,tape]
  };

  let pyshell = new PythonShell('interface.py', options);

  let output = document.getElementById('OUTPUT');
  var array = [];

  pyshell.on('message', function(message) {
    array.push("\n[INPUT] - " + input);
    array.push("\n[INPUT TAPE] - " + tape);
    // evaluated = eval(message);
    array.push(message);
    output.innerHTML = array;
  });
}