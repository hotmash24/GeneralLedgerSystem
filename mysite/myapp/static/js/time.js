// function updateTime() {
//     const checktimeElement = document.getElementById("checktime");
  
//     // Get the current date and time
//     const currentTime = new Date();
  
//     // Format the time as you desire
//     const hours = currentTime.getHours().toString().padStart(2, "0");
//     const minutes = currentTime.getMinutes().toString().padStart(2, "0");
//     const seconds = currentTime.getSeconds().toString().padStart(2, "0");
  
//     // Format the date as you desire
//     const day = currentTime.getDate().toString().padStart(2, "0");
//     const month = (currentTime.getMonth() + 1).toString().padStart(2, "0");
//     const year = currentTime.getFullYear().toString();
  
//     // Determine if it's AM or PM
//     const ampm = hours >= 12 ? "PM" : "AM";
  
//     // Convert to 12-hour format
//     const hours12 = (hours % 12) || 12;
  
//     // Set the value of the input field to the current date and time
//     checktimeElement.value = `${month}/${day}/${year} ${hours12}:${minutes}:${seconds} ${ampm}`;
//   }
  
//   // Call updateTime every second to update the time continuously
//   setInterval(updateTime, 1000);
  
//   // Run updateTime once immediately to display the time on page load
//   updateTime();
function updateClock(){
    var now = new Date();
    var dname = now.getDay(),
        mo = now.getMonth(),
        dnum = now.getDate(),
        yr = now.getFullYear(),
        hou = now.getHours(),
        min = now.getMinutes(),
        sec = now.getSeconds(),
        pe = "AM";

        if(hou >= 12){
          pe = "PM";
        }
        if(hou == 0){
          hou = 12;
        }
        if(hou > 12){
          hou = hou - 12;
        }

        Number.prototype.pad = function(digits){
          for(var n = this.toString(); n.length < digits; n = 0 + n);
          return n;
        }

        var months = ["January", "February", "March", "April", "May", "June", "July", "Augest", "September", "October", "November", "December"];
        var week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
        var ids = ["dayname", "month", "daynum", "year", "hour", "minutes", "seconds", "period"];
        var values = [week[dname], months[mo], dnum.pad(2), yr, hou.pad(2), min.pad(2), sec.pad(2), pe];
        for(var i = 0; i < ids.length; i++)
        document.getElementById(ids[i]).firstChild.nodeValue = values[i];
  }

  function initClock(){
    updateClock();
    window.setInterval("updateClock()", 1);
  }

  initClock();


