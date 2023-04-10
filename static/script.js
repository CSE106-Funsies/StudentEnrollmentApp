// there will be javascript here

function login(){
    var xhttp = new XMLHttpRequest();
    var url = '/login/';
    // check to see whether we have an account
    // check to see if we have a student
    // modify the url to make a request to go to student dashboard
    // check to see if we have a professor
    // modify the url to make a request to go to professor dashboard
    xhttp.open('POST', url);
    xhttp.setRequestHeader("Content-Type", "application/json");
    
    
    var enteredName = document.getElementById("personUsername").value;
    var enteredPassword = document.getElementById("personPassword").value;
    const body = {"username": enteredName, "password": enteredPassword}

    xhttp.send(JSON.stringify(body));

    xhttp.onload = function() {
        console.log(this.responseText)
        // document.getElementById("demo").innerHTML = this.responseText;

    };
}
