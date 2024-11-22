class SeasonalButton extends HTMLElement {
    constructor() {
      super();
  
      // Attach shadow DOM for encapsulation
      const shadow = this.attachShadow({ mode: 'open' });
  
      // Create the button
      const button = document.createElement('button');
      const buttonText = this.getAttribute('text');
      button.textContent = buttonText || 'Click me!';
  
      // Determine the current season
      const season = this.getSeason();
      const seasonColors = {
        winter: 'white',
        spring: 'lightgreen',
        summer: 'yellow',
        autumn: 'orange',
      };
      button.style.backgroundColor = seasonColors[season];
      button.style.border = '1px solid black';
      button.style.padding = '10px 20px';
      button.style.cursor = 'pointer';
  
      // Add click handling
      button.addEventListener('click', () => {
        const onclickAttr = this.getAttribute('onclick');
        if (onclickAttr) {
          new Function(onclickAttr)();
        }
      });
  
      shadow.appendChild(button);
    }
  
    // Helper to determine the season
    getSeason() {
      const month = new Date().getMonth(); // 0 = January, 11 = December
      if (month >= 2 && month <= 4) return 'spring';
      if (month >= 5 && month <= 7) return 'summer';
      if (month >= 8 && month <= 10) return 'autumn';
      return 'winter';
    }
  }
  
  // Register the custom element
  customElements.define('seasonal-button', SeasonalButton);
  
