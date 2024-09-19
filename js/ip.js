// Fetch IP from ipify API
fetch('https://api.ipify.org?format=json')
.then(response => response.json())
.then(data => {
    document.getElementById('ip-address').innerText = data.ip;
})
.catch(error => {
    document.getElementById('ip-address').innerText = 'Unable to fetch IP address.';
});

// Copy IP to clipboard and show confirmation message
function copyToClipboard() {
    const ipText = document.getElementById('ip-address').innerText;
    navigator.clipboard.writeText(ipText).then(() => {
        const confirmation = document.getElementById('confirmation');
        confirmation.style.display = 'block';

        // Hide confirmation message after 2 seconds
        setTimeout(() => {
            confirmation.style.display = 'none';
          }, 2000);
    });
}
