/*!--Validar campos del empelado--!*/
document.addEventListener('DOMContentLoaded', (event) => {
    const DNI = document.getElementById('id_dni');
    const email = document.getElementById('id_email');
    const telefono = document.getElementById('id_telefono');
    const divValidar = document.querySelector('.div-validar');
    const formulario = document.querySelector('.formulario');

    //expresion hecha para verificar el formato del email (texto + @ + texto + . + texto
    let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    //funcion para devolver un mensaje especifico en cada caso
     function showMessage(message) {
         divValidar.innerHTML = '';
         let mensaje = document.createElement('p');
         mensaje.innerText = message;
         divValidar.appendChild(mensaje);
     }

    DNI.addEventListener('blur', (event) => {
        const value = DNI.value;
        if (value.length !== 9 && value.length !== 0) {
            showMessage('La longitud del DNI debe ser igual a 9');
        } else {
            divValidar.innerHTML = '';
        }
    });

     telefono.addEventListener('blur', (event) => {
        const value = telefono.value;
        if (value.length !== 9 && value.length !== 0) {
            showMessage('La longitud del telefono debe ser igual a 9');
        } else {
            divValidar.innerHTML = '';
        }
    });

     email.addEventListener('blur', (event) => {
        const value = email.value;
        if (!emailRegex.test(value)) {
            showMessage('El formato del correo electrónico no es válido.');
        } else {
            divValidar.innerHTML = '';
        }
    });

    //Funcion para cancelar el envio en caso de que no cumpla con las caracteristicas requeridas
    function validarLongitud(event) {
        if (DNI.value.length !== 9 || telefono.value.length !== 9 || !emailRegex.test(value)) {
            event.preventDefault();
        }
    }
    formulario.addEventListener('submit', validarLongitud);
});