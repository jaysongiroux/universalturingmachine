const log = require("electron-log");


function input(){
    let inputReg = RegExp('aaa');
    let input = document.getElementById("INPUT").value;

    //    run through regex
    if (inputReg.test(input)){
        alert("input is valid");
    }
    else{
        alert("input is not valid")
    }
    
}