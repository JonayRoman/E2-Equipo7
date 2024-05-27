//archivo donde se encuentra la lógica del buscador para buscar por un unico campo en cada lista de elementos

//Constantes en las que se almacenan elementos del codigo html
const nombreBuscado = document.getElementById('input-buscador');
const sinResultadoDiv = document.querySelector('.sin-resultado');
const nadaCreadoDiv = document.querySelector('.nada-creado');
const searchQuerySpan = document.getElementById('nombre-buscado');

//if para interactuar con el contenedor con estilos css cuando no encuentra ningun campo
if (nadaCreadoDiv) {
    nadaCreadoDiv.style.display = 'none';
    sinResultadoDiv.style.display = 'flex'
    searchQuerySpan.textContent = nombreBuscado.value.trim();
}
