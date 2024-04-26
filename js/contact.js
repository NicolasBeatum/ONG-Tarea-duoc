function boton(){   
    var form = document.querySelector('form');
    if (!form.checkValidity()) {
        alert('Por favor, completa todos los campos requeridos.');
        return;
    }
    
    var nombres = document.getElementById("nombres").value;
    var email = document.getElementById("email").value;

    alert("Gracias " + nombres + " por contactarnos, te responderemos a la brevedad a tu correo " + email);
}