// Javascript function 


//Collecting information supplied in the form on contact.html
function sendMail(contactForm) {
    emailjs.send("gmail", "data_centric_milestone", {
        "firstname": contactForm.firstname.value,
        "lastname": contactForm.lastname.value,
        "email": contactForm.email.value,
        "message": contactForm.message.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error);
        });
    return false;
}