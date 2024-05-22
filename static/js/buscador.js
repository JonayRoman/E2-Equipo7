document.addEventListener("DOMContentLoaded", function() {
    const nombreBuscado = document.getElementById('input-buscador');
    const sinResultadoDiv = document.querySelector('.sin-resultado');
    const nadaCreadoDiv = document.querySelector('.nada-creado');
    const searchQuerySpan = document.getElementById('nombre-buscado');

    if (nadaCreadoDiv) {
        nadaCreadoDiv.style.display = 'none';
        sinResultadoDiv.style.display = 'flex'
        searchQuerySpan.textContent = nombreBuscado.value.trim();
    }
});