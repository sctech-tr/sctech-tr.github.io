// Function to get URL parameters
function getUrlParameter(name) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(name);
}

// Check if 'from-neocities' parameter is true
if (getUrlParameter('from-neocities') === 'true') {
    alert('sctech-tr.neocities.org has been moved here.');
}
