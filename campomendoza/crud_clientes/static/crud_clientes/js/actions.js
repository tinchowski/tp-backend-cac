const mailformat = /(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])/;

addEventListener('submit',(event)=>{
    event.preventDefault()

    const fullname=document.getElementById('fullname').value
    const fecha_elegida=document.getElementById('date').value
    const cant_personas=document.getElementById('cant_personas').value
    const plan_select=parseInt(document.querySelector('#plan-select option:checked').value)
    const email=document.getElementById('cant_personas').value
    const photo=document.getElementById('photo').value
    const message=document.getElementById('form-mensaje')

    if( /^\s*$/.test(fullname) ||
        /^\s*$/.test(cant_personas) ||
        /^\s*$/.test(fecha_elegida) ||
        /^\s*$/.test(photo) ||
        /^\s*$/.test(email) ) {
            message.textContent="Por favor, complete los campos faltantes."
            return
    }

    if( cant_personas <= 0 || cant_personas > 10 ) {
        message.textContent="Cantidad de personas entre 1 y 10."
        return
    }

    if( mailformat.test(email) ) {
        message.textContent="Correo electrónico inválido."
        return
    }

    if( Date.parse(fecha_elegida) <= Date.now() ) {
        message.textContent="Ingrese fecha posterior a la actual."
        return
    }

    message.textContent="¡Gracias por registrarse en Campo Mendoza!"
    event.target.submit()
})


document.getElementById('photo').onchange=()=>{
    document.querySelector('label.file-label').textContent="Foto Seleccionada"
}


