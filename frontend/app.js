
const uploadForm = document.getElementById('upload-form');
const patientIdInput = document.getElementById('patient-id-input');
const fileInput = document.getElementById('file-input');
const resultsContainer = document.getElementById('results-container');


uploadForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const patientId = patientIdInput.value;
    const file = fileInput.files[0];

    if (!patientId || !file) {
        alert("Please provide a Patient ID and select a file.");
        return;
    }


    const formData = new FormData();
    formData.append('patient_id', patientId);
    formData.append('file', file);

    try {
      
        const response = await fetch('http://127.0.0.1:8000/analyze', {
            method: 'POST',
            body: formData 
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        
        displayResults(data.current_results, data.previous_results);

    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
        resultsContainer.innerHTML = `<p class="error">Error: Could not analyze the document.</p>`;
    }
});


function displayResults(currentResults, previousResults) {
    if (!currentResults || currentResults.length === 0) {
        resultsContainer.innerHTML = `<p>No valid results found to display.</p>`;
        return;
    }

    let tableHTML = `
        <h3>Current Results</h3>
        <table>
            <thead>
                <tr>
                    <th>Test Name</th>
                    <th>Value</th>
                    <th>Flag</th>
                </tr>
            </thead>
            <tbody>
    `;

    currentResults.forEach(result => {
        tableHTML += `
            <tr class="${result.flag.toLowerCase()}">
                <td>${result.name}</td>
                <td>${result.value}</td>
                <td>${result.flag}</td>
            </tr>
        `;
    });

    tableHTML += `</tbody></table>`;
    resultsContainer.innerHTML = tableHTML;
}