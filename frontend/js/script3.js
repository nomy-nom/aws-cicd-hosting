document.addEventListener("DOMContentLoaded", function() {
    // URL of your API Gateway endpoint
    const apiUrl = 'https://kwbx2ah611.execute-api.us-east-1.amazonaws.com/prod/git/';

    // Fetch the data from the API
    fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
        // Extract the README content from the response body
        let readmeContent = data.readme_content;

        // Replace markdown image syntax with HTML img tags
        readmeContent = readmeContent.replace(/!\[([^\]]+)\]\(([^)]+)\)/g, '<img src="$2" alt="$1">');

        // Replace newline characters with HTML line break tags
        readmeContent = readmeContent.replace(/\n/g, '<br>');

        // Wrap the formatted content in a table with bold border
        const formattedContent = `
            <table style="border: 3px solid black;">
                <tr>
                    <td>${readmeContent}</td>
                </tr>
            </table>
        `;

        // Update the HTML element with the formatted README content
        document.getElementById('readme').innerHTML = formattedContent;
    })
    .catch(error => console.error('Error fetching README:', error));
});
