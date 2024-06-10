document.getElementById("random_button").addEventListener('click', () => {
  fetch('/get_random_data')
    .then(response => response.json())
    .then(data => {
      document.getElementById('name_variable').textContent = "nome = " + data.name;
      document.getElementById('status_variable').textContent = "status = " + data.status;
      document.getElementById('specie_variable').textContent = "especie = " + data.species;
      document.getElementById('random_img').setAttribute("src", data.image);
    })
    .catch(error => console.error('Erro:', error))
})