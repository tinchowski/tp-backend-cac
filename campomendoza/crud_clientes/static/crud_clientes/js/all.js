/* scripts de all.html */

function confirmar(fullname){
    if( window.confirm("Desea eliminar : "+fullname) ) return;
    event.preventDefault()
}
