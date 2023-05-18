  // Get the elements
  const toaster = document.getElementById('toaster');
  const errorMessage = toaster.querySelector('.error-message');
  const closeButton = toaster.querySelector('.close-button');

  // Function to show the toaster with the error message
  function showError(message) {
    errorMessage.textContent = message;
    toaster.classList.add('show');
  }

  // Function to hide the toaster
  function hideToaster() {
    toaster.classList.remove('show');
  }

  // Event listener for the close button
  closeButton.addEventListener('click', hideToaster);

