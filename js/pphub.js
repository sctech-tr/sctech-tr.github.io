function redirectToPage() {
    const pageUrl = document.getElementById("pageUrl").value;
    if (pageUrl) {
      window.location.href = "users/" + pageUrl + ".html";
    } else {
      alert("please enter a valid username");
    }
}
