/*!--Autocalcular el correo electronico con el nombre y el apellido--!*/
function generarEmail() {
    // Obtenemos los valores del formulario
    const nombre = document.getElementById('nombre').value.trim().toLowerCase();
    const apellido = document.getElementById('apellido').value.trim().toLowerCase();

    // Generamos el correo electrónico
    const email = `${nombre}.${apellido}@ejemplo.com`;

    // Mostramos el correo generado
    document.getElementById('emailGenerado').textContent = `Correo electrónico generado: ${email}`;
}
