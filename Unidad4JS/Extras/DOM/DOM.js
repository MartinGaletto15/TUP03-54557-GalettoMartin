function cambiarTexto(){
    let mensaje = document.getElementById('cambio');
    let mensajeInicial = 'HOLA MUNDO';
    if(mensaje.innerHTML === mensajeInicial){
        mensaje.innerHTML = 'Ahora el texto cambió';
        mensaje.style.color = 'red'
        let button = document.getElementById('button');
        button.innerHTML = 'Volver atras'
    } else {
        mensaje.innerHTML = 'HOLA MUNDO';
        mensaje.style.color = 'black'
        let button = document.getElementById('button');
        button.innerHTML = 'Cambiar texto'
    }
}