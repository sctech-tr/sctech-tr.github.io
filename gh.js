function redirectToUrl(event) {
      event.preventDefault(); // Prevent the default form submission

      // Get the values from the textboxes
      const username = document.getElementById('username').value;
      const repo = document.getElementById('repo').value;
      const page = document.getElementById('page').value;

      // Construct the URL
      const url = `https://sctech-tr.github.io/gh_redir?u=${encodeURIComponent(username)}&r=${encodeURIComponent(repo)}&p=${encodeURIComponent(page)}`;

      // Redirect to the constructed URL
      window.location.href = url;
}

function generateAndCopyLink() {
      // Get the values from the textboxes
      const username = document.getElementById('username').value;
      const repo = document.getElementById('repo').value;
      const page = document.getElementById('page').value;

      // Construct the URL
      const url = `https://sctech-tr.mooo.com/gh_redir?u=${encodeURIComponent(username)}&r=${encodeURIComponent(repo)}&p=${encodeURIComponent(page)}`;

      // Copy the URL to the clipboard
      navigator.clipboard.writeText(url);

      // Display the generated URL
      const generatedUrlElement = document.getElementById('generatedUrl');
      generatedUrlElement.textContent = `Generated URL: ${url}`;
}

function togglePageDropdown() {
      const repoInput = document.getElementById('repo');
      const pageDropdown = document.getElementById('page');

      // Enable or disable the page dropdown based on the repo input
      pageDropdown.disabled = !repoInput.value.trim();
}
