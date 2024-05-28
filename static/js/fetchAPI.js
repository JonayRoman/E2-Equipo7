const API_URL_EMPLEADOS = "http://127.0.0.1:8000/APIempleados"

const params = new Proxy(new URLSearchParams(window.location.search), {
    get: (searchParams, prop) => searchParams.get(prop),
  });
const apiEndpoint = params.page ? `${API_URL_EMPLEADOS}?page=${params.page}` : API_URL_EMPLEADOS
// ------------------------------------------- PROVEEDORES LISTVIEW -------------------------------------------
//console.log(params.page);
fetch(apiEndpoint)
    .then(response => response.json())
    .then( json => {
        addRowsEmpleadosLV(json);
    });

function addRowsEmpleadosLV(empleados) {
    tbody = document.querySelector("#fetchEmpleadosLV");
    if(tbody) {
        empleados.forEach(element => {
            tbody.appendChild(createEmpleadosLVRow(element))
        });
    }
}

function createEmpleadosLVRow(empleados){
    let row = document.createElement("tr")

    let name = document.createElement("td")
    let link_detail = document.createElement("a")
        link_detail.setAttribute('href', "http://127.0.0.1:8000/empleados/"+empleados.dni);
        link_detail.innerHTML = empleados.nombre;
        name.append(link_detail)
        row.appendChild(name);

    let tel = document.createElement("td");
        tel.textContent = empleados.telefono;
        row.appendChild(tel);

    let address = document.createElement("td")
        address.textContent = empleados.direccion;
        row.appendChild(address);
    
    let link_row = document.createElement("td")
    let link_edit = document.createElement("a")
        link_edit.setAttribute('href', "http://127.0.0.1:8000/empleados/"+empleados.dni+"/editar");
        link_edit.className = "btn-link";
        link_edit.innerHTML = "Editar";
        link_row.append(link_edit);
    let link_delete = document.createElement("a")
        link_delete.setAttribute('href', "http://127.0.0.1:8000/empleados/"+empleados.id+"/borrar");
        link_delete.className = "btn-link btn-link-red";
        link_delete.innerHTML = "Borrar";
        link_row.append(link_delete);
        row.appendChild(link_row);

    return row;
}