let {PythonShell} = require('python-shell');
let path = require("path");
const fs = require('fs');

function tabs(evt, cityName) {
  // Declare all variables
  let i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}


function closeModal(){
  let modal = document.getElementById("modal");
  modal.style.display = "none";
}

function OpenModal(){
  let modal = document.getElementById("modal");
  modal.style.display = "block";
}

// tripper modals depending on turing machine
function turingMachineStatus(status, finalTape = []){
  let title = document.getElementById("modal-title");
  let info = document.getElementById("modal-info");
  if (status === true){
    title.innerHTML = "Turing Machine Accepted";
    info.innerHTML = finalTape;
    OpenModal()
  }

  else if(status === false){
    title.innerHTML = "Turing Machine Was Unfavorable.";
    info.innerHTML = "Turing Machine Was Unfavorable.";
    OpenModal()
  }
}

function displayRadioValue() {
  var ele = document.getElementsByName('example');
  let exampleNum = 0;
  for(i = 0; i < ele.length; i++) {
    if(ele[i].checked)
      exampleNum = ele[i].value;
  }
  return exampleNum
}

function parseFinalTape(str){
    res = str.toString();
    return res
}

// main function called from submit button
function input(){
  let input = document.getElementById("INPUT").value;
  let tape = document.getElementById("TAPE").value;
  let finaltape = document.getElementById("FINALTAPE");

  exampleNum = displayRadioValue();

  // CREATE TAPE FILE
  fs.writeFile('engine/tape.txt', tape, (err) => {
    // In case of a error throw err.
    if (err) throw err;
  });


  let options = {
    scriptPath : path.join(__dirname, '/../engine/'),
    args : [input,exampleNum]
  };

  let pyshell = new PythonShell('interface.py', options);

  let output = document.getElementById('OUTPUT');
  let encoding = document.getElementById("dynamicTable");
  output.innerHTML = "";
  encoding.innerText = "";
  let l = [];
  let counter = 1;
  let temp = [];

  pyshell.on('message', function(message) {
    let tempMessage = "\n"+counter +": "+message;
    output.innerHTML += tempMessage;
    l.push(message);
    counter ++;
    if (tempMessage.includes("ACCEPTED")===true){
      turingMachineStatus(true,l[counter-4]);
      finaltape.innerHTML = parseFinalTape(l[counter-4]);
//        show the check for accepted
      document.getElementById("check").style.visibility= "visible";
      document.getElementById("ex").style.visibility = "hidden";
      document.getElementById("modal-header").style.backgroundColor ="#049700";
      return true
    }
    // if the turing machine could not finish
    else if(tempMessage.includes("STOPPED")===true){
      finaltape.innerHTML = "Turing Machine Was Unfavorable.";
      turingMachineStatus(false);
//        display the X for rejected
      document.getElementById("ex").style.visibility= "visible";
      document.getElementById("check").style.visibility = "hidden";
      // change modal to red for failed
      document.getElementById("modal-header").style.backgroundColor ="#ff0000";
    }
    if (message.includes("Encoded State:")===true){
      temp.push("\n"+message);
      encoding.innerHTML += "\n <br>"+ message

    }
  });
  console.log(temp)
}