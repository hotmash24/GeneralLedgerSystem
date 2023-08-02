
$('#togglesidebar').on('click',function(){
  toggleSidebar();
});

function toggleSidebar() {
  const sidebar = document.getElementById("sidebar");
  const container = document.getElementById("bodyid");


  sidebar.classList.toggle("minimized");
  container.classList.toggle("minimized");

}


  $('#logout').on('click', function() {
    var logoutModal = document.getElementById('logoutModal');
    var logoutYes = document.getElementById('logoutYes');
    logoutModal.style.display = 'block'
 
    logoutYes.focus();
  });


  $('#logoutModal').on('keydown', function(event) {
    const logoutBtn1111 = Array.from(document.querySelectorAll('#logoutModal button'));
    let selectedButtonIndex = 1; 
    const key = event.key;
    if (key === 'ArrowLeft' && selectedButtonIndex > 0) {
      selectedButtonIndex--; // Decrement the selected button index
    } else if (key === 'ArrowRight' && selectedButtonIndex < logoutBtn1111.length - 1) {
      selectedButtonIndex++; // Increment the selected button index
  
    }
  
    logoutBtn1111.forEach(function(button, index) {
      if (index === selectedButtonIndex) {
        button.classList.add('selected'); // Add a class to highlight the selected button
      } else {
        button.classList.remove('selected'); // Remove the class from other buttons
      }
    });
  
    logoutBtn1111[selectedButtonIndex].focus(); // Set focus on the newly selected button
  });
  

  $('#logoutYes').on('click',function(){
    var csrfToken = $('#logoutModalid [name=csrfmiddlewaretoken]').val(); // Get the CSRF token from the form
  
    $.ajax({
      type: 'POST',
      url: '/logout/',  // Replace '/logout/' with the actual URL to your logout_view
      headers: {
        'X-CSRFToken': csrfToken  // Include the CSRF token in the headers
      },
      dataType: 'json',
      success: function(data) {
        // Redirect to the login page after logout
        window.location.href = '/login/';  // Replace '/login/' with the actual URL to your login page
      },
      error: function(xhr, status, error) {
        console.error('Error during logout:', error);
        console.log(xhr.responseText);
      }
    });
  });


  
  $('#logoutYes').on('keydown',function(event){
    if (event.key === 'Enter'){
    var csrfToken = $('#logoutModalid [name=csrfmiddlewaretoken]').val(); // Get the CSRF token from the form
      console.log('adasdasd3qeqwhd');
    $.ajax({
      type: 'POST',
      url: '/logout/',  // Replace '/logout/' with the actual URL to your logout_view
      headers: {
        'X-CSRFToken': csrfToken  // Include the CSRF token in the headers
      },
      dataType: 'json',
      success: function(data) {
        // Redirect to the login page after logout
        window.location.href = '/login/';  // Replace '/login/' with the actual URL to your login page
      },
      error: function(xhr, status, error) {
        console.error('Error during logout:', error);
        console.log(xhr.responseText);
      }
    });
  }
  });

 $('#logoutNo').on('click',function(){
    var logoutModal = document.getElementById('logoutModal');
    logoutModal.style.display = 'none'
  });