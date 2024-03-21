function startTypewriterEffect(elementId, delay) {
    setTimeout(() => {
      const typer = document.getElementById(elementId);
      const text = typer.textContent;
      typer.textContent = ''; // Clear the content

      text.split('').forEach((char, index) => {
        setTimeout(() => {
          typer.textContent += char;
        }, 100 * index); 
      });
    }, delay);
  }

  // Start typewriter effect for typer1 with a delay of 2 seconds
  startTypewriterEffect('typer1', 2000);
  // Start typewriter effect for typer2 with a delay of 4 seconds
  startTypewriterEffect('typer2', 3000);
  startTypewriterEffect('typer3', 4000);
  startTypewriterEffect('typer4', 5000);
  startTypewriterEffect('typer5', 6000);
  startTypewriterEffect('typer6', 10000);

  // Preventing page reloading
  document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('submitButton').addEventListener('click', function(event) {
      event.preventDefault(); // Prevent the default form submission      
      document.getElementById('myForm').submit(); // Manually submit the form
    });
  });


  
  function typeWriter(el) {
      const textArray = el.innerHTML.split('');
      el.innerHTML = '';
      textArray.forEach((letter, i) =>
          setTimeout(() => (el.innerHTML += letter), 95 * i)
      );
  }

  // Get the element by its ID
  const elementEl = document.getElementById('elementEl');

  // Call the typeWriter function once
  typeWriter(elementEl);

