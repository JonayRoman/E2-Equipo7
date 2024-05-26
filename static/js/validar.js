/*!--Validar campos del formulario--!*/

document.addEventListener('DOMContentLoaded', (event) => {
    const marca = document.getElementById('marca');
    const modelo = document.getElementById('modelo');
    const tipo = document.getElementById('tipo');
    const message = document.getElementById('message');  // Añadido aquí

    const showMessage = (msg) => {
        message.innerText = msg;
    };

    marca.addEventListener('blur', (event) => {
        const value = marca.value;

        if (value.length > 3) {
            showMessage('La longitud del texto es mayor a 3 caracteres.');
        } else {
            showMessage('La longitud del texto es 3 o menos caracteres.');
        }
    });

    modelo.addEventListener('blur', (event) => {
        const value = modelo.value;

        if (value.length > 3) {
            showMessage('La longitud del texto es mayor a 3 caracteres.');
        } else {
            showMessage('La longitud del texto es 3 o menos caracteres.');
        }
    });

    tipo.addEventListener('blur', (event) => {
        const value = tipo.value;

        if (value.length > 3) {
            showMessage('La longitud del texto es mayor a 3 caracteres.');
        } else {
            showMessage('La longitud del texto es 3 o menos caracteres.');
        }
    });
});




