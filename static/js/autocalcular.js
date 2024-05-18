// Autocalcular el correo electronico con el nombre y el apellido

function generarEmail() {
    //Obtenemos los valores del formulario
    const nombre = document.getElementById('nombre').ariaValueMax.trim().toLowerCase();
    const apellido = document.getElementById('apellido').ariaValueMax.trim().toLowerCase();
    
    //Generamos el correo electronico
    const email = '${nombre}.${apellido}@ejemplo.com';

    //Para mostrar el correo generado
    document.getElementById('emailGenerado').textContent = `Correo electronico generado: ${email}`;
}