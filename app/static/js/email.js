window.onload = function() {
    contactForm = document.getElementById('contact-form')
    contactForm.addEventListener('submit', function(event) 
    {
        event.preventDefault();
        // these IDs from the previous steps
        emailjs.sendForm('service_81ea4ap', 'template_bql1vla', contactForm)
            .then(function() {
                contactForm.reset();
                alert("Message sent successfully,  Madeleine will get back to you shortly!");
            }, function(error) {
                alert("Uh oh! It looks like there was an error in your form,  please try that again!");
                console.log(error)
                
            });
    });
}