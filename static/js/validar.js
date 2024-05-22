/*!--Validar campos del formulario--!*/

document.addEventListener('DOMContentLoaded', (event) => {
    const marca = document.getElementById('id_marca');
    const modelo = document.getElementById('id_modelo');
    const tipo = document.getElementById('id_tipo');

    marca.addEventListener('blur', (event) => {
        const value = marca.value;

        if (value.length > 3) {
            console.log('La longitud del texto es mayor a 3 caracteres.');
        } else {
            console.log('La longitud del texto es 3 o menos caracteres.');
        }
    });

    modelo.addEventListener('blur', (event) => {
        const value = modelo.value;
    
        if (value.length > 3) {
            console.log('La longitud del texto es mayor a 3 caracteres.');
        } else {
            console.log('La longitud del texto es 3 o menos caracteres.');
        }
    });

    tipo.addEventListener('blur', (event) => {
        const value = tipo.value;
    
        if (value.length > 3) {
            console.log('La longitud del texto es mayor a 3 caracteres.');
        } else {
            console.log('La longitud del texto es 3 o menos caracteres.');
        }
    });
});



