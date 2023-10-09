function triggerRefreshWorkflow() {
const token = document.getElementById('tokenInput').value;
const owner = 'npvno';
const repo = 'npvno.github.io';

// Create a payload for the repository dispatch event
const payload = {
    event_type: 'refresh-button-pressed' // Replace with your event type
};

fetch(`https://api.github.com/repos/${owner}/${repo}/dispatches`, {
    method: 'POST',
    headers: {
    'Authorization': `token ${token}`,
    'Accept': 'application/vnd.github.v3+json',
    'Content-Type': 'application/json'
    },
    body: JSON.stringify(payload)
})
    .then(response => {
    if (response.ok) {
        console.log('Workflow triggered successfully.');
    } else {
        console.error('Failed to trigger workflow:', response.statusText);
    }
    })
    .catch(error => {
    console.error('Error:', error);
    });
}

document.getElementById('refreshButton').addEventListener('click', triggerRefreshWorkflow);