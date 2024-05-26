/*!--Validar campos del equipo--!*/
document.addEventListener('DOMContentLoaded', (event) => {
    const marca = document.getElementById('id_marca');
    const modelo = document.getElementById('id_modelo');
    const divValidar = document.querySelector('.div-validar');
    const formulario = document.querySelector('.formulario');

     function showMessage(message) {
         divValidar.innerHTML = '';
         let mensaje = document.createElement('p');
         mensaje.innerText = message;
         divValidar.appendChild(mensaje);
     }

    marca.addEventListener('blur', (event) => {
        const value = marca.value;
        if (value.length < 3 && value.length !== 0) {
            showMessage('La longitud del texto de la marca debe ser mayor a 3 caracteres.');
        } else {
            divValidar.innerHTML = '';
        }
    });

    modelo.addEventListener('blur', (event) => {
        const value = modelo.value;
        if (value.length < 3) {
            showMessage('La longitud del texto del modelo debe ser mayor a 3 caracteres.');
        } else {
            divValidar.innerHTML = '';
        }
    });

    //Funcion para cancelar el envio en caso de que no cumpla con las caracteristicas requeridas
    function validarLongitud(event) {
        if (marca.value.length < 3 || modelo.value.length < 3) {
            event.preventDefault();
        }
    }
    formulario.addEventListener('submit', validarLongitud);
});