const form = document.getElementById('form-paciente');
const lista = document.getElementById('lista-pacientes');

const API_URL = 'http://127.0.0.1:5000/pacientes';

function cargarPacientes() {
  fetch(API_URL)
    .then(res => res.json())
    .then(pacientes => {
      lista.innerHTML = '';
      pacientes.forEach(p => {
        const li = document.createElement('li');
        li.textContent = `${p.nombre} ${p.apellido} - ${p.numero_identificacion}`;
        lista.appendChild(li);
      });
    });
}

form.addEventListener('submit', (e) => {
  e.preventDefault();
  const data = Object.fromEntries(new FormData(form));
  
  fetch(API_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  })
  .then(res => {
    if (res.ok) {
      form.reset();
      cargarPacientes();
    } else {
      alert('Error al guardar el paciente.');
    }
  });
});

window.addEventListener('DOMContentLoaded', cargarPacientes);
