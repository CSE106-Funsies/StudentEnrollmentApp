// there will be javascript here

function login(){
    var xhttp = new XMLHttpRequest();
    var url = ''
    // check to see whether we have an account
        // check to see if we have a student
            // modify the url to make a request to go to student dashboard
        // check to see if we have a professor
            // modify the url to make a request to go to professor dashboard
    xhttp.open('POST', url);

    xhttp.send();
}
