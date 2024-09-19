// Initialize Auth0 client
let auth0 = null;

async function initAuth0() {
    auth0 = await createAuth0Client({
        domain: 'dev-qtedxnmpenza4fd5.us.auth0.com',
        client_id: 'ozPW51Xfi4X96HnEM17axcBnfMSzOlmo',
        redirect_uri: window.location.origin + '/callback.html',
        audience: 'https://api.github.com/',
        scope: 'read:user repo'
    });
}

initAuth0();

// Handle login with GitHub via Auth0
document.getElementById('login').addEventListener('click', async function() {
    await auth0.loginWithRedirect();
});

// After the user is redirected, fetch the GitHub repos using the token
async function fetchGitHubRepos() {
    const token = localStorage.getItem('github_token');
    if (token) {
        fetch('https://api.github.com/user/repos', {
            headers: {
                Authorization: `Bearer ${token}`
            }
        })
        .then(response => response.json())
        .then(repos => {
            const repoList = document.getElementById('repo-list');
            repos.forEach(repo => {
                const li = document.createElement('li');
                li.textContent = repo.name;
                repoList.appendChild(li);
            });
        });
    }
}

fetchGitHubRepos();
