
const analyzeButton = document.getElementById('analyze-button');
const reportInput = document.getElementById('report-input');
const resultsContainer = document.getElementById('results-container');

analyzeButton.addEventListener('click', async () => {
    const reportText = reportInput.value;


    if (!reportText) {
        alert("Please paste a lab report first.");
        return;
    }

    try {

        const response = await fetch('http://127.0.0.1:8000/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: reportText })
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        

        displayResults(data.results);

    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
        resultsContainer.innerHTML = `<p class="error">Error: Could not analyze the report.</p>`;
    }
});


function displayResults(results) {
    if (!results || results.length === 0) {
        resultsContainer.innerHTML = `<p>No valid results found to display.</p>`;
        return;
    }


    let tableHTML = `
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

    results.forEach(result => {

        tableHTML += `
            <tr class="${result.flag.toLowerCase()}">
                <td>${result.name}</td>
                <td>${result.value}</td>
                <td>${result.flag}</td>
            </tr>
        `;
    });

    tableHTML += `
            </tbody>
        </table>
    `;


    resultsContainer.innerHTML = tableHTML;
}