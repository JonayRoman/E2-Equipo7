/*!--Validar campos del formulario--!*/

function validarFormularioEquipo() {
    var modelo = document.getElementById('modelo').value;
    var marca = document.getElementById('marca').value;
    var tipo = document.getElementById('tipo').value;
    const fecha_adquisicion = new Date().toISOString().split('T')[0];
    const fecha_instalacion = new Date().toISOString().split('T')[0];
    var mensaje = document.getElementById('mensaje');

    // Realiza la validación comparando las fechas
    if (fechaPuestaMarcha < fecha_adquisicion) {
      mensaje.textContent = 'La fecha de puesta en marcha debe ser mayor o igual al día de hoy.';
      return false;
    } else {
      mensaje.textContent = ''; // Limpiar el mensaje si los campos son válidos
    }

    // Comprobamos que los campos tienen al menos 3 caracteres
    if (marca.length < 3 || modelo.length < 3 || tipo.length < 3) {
      mensaje.textContent = 'Los campos Marca, Modelo y Tipo de Equipo deben tener al menos 3 caracteres.';
      return false;
    } else {
      mensaje.textContent = ''; // Limpiar el mensaje si los campos son válidos
    }

    // Si todas las validaciones son exitosas, enviar el formulario
    return true;
  }

function validarFormularioEmpleado() {

    var dni = document.getElementById('dni').value;
    var nombre = document.getElementById('nombre').value;
    var apellidos = document.getElementById('apellidos').value;
    var telefono = document.getElementById('telefono').value;
    var email = document.getElementById('email').value;
    var mensaje = document.getElementById('mensaje');

    if (dni.length !== 9) {
      mensaje.textContent = 'El DNI debe tener exactamente 9 caracteres.';
      return false;
    } else if (nombre.length < 3) {
      mensaje.textContent = 'El nombre debe tener al menos 3 caracteres.';
      return false;
    } else if (apellidos.length < 3) {
      mensaje.textContent = 'Los apellidos deben tener al menos 3 caracteres.';
      return false;
    } else if (telefono.length !== 9) {
      mensaje.textContent = 'El teléfono debe tener exactamente 9 caracteres.';
      return false;
    } else if (!email.includes('@')) {
      mensaje.textContent = 'El email debe tener una estructura válida.';
      return false;
    } else {
      mensaje.textContent = ''; // Limpiar el mensaje si los campos son válidos
      
      // Si todas las validaciones son exitosas, enviar el formulario
      return true;
    }
  }