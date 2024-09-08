async function pingSite() {
    const target = document.getElementById('target').value;
    const resultElement = document.getElementById('result');
    resultElement.innerHTML = "pinging...";

    try {
        // Send the ping request to the Check-Host API
        const response = await fetch(`https://check-host.net/check-ping?host=${target}`);
        const result = await response.json();

        if (result && result.request_id) {
            // Poll the API every 3 seconds to get the ping results
            pollResults(result.request_id, resultElement);
        } else {
            resultElement.innerHTML = 'error initiating the ping.';
        }
    } catch (error) {
        resultElement.innerHTML = 'error pinging the site.';
    }
}

async function pollResults(requestId, resultElement) {
    const interval = setInterval(async () => {
        try {
            const response = await fetch(`https://check-host.net/check-result/${requestId}`);
            const resultData = await response.json();

            // Check if results are ready
            if (resultData && !resultData.error) {
                clearInterval(interval); // Stop polling once we have the results

                // Format and display the results
                let output = '<h3>Ping Results:</h3>';
                for (let location in resultData) {
                    output += `<p><strong>${location}:</strong> ${formatPingResult(resultData[location])}</p>`;
                }
                resultElement.innerHTML = output;
            }
        } catch (error) {
            resultElement.innerHTML = 'error fetching the ping results.';
        }
    }, 3000); // Poll every 3 seconds
}

function formatPingResult(pingResult) {
    if (Array.isArray(pingResult)) {
        return pingResult.map(time => `${time} ms`).join(', ');
    } else {
        return 'Unreachable';
    }
}
