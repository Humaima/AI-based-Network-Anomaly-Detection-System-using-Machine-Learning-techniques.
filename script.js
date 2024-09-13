document.getElementById('predictForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const formData = new FormData(this);
    
    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        const modal = document.getElementById('resultModal');
        const modalResult = document.getElementById('modalResult');
        const closeSpan = document.querySelector('.close');
        
        if (data.error) {
            modalResult.innerHTML = 'Error: ' + data.error;
        } else {
            modalResult.innerHTML = 'Prediction: ' + data.label + '<br>Attack Category: ' + data.attack_category;
        }

        // Show the modal
        modal.style.display = 'block';

        // Close the modal when the user clicks on <span> (x)
        closeSpan.onclick = function() {
            modal.style.display = 'none';
        }

        // Close the modal when the user clicks anywhere outside of the modal
        window.onclick = function(event) {
            if (event.target === modal) {
                modal.style.display = 'none';
            }
        }
    })
    .catch(error => {
        console.error('Error:', error);
        const modal = document.getElementById('resultModal');
        const modalResult = document.getElementById('modalResult');
        
        modalResult.innerHTML = 'Error: ' + error.message;

        // Show the modal
        modal.style.display = 'block';
    });
});
