/*!--Validar campos del proceso--!*/
document.addEventListener('DOMContentLoaded', (event) => {
    const codigo_proceso = document.getElementById('id_codigo');
    const nombre_proceso = document.getElementById('id_nombre');
    const divValidar = document.querySelector('.div-validar');
    const formulario = document.querySelector('.formulario');

     function showMessage(message) {
         divValidar.innerHTML = '';
         let mensaje = document.createElement('p');
         mensaje.innerText = message;
         divValidar.appendChild(mensaje);
     }
    
    //validar que el codigo tiene mas de 3 caracteres
    codigo_proceso.addEventListener('blur', (event) => {
        const value = codigo_proceso.value;
        if (value.length < 3 && value.length !== 0) {
            showMessage('La longitud del texto del codigo debe ser mayor a 3 caracteres.');
        } else {
            divValidar.innerHTML = '';
        }
    });

    nombre_proceso.addEventListener('blur', (event) => {
        const value = nombre_proceso.value;
        if (value.length < 3) {
            showMessage('La longitud del texto del nombre debe ser mayor a 3 caracteres.');
        } else {
            divValidar.innerHTML = '';
        }
    });

    //Funcion para cancelar el envio en caso de que no cumpla con las caracteristicas requeridas
    function validarLongitud(event) {
        if (codigo_proceso.value.length < 3 || nombre_proceso.value.length < 3) {
            event.preventDefault();
        }
    }
    formulario.addEventListener('submit', validarLongitud);
});