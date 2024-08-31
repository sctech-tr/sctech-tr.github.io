window.onload = function() {
    const referrer = document.referrer;
    const targetURL = "https://sctech-tr.neocities.org";

    if (referrer.startsWith(targetURL)) {
        alert('sctech-tr.neocities.org has been moved here.');
    } else {
        console.log("User came from: " + referrer);
    }
};
