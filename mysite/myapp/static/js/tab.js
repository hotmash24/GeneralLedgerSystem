function changeTab(tabIndex) {
    // Hide all tab content
    var contentElements = document.querySelectorAll('.tab-content .content');
    for (var i = 0; i < contentElements.length; i++) {
      contentElements[i].classList.remove('show');
    }
    
    // Show selected tab content
    var selectedContent = document.getElementById('tab' + (tabIndex + 1));
    selectedContent.classList.add('show');

    var tabs = document.getElementsByClassName("tab");

    // Remove the "selected" class from all tabs
    for (var i = 0; i < tabs.length; i++) {
        tabs[i].classList.remove("selected");
    }

    // Add the "selected" class to the clicked tab
    tabs[tabIndex].classList.add("selected");
    
  }

   window.addEventListener('DOMContentLoaded', function() {
    var tabIndex = 0; // Index of the tab you want to select (0-based index)

    var selectedContent = document.getElementById('tab' + (tabIndex + 1));
    selectedContent.classList.add('show');

    var tabs = document.getElementsByClassName("tab");

    // Remove the "selected" class from all tabs
    for (var i = 0; i < tabs.length; i++) {
      tabs[i].classList.remove("selected");
    }

    // Add the "selected" class to the clicked tab
    tabs[tabIndex].classList.add("selected");
  });