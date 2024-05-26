document.addEventListener("DOMContentLoaded", function() {
    // Constante con el id del boton para aumentar el tamaño del texto
    const aumentarTextoBtn = document.getElementById("aumentarTexto");
    // Constante con el id del boton para disminuir el tamaño del texto
    const disminuirTextoBtn = document.getElementById("disminuirTexto");
    //Constante de la tabla donde se hacen los ajustes de texto
    const tabla = document.querySelector(".tabla");


    let fontSize = 15; 

    // Crear el evento que detecta el click en el boton 
    aumentarTextoBtn.addEventListener("click", function(event) {
        event.preventDefault();
        // Aumenta el tamaño del texto en 1 pixel
        fontSize += 1;
        // Llama a la función para cambiar el tamaño del texto
        cambiarTamanoTexto(fontSize);
    });

    // Crear el evento que detecta el clic en el boton
    disminuirTextoBtn.addEventListener("click", function(event) {
        // Evita que el formulario se envie al hacer clic en el boton
        event.preventDefault();
        // Disminuye el tamaño de la fuente en 1 pixel
        fontSize -= 1;
        // Llama a la función para cambiar el tamaño del texto
        cambiarTamanoTexto(fontSize);
    });

    // Función para cambiar el tamaño del texto en la tabla
    function cambiarTamanoTexto(tamano) {
        // Obtiene todos (añadir All) los elementos de texto (td y th) dentro de la tabla
        const elementosTexto = tabla.querySelectorAll("td, th");
        // Itera sobre cada elemento y cambia su tamaño de texto
        elementosTexto.forEach(function(elemento) {
            elemento.style.fontSize = tamano + "px";
        });
    }
});
