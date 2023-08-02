const { timers } = require("jquery");

window.addEventListener('DOMContentLoaded', function() {
    var currentDate = new Date();
    date1 = currentDate.toLocaleDateString();
    time = currentDate.toLocaleTimeString();

    date2 = date1 + ' ' + time ;

    this.document.getElementById('checktime').value = date2
  
  });

  var currentDate = new Date();
  date1 = currentDate.toLocaleDateString();
  time = currentDate.toLocaleTimeString();

  date2 = date1 + ' ' + time ;

  this.document.getElementById('checktime').value = date2

  function toggleSidebar() {
    const sidebar = document.getElementById("sidebar");
    const content = document.querySelector(".content");
  
    sidebar.classList.toggle("minimized");
    content.classList.toggle("minimized");
  }