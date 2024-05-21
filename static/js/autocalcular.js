/*!--Autocalcular el correo electronico con el nombre y el apellido--!*/
function generarEmail() {
    let nombre = document.getElementById("nombre").value;
    let apellidos = document.getElementById("apellidos").value;
    let email = nombre.charAt(0).toLowerCase() + apellidos.toLowerCase().replace(/\s+/g, '') + "@gmail.com";
    document.getElementById("email").value = email;
}
