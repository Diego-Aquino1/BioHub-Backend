document.getElementById('alignmentForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const seq1 = document.getElementById('seq1').value;
    const seq2 = document.getElementById('seq2').value;
    
    const data = {
        seq1: seq1,
        seq2: seq2
    };
    
    fetch('http://localhost:8000/algorithms/needleman', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        displayResults(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

function displayResults(data) {
    document.getElementById('finalScore').textContent = 'Final Score: ' + data.final_score;
    
    const scoreMatrix = document.getElementById('scoreMatrix');
    scoreMatrix.innerHTML = ''; // Clear previous results
    
    data.score_matrix.forEach(row => {
        const rowDiv = document.createElement('div');
        rowDiv.style.display = 'flex';
        row.forEach(cell => {
            const cellDiv = document.createElement('div');
            cellDiv.textContent = cell;
            rowDiv.appendChild(cellDiv);
        });
        scoreMatrix.appendChild(rowDiv);
    });
}
