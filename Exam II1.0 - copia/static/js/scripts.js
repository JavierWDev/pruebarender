console.log('El archivo JS se ha cargado correctamente');

document.getElementById('dataForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevenir que el formulario se envíe

    // Mostrar mensaje de alerta
    alert('Datos guardados correctamente, Bienvenido al Seminario');

    // Limpiar los campos del formulario
    document.getElementById('dataForm').reset();
});

