fetch('https://dog.ceo/api/breeds/image/random')
    .then(response => response.json())
    .then(data => {
        const imgElement = document.getElementById('dog-image');
        imgElement.src = data.message;
    })
    .catch(error => console.error('Error:', error));