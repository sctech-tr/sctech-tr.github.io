// Get the canvas element
var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d");

// Make the canvas cover the full screen
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Set the initial position of the square (dot)
var x = canvas.width / 2;
var y = canvas.height / 2;

// Set the initial change in position
var dx = 0;
var dy = 0;

// Set the game loop
function gameLoop() {
  // Clear the canvas (with black background)
  ctx.fillStyle = "black";
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  // Draw the white dot
  ctx.fillStyle = "white";
  ctx.fillRect(x, y, 20, 20);

  // Update the position of the dot
  x += dx;
  y += dy;

  // Request the next frame
  requestAnimationFrame(gameLoop);
}

// Start the game loop
gameLoop();

// Add event listeners for keyboard input
document.addEventListener("keydown", function(event) {
  switch (event.key) {
    case "ArrowLeft":
      dx = -10;
      dy = 0;
      break;
    case "ArrowRight":
      dx = 10;
      dy = 0;
      break;
    case "ArrowUp":
      dy = -10;
      dx = 0;
      break;
    case "ArrowDown":
      dy = 10;
      dx = 0;
      break;
  }
});

// Adjust canvas size if the window is resized
window.addEventListener('resize', function() {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  x = canvas.width / 2;
  y = canvas.height / 2;
});
