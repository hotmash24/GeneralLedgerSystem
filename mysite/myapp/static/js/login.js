document.addEventListener("DOMContentLoaded", function () {
    const passwordInput = document.getElementById("password");
    const togglePassword = document.getElementById("togglePassword");

    // Event listener to toggle password visibility
    togglePassword.addEventListener("click", function () {
      if (passwordInput.type === "password") {
        passwordInput.type = "text";
        togglePassword.classList.remove("fa-eye");
        togglePassword.classList.add("fa-eye-slash");
      } else {
        passwordInput.type = "password";
        togglePassword.classList.remove("fa-eye-slash");
        togglePassword.classList.add("fa-eye");
      }
    });
  });

var loginButton = document.getElementById('login')
loginButton.addEventListener('click',function(){
  fetch('/ip-address/')
  .then(response => response.text())
  .then(data => {
    // 'data' contains the client's IP address returned from the Django view
    alert('Your IP address is: ' + data);
  })
  .catch(error => {
    console.error('Error:', error);
  });
});
