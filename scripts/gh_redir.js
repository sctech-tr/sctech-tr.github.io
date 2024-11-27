function getParameterByName(name, url = window.location.href) {
    name = name.replace(/[\[\]]/g, '\\$&');
    var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, ' '));
  }
  
  window.onload = function() {
    var username = getParameterByName('u');
    var repo = getParameterByName('r');
    var page = getParameterByName('p');
  
    if (username) {
      let redirectUrl = 'https://github.com/' + username;
      if (repo) {
        redirectUrl += '/' + repo;
      }
      if (page) {
        redirectUrl += '/' + page;
      }
      window.location.href = redirectUrl;
    } else {
      window.location.href = 'gh_noparam.html';
    }
  };
  