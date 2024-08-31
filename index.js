window.onload = function() {
    // Check the referrer URL
    const referrer = document.referrer;

    // Compare it with the specific URL you are checking for
    const targetURL = "https://sctech-tr.neocities.org";

    if (referrer === targetURL) {
        alert('sctech-tr.neocities.org has been moved here.');
    } else {
        console.log("User came from: " + referrer);
    }
};
