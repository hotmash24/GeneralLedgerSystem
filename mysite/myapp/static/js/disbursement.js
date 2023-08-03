const SaveEntryModal = document.getElementById('savetransaction');
const UpdatetransactionModal = document.getElementById('Updatetransaction');
const TransModal = document.getElementById('mytranstype');
const  mymodal = document.getElementById('myModal');
const filterButton = document.getElementById('filterButton');
const cancelBtn = document.getElementById('cancelBtn');
const cancelBtn1 = document.getElementById('cancelBtn1');
var list_of_applied = [];
var list_of_applied_total = [];
var dataArray = [];
var data1 = [];
var selectedId = ''
var draweeid = ''
var sl_id = ''
var cv_no = ''
var ul = ''
let UpdateCDB = false
var check_number = ''

let total_debit = 0
let total_credit = 0
let total_diff = 0

window.addEventListener('DOMContentLoaded', function() {
  var currentDate = new Date();
  var formattedDate = currentDate.toISOString().split('T')[0];

  document.getElementById('Dateidcheck').value = formattedDate;

  document.getElementById('Date').value = formattedDate;

var newButton = document.getElementById('newButton');
newButton.focus();


});



function doc_typeRefresh() {
  console.log('4444',$('#ul').val());
  $('#doctype').empty();
  $('#doctype').append('<option value="Cash in Bank">CV</option>');
  $('#doctype').append('<option value="Petty Cash Fund">PCV</option>');
  $('#doctype').append('<option value="Cash in Bank">CV-PDC</option>');
  $('#doctype').append('<option value="Revolving Fund">RFV</option>');
  var currentDate = new Date();
  var formattedDate = currentDate.toISOString().split('T')[0];

  document.getElementById('Dateidcheck').value = formattedDate;

  document.getElementById('Date').value = formattedDate;

}


const buttons1 = Array.from(document.querySelectorAll('#buttonTab1 button'));
$('#buttonTab1').on('keydown', function(event) {
  // console.log('11');
  const key = event.key;
  if (key === 'ArrowLeft' && selectedButtonIndex > 0) {
    selectedButtonIndex--; // Decrement the selected button index
  } else if (key === 'ArrowRight' && selectedButtonIndex < buttons1.length - 1) {
    selectedButtonIndex++; // Increment the selected button index

  }

  else if (key === 'Enter'){
    $('activityid').focus();
    return;
  }

  buttons1.forEach(function(button, index) {
    if (index === selectedButtonIndex) {
      button.classList.add('selected'); // Add a class to highlight the selected button
    } else {
      button.classList.remove('selected'); // Remove the class from other buttons
    }
  });

  buttons1[selectedButtonIndex].focus(); // Set focus on the newly selected button
});

cancelBtn1.addEventListener('click', function () {
  TransModal.style.display = 'none';


});
cancelBtn.addEventListener('click', function () {
    mymodal.style.display = 'none';


});
filterButton.addEventListener('click', function () {
  mymodal.style.display = 'block';
  var modalInputs = mymodal.querySelectorAll('input, textarea, select');
  modalInputs.forEach(function (input) {
      input.removeAttribute('readonly');
      input.removeAttribute('disabled'); // Remove 'disabled' attribute if needed
      input.input = '';
  });

  // var currentDate = new Date();
  // var formattedDate = currentDate.toISOString().split('T')[0];

  // document.getElementById('from').value = formattedDate;

  // document.getElementById('to').value = formattedDate;

});




const confirmationModal = document.getElementById('confirmationModal');
var confirmButton = document.getElementById('confirmButton');
const AbortEncoding = document.getElementById('AbortEncoding');

window.addEventListener('keydown', function (event) {
  if (event.key === 'Escape') {
    var inputs = document.querySelectorAll('input');
    var areInputsWritable = false;

    var modalDisplay = window.getComputedStyle(confirmationModal).getPropertyValue('display');
    var modalDisplay1 = window.getComputedStyle(TransModal).getPropertyValue('display');
    var modalDisplay2 = window.getComputedStyle(mymodal).getPropertyValue('display');
    var modalDisplay3 = window.getComputedStyle(addEntryModal).getPropertyValue('display');
    var modalDisplay4 = window.getComputedStyle(ApplicationOfPaymentModal).getPropertyValue('display');
    var modalDisplay5 = window.getComputedStyle(AbortEncoding).getPropertyValue('display');
    var modalDisplay6 = window.getComputedStyle(SaveEntryModal).getPropertyValue('display');
    var modalDisplay7 = window.getComputedStyle(UpdatetransactionModal).getPropertyValue('display');



    // var modalDisplay5 = window.getComputedStyle(ApplicationOfPaymentModal).getPropertyValue('display');

    var acctContainer = document.getElementById('acctContainer');
  

    if (modalDisplay1 === 'block')  {
      TransModal.style.display='none';
      return;
      // console.log('Modal is not open');
    }else if (modalDisplay2 === 'block')  {
      mymodal.style.display='none';
      return;
      // console.log('Modal is not open');
    }
    else if (modalDisplay7 === 'block')  {
      UpdatetransactionModal.style.display='none';
      return;
      // console.log('Modal is not open');
    }else if (modalDisplay3 === 'block')  {
      addEntryModal.style.display='none';
      return;
      // console.log('Modal is not open');
    }else if (modalDisplay4 === 'block')  {
      ApplicationOfPaymentModal.style.display='none';
      $('#doctype').focus();
      // console.log('dsdfsdfsd');
      return;
      // console.log('Modal is not open');
    }
    else if (modalDisplay5 === 'block')  {
  
      AbortEncoding.style.display='none';
      return;
      // console.log('Modal is not open');
    }
    else if (acctContainer.style.display === "block") {
      AbortEncoding.style.display='block';
      $('#confirmAbort').focus();
      // acctContainer.style.display = "none";
      return;
    }

    else if (modalDisplay6 === 'block')  {
      SaveEntryModal.style.display='none';
      return;
      // console.log('Modal is not open');
    }

    else {
      var inputElement = document.getElementById('payeeInput');
      if (inputElement.readOnly) {
        return;

      }

      else{
              openConfirmationModal();
            var confirmButton = document.getElementById('confirmButton');
            confirmButton.focus();
      }
    }
    // inputs.forEach((input) => {
    //   if (input.hasAttribute('readonly')) {
    //     areInputsWritable = false;
    //     console.log(areInputsWritable);
    //     return;
    //   }
    // });
    // if (areInputsWritable === true) {

    //   console.log(areInputsWritable);
    //   // mymodal.style.display = 'none';
    //   openConfirmationModal();
    //   var confirmButton = document.getElementById('confirmButton');
    //   confirmButton.focus();
    // }

  }
  else if (event.key === 'Enter') {
    if (modalDisplay === 'block')  {
      event.preventDefault;
      return;
      // console.log('Modal is not open');
    }

  
  }

});


var New1 = document.getElementById('newButton');
New1.addEventListener('click' , function () {
  var inputField = document.getElementById("payee");
  if (inputField.readOnly) {
    inputField.readOnly = false; // Switch to writable

  } else {
    inputField.readOnly = true; // Switch to read-only
  }
 });

 confirmButton.addEventListener('click', function () {
  closeConfirmationModal();
});

confirmButton.addEventListener('keydown', function (event) {
  if (event.key === 'Enter'){
    closeConfirmationModal();
  }

});


/// close message prompt//
var cancelMessage = document.getElementById('cancelMessage');
cancelMessage.addEventListener('click', function () {
  closeConfirmationModal();
});

cancelMessage.addEventListener('keydown', function (event) {
  if (event.key === 'Enter'){
    closeConfirmationModal();
  }

});
//messgae box for escape//
function openConfirmationModal() {
  confirmationModal.style.display = 'block';
}

function closeConfirmationModal() {
  confirmationModal.style.display = 'none';
}


function openTranstype() {
TransModal.style.display = 'block';
}


// ------------------ TRANSTYPE select activity type --------------------------//'
$(document).ready(function() {
  SetDataFields();

  $('#activityid').on('click', function() {
    var selectedOption = $(this).val();
    $.ajax({
      url: '/api/trans-type/',
      method: 'GET',
      data: { selectedOption: selectedOption },
      success: function(data) {
        var select = $('#transactionTypeID');
        select.empty(); // Clear existing options
        select.append('<option selected disabled>--------Select--------</option>'); // Add default option
        data.forEach(function(trans_type) {
          select.append('<option value="' + trans_type.line_number + '">' + trans_type.cf_desc + '</option>');
        });
      },
      error: function(xhr, textStatus, errorThrown) {
        console.log('Error:', errorThrown);
      }
    });
  });

  // open Transtype Modal
  $('#newButton').on('click',function () {
    // console.log('q');
    openTranstype();
    var activityid = document.getElementById('activityid');
    activityid.focus();

  });

$('#newButton').on('keydown',function(event) {
if (event.key === 'Enter') {
  event.preventDefault();
  openTranstype();
  var activityid = document.getElementById('activityid');
  activityid.focus();
} 

else if (event.key === 'Enter') {

}
  });

  $('#activityid' ).on('keydown', function(event){
    if (event.key === 'Enter') {
      event.preventDefault();
      var transactionTypeID = document.getElementById('transactionTypeID');


      var selectedOption = $(this).val();
      $.ajax({
        url: '/api/trans-type/',
        method: 'GET',
        data: { selectedOption: selectedOption },
        success: function(data) {
          var select = $('#transactionTypeID');
          select.empty(); // Clear existing options
          // select.append('<option selected disabled>--------Select--------</option>'); // Add default option
          data.forEach(function(trans_type) {
            select.append('<option value="' + trans_type.line_number + '">' + trans_type.cf_desc + '</option>');
          });
        },
        error: function(xhr, textStatus, errorThrown) {
          console.log('Error:', errorThrown);
        }
      });
      transactionTypeID.focus();

    }
  });



  $('#transactionTypeID' ).on('keydown', function(event){
    if (event.key === 'Enter') {
      event.preventDefault();
      var oktranstype = document.getElementById('oktranstype');

      var textFields = document.querySelectorAll('select');
      textFields.forEach(function (field) {
        field.removeAttribute('disabled'); // Remove 'disabled' attribute if needed
      });

      var textFields = document.querySelectorAll('button');
      textFields.forEach(function (field) {
        field.removeAttribute('disabled'); // Remove 'disabled' attribute if needed
      });
    
      oktranstype.focus();

    }
  });


  // ----------------SEARCH PAYOR-------------------//
  $('#payeeInput').on('input', function() {
    var payeeInput = $(this).val();
    var transactionTypeID = $('#transactionTypeID').find('option:selected').text();
    // var transactionTypeID = $('#transactionTypeID').val();
    // console.log('ssss',transactionTypeID);
    if (payeeInput.trim() === '') {
      $('#payeeResults').empty();
      return;
    }
   
    $.ajax({
      url: '/api/payee-list/',
      method: 'GET',
      data: { payeeInput: payeeInput,
               transactionTypeID: transactionTypeID },
      success: function(data) {
        var resultsContainer = $('#payeeResults');
        resultsContainer.empty(); // Clear existing results
        if (data.length > 0) {
          var resultsHtml = '<ul>';
          data.forEach(function(payee_list) {
            resultsHtml += '<li data-id="' + payee_list.id_code + '" data-custom="'+ payee_list.address +'">' + payee_list.id_code + ' - ' + payee_list.payee_name + '</li>';
           
            // resultsHtml += '<li data-id="' + payee_list.id_code + '">' + payee_list.id_code + ' - ' + payee_list.payee_name + '</li>';
            // resultsHtml += '<li data-id="' + payee_list.id_code + '">' + payee_list.payee_name + '</li>';
          });
          resultsHtml += '</ul>';
          resultsContainer.html(resultsHtml);
          
          // Handle click event on the list items
          $('#payeeResults li').click(function() {
            //  selectedId = $(this).data('id');
            // Perform your desired action with the selectedId
            selectedId = selectedItem.attr('data-id');
            var selectedPayee = $(this).text().split(' - ')[1];
            const customData = $(this).data('custom');
            console.log('Payee ID:',selectedId);
            // Set the selected value in the payeeInput
            $('#Address').val(customData);
       
            $('#payeeInput').val(selectedPayee);
            
            // Clear the search results and hide the container
            resultsContainer.empty();
            // var draweeInput = document.getElementById('draweeInput');
            // draweeInput.focus()
            ApplicationOfPayment();
            // $('#applicationTable').empty();
            // console.log('1');
            var fromApp = document.getElementById('fromApp');
            fromApp.focus();
          });
        } else {
          resultsContainer.html('No results found.');
        }
      },
      error: function(xhr, textStatus, errorThrown) {
        console.log('Error:', errorThrown);
      }
    });
  });

  $('#payeeInput').on('keydown', function(event) {

    const key = event.key;
    const resultsContainer = $('#payeeResults');
    const payeeItems = resultsContainer.find('li');

    if (key === 'ArrowDown') {
      event.preventDefault();
      const currentSelectedItem = payeeItems.filter('.selected');
      const nextItem = currentSelectedItem.next('li');
      if (nextItem.length) {
        currentSelectedItem.removeClass('selected');
        nextItem.addClass('selected');
        const payeeText = nextItem.text();
        $('#payeeInput').val(payeeText);
        nextItem.focus();

      } else {
        payeeItems.first().addClass('selected');
      }
    } else if (key === 'ArrowUp') {
      event.preventDefault();
      const currentSelectedItem = payeeItems.filter('.selected');
      const prevItem = currentSelectedItem.prev('li');
      if (prevItem.length) {
        currentSelectedItem.removeClass('selected');
        prevItem.addClass('selected');
        const payeeText = prevItem.text();
        $('#payeeInput').val(payeeText);
        prevItem.focus();

      } else {
        payeeItems.last().addClass('selected');
      }
  
    } else if (key === 'Enter') {
      const selectedItem = payeeItems.filter('.selected');
      if (selectedItem.length) {

        // console.log('wwqewerwewew');
        // Handle the selected item
         selectedId = selectedItem.attr('data-id');
        var selectedPayee = selectedItem.text().split(' - ')[1];
        const customData = selectedItem.data('custom');
        console.log('Payee ID:',selectedId);
        $('#Address').val(customData);
        // const payeeText = selectedItem.text();
        $('#payeeInput').val(selectedPayee);
        resultsContainer.empty();
        // payeeText.focus();
        ApplicationOfPayment();
        // $('#applicationTable').empty();
        var fromApp = document.getElementById('fromApp');
        fromApp.focus();

      }
    }

    else if (event.key ==='Escape') {
      return;
    }
    // if (event.key === 'Enter') {
    //   // Perform your desired action here when the "Escape" key is pressed
    //   event.preventDefault();

    // }
  });


  $(document).on('click', '#payeeResults li', function() {
    // Remove focus from any previously selected item
    $('#payeeResults li').removeClass('selected');
  
    // Add focus to the clicked item
    $(this).addClass('selected');
    $(this).focus();

    const selectedItem = $('#payeeResults li.selected');
    if (selectedItem.length) {
      // Handle the selected item
       selectedId = selectedItem.text().split(' - ')[0];
       console.log('Payee ID:',selectedId)
      const selectedPayee = selectedItem.text().split(' - ')[1];
   
      $('#payeeInput').val(selectedPayee);
      // Trigger a click event on the selected item
      // selectedItem.click();

      // Clear the results container
      $('#payeeResults').empty();
      // var draweeInput = document.getElementById('draweeInput');
      // draweeInput.focus();
      ApplicationOfPayment();
      var fromApp = document.getElementById('fromApp');

      fromApp.focus();
    }
  });

  $('#payeeInput').on('keydown', function(event) {
    if (event.key === 'Escape') {
      // confirmationModal.style.display='block';
      // console.log('Escape key pressed');

    }
    else if (event.key === 'Enter'){
      if ($('#payeeInput').val().length> 0){
      ApplicationOfPayment();
      var fromApp = document.getElementById('fromApp');
      fromApp.focus();
    }
    else{
       
      // Create a new <div> element
      const flashMessageDiv = document.createElement('div');

      // Set the flash message content
      flashMessageDiv.innerHTML = '<i class="fa fa-info-circle"></i>Please select Payee/Payor..!!';
    
      // Add CSS class for centering the flash message
      flashMessageDiv.classList.add('centered-message');
    
      // Add other CSS styling to the flash message (optional)
      // flashMessageDiv.style.backgroundColor = 'yellow';
      // flashMessageDiv.style.color = 'black';
      flashMessageDiv.style.padding = '10px';
      flashMessageDiv.style.borderRadius = '5px';
    
      // Append the flash message element to the body (you can change this to another container if needed)
      document.body.appendChild(flashMessageDiv);
    
      // Remove the flash message after a certain duration (e.g., 3 seconds)
      setTimeout(function() {
        document.body.removeChild(flashMessageDiv);
      }, 3000); // 3000 milliseconds = 3 seconds
    }

    }
  });

  $('#remarks').on('keydown', function(event) {
    if (event.key === 'Enter') {
      event.preventDefault();
      
      if (isNaN(parseFloat($('#Amount').val())) || parseFloat($('#Amount').val()) === 0 ){
        var acctContainer = document.getElementById('acctContainer');
        acctContainer.style.display = 'block';
        $('#debit').val('0.00');
        $('#credit').val('0.00');

      if ($('#ul').prop('disabled') === true) {
        var accCode = document.getElementById('accCode');
        accCode.focus();

      }else {
        var ul = document.getElementById('ul');
        ul.focus();
      }
 

      }
      else{
        

        const flashMessageDiv = document.createElement('div');

        if ($('#draweeInput').val() === ''){
          flashMessageDiv.innerHTML = '<i class="fa fa-info-circle"></i>Please select Drawee Bank..!!';
          flashMessageDiv.classList.add('centered-message');
          flashMessageDiv.style.padding = '10px';
          flashMessageDiv.style.borderRadius = '5px';
          document.body.appendChild(flashMessageDiv);
          setTimeout(function() {
            document.body.removeChild(flashMessageDiv);
          }, 3000); // 3000 milliseconds = 3 seconds
          $(this).focus();
        }
        else if ($('#payeeInput').val() === ''){
          flashMessageDiv.innerHTML = '<i class="fa fa-info-circle"></i>Please select Payee/Payor..!!';
          flashMessageDiv.classList.add('centered-message');
          flashMessageDiv.style.padding = '10px';
          flashMessageDiv.style.borderRadius = '5px';
          document.body.appendChild(flashMessageDiv);
          setTimeout(function() {
            document.body.removeChild(flashMessageDiv);
          }, 3000); // 3000 milliseconds = 3 seconds
          $(this).focus();
        }
        else if ($('#checkNo').val() === ''){
          // console.log($('#draweeInput').val());
          flashMessageDiv.innerHTML = '<i class="fa fa-info-circle"></i>Please Enter Amount..!!';
          flashMessageDiv.classList.add('centered-message');
          flashMessageDiv.style.padding = '10px';
          flashMessageDiv.style.borderRadius = '5px';
          document.body.appendChild(flashMessageDiv);
          setTimeout(function() {
            document.body.removeChild(flashMessageDiv);
          }, 3000); // 3000 milliseconds = 3 seconds
          $(this).focus();
        }


        else{
            getAccountTile();
        }
      
      }
    }
  });

  // ----------------SEARCH DRAWEE-------------------//
  $('#draweeInput').on('input', function()  {
    var draweeInput = $(this).val();
    if (draweeInput.trim() === '') {
      $('#draweeResults').empty();
      return;
    }
    $.ajax({
      url: '/api/drawee-list/',
      method: 'GET',
      data: { draweeInput: draweeInput },
      success: function(data) {
        var resultsContainer = $('#draweeResults');
        resultsContainer.empty(); // Clear existing results
        if (data.length > 0) {
          var resultsHtml = '<ul>';
          data.forEach(function(bank_drawee_list) {
            // resultsHtml += '<li data-id="'+ bank_drawee_list.id_code + '">' + bank_drawee_list.id_code + ' - ' +  bank_drawee_list.bank_abbreviation + '</li>';
            resultsHtml += '<li class="drawee-item" data-id="'+ bank_drawee_list.id_code + '">' + bank_drawee_list.id_code + ' - ' +  bank_drawee_list.bank_abbreviation + '</li>';
            //resultsHtml += '<li class="drawee-item" data-id="'+ bank_drawee_list.id_code + '">' +  bank_drawee_list.bank_abbreviation + '</li>';
          });
          resultsHtml += '</ul>';
          resultsContainer.html(resultsHtml);
          

          // Handle click event on the list items
          $('#draweeResults li').click(function() {
            // var draweeid = $(this).data('id');
            // Perform your desired action with the selectedId
             draweeid = $(this).data('id');
            var selectedDrawee = $(this).text().split(' - ')[1];
            // $('#draweeInput').val(empty);

            document.getElementById('draweeInput').value = '';
            // Set the selected value in the payeeInput

            $('#draweeInput').val(selectedDrawee);
           

            // Clear the search results and hide the container
            resultsContainer.empty();
            var checkdate = document.getElementById('Dateidcheck');
            checkdate.focus();
          });
        } else {
          resultsContainer.html('No results found.');
        }
      },
      error: function(xhr, textStatus, errorThrown) {
        console.log('Error:', errorThrown);
      }
    });
  });

  $('#draweeInput').on('keydown', function(event) {

    const key = event.key;
    const resultsContainer = $('#draweeResults');
    const payeeItems = resultsContainer.find('li');

    if (key === 'ArrowDown') {
      event.preventDefault();
      const currentSelectedItem = payeeItems.filter('.selected');
      const nextItem = currentSelectedItem.next('li');
      if (nextItem.length) {
        currentSelectedItem.removeClass('selected');
        nextItem.addClass('selected');
        const payeeText = nextItem.text();
        $('#draweeInput').val(payeeText);
        nextItem.focus();

      } else {
        payeeItems.first().addClass('selected');
      }
    } else if (key === 'ArrowUp') {
      event.preventDefault();
      const currentSelectedItem = payeeItems.filter('.selected');
      const prevItem = currentSelectedItem.prev('li');
      if (prevItem.length) {
        currentSelectedItem.removeClass('selected');
        prevItem.addClass('selected');
        const payeeText = prevItem.text();
        $('#draweeInput').val(payeeText);
        prevItem.focus();

      } else {
        payeeItems.last().addClass('selected');
      }
  
    } else if (key === 'Enter') {
      const selectedItem = payeeItems.filter('.selected');
      if (selectedItem.length) {
        // Handle the selected item
        const payeeId = selectedItem.attr('data-id');
        const payeeText = selectedItem.text().split(' - ')[1];

        $('#draweeInput').val(payeeText);
        resultsContainer.empty();
        // payeeText.focus();

        var Dateidcheck = document.getElementById('Dateidcheck');
        Dateidcheck.focus();
        // Perform further actions as needed
      }
    }
    // if (event.key === 'Enter') {
    //   // Perform your desired action here when the "Escape" key is pressed
    //   event.preventDefault();

    // }
  });


  
  $('#draweeInput').on('keydown', function(event) {
    if (event.key === 'Escape') {
      // Perform your desired action here when the "Escape" key is pressed
      console.log('Escape key pressed');
    }
    else if (event.key === 'Enter'){
      if ($('#draweeInput').val() === ''){
        const flashMessageDiv = document.createElement('div');
        flashMessageDiv.innerHTML = '<i class="fa fa-info-circle"></i>Please Enter Drawee Bank..!!';
        flashMessageDiv.classList.add('centered-message');
        flashMessageDiv.style.padding = '10px';
        flashMessageDiv.style.borderRadius = '5px';
        document.body.appendChild(flashMessageDiv);
        setTimeout(function() {
          document.body.removeChild(flashMessageDiv);
        }, 3000); // 3000 milliseconds = 3 seconds
        $(this).focus();
      }
    
    else{
      var Dateidcheck = document.getElementById('Dateidcheck');
      Dateidcheck.focus();
    }
    
    }
  });

  $(document).on('click', '#draweeResults li', function() {
    // Remove focus from any previously selected item
    $('#draweeResults li').removeClass('selected');
  
    // Add focus to the clicked item
    $(this).addClass('selected');
    $(this).focus();

    const selectedItem = $('#draweeResults li.selected');
    if (selectedItem.length) {
      // Handle the selected item
       draweeid = selectedItem.text().split(' - ')[0];
      const selectedDrawee = selectedItem.text().split(' - ')[1];
   
      $('#draweeInput').val(selectedDrawee);
      // Trigger a click event on the selected item
      // selectedItem.click();

      // Clear the results container
      $('#draweeResults').empty();
      var checkdate = document.getElementById('Dateidcheck');
      checkdate.focus();
    }
  });



//--------------------- SEARC ACCOUNT TITLE ---------------//
  $('#accCode').on('input', function()  {
    var accCode = $(this).val();
    if (accCode.trim() === '') {
      $('#AccCodeResults').empty();
      return;
    }
    $.ajax({
      url: '/api/acct-title/',
      method: 'GET',
      data: { accCode: accCode },
      success: function(data) {
        var resultsContainer = $('#AccCodeResults');
        resultsContainer.empty(); // Clear existing results
        if (data.length > 0) {
          var resultsHtml = '<ul>';
          data.forEach(function(acct_title_list) {
            // resultsHtml += '<li data-id="'+ bank_drawee_list.id_code + '">' + bank_drawee_list.id_code + ' - ' +  bank_drawee_list.bank_abbreviation + '</li>';
            resultsHtml += '<li class="accCode-item" data-id="'+ acct_title_list.code + '">' + acct_title_list.code + ' - ' +  acct_title_list.acct_title + '</li>';

          });
          resultsHtml += '</ul>';
          resultsContainer.html(resultsHtml);
          
          // Handle click event on the list items
          $('#AccCodeResults li').click(function() {
            var selectedId = $(this).data('id');
            // Perform your desired action with the selectedId
            var accCode = $(this).data('id');
            var accTitle = $(this).text().split(' - ')[1];
            var acctTitle2 = $(this).text().split(' - ')[2];
            // Set the selected value in the payeeInput
            // $('#accCode').val(accCode);
            // $('#accTitle').val(accTitle);

            $('#accCode').val(accCode);
    
            if (!acctTitle2) {
              $('#accTitle').val(accTitle);
            } else {
              const combinedText = accTitle + ' - ' + acctTitle2;
              $('#accTitle').val(combinedText);
            }

            var accTitle = document.getElementById('accTitle');

            // Clear the search results and hide the container
            resultsContainer.empty();
            accTitle.focus();
          });
        } else {
          resultsContainer.html('No results found.');
        }
      },
      error: function(xhr, textStatus, errorThrown) {
        console.log('Error:', errorThrown);
      }
    });
  });



  $('#accCode').on('keydown', function(event) {

    const key = event.key;
    const resultsContainer = $('#AccCodeResults');
    const draweeItems = resultsContainer.find('li');

    if (key === 'ArrowDown') {
      event.preventDefault();
      const currentSelectedItem = draweeItems.filter('.selected');
      const nextItem = currentSelectedItem.next('li');
      if (nextItem.length) {
        currentSelectedItem.removeClass('selected');
        nextItem.addClass('selected');
        const draweeText = nextItem.text();
        // $('#accCode').val(payeeText);
        nextItem.focus();

      } else {
        draweeItems.first().addClass('selected');
      }
    } else if (key === 'ArrowUp') {
      event.preventDefault();
      const currentSelectedItem = draweeItems.filter('.selected');
      const prevItem = currentSelectedItem.prev('li');
      if (prevItem.length) {
        currentSelectedItem.removeClass('selected');
        prevItem.addClass('selected');
        const draweeText = prevItem.text();
        // $('#accCode').val(acctcode);
        prevItem.focus();

      } else {
        draweeItems.last().addClass('selected');
      }
  
    } else if (key === 'Enter') {
      const selectedItem = draweeItems.filter('.selected');
      if (selectedItem.length) {
        // Handle the selected item
        const acctcode = selectedItem.text().split(' - ')[0];

        const acctTitle = selectedItem.text().split(' - ')[1];
        const acctTitle2 = selectedItem.text().split(' - ')[2];
        $('#accCode').val(acctcode);

        if (!acctTitle2) {
          $('#accTitle').val(acctTitle);
        } else {
          const combinedText = acctTitle + ' - ' + acctTitle2;
          $('#accTitle').val(combinedText);
        }
        resultsContainer.empty();

      }
    }

    

  });
  

  $(document).on('click', '#AccCodeResults li', function() {
    // Remove focus from any previously selected item
    $('#AccCodeResults li').removeClass('selected');
  
    // Add focus to the clicked item
    $(this).addClass('selected');
    $(this).focus();

    const selectedItem = $('#AccCodeResults li.selected');
    if (selectedItem.length) {
      // Handle the selected item
      const acctcode = selectedItem.text().split(' - ')[0];
      const acctTitle = selectedItem.text().split(' - ')[1];
      const acctTitle2 = selectedItem.text().split(' - ')[2];
      $('#accCode').val(acctcode);

      if (!acctTitle2) {
        $('#accTitle').val(acctTitle);
      } else {
        const combinedText = acctTitle + ' - ' + acctTitle2;
        $('#accTitle').val(combinedText);
      }

      // Trigger a click event on the selected item
      // selectedItem.click();

      // Clear the results container
      $('#AccCodeResults').empty();
      var slacct = document.getElementById('slAcc');
      slacct.focus();
    }
  });



  $('#Dateidcheck').on('keydown', function(event) {
    if (event.key === 'Escape') {
      // Perform your desired action here when the "Escape" key is pressed
      console.log('Escape key pressed');
      confirmationModal.style.display='block';
    }
    else if (event.key === 'Enter'){
      event.preventDefault();
      var checkNo = document.getElementById('checkNo');
      checkNo.focus();
    }
  });
  


  $('#checkNo').on('keydown', function(event) {
    if (event.key === 'Escape') {
      // Perform your desired action here when the "Escape" key is pressed
      console.log('Escape key pressed');
    }
    else if (event.key === 'Enter'){

        if ($('#checkNo').val() === ''){
          const flashMessageDiv = document.createElement('div');
          flashMessageDiv.innerHTML = '<i class="fa fa-info-circle"></i>Please Enter Check Number..!!';
          flashMessageDiv.classList.add('centered-message');
          flashMessageDiv.style.padding = '10px';
          flashMessageDiv.style.borderRadius = '5px';
          document.body.appendChild(flashMessageDiv);
          setTimeout(function() {
            document.body.removeChild(flashMessageDiv);
          }, 3000); // 3000 milliseconds = 3 seconds
          $(this).focus();
        }
      
      else{
        var remarks = document.getElementById('remarks');
        remarks.focus();
      }
  
    }
  });

  $('#Contact').on('keydown', function(event) {
    if (event.key === 'Escape') {
      // Perform your desired action here when the "Escape" key is pressed
      console.log('Escape key pressed');
    }
    else if (event.key === 'Enter'){
      var remarks = document.getElementById('remarks');
      remarks.focus();
    }
  });


  $('#Amount').on('keydown', function(event) {
    if (event.key === 'Escape') {
      // Perform your desired action here when the "Escape" key is pressed
      console.log('Escape key pressed');
      confirmationModal.style.display='block';
    }
    else if (event.key === 'Enter'){
      var selectedText = $('#doctype').find('option:selected').text();
      if (selectedText === 'CV' || selectedText === 'CV-PDC') {

        convertAmount();
        $('#draweeInput').focus();
      }
      else{
        if (isNaN(parseFloat($('#Amount').val())) || parseFloat($('#Amount').val()) === 0 ){
          const flashMessageDiv = document.createElement('div');
          flashMessageDiv.innerHTML = '<i class="fa fa-info-circle"></i>Please Enter Amount..!!';
          flashMessageDiv.classList.add('centered-message');
          flashMessageDiv.style.padding = '10px';
          flashMessageDiv.style.borderRadius = '5px';
          document.body.appendChild(flashMessageDiv);
          setTimeout(function() {
            document.body.removeChild(flashMessageDiv);
          }, 3000); // 3000 milliseconds = 3 seconds
          $(this).focus();
        }

        else{
          getAccountTile();
        }

      
      }
    }
  });

  // $('#Amount').on('keydown', function(event) {
  //   if (event.key === 'Escape') {
  //     // Perform your desired action here when the "Escape" key is pressed
  //     console.log('Escape key pressed');
  //     confirmationModal.style.display='block';
  //   }
  //   else if (event.key === 'Enter'){

  //     var docref = document.getElementById('docref');
  //     docref.focus();
  //     event.preventDefault();
  //     if ($('#draweeInput').val() !== '' && !isNaN(parseFloat($('#Amount').val()))   && $('#payeeInput').val() !== '' )  {
  //       if (parseInt($('#Amount').val()) !== 0) {
  //         var selectedText = $('#doctype').find('option:selected').text();
  //         // console.log('111111',$(this).find('option:selected').text());
  //         if (selectedText === 'CV' || selectedText === 'CV-PDC') {
           
  //           if ($('#checkNo').val() !=='') {

  //             getAccountTile();
  //           }

  //           else {
  //            $('#draweeInput').focus();
  //             // const flashMessageDiv = document.createElement('div');
  //             // flashMessageDiv.innerHTML = '<i class="fa fa-info-circle"></i>Please Enter Check No...!!';
  //             // flashMessageDiv.classList.add('centered-message');
  //             // flashMessageDiv.style.padding = '10px';
  //             // flashMessageDiv.style.borderRadius = '5px';
  //             // document.body.appendChild(flashMessageDiv);
  //             // setTimeout(function() {
  //             // document.body.removeChild(flashMessageDiv);
  //             // }, 3000); // 3000 milliseconds = 3 seconds
  //             // $(this).focus();
  //           }
  //         }

  //         else{
  //           getAccountTile();
  //         }
  //         console.log($('#checkNo').val());

  //         // debitCredit();
  //       }
  //       else{

  //         const flashMessageDiv = document.createElement('div');
  //         flashMessageDiv.innerHTML = '<i class="fa fa-info-circle"></i>Cannot accept Entry Amount to Zero..!!';
  //         flashMessageDiv.classList.add('centered-message');
  //         flashMessageDiv.style.padding = '10px';
  //         flashMessageDiv.style.borderRadius = '5px';
  //         document.body.appendChild(flashMessageDiv);
  //         setTimeout(function() {
  //         document.body.removeChild(flashMessageDiv);
  //         }, 3000); // 3000 milliseconds = 3 seconds
  //         $(this).focus();
  //       }
  
  //     }

  //     else {
  //       const flashMessageDiv = document.createElement('div');

  //       if ($('#draweeInput').val() === ''){
  //         flashMessageDiv.innerHTML = '<i class="fa fa-info-circle"></i>Please select Drawee Bank..!!';
  //       }
  //       else if ($('#payeeInput').val() === ''){
  //         flashMessageDiv.innerHTML = '<i class="fa fa-info-circle"></i>Please select Payee/Payor..!!';
  //       }
  //       else{
  //         console.log($('#draweeInput').val());
  //         flashMessageDiv.innerHTML = '<i class="fa fa-info-circle"></i>Please Enter Amount..!!';
  //       }
  //       flashMessageDiv.classList.add('centered-message');
  //       flashMessageDiv.style.padding = '10px';
  //       flashMessageDiv.style.borderRadius = '5px';
  //       document.body.appendChild(flashMessageDiv);
  //       setTimeout(function() {
  //         document.body.removeChild(flashMessageDiv);
  //       }, 3000); // 3000 milliseconds = 3 seconds
  //       $(this).focus();
       
  //     }
  //     // var acctContainer = document.getElementById('acctContainer');
  //     // acctContainer.style.display = 'block';
  //     // var acctCode = document.getElementById('accCode');
  //     // $('#debit').prop('readonly', true);
  //     // // ApplicationOfPayment();
  //     // acctCode.focus();

  
  //     // convertAmount();
     
  //   }
  // });


  var account_title = '';
    var account_code = '';
  function getAccountTile(){
    var acctTitle = $('#doctype').val();
    $.ajax({
      url: '/api/acct-title/',
      method: 'GET',
      data: { acctTitle: acctTitle },
      success: function(data) {
        if (data.length > 0) {
          data.forEach(function(acct_title_list) {
            account_code = acct_title_list.code 
            account_title = acct_title_list.acct_title
            // console.log(account_code);
            // console.log(account_title);
            addAccountEntryfromAmount();
            debitCredit();
          });
        }
      }
    });

  }

  var amount = document.getElementById("Amount");
  amount.addEventListener("input", function() {

      var currentValue = amount.value;
      var numericValue = currentValue.replace(/[^0-9.]/g, "")
      .replace(/(\..*)\./g, "$1");
      amount.value = numericValue;
  });
  

  function convertAmount() {
    var currentValue = parseFloat(amount.value);
    
    var parts = currentValue.toString().split(".");
    // console.log('Parts',parts[1]);
    const numberPart = parts[0];
    const decimalPart = parts[1];
    const thousands = /\B(?=(\d{3})+(?!\d))/g;
    // console.log(numberPart);
    $('#Amount').empty();
    if (decimalPart===undefined){
      // console.log(numberPart.replace(thousands, ",") + (decimalPart ? "." + decimalPart : ".00"));
      return  $('#Amount').val(numberPart.replace(thousands, ",") + (decimalPart ? "." + decimalPart : ".00"));
    }
    else{
      // console.log(numberPart.replace(thousands, ",") + (decimalPart ? "." + decimalPart : "."));
      return $('#Amount').val(numberPart.replace(thousands, ",") + (decimalPart ? "." + decimalPart : ""));
    }
  }

  

  function convert(c) {
    var currentValue = c;

    // Remove non-numeric and non-decimal characters except the last dot
    var numericValue = currentValue.replace(/[^0-9.]/g, "")
      .replace(/(\..*)\./g, "$1");
    // Ensure that the numeric value has two decimal places
    var parts = numericValue.split(".");
    if (parts.length > 1) {
      parts[1] = parts[1].slice(0, 3); // Limit the decimal places to two digits
    } else {
      parts.push("00"); // If there are no decimal places, add .00
    }
    // Ensure that the integer part has at least one digit
    if (parts[0] === "") {
      parts[0] = "0";
    }
    // Format the numeric value with thousand separators
    parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    var formattedValue = parts.join(".");
    // Update the input field value
   return  formattedValue;
}
  

  function addAccountEntryfromAmount() {

    const table = document.getElementById('AcctEntry');
    const tbody = document.getElementById('acctEntryBody');
  
    const newRow = document.createElement('tr');
    const ul = document.createElement('td');
    const acctCode = document.createElement('td');
    const acctTitle = document.createElement('td');
    const slAcct = document.createElement('td');
    const debit = document.createElement('td');
    const credit = document.createElement('td');
  
    var ulentry = document.getElementById('ul').value;
    var codeentry = account_code;
    var TITLEentry = account_title;
    var slentry = document.getElementById('draweeInput').value;
    var debitentry = '0.00'
    var creditentry = document.getElementById('Amount').value;
 
    ul.textContent = ulentry;
    acctCode.textContent = codeentry;
    acctTitle.textContent = TITLEentry;
    slAcct.textContent = slentry;

    var debitValue = parseFloat(debitentry); 
    var creditValue =creditentry.replace(/,(?=\d{3})/g, '')
    debit.textContent = debitValue.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    credit.textContent = convert(creditValue);
    


    const nameToCellIdMap = {
      ul_code: 'cell-ul-code',
      acct_code: 'cell-acct-code',
      acct_title: 'cell-acct-title',
      sl_acct: 'cell-sl-acct',
      credit_amount: 'cell-credit-amount',
      debit_amount: 'cell-debit-amount',
      code: 'cell-code',
      code1: 'cell-code1',
      code2: 'cell-code2',
      code3: 'cell-code3',

    };
    
    // Get the existing table
    const deletetable = document.getElementById('AcctEntry'); // Replace "your-table-id" with the actual ID of your table element
    const rows = deletetable.getElementsByTagName('tr'); // Get all the rows in the table

    for (let i = 0; i < rows.length; i++) {
      const row = rows[i];
      const cells = row.getElementsByTagName('td'); // Get all the cells in the current row
      
      for (let j = 0; j < cells.length; j++) {
        const cell = cells[j];
        const columnName = Object.keys(nameToCellIdMap)[j]; // Get the column name based on the cell index
        
        if (columnName === 'sl_acct') {
          const cellValue = cell.textContent; // Get the numeric value from the cell
          
          if (cellValue === slentry) {
            row.remove();
          }
        }

      }
    }
    
  GetAccountCodeIndividual(TITLEentry);

  if (slentry=='GENERAL'){
    sl_code_entry ='9999'
  }

  else{
    var c = localStorage.sl_type_per_acct_Title
    GetSLCodeEntry(c,slentry);
  }


  // console.log('code invidual:',localStorage.acct_code0,localStorage.acct_code1,localStorage.acct_code2,localStorage.acct_code3,localStorage.sl_id_code)
  const sl_code = document.createElement('td');
  sl_code.textContent = localStorage.sl_id_code;
  sl_code.classList.add('hidden');
  // newRow.appendChild(sl_code);

  const code = document.createElement('td');
  code.textContent = localStorage.acct_code0;
  code.classList.add('hidden');
  // newRow.appendChild(code);
  const code1 = document.createElement('td');
  code1.textContent = localStorage.acct_code1;
  code1.classList.add('hidden');
  // newRow.appendChild(code1);

  const code2 = document.createElement('td');
  code2.textContent = localStorage.acct_code2;
  code2.classList.add('hidden');
  // newRow.appendChild(code2);

  const code3 = document.createElement('td');
  code3.textContent = localStorage.acct_code3;
  code3.classList.add('hidden');
  // newRow.appendChild(code3);

    
    const buttonCell = document.createElement('td');
    const Delete = document.createElement('button');
    Delete.classList.add('btn', 'btn-primary');
    const icon = document.createElement('i');
    icon.classList.add('fas', 'fa-trash');
    Delete.textContent = 'Delete';
    Delete.addEventListener('click', function() {
      var parentElement = Delete.parentNode;
      parentElement.parentNode.remove();
      debitCredit();
    });
  
    ul.appendChild(Delete);
  
    newRow.appendChild(ul);
    newRow.appendChild(acctCode);
    newRow.appendChild(acctTitle);
    newRow.appendChild(slAcct);
    newRow.appendChild(debit);
    newRow.appendChild(credit);
    newRow.appendChild(buttonCell);
    newRow.appendChild(sl_code);
    newRow.appendChild(code);
    newRow.appendChild(code1);
    newRow.appendChild(code2);
    newRow.appendChild(code3);
    // buttonCell.appendChild(Edit);
    buttonCell.appendChild(Delete);
    // buttonCell.appendChild(Details);
    tbody.appendChild(newRow);
  
  //  document.getElementById('ul').value = '';
   document.getElementById('accCode').value = '';
   document.getElementById('accTitle').value = '';
   document.getElementById('slAcc').value = '';
   document.getElementById('debit').value = '0.00';
   document.getElementById('Amount').value = '0.00';
  
   DisplayAddentryModal();
  }
  


  $('#doctype').on('keydown', function(event) {
    if (event.key === 'Escape') {
      // Perform your desired action here when the "Escape" key is pressed
      console.log('Escape key pressed');
    }
    else if (event.key === 'Enter'){
      event.preventDefault();
      var Date = document.getElementById('Date');
      Date.focus();
    }
  });
  // document.getElementById('doctype').addEventListener('change', function() {
  //   // Transfer focus to the input element when the selection changes.
  //   document.getElementById('Date').focus();
  // });

  $('#docref').on('keydown', function(event) {
    if (event.key === 'Escape') {
      // Perform your desired action here when the "Escape" key is pressed
      console.log('Escape key pressed');
    }
    else if (event.key === 'Enter'){
      var Date = document.getElementById('Date');
      Date.focus();
    }
  });

  
  $('#Date').on('keydown', function(event) {
    if (event.key === 'Escape') {
      // Perform your desired action here when the "Escape" key is pressed
      console.log('Escape key pressed');
    }
    else if (event.key === 'Enter'){
      event.preventDefault();
      var Amount = document.getElementById('Amount');
      Amount.focus();
    }
  });

    
  $('#accCode').on('keydown', function(event) {
    if (event.key === 'Escape') {
      // Perform your desired action here when the "Escape" key is pressed
      console.log('Escape key pressed');
    }
    else if (event.key === 'Enter'){
      var accTitle = document.getElementById('accTitle');
      accTitle.focus();
    }
  });


  $('#accTitle').on('keydown', function(event) {
    if (event.key === 'Escape') {
      // Perform your desired action here when the "Escape" key is pressed
      console.log('Escape key pressed');
    }
    else if (event.key === 'Enter'){
      var slAcc = document.getElementById('slAcc');
      slAcc.focus();
    }
  });

  $('#slAcc').on('keydown', function(event) {
    if (event.key === 'Escape') {
      // Perform your desired action here when the "Escape" key is pressed
      console.log('Escape key pressed');
    }
    else if (event.key === 'Enter'){
      event.preventDefault();
      var debit = document.getElementById('debit');
      debit.focus();
    }
  });


  $('#debit').on('keydown', function(event) {
    if (event.key === 'Escape') {
      // Perform your desired action here when the "Escape" key is pressed
      console.log('Escape key pressed');
    }
    else if (event.key === 'Enter'){
      if (isNaN($(this).val()) || $(this).val()=='' ) {
        $(this).val('0.00');
      }
      var credit = document.getElementById('credit');
      credit.focus().select();
    }
  });



  $('#credit').on('keydown', function(event) {
    if (event.key === 'Escape') {
      console.log('Escape key pressed');
    }
    else if (event.key === 'Enter'){
      if (isNaN($(this).val()) || $(this).val()=='' ) {
        $(this).val('0.00');
      }
     var credit = $(this).val();
     const acct = $('#accCode').val();
     const sl =  $('#slAcct').val();

   

     if (credit > 0 && acct !==''  && sl!=='') {

      if ($('#debit').val() > 0){
        const flashMessageDiv = document.createElement('div');
        flashMessageDiv.innerHTML = '<i class="fa fa-info-circle"></i>Error Debit and Credit both have Amount..!!';
        flashMessageDiv.classList.add('centered-message');
        flashMessageDiv.style.padding = '10px';
        flashMessageDiv.style.borderRadius = '5px';
        document.body.appendChild(flashMessageDiv);
      
        setTimeout(function() {
          document.body.removeChild(flashMessageDiv);
        }, 3000); 
      }

      else{
        event.preventDefault();
        addAccountEntry();
        debitCredit();
      }

      }
      else{
       
          const flashMessageDiv = document.createElement('div');

          if (acct === ''){
          flashMessageDiv.innerHTML = '<i class="fa fa-info-circle"></i>Please select Account Title..!!';
          flashMessageDiv.classList.add('centered-message');
          flashMessageDiv.style.padding = '10px';
          flashMessageDiv.style.borderRadius = '5px';
          document.body.appendChild(flashMessageDiv);
        
          setTimeout(function() {
            document.body.removeChild(flashMessageDiv);
          }, 3000); 
          }
          else if (sl === ''){
            flashMessageDiv.innerHTML = '<i class="fa fa-info-circle"></i>Please select Subsidiary Account..!!';
            
          flashMessageDiv.classList.add('centered-message');
      
          flashMessageDiv.style.padding = '10px';
          flashMessageDiv.style.borderRadius = '5px';
        
          document.body.appendChild(flashMessageDiv);
        
          setTimeout(function() {
            document.body.removeChild(flashMessageDiv);
          }, 3000); 
          }
          else if ($('#debit').val() > 0){
    
            event.preventDefault();
            addAccountEntry();
            debitCredit();
          }
          else{
            flashMessageDiv.innerHTML = '<i class="fa fa-info-circle"></i>Please Enter Amount..!!';
            
          flashMessageDiv.classList.add('centered-message');
        
          flashMessageDiv.style.padding = '10px';
          flashMessageDiv.style.borderRadius = '5px';
        
          document.body.appendChild(flashMessageDiv);
        
          setTimeout(function() {
            document.body.removeChild(flashMessageDiv);
          }, 3000); 
          }
        }
      

    }
  });


// ------------GET SUBSIDIARY ACCCOUNT DEPEND ON SL TYPE OF ACCOUNT TITLE ---------------
  $('#slAcc').on('input', function()  {
    var slAcc = $('#accTitle').val();
    var sl = $(this).val();
    if ((sl).trim() === '') {
      $('#slAccResults').empty();
      return;
    }

    $.ajax({
      url: '/api/slAccount/',
      method: 'GET',
      data: { slAcc: slAcc },
      success: function(data) {
        var resultsContainer = $('#slAccResults');
        resultsContainer.empty(); // Clear existing results
        if (data.length > 0) {
          var resultsHtml = '<ul>';
          data.forEach(function(sl_list) {
            // resultsHtml += '<li data-id="'+ bank_drawee_list.id_code + '">' + bank_drawee_list.id_code + ' - ' +  bank_drawee_list.bank_abbreviation + '</li>';
            resultsHtml += '<li class="sl-item" data-id="'+ sl_list.id_code + '">' + sl_list.id_code + ' - ' +  sl_list.sl_name + '</li>';
            //resultsHtml += '<li class="drawee-item" data-id="'+ bank_drawee_list.id_code + '">' +  bank_drawee_list.bank_abbreviation + '</li>';
          });
          resultsHtml += '</ul>';
          resultsContainer.html(resultsHtml);
          

          // Handle click event on the list items
          $('#slAccResults li').click(function() {
            // var selectedId = $(this).data('id');
            // Perform your desired action with the selectedId
             sl_id = $(this).data('id');
            var selectedSL = $(this).text().split(' - ')[1];
            
            // Set the selected value in the payeeInput
            $('#slAcc').val(selectedSL);
            // var checkdate = document.getElementById('Dateidcheck');
        
            // Clear the search results and hide the container
            resultsContainer.empty();
            $('#debit').focus();
            // credit.focus();
          });
        } else {
          resultsContainer.html('No results found.');
        }
      },
      error: function(xhr, textStatus, errorThrown) {
        console.log('Error:', errorThrown);
      }
    });
  });

  $(document).on('click', '#slAccResults li', function() {
    // Remove focus from any previously selected item
    $('#slAccResults li').removeClass('selected');
  
    // Add focus to the clicked item
    $(this).addClass('selected');
    $(this).focus();

    const selectedItem = $('#slAccResults li.selected');
    if (selectedItem.length) {
      // Handle the selected item
      const slid = selectedItem.text().split(' - ')[0];
      const selectedsl = selectedItem.text().split(' - ')[1];
   
      $('#slAcc').val(selectedsl);
      // Trigger a click event on the selected item
      // selectedItem.click();

      // Clear the results container
      $('#slAccResults').empty();
      var debit = document.getElementById('debit');
      debit.focus();
    }
  });


  $('#slAcc').on('keydown', function(event) {

    const key = event.key;
    const resultsContainer = $('#slAccResults');
    const payeeItems = resultsContainer.find('li');

    if (key === 'ArrowDown') {
      event.preventDefault();
      const currentSelectedItem = payeeItems.filter('.selected');
      const nextItem = currentSelectedItem.next('li');
      if (nextItem.length) {
        currentSelectedItem.removeClass('selected');
        nextItem.addClass('selected');
        const payeeText = nextItem.text();
        $('#slAcc').val(payeeText);
        nextItem.triggerHandler('focus');
        // nextItem.focus();

      } else {
        payeeItems.first().addClass('selected');
      }
    } else if (key === 'ArrowUp') {
      event.preventDefault();
      const currentSelectedItem = payeeItems.filter('.selected');
      const prevItem = currentSelectedItem.prev('li');
      if (prevItem.length) {
        currentSelectedItem.removeClass('selected');
        prevItem.addClass('selected');
        const payeeText = prevItem.text();
        $('#slAcc').val(payeeText);
        prevItem.triggerHandler('focus');

      } else {
        payeeItems.last().addClass('selected');
      }
  
    } else if (key === 'Enter') {
      const selectedItem = payeeItems.filter('.selected');
      if (selectedItem.length) {
        // Handle the selected item
        const slid = selectedItem.attr('data-id');
        const slname = selectedItem.text().split(' - ')[1];

        $('#slAcc').val(slname);
        resultsContainer.empty();
        // payeeText.focus();

        var debit = document.getElementById('debit');
        debit.focus().select();
        // Perform further actions as needed
      }
    }
    // if (event.key === 'Enter') {
    //   // Perform your desired action here when the "Escape" key is pressed
    //   event.preventDefault();

    // }
  });



///-- GENERATE APPLICATION OF PAYMENT
$(document).on('click', '#GenerateButton', function(){
  list_of_applied = [];
 
  $('#countid').val('0');
  $('#total1').val('0.00');
  $('#total2').val('0.00');
// console.log('1',dataArray )
// console.log('2',list_of_applied )
// console.log('3',list_of_applied_total )
// console.log('11',newItem )
  dateFrom = $('#fromApp').val();
  dateTo = $('#toApp').val();
  Account_title = $('#Account_title').val();
  payee = $('#payeeInput').val();
  data = [];
  payeeId = selectedId;
  console.log('Payee 11ID:',selectedId);
  if (Account_title ===''){
    Account_title = 'ALL'
  }

  $.ajax({

    url: '/api/ApplicationOfPayment/',
    type: 'GET',
    data: {
      payeeId: selectedId,
      payee: payee,
      Datefrom: dateFrom,
      DateTo: dateTo,
      Acct_title: Account_title,
    },
    success: function(data) {
      var resultsContainer = $('#applicationTable');
      resultsContainer.empty(); // Clear existing results
      
      if (data.length > 0) {
        var tableHtml = "<tr>" +
          "<th style='width:150px'>Reference No.</th>" +
          "<th style='width:140px'>Date</th>" +
          "<th style='width:140px'>Amount</th>" +
          "<th>Application of Payment</th>" +
          "<th style='width:40px;'><input type='checkbox' id='selectAllCheckbox' style='width:15px; height:15px;'></th>" +
          "</tr>";
        let xx = 0;
        let count = 0;
        data1 = data;
        // console.log(data1);
        data.forEach(function(application_list,index) {
          // console.log('11111',index);
          var rowHtml = "<tr>";
          rowHtml += "<td>" + application_list.doc_type + '#' + application_list.cv_no + "</td>";
          rowHtml += "<td>" + application_list.date_trans + "</td>";
          rowHtml += "<td>" + application_list.credit_amount.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + "</td>";
          rowHtml += "<td><input type='text' id='input" + index + "' style='width:80px; height:20px; text-align:end;' value = 0.00></td>";
          rowHtml += "<td><input type='checkbox' data-index='" + index + "' style='width:15px; height:15px;'></td>";
          rowHtml += "</tr>";
          tableHtml += rowHtml;
          xx+= parseFloat(application_list.credit_amount);
          count+=1;
        });
        $('#countid').val(count);
        $('#total1').val(xx.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 }));
        resultsContainer.html(tableHtml);


        function validateInput(inputElement, index, debitAmount) {
          var inputValue = parseFloat(inputElement.value.replace(/,/g, ''));
          
          if (inputValue > debitAmount) {
            inputElement.value = debitAmount.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
          }
          
          // Additional logic specific to the index if needed
          // ...
        }
        
        data1.forEach(function (application_list, index) {
          var inputElement = document.getElementById('input' + index);
          inputElement.addEventListener('input', function () {
            var numericValue = this.value.replace(/[^0-9.]/g, '');
            this.value = numericValue;
            validateInput(this, index, application_list.credit_amount);
        
          });
        });


      }
      else {
        $('#countid').val('0');
        $('#total1').val('0.00');
        var tableHtml = "<tr>" +
        "<th style='width:150px'>Reference No.</th>" +
        "<th style='width:140px'>Date</th>" +
        "<th style='width:140px'>Amount</th>" +
        "<th>Application of Payment</th>" +
        "<th style='width:40px;'><input type='checkbox' id='selectAllCheckbox' style='width:15px; height:15px;'></th>" +
        "</tr>";
        resultsContainer.html(tableHtml);
        notFound();
      }
  
    },
    error: function(xhr, errmsg, err) {
      console.log(xhr.status + ": " + xhr.responseText);
    }
  });
});


$('#GenerateButton').on('keydown', function(event){
if (event.key === 'Enter'){

  list_of_applied = [];
 
  $('#countid').val('0');
  $('#total1').val('0.00');
  $('#total2').val('0.00');
  dateFrom = $('#fromApp').val();
  dateTo = $('#toApp').val();
  Account_title = $('#Account_title').val();
  payee = $('#payeeInput').val();
  payeeId = selectedId;
  console.log('Payee 11ID:',selectedId);
  data = [];
  if (Account_title ===''){
    Account_title = 'ALL'
  }
  $.ajax({

    url: '/api/ApplicationOfPayment/',
    type: 'GET',
    data: {
      payeeId: selectedId,
      payee: payee,
      Datefrom: dateFrom,
      DateTo: dateTo,
      Acct_title: Account_title,
    },
    success: function(data) {
      var resultsContainer = $('#applicationTable');
      resultsContainer.empty(); // Clear existing results
      
      if (data.length > 0) {
        var tableHtml = "<tr>" +
          "<th style='width:150px'>Reference No.</th>" +
          "<th style='width:140px'>Date</th>" +
          "<th style='width:140px'>Amount</th>" +
          "<th>Application of Payment</th>" +
          "<th style='width:40px;'><input type='checkbox' id='selectAllCheckbox' style='width:15px; height:15px;'></th>" +
          "</tr>";
        let xx = 0;
        let count = 0;
        data1 = data;
        // console.log(data1);
        data.forEach(function(application_list,index) {
          // console.log('11111',index);
          var rowHtml = "<tr>";
          rowHtml += "<td>" + application_list.doc_type + '#' + application_list.cv_no + "</td>";
          rowHtml += "<td>" + application_list.date_trans + "</td>";
          rowHtml += "<td>" + application_list.credit_amount.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + "</td>";
          rowHtml += "<td><input type='text' id='input" + index + "' style='width:80px; height:20px; text-align:end;' value = 0.00></td>";
          rowHtml += "<td><input type='checkbox' data-index='" + index + "' style='width:15px; height:15px;'></td>";
          rowHtml += "</tr>";
          tableHtml += rowHtml;
          xx+= parseFloat(application_list.credit_amount);
          count+=1;
        });
        $('#countid').val(count);
        $('#total1').val(xx.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 }));
        resultsContainer.html(tableHtml);


      }
      else {
        $('#countid').val('0');
        $('#total1').val('0.00');
      }
function validateInput(inputElement, index, debitAmount) {
  var inputValue = parseFloat(inputElement.value.replace(/,/g, ''));
  
  if (inputValue > debitAmount) {
    inputElement.value = debitAmount.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  }
  
  // Additional logic specific to the index if needed
  // ...
}

data1.forEach(function (application_list, index) {
  var inputElement = document.getElementById('input' + index);
  inputElement.addEventListener('input', function () {
    var numericValue = this.value.replace(/[^0-9.]/g, '');
    this.value = numericValue;
    validateInput(this, index, application_list.credit_amount);

  });
});

  
    },
    error: function(xhr, errmsg, err) {
      console.log(xhr.status + ": " + xhr.responseText);
    }
  });
}

});


//// end generate
$(document).on('#applicationTable change', 'input[type="checkbox"]', function() {
  totalApp =0;
var index = $(this).data('index');
var totalApp = $('#total2');
var elementId = $('#input' + index);

if (elementId.attr('id') === 'input' + index) {
var debitAmount = data1[index].credit_amount;


if ($(this).is(':checked')) {
  // console.log('1',debitAmount);
  elementId.val(debitAmount.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 }));
  // console.log('1',debitAmount);
  var totalValue = parseFloat(totalApp.val().replace(/,/g, ''));
  if (totalValue > 0) {
    totalValue = parseFloat(totalValue);
    totalValue+=debitAmount;
    totalApp.val(totalValue.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 }));
  }

  else{
    totalApp.val(debitAmount.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 }));
  }


} else {
  elementId.val('0.00');
  var totalValue = parseFloat(totalApp.val().replace(/,/g, ''));


  // console.log(totalValue);
  if (totalValue > 0) {
    totalValue = parseFloat(totalValue);
    console.log('debit',debitAmount);
    totalValue-=debitAmount;
  
    totalApp.val(totalValue.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 }));
  }
}
} else {
let x = 0;

var selectAllCheckbox = document.getElementById('selectAllCheckbox');
var inputElements = document.querySelectorAll('input[data-index]');

selectAllCheckbox.addEventListener('change', function() {
  var isChecked = this.checked;

  inputElements.forEach(function(inputElement) {
    inputElement.checked = isChecked;
  });

  updateInputValues(isChecked);
});



function updateInputValues(isChecked) {
  inputElements.forEach(function(inputElement) {
    var index = inputElement.getAttribute('data-index');
    var debitAmount = data1[index].credit_amount;
    var elementId = $('#input' + index);
    if (isChecked) {
      elementId.val(debitAmount.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 }));
      // elementId.val(debitAmount);
      // totalApp.val((parseInt(debitAmount) + parseInt(totalApp.val())).toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 }));
      x +=debitAmount;
    } else {
      elementId.val('0.00');
      // x -=debitAmount;
    }
    totalApp.val(x.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 }));
  });
}

}
});


var resultsContainer = $('#applicationTable');

$(document).on('#applicationTable change', 'input[type="text"]', function() {
  var inputElement = $(this);
  // var value1 = parseFloat(inputElement.val());
  var index = resultsContainer.find('input[type="text"]').index(inputElement);
  // console.log('ss',index);
  var numericValue = parseFloat(inputElement[0].value);

  var checkboxElement = $('input[type="checkbox"][data-index="' + index + '"]');
  var totalApp = $('#total2');
  // Check or uncheck the checkbox based on the input value
  checkboxElement.prop('checked', numericValue > 0);

  let xx = 0;
  var inputElements1 = resultsContainer.find('input[type="text"]');
  inputElements1.each(function() {
    var value = $(this).val();
    if (!isNaN(value) || value !== '0.00') {
      xx +=  parseFloat(value.replace(/,/g, ''));; // Add value to xx variable
      // console.log(xx);
    }
  });
  // xx += parseFloat(value1);
  
  totalApp.val(xx.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 }));
});

$(document).on('#applicationTable keydown', 'input[type="text"]', function(event) {
  if (event.key === 'Enter') {
    event.preventDefault(); // Prevent the default Enter key behavior

    var inputElement = $(this);
    var currentIndex = resultsContainer.find('input[type="text"]').index(inputElement);
    var nextIndex = currentIndex + 1;

    var nextInputElement = resultsContainer.find('input[type="text"]').eq(nextIndex);

    if (nextInputElement.length) {
      nextInputElement.focus();
    }
  }
});








// ----------------------- ADD TO ARRAY THE APPLIED PAYMENT -------------------------//
var okF10 = document.getElementById('okf10');
let ss = 0;
okF10.addEventListener('click',function(){


              dataArray = [];
                list_of_applied = [];
                list_of_applied_total = [];
                list_of_applied_total = [];
                newItem = [];
      
                $('#applicationTable tr').each(function(index) {
                  var checkbox = $(this).find('td:nth-child(5) input[type="checkbox"]');
                  if (checkbox.is(':checked')) {
                    index-=1;
                    var inputElement = $('#input' + index);
                    var list_of_applied = {
                      docType: data1[index].doc_type,
                      cvNo: data1[index].cv_no,
                      dateTrans: data1[index].date_trans,
                      debitAmount: data1[index].credit_amount,
                      inputValue: inputElement.val(),
                      sl_acct: data1[index].sl_acct,
                      acct_code: data1[index].acct_codef,
                      acct_title: data1[index].acct_title,
                      ul_code: data1[index].ul_code,
                      id_code: data1[index].id_code,
                      code: data1[index].primary_code,
                      code1: data1[index].secondary_code,
                      code2: data1[index].acct_code,
                      code3: data1[index].subsidiary_code,
                    };
                    dataArray.push(list_of_applied);
      
                    if (list_of_applied_total.length !== 0){
                      if (Array.isArray(list_of_applied_total)) {
                      const foundItem = list_of_applied_total.find(item => item.acct_code === data1[index].acct_codef);
      
                            if (foundItem) {
                             
                              const currentCreditAmount = parseFloat(foundItem.credit_amount.replace(/,/g, ''));
                              const x = parseFloat(inputElement.val().replace(/,/g, ''))
                              const updatedCreditAmount = currentCreditAmount + parseFloat(x);
                              foundItem.credit_amount = updatedCreditAmount.toLocaleString('en-US', { minimumFractionDigits: 2 });
                              // console.log('Matching item found:', foundItem);
                              // Perform additional actions with the found item
                            } else {
                              newItem = {
                                ul_code: data1[index].ul_code,
                                acct_code: data1[index].acct_codef,
                                acct_title: data1[index].acct_title,
                                sl_acct: data1[index].sl_acct,
                                credit_amount:inputElement.val(),
                                debit_amount: '0.00',
                                
                                };
                                list_of_applied_total.push(newItem);
                              console.log('No matching item found.');
                            }
          
                      }
      
                    }
                    else {
                      newItem = {
                        ul_code: data1[index].ul_code,
                        acct_code: data1[index].acct_codef,
                        acct_title: data1[index].acct_title,
                        sl_acct: data1[index].sl_acct,
                        credit_amount: inputElement.val(),
                        debit_amount: '0.00',
                        };
                        list_of_applied_total.push(newItem);
                    }
                  }
      
                });
                const nameToCellIdMap = {
                  ul_code: 'cell-ul-code',
                  acct_code: 'cell-acct-code',
                  acct_title: 'cell-acct-title',
                  sl_acct: 'cell-sl-acct',
                  credit_amount: 'cell-credit-amount',
                  debit_amount: 'cell-debit-amount',
                  button: 'cell-button',
                  id_code: 'cell-idcode',
                  code: 'cell-code',
                  code1: 'cell-code1',
                  code2: 'cell-code2',
                  code3: 'cell-code3',
          
                };
                
                // Get the existing table
                const table = document.getElementById('AcctEntry'); // Replace "your-table-id" with the actual ID of your table element
                const rows = table.getElementsByTagName('tr'); // Get all the rows in the table

                for (let i = 0; i < rows.length; i++) {
                  const row = rows[i];
                  const cells = row.getElementsByTagName('td'); // Get all the cells in the current row
                  
                  for (let j = 0; j < cells.length; j++) {
                    const cell = cells[j];
                    const columnName = Object.keys(nameToCellIdMap)[j]; // Get the column name based on the cell index
                    
                    if (columnName === 'credit_amount') {
                      const cellValue = parseFloat(cell.textContent); // Get the numeric value from the cell
                      
                      if (cellValue > 0) {
                        row.remove();
                      }
                    }

                  }
                }

                // Iterate over the array
                for (let i = 0; i < list_of_applied_total.length; i++) {
                  const data = list_of_applied_total[i];
                  const row = document.createElement('tr');

                  // Iterate over the specific names
                  for (const name in nameToCellIdMap) {
                    const cellId = nameToCellIdMap[name];
                    const cell = document.createElement('td'); // Create a new cell
                    cell.textContent = data[name]; // Set the cell content from the specific name
                    cell.id = cellId; // Set the cell ID
                      console.log('tabel name:', cellId);
                    if (cellId == 'cell-button'){
                      const buttonCell = document.createElement('td');
                      const Delete = document.createElement('button');
                      Delete.classList.add('btn', 'btn-primary');
                      const icon = document.createElement('i');
                      icon.classList.add('fas', 'fa-trash');
                      Delete.appendChild(icon);
                      Delete.textContent = 'Delete';
                      Delete.addEventListener('click', function() {
                        var parentElement = Delete.parentNode;
                        parentElement.parentNode.remove();
                        debitCredit();
                      });
                      
                      buttonCell.appendChild(Delete);
                      row.appendChild(buttonCell); 
                    }
                    else{
                      row.appendChild(cell); 
                    }
                  }
                
  // Add the cell with the button to the row
                  table.appendChild(row); // Add the row to the table
                }
                // Perform further processing or logging as needed
                debitCredit();
                $('#doctype').focus();
});

var debittotal = document.getElementById('debittotal');
var credittotal = document.getElementById('credittotal');
var diff = $('#diff').empty();
var credittotal = $('#credittotal').empty();
var debittotal = $('#debittotal').empty();


function debitCredit(){
  const nameToCellIdMap = {
    ul_code: 'cell-ul-code',
    acct_code: 'cell-acct-code',
    acct_title: 'cell-acct-title',
    sl_acct: 'cell-sl-acct',
    credit_amount: 'cell-credit-amount',
    debit_amount: 'cell-debit-amount',

  };
  var debit = 0;
  var credit = 0;
  var diffe = 0;
  diff.val(0);
  debittotal.val(0);
  credittotal.val(0);

  const table = document.getElementById('AcctEntry'); // Replace "your-table-id" with the actual ID of your table element
  const rows = table.getElementsByTagName('tr'); // Get all the rows in the table

  for (let i = 0; i < rows.length; i++) {
    const row = rows[i];
    const cells = row.getElementsByTagName('td'); // Get all the cells in the current row
 
    for (let j = 0; j < cells.length; j++) {
      const cell = cells[j];
      // console.log('credi111t:',cell);
      const columnName = Object.keys(nameToCellIdMap)[j]; // Get the column name based on the cell index
      
      if (columnName === 'credit_amount') {
        const cellValue = parseFloat(cell.textContent.replace(/,/g, ''));
       
        if (cellValue > 0) {
        
        debit+=cellValue;

        }
        else{
          debit+=0;
        }

      }

      else if  (columnName === 'debit_amount') {

        const cellValue = parseFloat(cell.textContent.replace(/,/g, ''));
        if (cellValue > 0) {
  
     
      credit+=cellValue;
    
        }

        else{
          credit+=0;
        }
      }
    }


  }


  diffe = debit - credit;
 
  // console.log('debit:',debit);
  // console.log('credit:',credit);
  // console.log('diff:',diffe);
  console.log('d11111ebit:',debit);
  console.log('credit:',credit);
  console.log('diff:',diffe);
  var formattedDiff = diffe.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  var formattedDebit = debit.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  var formattedCredit = credit.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  
  // Set the formatted values into the corresponding HTML elements using their IDs.
  $('#diff').val(formattedDiff);
  $('#debittotal').val(formattedDebit);
  $('#credittotal').val(formattedCredit);

  total_credit = formattedCredit;
  total_debit = formattedDebit;
  total_diff = formattedDiff;

  console.log('1--:',formattedCredit)
  console.log('1--:',formattedDebit)
  console.log('1--:',formattedDiff)
  // diff.val(diffe.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 }));
  // debittotal.val(debit.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 }));
  // credittotal.val(credit.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 }));
  
}

});
// end here
function debitCredit(){
  const nameToCellIdMap = {
    ul_code: 'cell-ul-code',
    acct_code: 'cell-acct-code',
    acct_title: 'cell-acct-title',
    sl_acct: 'cell-sl-acct',
    credit_amount: 'cell-credit-amount',
    debit_amount: 'cell-debit-amount',

  };
  var debit = 0;
  var credit = 0;
  var diffe = 0;
  // diff.val(0);
  // debittotal.val(0);
  // credittotal.val(0);

  const table = document.getElementById('AcctEntry'); // Replace "your-table-id" with the actual ID of your table element
  const rows = table.getElementsByTagName('tr'); // Get all the rows in the table

  for (let i = 0; i < rows.length; i++) {
    const row = rows[i];
    const cells = row.getElementsByTagName('td'); // Get all the cells in the current row
 
    for (let j = 0; j < cells.length; j++) {
      const cell = cells[j];
      // console.log('credi111t:',cell);
      const columnName = Object.keys(nameToCellIdMap)[j]; // Get the column name based on the cell index
      
      if (columnName === 'credit_amount') {
        const cellValue = parseFloat(cell.textContent.replace(/,/g, ''));
       
        if (cellValue > 0) {
        debit+=cellValue;
        }
        else{
          debit+=0;
        }

      }

      else if  (columnName === 'debit_amount') {
        const cellValue = parseFloat(cell.textContent.replace(/,/g, ''));
        if (cellValue > 0) {
  
          
      credit+=cellValue;
    
        }

        else{
          credit+=0;
        }
      }
    }


  }


  diffe = debit - credit;
 
  var formattedDiff = diffe.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  var formattedDebit = debit.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  var formattedCredit = credit.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  
  // Set the formatted values into the corresponding HTML elements using their IDs.
  $('#diff').val(formattedDiff);
  $('#debittotal').val(formattedDebit);
  $('#credittotal').val(formattedCredit);


  total_credit= formattedCredit;
  total_debit = formattedDebit;
  total_diff = formattedDiff;

  console.log('1--:',formattedCredit)
  console.log('1--:',formattedDebit)
  console.log('1--:',formattedDiff)
}
 /// AFTER CLICK OKEY IN SELECT TRANSTYPE ///
document.getElementById("TransTypeForm").addEventListener("submit", function(event) {
  event.preventDefault(); // Prevent the default form submission behavior

  var selectFields = document.querySelectorAll('textarea');
  selectFields.forEach(function (field) {
      field.removeAttribute('readonly');
      field.removeAttribute('disabled');
      field.value = ''
  });

  var dateFields = document.querySelectorAll('input[type="date"]');
  dateFields.forEach(function (field) {
      field.removeAttribute('readonly');
      field.removeAttribute('disabled');
  });

  var textFields = document.querySelectorAll('#paymentID input[type="text"]');
  textFields.forEach(function (field) {
      field.removeAttribute('readonly');
      field.removeAttribute('disabled');
      field.value = ''
  });

  var textFields = document.querySelectorAll('input[type="text"]');
  textFields.forEach(function (field) {
      field.removeAttribute('readonly');
      field.removeAttribute('disabled');

  });


  
  var textFields = document.querySelectorAll('select');
  textFields.forEach(function (field) {
    field.removeAttribute('disabled'); // Remove 'disabled' attribute if needed
  });


  
  var textFields = document.querySelectorAll('button');
  textFields.forEach(function (field) {
    field.removeAttribute('disabled'); // Remove 'disabled' attribute if needed
  });



  var textFields = document.querySelectorAll('#acctEntryBody tr');
  textFields.forEach(function(trElement) {
    trElement.remove();
  });
  TransModal.style.display = 'none';

  var transactionTypeID = document.getElementById('transactionTypeID');
  var remark = document.getElementById('remarks');

    var selectedOption = transactionTypeID.options[transactionTypeID.selectedIndex];
    remark.value = selectedOption.text;
    $('#debittotal').prop('readonly', true);
    $('#credittotal').prop('readonly', true);
    $('#diff').prop('readonly', true);
  doc_typeRefresh();
  cvNumber();
  openTab(1);
  var payee = document.getElementById('payeeInput');
  payee.focus();
});


$('#oktranstype').on('keydown', function(event){
if (event.key === 'Enter'){
  event.preventDefault(); // Prevent the default form submission behavior

  var selectFields = document.querySelectorAll('textarea');
  selectFields.forEach(function (field) {
      field.removeAttribute('readonly');
      field.removeAttribute('disabled');
      field.value = ''
  });

  var dateFields = document.querySelectorAll('input[type="date"]');
  dateFields.forEach(function (field) {
      field.removeAttribute('readonly');
      field.removeAttribute('disabled');
  });

  var textFields = document.querySelectorAll('#paymentID input[type="text"]');
  textFields.forEach(function (field) {
      field.removeAttribute('readonly');
      field.removeAttribute('disabled');
      field.value = ''
  });
  var textFields = document.querySelectorAll('input[type="text"]');
  textFields.forEach(function (field) {
      field.removeAttribute('readonly');
      field.removeAttribute('disabled');
  });
  var textFields = document.querySelectorAll('select');
  textFields.forEach(function (field) {
    field.removeAttribute('disabled'); // Remove 'disabled' attribute if needed
    field.removeAttribute('disabled');
  });


  var textFields = document.querySelectorAll('button');
  textFields.forEach(function (field) {
    field.removeAttribute('disabled');

  });

  var textFields = document.querySelectorAll('#acctEntryBody tr');
  textFields.forEach(function(trElement) {
    trElement.remove();
  });
  TransModal.style.display = 'none';

  var transactionTypeID = document.getElementById('transactionTypeID');
  var remark = document.getElementById('remarks');

    var selectedOption = transactionTypeID.options[transactionTypeID.selectedIndex];
    remark.value = selectedOption.text;
    $('#debittotal').prop('readonly', true);
    $('#credittotal').prop('readonly', true);
    $('#diff').prop('readonly', true);
    // $('#ul').prop('readonly', true);
    doc_typeRefresh();
  cvNumber();
  openTab(1);
  var payee = document.getElementById('payeeInput');
  payee.focus();
}
});



function openTab(tabIndex) {
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




var checkNo = document.getElementById("checkNo");
checkNo.addEventListener("input", function() {
  var currentValue = checkNo.value;
  // Remove non-numeric characters
  var numericValue = currentValue.replace(/[^0-9]/g, "");
  // Update the input field value
  checkNo.value = numericValue;
});

function cvNumber() {
    doctype = 'CV';
    // console.log(doctype);
  $.ajax({
    url: '/api/cv-number/',
    method: 'GET',
    data: { doctype: doctype },
    success: function(response) {
      var cvNumber = response.cv_number;
      // console.log(cvNumber);
      var docrefInput = $('#docref');
      if (cvNumber !== null) {
        var formattedNumber = String(cvNumber).padStart(10, '0');
        docrefInput.val(formattedNumber);
      } else {
        docrefInput.val('No CV number found.');
      }
    },
    error: function(xhr, textStatus, errorThrown) {
      console.log('Error:', errorThrown);
    }
  });
}


function cvNumberwith(doctype) {
  if (doctype ===''){
    doctype = 'CV';
  }
  $.ajax({
    url: '/api/cv-number/',
    method: 'GET',
    data: { doctype: doctype },
    success: function(response) {
      var cvNumber = response.cv_number;
      // console.log(cvNumber);
      var docrefInput = $('#docref');
      if (cvNumber !== null) {
        var formattedNumber = String(cvNumber).padStart(10, '0');
        docrefInput.val(formattedNumber);
      } else {
        docrefInput.val('No CV number found.');
      }
    },
    error: function(xhr, textStatus, errorThrown) {
      console.log('Error:', errorThrown);
    }
  });
}

function addAccountEntry() {
  const table = document.getElementById('AcctEntry');
  const tbody = document.getElementById('acctEntryBody');

  const newRow = document.createElement('tr');
  const ul = document.createElement('td');
  const acctCode = document.createElement('td');
  const acctTitle = document.createElement('td');
  const slAcct = document.createElement('td');
  const debit = document.createElement('td');
  const credit = document.createElement('td');


  // if (isNaN('#credit')) {
  //   $('#credit').val('0.00');
  // } else if (isNaN($('#debit').val())) {
  //   $('#debit').val('0.00');
  // }



  var ulentry = document.getElementById('ul').value;
  var codeentry = document.getElementById('accCode').value;
  var TITLEentry = document.getElementById('accTitle').value;
  var slentry = document.getElementById('slAcc').value;
  var debitentry = document.getElementById('debit').value;
  var creditentry = document.getElementById('credit').value;

  ul.textContent = ulentry;
  acctCode.textContent = codeentry;
  acctTitle.textContent = TITLEentry;
  slAcct.textContent = slentry;
  // debit.textContent = debitentry;
  // credit.textContent = creditentry;
  var debitValue = parseFloat(debitentry); // Convert string to a number
  var creditValue = parseFloat(creditentry); // Convert string to a number
  
  debit.textContent = debitValue.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  credit.textContent = creditValue.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });

  
  const buttonCell = document.createElement('td');
  const Delete = document.createElement('button');
  Delete.classList.add('btn', 'btn-primary');
  const icon = document.createElement('i');
  icon.classList.add('fas', 'fa-trash');
  Delete.textContent = 'Delete';
  Delete.addEventListener('click', function() {
    var parentElement = Delete.parentNode;
    parentElement.parentNode.remove();
    // debitCredit();
  });




  const nameToCellIdMap = {
    ul_code: 'cell-ul-code',
    acct_code: 'cell-acct-code',
    acct_title: 'cell-acct-title',
    sl_acct: 'cell-sl-acct',
    credit_amount: 'cell-credit-amount',
    debit_amount: 'cell-debit-amount',
    code: 'cell-code',
    code1: 'cell-code1',
    code2: 'cell-code2',
    code3: 'cell-code3',

  };
  
  // Get the existing table
  const deletetable = document.getElementById('AcctEntry'); // Replace "your-table-id" with the actual ID of your table element
  const rows = deletetable.getElementsByTagName('tr'); // Get all the rows in the table

  for (let i = 0; i < rows.length; i++) {
    const row = rows[i];
    const cells = row.getElementsByTagName('td'); // Get all the cells in the current row
    
    for (let j = 0; j < cells.length; j++) {
      const cell = cells[j];
      const columnName = Object.keys(nameToCellIdMap)[j]; // Get the column name based on the cell index
      
      if (columnName === 'sl_acct') {
        const cellValue = cell.textContent; // Get the numeric value from the cell
        
        if (cellValue === slentry) {
          row.remove();
        }
      }

    }
  }
      
  GetAccountCodeIndividual(TITLEentry);

  if (slentry=='GENERAL'){
    localStorage.sl_id_code ='9999'
  }

  else{
    var c = localStorage.sl_type_per_acct_Title
    GetSLCodeEntry(c,slentry);
  }


  // console.log('code invidual:',localStorage.acct_code0,localStorage.acct_code1,localStorage.acct_code2,localStorage.acct_code3,localStorage.sl_id_code)
  const sl_code = document.createElement('td');
  sl_code.textContent = localStorage.sl_id_code;
  sl_code.classList.add('hidden');
  // newRow.appendChild(sl_code);

  const code = document.createElement('td');
  code.textContent = localStorage.acct_code0;
  code.classList.add('hidden');
  // newRow.appendChild(code);
  const code1 = document.createElement('td');
  code1.textContent = localStorage.acct_code1;
  code1.classList.add('hidden');
  // newRow.appendChild(code1);

  const code2 = document.createElement('td');
  code2.textContent = localStorage.acct_code2;
  code2.classList.add('hidden');
  // newRow.appendChild(code2);

  const code3 = document.createElement('td');
  code3.textContent = localStorage.acct_code3;
  code3.classList.add('hidden');


  ul.appendChild(Delete);
  newRow.appendChild(ul);
  newRow.appendChild(acctCode);
  newRow.appendChild(acctTitle);
  newRow.appendChild(slAcct);
  newRow.appendChild(debit);
  newRow.appendChild(credit);
  newRow.appendChild(buttonCell);
  newRow.appendChild(sl_code);
  newRow.appendChild(code);
  newRow.appendChild(code1);
  newRow.appendChild(code2);
  newRow.appendChild(code3);
  // buttonCell.appendChild(Edit);
  buttonCell.appendChild(Delete);
  // buttonCell.appendChild(Details);
  tbody.appendChild(newRow);

//  document.getElementById('ul').value = '';
 document.getElementById('accCode').value = '';
 document.getElementById('accTitle').value = '';
 document.getElementById('slAcc').value = '';
 document.getElementById('debit').value = '0.00';
 document.getElementById('credit').value = '0.00';

 DisplayAddentryModal();
}

var addEntryYes = document.getElementById('AddEntryYes');

var addEntryNo = document.getElementById('AddEntryNo');
var AddNewEntry = document.getElementById('AddNewEntry');
var addEntryModal = document.getElementById('AddEntry');


$('#AddEntryYes').on('keydown', function(event) {
  if (event.key === 'Escape') {
    // Perform your desired action here when the "Escape" key is pressed
    console.log('Escape key pressed');
  }
  else if (event.key === 'Enter'){
    event.preventDefault();
    addEntryModal.style.display = 'none';
    var acctContainer = document.getElementById('acctContainer');
    var acctContainer = document.getElementById('acctContainer');
    acctContainer.style.display = 'block';
    $('#debit').val('0.00');
    $('#credit').val('0.00');
    $('#accCode').focus();
    

  }
});

$('#AddEntryNo').on('keydown', function(event) {
  if (event.key === 'Escape') {
    // Perform your desired action here when the "Escape" key is pressed
    console.log('Escape key pressed');
  }
  else if (event.key === 'Enter'){
    event.preventDefault();
    addEntryModal.style.display = 'none';

    if (UpdateCDB == false){
      SaveEntryModal.style.display = 'block';
      var SaveYes = document.getElementById('SaveYes');
      SaveYes.focus();

    }

    else{
      UpdatetransactionModal.style.display = 'block';
      var UpdateYes = document.getElementById('UpdateYes');
      UpdateYes.focus();
    }
    var acctContainer = document.getElementById('acctContainer');
    acctContainer.style.display = 'none';
  }
});





function DisplayAddentryModal(){
addEntryModal.style.display = 'block';
addEntryYes.focus();
}


addEntryYes.addEventListener('click',function(){
  addEntryModal.style.display = 'none';
  var acctContainer = document.getElementById('acctContainer');
  acctContainer.style.display = 'block';
  $('#accCode').focus();
  $('#debit').val('0.00');
  $('#credit').val('0.00');
});


addEntryNo.addEventListener('click',function(){

  console.log('rrrrr',UpdateCDB);
addEntryModal.style.display = 'none';
var acctContainer = document.getElementById('acctContainer');
acctContainer.style.display = 'none';
if (UpdateCDB == false){
  SaveEntryModal.style.display = 'block';
  var SaveYes = document.getElementById('SaveYes');
  SaveYes.focus();

}

else{
  UpdatetransactionModal.style.display = 'block';
  var UpdateYes = document.getElementById('UpdateYes');
  UpdateYes.focus();
}
var acctContainer = document.getElementById('acctContainer');
acctContainer.style.display = 'none';

});



AddNewEntry.addEventListener('click',function(){
  DisplayAddentryModal();
  addEntryYes.focus();
});


// INPUT NUMERIC ONLY DEBIT
var debit = document.getElementById("debit");
debit.addEventListener("input", function() {
  var currentValue = debit.value;
  // Remove non-numeric characters
  var numericValue = currentValue.replace(/[^0-9.]/g, "");
  // Update the input field value
  debit.value = numericValue;
});

// INPUT NUMERIC ONLY CREDIT
var credit = document.getElementById("credit");
credit.addEventListener("input", function() {
  var currentValue = credit.value;
  // Remove non-numeric and non-decimal characters
  var numericValue = currentValue.replace(/[^0-9.]/g, "");
  // Update the input field value
  credit.value = numericValue;
});

const modalContainer = document.getElementById('AddEntry');
const buttons = modalContainer.querySelectorAll('.modal-buttons button');

let selectedButtonIndex = 0; // Current selected button index

modalContainer.addEventListener('keydown', function(event) {
  const key = event.key;
  if (key === 'ArrowLeft' && selectedButtonIndex > 0) {
    selectedButtonIndex--; // Decrement the selected button index
  } else if (key === 'ArrowRight' && selectedButtonIndex < buttons.length - 1) {
    selectedButtonIndex++; // Increment the selected button index
  }

  buttons.forEach(function(button, index) {
    if (index === selectedButtonIndex) {
      button.classList.add('selected'); // Add a class to highlight the selected button
    } else {
      button.classList.remove('selected'); // Remove the class from other buttons
    }
  });

  buttons[selectedButtonIndex].focus(); // Set focus on the newly selected button
});

// const confirmationModal = document.getElementById('confirmationModal');




const ApplicationOfPaymentModal = document.getElementById('ApplicationOfPayment');
function ApplicationOfPayment(){
$('#applicationTable').empty();
  ApplicationOfPaymentModal.style.display='block';
}

var okf10 = document.getElementById('okf10');
okf10.addEventListener('click',function(){
  ApplicationOfPaymentModal.style.display='none';
});



$('#confirmAbort').on('click', function(){
  AbortEncoding.style.display='none';
  acctContainer.style.display='none';
  $('#payeeInput').focus();
});


$('#confirmAbort').on('keydown', function(event){
  if (event.key === 'Enter'){
event.preventDefault();
    // console.log('cofirm:')
    AbortEncoding.style.display='none';
    acctContainer.style.display='none';
    $('#payeeInput').focus();
    return;
  }

else if (event.key === 'Escape') {
  AbortEncoding.style.display='none';
  $('#accCode').focus();
}
});


$('#cancelAbort').on('click', function(){
  AbortEncoding.style.display='none';
  $('#accCode').focus();
});

$('#cancelAbort').on('keydown', function(event){
  if (event.key === 'Enter'){
    event.preventDefault();
    AbortEncoding.style.display='none';
    $('#accCode').focus();
  }
});

const buttons2 = Array.from(document.querySelectorAll('#AbortEncoding button'));
$('#AbortEncoding').on('keydown', function(event) {
  // console.log('11');
  const key = event.key;
  if (key === 'ArrowLeft' && selectedButtonIndex > 0) {
    selectedButtonIndex--; // Decrement the selected button index
  } else if (key === 'ArrowRight' && selectedButtonIndex < buttons2.length - 1) {
    selectedButtonIndex++; // Increment the selected button index

  }

  buttons2.forEach(function(button, index) {
    if (index === selectedButtonIndex) {
      button.classList.add('selected'); // Add a class to highlight the selected button
    } else {
      button.classList.remove('selected'); // Remove the class from other buttons
    }
  });

  buttons2[selectedButtonIndex].focus(); // Set focus on the newly selected button
});


const buttons3 = Array.from(document.querySelectorAll('#confirmationModal button'));
$('#confirmationModal').on('keydown', function(event) {
  // console.log('11');
  const key = event.key;
  if (key === 'ArrowLeft' && selectedButtonIndex > 0) {
    selectedButtonIndex--; // Decrement the selected button index
  } else if (key === 'ArrowRight' && selectedButtonIndex < buttons3.length - 1) {
    selectedButtonIndex++; // Increment the selected button index

  }

  buttons3.forEach(function(button, index) {
    if (index === selectedButtonIndex) {
      button.classList.add('selected'); // Add a class to highlight the selected button
    } else {
      button.classList.remove('selected'); // Remove the class from other buttons
    }
  });

  buttons3[selectedButtonIndex].focus(); // Set focus on the newly selected button
});

$('#doctype').on('change', function() {
  // console.log($('#doctype').val());
  if ($(this).val() === 'Cash in Bank' || $(this).val() === 'CV-PDC') {
    $('label[for="docref"]').text('Check Voucher No.');
    $('label[for="Amount"]').text('Amt Check:');
    $('label[for="draweeInput"]').text('Drawee Bank:');
    $('#draweeInput').prop('readonly',false);
    $('#Dateidcheck').prop('readonly',false);
    $('#checkNo').prop('readonly',false);
    $('#draweeInput').val('');

  } else if ($(this).val() === 'Petty Cash Fund') {
    $('label[for="docref"]').text('Petty Cash Voucher No.');
    $('label[for="Amount"]').text('Amt PCV:');
    $('label[for="draweeInput"]').text('Drawee Bank:');
    $('#draweeInput').prop('readonly',true);
    $('#Dateidcheck').prop('readonly',true);
    $('#checkNo').prop('readonly',true);
    $('#draweeInput').val('GENERAL');

  } else if ($(this).val() === 'Revolving Fund') {
    $('label[for="docref"]').text('Revolving Fund Voucher No.');
    $('label[for="Amount"]').text('Amt RFV:');
    $('label[for="draweeInput"]').text('Subsidiary Gedger:');
    $('#draweeInput').prop('readonly',true);
    $('#Dateidcheck').prop('readonly',true);
    $('#checkNo').prop('readonly',true);
    $('#draweeInput').val('GENERAL');

  }
  var selectedText = $(this).find('option:selected').text();
  cvNumberwith(selectedText);
});

$('#Account_title').on('input', function()  {
  var acct_title = $(this).val();
  if (acct_title.trim() === '') {
    $('#acctTilteList').empty();
    return;
  }
  $.ajax({
    url: '/api/acct-title-list/',
    method: 'GET',
    data: { acct_title: acct_title },
    success: function(data) {
      var resultsContainer = $('#acctTilteList');
      resultsContainer.empty(); // Clear existing results
      if (data.length > 0) {
        var resultsHtml = '<ul>';

        // console.log('acct_title_list');
        data.forEach(function(acct_title_list) {
          // console.log('qqq',acct_title_list)
          resultsHtml += '<li data-id="'+ acct_title_list.code + '">' + acct_title_list.code + ' - ' +  acct_title_list.acct_title + '</li>';
          // resultsHtml += '<li class="accCode-item" data-id="'+ acct_title_list.code + '">' + acct_title_list.code + ' - ' +  acct_title_list.acct_title + '</li>';

        });
        resultsHtml += '</ul>';
        resultsContainer.html(resultsHtml);
        
        // Handle click event on the list items
        $('#acctTilteList li').click(function() {
          // var selectedId = $(this).data('id');
          // Perform your desired action with the selectedId
          var accCode = $(this).data('id');
          var accTitle = $(this).text().split(' - ')[1];
          var acctTitle2 = $(this).text().split(' - ')[2];

          if (!acctTitle2) {
            $('#Account_title').val(accTitle);
          } else {
            const combinedText = accTitle + ' - ' + acctTitle2;
            $('#Account_title').val(combinedText);
          }

          var accTitle = document.getElementById('Account_title');

          // Clear the search results and hide the container
          resultsContainer.empty();
          // accTitle.focus();
          $('#fromApp').focus();
        });
      } else {
        resultsContainer.html('No results found.');
      }
    },
    error: function(xhr, textStatus, errorThrown) {
      console.log('Error:', errorThrown);
    }
  });
});


$('#Account_title').on('keydown', function(event) {

  const key = event.key;
  const resultsContainer = $('#acctTilteList');
  const payeeItems = resultsContainer.find('li');

  if (key === 'ArrowDown') {
    event.preventDefault();
    const currentSelectedItem = payeeItems.filter('.selected');
    const nextItem = currentSelectedItem.next('li');
    if (nextItem.length) {
      currentSelectedItem.removeClass('selected');
      nextItem.addClass('selected');
      const acctTitle = nextItem.text();
      $('#Account_title').val(acctTitle);
      nextItem.focus();

    } else {
      payeeItems.first().addClass('selected');
    }
  } else if (key === 'ArrowUp') {
    event.preventDefault();
    const currentSelectedItem = payeeItems.filter('.selected');
    const prevItem = currentSelectedItem.prev('li');
    if (prevItem.length) {
      currentSelectedItem.removeClass('selected');
      prevItem.addClass('selected');
      const acctTitle = prevItem.text();
      $('#Account_title').val(acctTitle);
      prevItem.focus();

    } else {
      payeeItems.last().addClass('selected');
    }

  } else if (key === 'Enter') {
    const selectedItem = payeeItems.filter('.selected');
    if (selectedItem.length) {
      // Handle the selected item
      const slid = selectedItem.attr('data-id');
      // const acctTitle = selectedItem.text().split(' - ')[1];
      var accTitle = selectedItem.text().split(' - ')[1];
      var acctTitle2 = selectedItem.text().split(' - ')[2];

      if (!acctTitle2) {
        $('#Account_title').val(accTitle);
      } else {
        const combinedText = accTitle + ' - ' + acctTitle2;
        $('#Account_title').val(combinedText);
      }
      // $('#Account_title').val(acctTitle);
      resultsContainer.empty();
      // payeeText.focus();

      var credit = document.getElementById('credit');
      credit.focus();
      // Perform further actions as needed
    }
  }
  // if (event.key === 'Enter') {
  //   // Perform your desired action here when the "Escape" key is pressed
  //   event.preventDefault();

  // }
});


function notFound(){

   // Create a new <div> element
   const flashMessageDiv = document.createElement('div');

   // Set the flash message content
   flashMessageDiv.innerHTML = '<i class="fa fa-info-circle"></i>No Record Found.!!';
 
   // Add CSS class for centering the flash message
   flashMessageDiv.classList.add('centered-message');
 
   // Add other CSS styling to the flash message (optional)
   // flashMessageDiv.style.backgroundColor = 'yellow';
   // flashMessageDiv.style.color = 'black';
   flashMessageDiv.style.padding = '10px';
   flashMessageDiv.style.borderRadius = '5px';
   flashMessageDiv.style.zIndex = '99999';
 
   // Append the flash message element to the body (you can change this to another container if needed)
   document.body.appendChild(flashMessageDiv);
 
   // Remove the flash message after a certain duration (e.g., 3 seconds)
   setTimeout(function() {
     document.body.removeChild(flashMessageDiv);
   }, 3000); // 3000 milliseconds = 3 seconds
}

var SaveData = document.getElementById('SaveData');
SaveData.addEventListener('click',function(){

  debit = $('#debittotal').val();
  credit = $('#credittotal').val();
  diff = $('#diff').val();

  console.log('Debit:', debit);
  console.log('credit:', credit);
  console.log('diff:', diff);

  if (debit !=='' && parseFloat(diff *-1)===0){
    // SaveEntryModal.style.display='block'
    // SaveEntryModal.zIndex = 9999999;
    // $('#SaveYes').focus();

    
    if (UpdateCDB == false){
      SaveEntryModal.style.display = 'block';
      var SaveYes = document.getElementById('SaveYes');
      SaveYes.focus();

    }
    else{
      UpdatetransactionModal.style.display = 'block';
      var UpdateYes = document.getElementById('UpdateYes');
      UpdateYes.focus();
    }
  }

  else if (parseFloat(credit)===0  && parseFloat(diff)===0 && parseFloat(debit)===0) {
    const flashMessageDiv = document.createElement('div');

    // Set the flash message content
    flashMessageDiv.innerHTML = '<i class="fa fa-info-circle"></i>Please Add Transaction...!!';
  
    flashMessageDiv.classList.add('centered-message');

    flashMessageDiv.style.padding = '10px';
    flashMessageDiv.style.borderRadius = '5px';
    flashMessageDiv.style.zIndex = '99999';
    document.body.appendChild(flashMessageDiv);
  
    setTimeout(function() {
      document.body.removeChild(flashMessageDiv);
    }, 3000); // 3000 milliseconds = 3 seconds
  }


  else if (credit==='' && debit==='' && credit==='') {
    const flashMessageDiv = document.createElement('div');

    // Set the flash message content
    flashMessageDiv.innerHTML = '<i class="fa fa-info-circle"></i>Please Add Transaction...!!';
  
    flashMessageDiv.classList.add('centered-message');

    flashMessageDiv.style.padding = '10px';
    flashMessageDiv.style.borderRadius = '5px';
    flashMessageDiv.style.zIndex = '99999';
    document.body.appendChild(flashMessageDiv);
  
    setTimeout(function() {
      document.body.removeChild(flashMessageDiv);
    }, 3000); // 3000 milliseconds = 3 seconds
  }

  else{
    const flashMessageDiv = document.createElement('div');

    // Set the flash message content
    flashMessageDiv.innerHTML = '<i class="fa fa-info-circle"></i>Debit and Credit is Not Equal...!!';
  
    flashMessageDiv.classList.add('centered-message');

    flashMessageDiv.style.padding = '10px';
    flashMessageDiv.style.borderRadius = '5px';
    flashMessageDiv.style.zIndex = '99999';
    document.body.appendChild(flashMessageDiv);
  
    setTimeout(function() {
      document.body.removeChild(flashMessageDiv);
    }, 3000); // 3000 milliseconds = 3 seconds
  }

});


const SaveButton = Array.from(document.querySelectorAll('#savetransaction button'));
$('#savetransaction').on('keydown', function(event) {
  // console.log('11');
  const key = event.key;
  if (key === 'ArrowLeft' && selectedButtonIndex > 0) {
    selectedButtonIndex--; // Decrement the selected button index
  } else if (key === 'ArrowRight' && selectedButtonIndex < SaveButton.length - 1) {
    selectedButtonIndex++; // Increment the selected button index

  }

  SaveButton.forEach(function(button, index) {
    if (index === selectedButtonIndex) {
      button.classList.add('selected'); // Add a class to highlight the selected button
    } else {
      button.classList.remove('selected'); // Remove the class from other buttons
    }
  });

  SaveButton[selectedButtonIndex].focus(); // Set focus on the newly selected button
});

$('#SaveNo').on('click', function(){
  SaveEntryModal.style.display ='none'
  $('#payeeInput').focus();
});




$('#SaveYes').on('click', function(){
  SaveEntryModal.style.display ='none'
  var payee = $('#payeeInput').val();
  var bank  = $('#draweeInput').val();
  // var bank  = $('#draweeInput').find('option:selected').text();
  var Entrylist = list_of_applied;
  var EntryTotal = list_of_applied_total;
  var totaldebit = $('#debittotal').val();
  var totalcredit = $('#credittotal').val();
  var doc_type = $('#doctype').find('option:selected').text()
  var docref = $('#docref').val();
  var Voucherdate = $('#Date').val();
  var Checkdate = $('#Dateidcheck').val();
  var checkNo = $('#checkNo').val();
  var remark = $('#remarks').val();
  var prepared = $('#prepared').find('option:selected').text()
  var reviewed =$('#reviewed').find('option:selected').text()
  var approved = $('#approved').find('option:selected').text()
  var transactionTypeID = $('#transactionTypeID').find('option:selected').text()

  totaldebit =parseFloat(totaldebit.replace(',', ''));
  totalcredit = parseFloat(totalcredit.replace(',', ''));
  // var prepared = $('#prepared').val();
  // var reviewed = $('#reviewed').val();
  // var approved = $('#approved').val();
  // var payeeid = selectedId;
  // console.log('payee',payee);
  // console.log('bank',bank);
  // console.log('Entrylist',Entrylist);
  // console.log('EntryTotal',EntryTotal);
  // console.log('totaldebit',total_debit);
  // console.log('totalcredit',total_credit);
  // console.log('doc_type',doc_type);
  // console.log('Voucherdate',Voucherdate);
  // console.log('Checkdate',Checkdate);
  // console.log('docref',docref);
  // console.log('checkNo',checkNo);
  // console.log('remark',remark);
  // console.log('prepared',prepared);
  // console.log('reviewed',reviewed);
  // console.log('approved',approved);



  const nameToCellIdMap = {
    ul_code: 'cell-ul-code',
    acct_code: 'cell-acct-code',
    acct_title: 'cell-acct-title',
    sl_acct: 'cell-sl-acct',
    debit_amount: 'cell-debit-amount',
    credit_amount: 'cell-credit-amount',
    button: 'cell-button',
    id_code: 'cell-id-code',
    primary_code: 'cell-primary-code',
    secondary_code: 'cell-secondary-code',
    acct_code2: 'cell-acct-code',
    subsidiary_code: 'cell-subsidiary-code',
  };


  const table = document.getElementById('AcctEntry'); // Replace "your-table-id" with the actual ID of your table element
  const rows = table.getElementsByTagName('tr'); // Get all the rows in the table
  
  const table_list = []; // Create an array to store the data (column name and value)
  
  for (let i = 1; i < rows.length; i++) {
    const row = rows[i];
    const cells = row.getElementsByTagName('td'); // Get all the cells in the current row
  
    const rowData = {}; // Create an object to store the data for the current row
  
    for (let j = 0; j < cells.length; j++) {
      const cell = cells[j];
      const columnName = Object.keys(nameToCellIdMap)[j];
      const cellValue = cell.textContent.trim(); // Get the text content of the cell and remove any leading/trailing whitespace
      rowData[columnName] = cellValue; // Associate the column name with the cell value in the rowData object
    }
  
    table_list.push(rowData); // Add the rowData object to the data array
  }
  console.log(table_list); 
  var csrfToken = $('#accountEntryID [name=csrfmiddlewaretoken]').val();

  $.ajax({
    url: '/api/Save-Cash-Disbursement/',
    method: 'POST',
    headers: {
      'X-CSRFToken': csrfToken  // Include the CSRF token in the headers
    },
    dataType: 'json',
    data: {payeeId : selectedId,
           payee: payee,
          bank: bank,
          doc_type: doc_type,
          docref: docref,
          Voucherdate: Voucherdate,
          Checkdate: Checkdate,
          checkNo: checkNo,
          totalcredit: totalcredit,
          totaldebit: totaldebit,
          remarks: remark,
          approved: approved,
          reviewed:reviewed,
          prepared:prepared,
          transactionTypeID:transactionTypeID,
          table_list: JSON.stringify(table_list) },
    success: function(data) {
      const flashMessageDiv = document.createElement('div');
      flashMessageDiv.innerHTML = '<i class="fa fa-info-circle"></i>Transaction Successfully Save...!!';
    
      flashMessageDiv.classList.add('centered-message');
  
      flashMessageDiv.style.padding = '10px';
      flashMessageDiv.style.borderRadius = '5px';
      flashMessageDiv.style.zIndex = '99999';
      document.body.appendChild(flashMessageDiv);
      setTimeout(function() {
        document.body.removeChild(flashMessageDiv);
      }, 3000); // 3000 milliseconds = 3 seconds
      // window.location.href = "{ url 'index' }";
      SetDataFields();
    }
    
  });
});

$('#SaveYes').on('keydown', function(event){
  if (event.key === 'Enter'){
    event.preventDefault();
  SaveEntryModal.style.display ='none'
  var payee = $('#payeeInput').val();
  var bank  = $('#draweeInput').val();
  // var bank  = $('#draweeInput').find('option:selected').text();
  var Entrylist = list_of_applied;
  var EntryTotal = list_of_applied_total;
  var totaldebit = $('#debittotal').val();
  var totalcredit = $('#credittotal').val();
  var doc_type = $('#doctype').find('option:selected').text()
  var docref = $('#docref').val();
  var Voucherdate = $('#Date').val();
  var Checkdate = $('#Dateidcheck').val();
  var checkNo = $('#checkNo').val();
  var remark = $('#remarks').val();
  var prepared = $('#prepared').find('option:selected').text()
  var reviewed =$('#reviewed').find('option:selected').text()
  var approved = $('#approved').find('option:selected').text()
  var transactionTypeID = $('#transactionTypeID').find('option:selected').text()

  totaldebit =parseFloat(totaldebit.replace(',', ''));
  totalcredit = parseFloat(totalcredit.replace(',', ''));

  var payeeid = selectedId;

  const nameToCellIdMap = {
    ul_code: 'cell-ul-code',
    acct_code: 'cell-acct-code',
    acct_title: 'cell-acct-title',
    sl_acct: 'cell-sl-acct',
    debit_amount: 'cell-debit-amount',
    credit_amount: 'cell-credit-amount',
    button: 'cell-button',
    id_code: 'cell-id-code',
    primary_code: 'cell-primary-code',
    secondary_code: 'cell-secondary-code',
    acct_code2: 'cell-acct-code',
    subsidiary_code: 'cell-subsidiary-code',
  };


  const table = document.getElementById('AcctEntry'); // Replace "your-table-id" with the actual ID of your table element
  const rows = table.getElementsByTagName('tr'); // Get all the rows in the table
  
  const table_list = []; // Create an array to store the data (column name and value)
  
  for (let i = 1; i < rows.length; i++) {
    const row = rows[i];
    const cells = row.getElementsByTagName('td'); // Get all the cells in the current row
  
    const rowData = {}; // Create an object to store the data for the current row
  
    for (let j = 0; j < cells.length; j++) {
      const cell = cells[j];
      const columnName = Object.keys(nameToCellIdMap)[j];
      const cellValue = cell.textContent.trim(); // Get the text content of the cell and remove any leading/trailing whitespace
      rowData[columnName] = cellValue; // Associate the column name with the cell value in the rowData object
    }
  
    table_list.push(rowData); // Add the rowData object to the data array
  }
  deleterow();
  // console.log('save listing:',table_list); 
  var csrfToken = $('#accountEntryID [name=csrfmiddlewaretoken]').val();
  
  $.ajax({
    url: '/api/Save-Cash-Disbursement/',
    method: 'POST',
    headers: {
      'X-CSRFToken': csrfToken  // Include the CSRF token in the headers
    },
    dataType: 'json',
    data: {payeeId : selectedId,
           payee: payee,
          bank: bank,
          doc_type: doc_type,
          docref: docref,
          Voucherdate: Voucherdate,
          Checkdate: Checkdate,
          checkNo: checkNo,
          totalcredit: totalcredit,
          totaldebit: totaldebit,
          remarks: remark,
          approved: approved,
          reviewed:reviewed,
          prepared:prepared,
          transactionTypeID:transactionTypeID,
          table_list: JSON.stringify(table_list) },
    success: function(data) {
      const flashMessageDiv = document.createElement('div');
      // flashMessageDiv.innerHTML = '<i class="fa fa-info-circle"></i>Transaction Successfully Save...!!';
      flashMessageDiv.innerHTML = `<i class="fa fa-info-circle"></i> ${data.message}`;
      flashMessageDiv.classList.add('centered-message');
  
      flashMessageDiv.style.padding = '10px';
      flashMessageDiv.style.borderRadius = '5px';
      flashMessageDiv.style.zIndex = '99999';
      document.body.appendChild(flashMessageDiv);
      setTimeout(function() {
        document.body.removeChild(flashMessageDiv);
      }, 3000); // 3000 milliseconds = 3 seconds
      setTimeout(function() {
        window.location.reload();
      }, 3000);
      SetDataFields();
    }
    
  });
}
});

function SetDataFields(){
  cv_no = ''
  $.ajax({
    url: '/api/set-data-fields/',
    type: 'GET',
    data: {
      cv_no: cv_no
    },
    success: function(data) {
      var inputElement = document.getElementById("payeeInput");

        inputElement.setAttribute("data-customdata",data[4]);
        $('#payeeInput').val(data[5]);
        $('#doctype').find('option:selected').text(data[3])
        $('#docref').val(data[0]);
        cv_no = data[0];
        check_number=data[9];
        $('#Voucherdate').val(data[2]);
        console.log('Amount:',data[6]);
        $('#Amount').val(data[6].toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 }));
        $('#checkNo').val(data[9]);
        $('#remarks').val(data[10]);
        $('#transactionTypeID').val(data[11]);
        $('#prepared').text=data[12];
        $('#draweeInput').val(data[7]);
        $('#reviewed').text=data[13];
        $('#approved').text=data[14];

        
        DisplayEntry();
        // debitCredit2();
    }

  });
}


function DisplayEntry(){
  // console.log('cv_no:g',cv_no);
  $.ajax({
    url: '/api/set-display-entry/',
    type: 'GET',
    data: {
      cv_no: cv_no,
      checkNo: check_number,
    },

   
    success: function(data) {
      data.sort((a, b) => b.debit_amount - a.debit_amount);
      let debit1 = 0
      let credit1 = 0
      let diffe1 = 0
      for (var i = 0; i < data.length; i++) {
        var entry = data[i];

        const table = document.getElementById('AcctEntry');
        const tbody = document.getElementById('acctEntryBody');
      
        const newRow = document.createElement('tr');
        const ul = document.createElement('td');
        const acctCode = document.createElement('td');
        const acctTitle = document.createElement('td');
        const slAcct = document.createElement('td');
        const debit = document.createElement('td');
        const credit = document.createElement('td');
      
        var ulentry =  entry['ul_code'];
        var codeentry =  entry['acct_code'];
        var TITLEentry = entry['acct_title'];
        var slentry =  entry['sl_name'];
        var debitentry =  entry['debit_amount'];
        var creditentry =  entry['credit_amount'];

        ul.textContent = ulentry;
        acctCode.textContent = codeentry;
        acctTitle.textContent = TITLEentry;
        slAcct.textContent = slentry;
    
        var debitValue = parseFloat(debitentry); 
        var creditValue =parseFloat(creditentry); 
     
        debit1 += parseFloat(debitentry);
        credit1 += parseFloat(creditentry);

        debit.textContent = debitValue.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
        credit.textContent = creditValue.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });

      
      const sl_code = document.createElement('td');
      sl_code.textContent =  entry['id_code'];
      sl_code.classList.add('hidden');

    
      const code = document.createElement('td');
      code.textContent = entry['primary_code'];
      code.classList.add('hidden');

      const code1 = document.createElement('td');
      code1.textContent =entry['secondary_code'];
      code1.classList.add('hidden');

    
      const code2 = document.createElement('td');
      code2.textContent = entry['acct_code2'];
      code2.classList.add('hidden');

    
      const code3 = document.createElement('td');
      code3.textContent = entry['subsidiary_code'];
      code3.classList.add('hidden');
        
        const buttonCell = document.createElement('td');
        const Delete = document.createElement('button');
        Delete.classList.add('btn', 'btn-primary');
        const icon = document.createElement('i');
        icon.classList.add('fas', 'fa-trash');
        Delete.textContent = 'Delete';
        Delete.addEventListener('click', function() {
          var parentElement = Delete.parentNode;
          parentElement.parentNode.remove();
          debitCredit();
        });
        ul.appendChild(Delete);
        newRow.appendChild(ul);
        newRow.appendChild(acctCode);
        newRow.appendChild(acctTitle);
        newRow.appendChild(slAcct);
        newRow.appendChild(debit);
        newRow.appendChild(credit);
        newRow.appendChild(buttonCell);
        newRow.appendChild(sl_code);
        newRow.appendChild(code);
        newRow.appendChild(code1);
        newRow.appendChild(code2);
        newRow.appendChild(code3);
        buttonCell.appendChild(Delete);
        tbody.appendChild(newRow);
      }
      
      diffe = debit1 - credit1;
      // console.log(debit1,credit1);
    
      $('#diff').val(diffe.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 }));
      $('#debittotal').val(debit1.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 }));
      $('#credittotal').val(credit1.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 }));
      // sortTableByNumericValues(5);
    },
    error: function(error) {
      console.error('Error:', error);
    }
  });
}

const tableRows = document.querySelectorAll('#tablerowtab tr');

// Add a click event listener to each row
tableRows.forEach((row, index) => {
  row.addEventListener('click', () => {
    // Get the index of the clicked row
    // console.log('Clicked row index:', index);
    deleterow();
    // Get the cell values in the clicked row
    const cells = row.querySelectorAll('td');
    const cellValues = Array.from(cells).map(cell => cell.textContent);
    cv_no = cellValues[2].split('#')[1];
    checkNo = cellValues[3];
    SetDataFields2(cv_no,checkNo);

    var edit = document.getElementById('EditTransaction');
    edit.removeAttribute('disabled')

    // edit.forEach(function (field) {
    //   field.removeAttribute('disabled');
  
    // });

    // $('#editButton').removeAttr('disabled');
    openTab(1);
    
  });
});

function deleterow(){
  const table = document.getElementById('acctEntryBody');

  // Remove all rows from the table
  while (table.rows.length > 0) {
    table.deleteRow(0);
}
}
function SetDataFields2(cv_no,checkNo){
  
  $.ajax({
    url: '/api/set-data-fields/',
    type: 'GET',
    data: {
      cv_no: cv_no,
      checkNo: checkNo,
    },
    success: function(data) {
      var inputElement = document.getElementById("payeeInput");

      inputElement.setAttribute("data-customdata",data[4]);
        $('#payeeInput').val(data[5]);
        $('#doctype').find('option:selected').text(data[3])
        $('#docref').val(data[0]);
        cv_no = data[0];
        check_number = data[9];
        $('#Voucherdate').val(data[2]);
        $('#Amount').val(data[6].toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 }));
        $('#checkNo').val(data[9]);
        $('#remarks').val(data[10]);
        $('#transactionTypeID').val(data[11]);
        $('#prepared').text=data[12];
        $('#draweeInput').val(data[7]);
        $('#reviewed').text=data[13];
        $('#approved').text=data[14];
        DisplayEntry();
  
    }

  });


}


function debitCredit2(){
  const nameToCellIdMap = {
    ul_code: 'cell-ul-code',
    acct_code: 'cell-acct-code',
    acct_title: 'cell-acct-title',
    sl_acct: 'cell-sl-acct',
    credit_amount: 'cell-credit-amount',
    debit_amount: 'cell-debit-amount',

  };
  var debit = 0;
  var credit = 0;
  var diffe = 0;


  const table = document.getElementById('acctEntryBody'); // Replace "your-table-id" with the actual ID of your table element
  const rows = table.getElementsByTagName('tr'); // Get all the rows in the table
  // console.log('1212',rows.length);
  for (let i = 0; i < rows.length; i++) {
    const row = rows[i];
    const cells = row.getElementsByTagName('td'); // Get all the cells in the current row
 
    for (let j = 0; j < cells.length; j++) {
      const cell = cells[j];
      // console.log('credi111t:',cell);
      const columnName = Object.keys(nameToCellIdMap)[j]; // Get the column name based on the cell index
      
      if (columnName === 'credit_amount') {
        const cellValue = parseFloat(cell.textContent.replace(',', ''));
        if (cellValue > 0) {
        debit+=cellValue;
        }
        else{
          debit+=0;
        }

      }

      else if  (columnName === 'debit_amount') {
        const cellValue = parseFloat(cell.textContent.replace(',', ''));
        if (cellValue > 0) {
  
          
      credit+=cellValue;
    
        }

        else{
          credit+=0;
        }
      }
    }
  }

  diffe = debit - credit;
  console.log(debit,credit);

  $('#diff').val(diffe.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 }));
  $('#debittotal').val(debit.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 }));
  $('#credittotal').val(credit.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 }));
  
}

$('#EditTransaction').on('click',function(){
  var selectFields = document.querySelectorAll('textarea');
  selectFields.forEach(function (field) {
      field.removeAttribute('readonly');
      field.removeAttribute('disabled');
  });

  var dateFields = document.querySelectorAll('input[type="date"]');
  dateFields.forEach(function (field) {
      field.removeAttribute('readonly');
      field.removeAttribute('disabled');
    
  });

  var textFields = document.querySelectorAll('input[type="text"]');
  textFields.forEach(function (field) {
      field.removeAttribute('readonly');
      field.removeAttribute('disabled');
 
  });

  var textFields = document.querySelectorAll('select');
  textFields.forEach(function (field) {
    field.removeAttribute('disabled'); // Remove 'disabled' attribute if needed
    field.removeAttribute('disabled');
  });


  var textFields = document.querySelectorAll('button');
  textFields.forEach(function (field) {
    field.removeAttribute('disabled');

  });

  var SaveData = document.getElementById('SaveData');

  SaveData.textContent = 'Update'
    UpdateCDB = true
    // var selectedOption = transactionTypeID.options[transactionTypeID.selectedIndex];
    // $('#remarks').value = selectedOption.text;
    $('#debittotal').prop('readonly', true);
    $('#credittotal').prop('readonly', true);
    $('#diff').prop('readonly', true);
    // $('#ul').prop('readonly', true);
    doc_typeRefresh();
  var payee = document.getElementById('payeeInput');
  payee.focus();
});



$('#ul').on('input', function()  {
  var ul = $(this).val();
  if (ul.trim() === '') {
    $('#ulResults').empty();
    return;
  }
  $.ajax({
    url: '/api/location-select/',
    method: 'GET',
    data: { ul: ul },
    success: function(data) {
      var resultsContainer = $('#ulResults');
      resultsContainer.empty(); // Clear existing results
      if (data.length > 0) {
        var resultsHtml = '<ul>';
        data.forEach(function(ul_list) {
          // resultsHtml += '<li data-id="'+ bank_drawee_list.id_code + '">' + bank_drawee_list.id_code + ' - ' +  bank_drawee_list.bank_abbreviation + '</li>';
          resultsHtml += '<li class="ul-item" data-id="'+ ul_list.ul_code + '">' + ul_list.ul_code + ' - ' +  ul_list.unit_description + '</li>';
          //resultsHtml += '<li class="drawee-item" data-id="'+ bank_drawee_list.id_code + '">' +  bank_drawee_list.bank_abbreviation + '</li>';
        });
        resultsHtml += '</ul>';
        resultsContainer.html(resultsHtml);
        

        // Handle click event on the list items
        $('#ulResults li').click(function() {
          // var draweeid = $(this).data('id');
          // Perform your desired action with the selectedId
           ul = $(this).data('id');
          var ul_description = $(this).text().split(' - ')[1];
          // $('#draweeInput').val(empty);

          document.getElementById('ul').value = '';
          // Set the selected value in the payeeInput

          $('#ul').val(ul);
         

          // Clear the search results and hide the container
          resultsContainer.empty();
          var accCode = document.getElementById('accCode');
          accCode.focus();
        });
      } else {
        resultsContainer.html('No results found.');
      }
    },
    error: function(xhr, textStatus, errorThrown) {
      console.log('Error:', errorThrown);
    }
  });
});



$('#ul').on('keydown',function(event){
  if (event.key ==='Enter'){
    event.preventDefault();
    var accCode = document.getElementById('accCode');
    accCode.focus();
  }
});
$('#ul').on('keydown', function(event) {

  const key = event.key;
  const resultsContainer = $('#ulResults');
  const ulitems = resultsContainer.find('li');

  if (key === 'ArrowDown') {
    event.preventDefault();
    const currentSelectedItem = ulitems.filter('.selected');
    const nextItem = currentSelectedItem.next('li');
    if (nextItem.length) {
      currentSelectedItem.removeClass('selected');
      nextItem.addClass('selected');
      const ul = nextItem.text();
      $('#ulResults').val(ul);
      nextItem.focus();

    } else {
      ulitems.first().addClass('selected');
    }
  } else if (key === 'ArrowUp') {
    event.preventDefault();
    const currentSelectedItem = ulitems.filter('.selected');
    const prevItem = currentSelectedItem.prev('li');
    if (prevItem.length) {
      currentSelectedItem.removeClass('selected');
      prevItem.addClass('selected');
      const ul = prevItem.text();
      $('#ulResults').val(ul);
      prevItem.focus();

    } else {
      ulitems.last().addClass('selected');
    }

  } else if (key === 'Enter') {
    event.preventDefault();
    const selectedItem = ulitems.filter('.selected');
    if (selectedItem.length) {
      // Handle the selected item
       ul = selectedItem.text().split(' - ')[0];
      const ul_desc = selectedItem.text().split(' - ')[1];
      $('#ul').val(ul);
      resultsContainer.empty();
      var accCode = document.getElementById('accCode');
      accCode.focus();
      // Perform further actions as needed
    }
  }
  // if (event.key === 'Enter') {
  //   // Perform your desired action here when the "Escape" key is pressed
  //   event.preventDefault();

  // }
});


$(document).on('click', '#ulResults li', function() {
  // Remove focus from any previously selected item
  $('#ulResults li').removeClass('selected');

  // Add focus to the clicked item
  $(this).addClass('selected');
  $(this).focus();

  const selectedItem = $('#ulResults li.selected');
  if (selectedItem.length) {
    // Handle the selected item
     ul = selectedItem.text().split(' - ')[0];
    console.log('UL:',ul)
    const ul_desc = selectedItem.text().split(' - ')[1];
    $('#ul').val('')
    $('#ul').val(ul);
    // Trigger a click event on the selected item
    // selectedItem.click();

    // Clear the results container
    $('#ulResults').empty();
    var accCode = document.getElementById('accCode');
    accCode.focus();
  }
});



$('#UpdateNo').on('keydown', function(event) {
  if (event.key === 'Escape') {
    // Perform your desired action here when the "Escape" key is pressed
    console.log('Escape key pressed');
  }
  else if (event.key === 'Enter'){
    event.preventDefault();
    UpdatetransactionModal.style.display = 'none';
  }
});

$('#UpdateYes').on('keydown', function(event) {
  if (event.key === 'Escape') {
    // Perform your desired action here when the "Escape" key is pressed
    console.log('Escape key pressed');
  }
  else if (event.key === 'Enter'){
    event.preventDefault();
    UpdatetransactionModal.style.display = 'none';
    var inputElement = document.getElementById("payeeInput");
    selectedId = inputElement.dataset.customdata;
    SaveEntryModal.style.display ='none'
    var payee = $('#payeeInput').val();
    var bank  = $('#draweeInput').val();
    // var bank  = $('#draweeInput').find('option:selected').text();
    var Entrylist = list_of_applied;
    var EntryTotal = list_of_applied_total;
    var totaldebit = $('#debittotal').val();
    var totalcredit = $('#credittotal').val();
    var doc_type = $('#doctype').find('option:selected').text()
    var docref = $('#docref').val();
    var Voucherdate = $('#Date').val();
    var Checkdate = $('#Dateidcheck').val();
    var checkNo = $('#checkNo').val();
    var remark = $('#remarks').val();
    var prepared = $('#prepared').find('option:selected').text()
    var reviewed =$('#reviewed').find('option:selected').text()
    var approved = $('#approved').find('option:selected').text()
    var transactionTypeID = $('#transactionTypeID').find('option:selected').text()
  
    totaldebit =parseFloat(totaldebit.replace(',', ''));
    totalcredit = parseFloat(totalcredit.replace(',', ''));
    // var prepared = $('#prepared').val();
    // var reviewed = $('#reviewed').val();
    // var approved = $('#approved').val();

    // console.log('payee',payee);
    // console.log('bank',bank);
    // console.log('Entrylist',Entrylist);
    // console.log('EntryTotal',EntryTotal);
    // console.log('totaldebit',totaldebit);
    // console.log('totalcredit',totalcredit);
    // console.log('doc_type',doc_type);
    // console.log('Voucherdate',Voucherdate);
    // console.log('Checkdate',Checkdate);
    // console.log('docref',docref);
    // console.log('checkNo',checkNo);
    // console.log('remark',remark);
    // console.log('prepared',prepared);
    // console.log('reviewed',reviewed);
    // console.log('approved',approved);
  
  
  
    const nameToCellIdMap = {
      ul_code: 'cell-ul-code',
      acct_code: 'cell-acct-code',
      acct_title: 'cell-acct-title',
      sl_acct: 'cell-sl-acct',
      debit_amount: 'cell-debit-amount',
      credit_amount: 'cell-credit-amount',
      button: 'cell-button',
      id_code: 'cell-id-code',
      primary_code: 'cell-primary-code',
      secondary_code: 'cell-secondary-code',
      acct_code2: 'cell-acct-code',
      subsidiary_code: 'cell-subsidiary-code',
    };
  
  
    const table = document.getElementById('AcctEntry'); // Replace "your-table-id" with the actual ID of your table element
    const rows = table.getElementsByTagName('tr'); // Get all the rows in the table
    
    const table_list = []; // Create an array to store the data (column name and value)
    
    for (let i = 1; i < rows.length; i++) {
      const row = rows[i];
      const cells = row.getElementsByTagName('td'); // Get all the cells in the current row
    
      const rowData = {}; // Create an object to store the data for the current row
    
      for (let j = 0; j < cells.length; j++) {
        const cell = cells[j];
        const columnName = Object.keys(nameToCellIdMap)[j];
        const cellValue = cell.textContent.trim(); // Get the text content of the cell and remove any leading/trailing whitespace
        rowData[columnName] = cellValue; // Associate the column name with the cell value in the rowData object
      }
    
      table_list.push(rowData); // Add the rowData object to the data array
    }
    console.log(table_list); 
    var csrfToken = $('#accountEntryID [name=csrfmiddlewaretoken]').val();
  
    $.ajax({
      url: '/api/update-Cash-Disbursement/',
      method: 'POST',
      headers: {
        'X-CSRFToken': csrfToken  // Include the CSRF token in the headers
      },
      dataType: 'json',
      data: {payeeId : selectedId,
             payee: payee,
            bank: bank,
            doc_type: doc_type,
            docref: docref,
            Voucherdate: Voucherdate,
            Checkdate: Checkdate,
            checkNo: checkNo,
            total_credit: total_credit,
            total_debit: total_debit,
            remarks: remark,
            approved: approved,
            reviewed:reviewed,
            prepared:prepared,
            transactionTypeID:transactionTypeID,
            table_list: JSON.stringify(table_list) },
      success: function(data) {
        const flashMessageDiv = document.createElement('div');
        flashMessageDiv.innerHTML = '<i class="fa fa-info-circle"></i>Transaction Successfully Update...!!';
      
        flashMessageDiv.classList.add('centered-message');
    
        flashMessageDiv.style.padding = '10px';
        flashMessageDiv.style.borderRadius = '5px';
        flashMessageDiv.style.zIndex = '99999';
        document.body.appendChild(flashMessageDiv);
        setTimeout(function() {
          document.body.removeChild(flashMessageDiv);
        }, 3000); // 3000 milliseconds = 3 seconds
        setTimeout(function() {
          window.location.reload();
        }, 3000);
        SetDataFields();
      }
      
    });
  }
});


$('#UpdateNo').on('click', function() {

    UpdatetransactionModal.style.display = 'none';
});

$('#UpdateYes').on('click', function() {
    // Perform your desired action here when the "Escape" key is pressed
    UpdatetransactionModal.style.display = 'none';
    var inputElement = document.getElementById("payeeInput");
    selectedId = inputElement.dataset.customdata;
    SaveEntryModal.style.display ='none'
    var payee = $('#payeeInput').val();
    var bank  = $('#draweeInput').val();
    // var bank  = $('#draweeInput').find('option:selected').text();
    var Entrylist = list_of_applied;
    var EntryTotal = list_of_applied_total;
    var totaldebit = $('#debittotal').val();
    var totalcredit = $('#credittotal').val();
    var doc_type = $('#doctype').find('option:selected').text()
    var docref = $('#docref').val();
    var Voucherdate = $('#Date').val();
    var Checkdate = $('#Dateidcheck').val();
    var checkNo = $('#checkNo').val();
    var remark = $('#remarks').val();
    var prepared = $('#prepared').find('option:selected').text()
    var reviewed =$('#reviewed').find('option:selected').text()
    var approved = $('#approved').find('option:selected').text()
    var transactionTypeID = $('#transactionTypeID').find('option:selected').text()
  
    totaldebit =parseFloat(totaldebit.replace(',', ''));
    totalcredit = parseFloat(totalcredit.replace(',', ''));


    const nameToCellIdMap = {
      ul_code: 'cell-ul-code',
      acct_code: 'cell-acct-code',
      acct_title: 'cell-acct-title',
      sl_acct: 'cell-sl-acct',
      debit_amount: 'cell-debit-amount',
      credit_amount: 'cell-credit-amount',
      button: 'cell-button',
      id_code: 'cell-id-code',
      primary_code: 'cell-primary-code',
      secondary_code: 'cell-secondary-code',
      acct_code2: 'cell-acct-code',
      subsidiary_code: 'cell-subsidiary-code',
    };
  
  
    const table = document.getElementById('AcctEntry'); // Replace "your-table-id" with the actual ID of your table element
    const rows = table.getElementsByTagName('tr'); // Get all the rows in the table
    
    const table_list = []; // Create an array to store the data (column name and value)
    
    for (let i = 1; i < rows.length; i++) {
      const row = rows[i];
      const cells = row.getElementsByTagName('td'); // Get all the cells in the current row
    
      const rowData = {}; // Create an object to store the data for the current row
    
      for (let j = 0; j < cells.length; j++) {
        const cell = cells[j];
        const columnName = Object.keys(nameToCellIdMap)[j];
        const cellValue = cell.textContent.trim(); // Get the text content of the cell and remove any leading/trailing whitespace
        rowData[columnName] = cellValue; // Associate the column name with the cell value in the rowData object
      }
    
      table_list.push(rowData); // Add the rowData object to the data array
    }
    console.log(table_list); 
    var csrfToken = $('#accountEntryID [name=csrfmiddlewaretoken]').val();
  
    $.ajax({
      url: '/api/update-Cash-Disbursement/',
      method: 'POST',
      headers: {
        'X-CSRFToken': csrfToken  // Include the CSRF token in the headers
      },
      dataType: 'json',
      data: {payeeId : selectedId,
             payee: payee,
            bank: bank,
            doc_type: doc_type,
            docref: docref,
            Voucherdate: Voucherdate,
            Checkdate: Checkdate,
            checkNo: checkNo,
            total_credit: total_credit,
            total_debit: total_debit,
            remarks: remark,
            approved: approved,
            reviewed:reviewed,
            prepared:prepared,
            transactionTypeID:transactionTypeID,
            table_list: JSON.stringify(table_list) },
      success: function(data) {
        const flashMessageDiv = document.createElement('div');
        flashMessageDiv.innerHTML = '<i class="fa fa-info-circle"></i>Transaction Successfully Update...!!';
        flashMessageDiv.classList.add('centered-message');
        flashMessageDiv.style.padding = '10px';
        flashMessageDiv.style.borderRadius = '5px';
        flashMessageDiv.style.zIndex = '99999';
        document.body.appendChild(flashMessageDiv);
        setTimeout(function() {
          document.body.removeChild(flashMessageDiv);
        }, 3000); // 3000 milliseconds = 3 seconds
        setTimeout(function() {
          window.location.reload();
        }, 3000);
        SetDataFields();
      }
    });
  });


$('#ReviewButton').on('click',function(){

  var result = window.confirm("Do you want to " + this.textContent + " this transaction.?");
  if (result) {
      StatusOfTransaction(this.textContent);
  } 
  
});

$('#ApproveButton').on('click',function(){
  var result = window.confirm("Do you want to " + this.textContent + " this transaction.?");
  if (result) {
      StatusOfTransaction(this.textContent);
  } 
});

$('#CancelButton').on('click',function(){
  var result = window.confirm("Do you want to " + this.textContent + " this transaction.?");
  if (result) {
      StatusOfTransaction(this.textContent);
  } 
});

function StatusOfTransaction(x) {
  const csrftoken = getCookie('csrftoken');
  $.ajax({
    url: '/api/status-of-transaction/',
    method: 'POST',
    dataType: 'json',
    data: {
      click: x,
      cv_no: $('#docref').val(),
      approved: $('#approved').val(),
      reviewed: $('#reviewed').val(),
      prepared: $('#prepared').val()
    },
    headers: {
      // Include the CSRF token in the request headers
      'X-CSRFToken': csrftoken
    },
    success: function(data) {
      console.log('sdasdas:',data);

      const flashMessageDiv = document.createElement('div');
      flashMessageDiv.innerHTML = `<i class="fa fa-info-circle"></i> ${data.message}`;
      // flashMessageDiv.innerHTML = '<i class="fa fa-info-circle"></i>Transaction Successfully Update...!!';
      flashMessageDiv.classList.add('centered-message');
      flashMessageDiv.style.padding = '10px';
      flashMessageDiv.style.borderRadius = '5px';
      flashMessageDiv.style.zIndex = '999999';
      document.body.appendChild(flashMessageDiv);
      setTimeout(function() {
        document.body.removeChild(flashMessageDiv);
      }, 3000); // 3000 milliseconds = 3 seconds
      setTimeout(function() {
        window.location.reload();
      }, 3000);
    }
  });
}


function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + '=') {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}


document.getElementById('PrintPDFList').addEventListener('click', function () {
  const nameToCellIdMap = {
    ul: 'cell-ul',
    Date: 'cell-Date',
    DocRef: 'cell-DocRef',
    CheckNO: 'cell-CheckNO',
    CheckDate: 'cell-CheckDate',
    Payee: 'cell-Payee',
    TransType: 'cell-TransType',
    Amount: 'cell-Amount',
  };


  const table = document.getElementById('tablerowtab'); // Replace "your-table-id" with the actual ID of your table element
  const rows = table.getElementsByTagName('tr'); // Get all the rows in the table
  
  const table_list = []; // Create an array to store the data (column name and value)
  
  for (let i = 1; i < rows.length; i++) {
    const row = rows[i];
    const cells = row.getElementsByTagName('td'); // Get all the cells in the current row
  
    const rowData = {}; // Create an object to store the data for the current row
  
    for (let j = 0; j < cells.length; j++) {
      const cell = cells[j];
      const columnName = Object.keys(nameToCellIdMap)[j];
      const cellValue = cell.textContent.trim(); // Get the text content of the cell and remove any leading/trailing whitespace
      rowData[columnName] = cellValue; // Associate the column name with the cell value in the rowData object
    }
  
    table_list.push(rowData); // Add the rowData object to the data array
  }
  const csrftoken = getCookie('csrftoken');
  fetch('/pdf-report/', {
    method: 'POST', // Specify the HTTP method as POST
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken, // Set the content type to JSON
    },
    body: JSON.stringify(table_list), // Convert the data to a JSON string and send it in the request body
  })
  
    .then(response => response.blob())
    .then(blob => {
      const url = URL.createObjectURL(blob);

      // Download the PDF by creating an anchor element
      const a = document.createElement('a');
      a.href = url;
      a.download = 'cvList.pdf'; // Provide a default filename
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);

  
      const newTab = window.open(url, '_blank');
      newTab.onload = function() {
        // Trigger the print process automatically
        newTab.print();
        
        // Close the tab after printing (optional)
        // newTab.close();
      };
      URL.revokeObjectURL(url);

      // url.print();
    });
});

// Helper function to convert hex string to bytes
function hexToBytes(hex) {
  for (var bytes = [], c = 0; c < hex.length; c += 2)
    bytes.push(parseInt(hex.substr(c, 2), 16));
  return new Uint8Array(bytes);
}


// document.getElementById('PrintCVPR').addEventListener('click', function () {

  
// });

document.getElementById('PrintPDF').addEventListener('click', function () {
  const nameToCellIdMap = {
    ul: 'cell-ul',
    acct_code: 'cell-acct_code',
    acct_title: 'cell-acct_code',
    sl_name: 'cell-sl_name',
    debit_amount: 'cell-debit_amount',
    credit_amount: 'cell-credit_amount',

  };


  const table = document.getElementById('AcctEntry'); // Replace "your-table-id" with the actual ID of your table element
  const rows = table.getElementsByTagName('tr'); // Get all the rows in the table
  
  const table_list = []; // Create an array to store the data (column name and value)
  
  for (let i = 1; i < rows.length; i++) {
    const row = rows[i];
    const cells = row.getElementsByTagName('td'); // Get all the cells in the current row
  
    const rowData = {}; // Create an object to store the data for the current row
  
    for (let j = 0; j < cells.length; j++) {
      const cell = cells[j];
      const columnName = Object.keys(nameToCellIdMap)[j];
      const cellValue = cell.textContent.trim(); // Get the text content of the cell and remove any leading/trailing whitespace
      rowData[columnName] = cellValue; // Associate the column name with the cell value in the rowData object
    }
  
    table_list.push(rowData); // Add the rowData object to the data array
  }
  var payee = $('#payeeInput').val();
  var bank  = $('#draweeInput').val();
  // var bank  = $('#draweeInput').find('option:selected').text();
  var Entrylist = list_of_applied;
  var EntryTotal = list_of_applied_total;
  var totaldebit = $('#debittotal').val();
  var totalcredit = $('#credittotal').val();
  var doc_type = $('#doctype').find('option:selected').text()
  var docref = $('#docref').val();
  var Voucherdate = $('#Date').val();
  var Checkdate = $('#Dateidcheck').val();
  var checkNo = $('#checkNo').val();
  var remark = $('#remarks').val();
  var prepared = $('#prepared').find('option:selected').text()
  var reviewed =$('#reviewed').find('option:selected').text()
  var approved = $('#approved').find('option:selected').text()
  var transactionTypeID = $('#transactionTypeID').find('option:selected').text()

  totaldebit =parseFloat(totaldebit.replace(',', ''));
  totalcredit = parseFloat(totalcredit.replace(',', ''));

  const csrftoken = getCookie('csrftoken');
  const requestData = {
    formData: {
      payeeId: selectedId,
      payee: payee,
      bank: bank,
      doc_type: doc_type,
      docref: docref,
      Voucherdate: Voucherdate,
      Checkdate: Checkdate,
      checkNo: checkNo,
      totalcredit: totalcredit,
      totaldebit: totaldebit,
      remarks: remark,
      approved: approved,
      reviewed: reviewed,
      prepared: prepared,
      transactionTypeID: transactionTypeID,
    },
    tableData: table_list, // Include the table_list array in the requestData
  };
  
  fetch('/cvpr-report1/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken,
    },
    body: JSON.stringify(requestData), // Convert the requestData object to a JSON string and send it in the request body
  })
  
    .then(response => response.blob())
    .then(blob => {
      const url = URL.createObjectURL(blob);

      // Download the PDF by creating an anchor element
      const a = document.createElement('a');
      a.href = url;
      a.download = 'CVPR.pdf'; // Provide a default filename
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);

      // Open the PDF in a new tab
      window.open(url, '_blank');
      // newTab.onload = function() {
      //   // Trigger the print process automatically
      //   newTab.print();
        
      //   // Close the tab after printing (optional)
      //   // newTab.close();
      // };
      URL.revokeObjectURL(url);

      // url.print();
    });
});

document.getElementById('PrintCVPRDoc').addEventListener('click', function () {
  const nameToCellIdMap = {
    ul: 'cell-ul',
    acct_code: 'cell-acct_code',
    acct_title: 'cell-acct_code',
    sl_name: 'cell-sl_name',
    debit_amount: 'cell-debit_amount',
    credit_amount: 'cell-credit_amount',

  };
  const table = document.getElementById('AcctEntry'); // Replace "your-table-id" with the actual ID of your table element
  const rows = table.getElementsByTagName('tr'); // Get all the rows in the table
  
  const table_list = []; // Create an array to store the data (column name and value)
  
  for (let i = 1; i < rows.length; i++) {
    const row = rows[i];
    const cells = row.getElementsByTagName('td'); // Get all the cells in the current row
  
    const rowData = {}; // Create an object to store the data for the current row
  
    for (let j = 0; j < cells.length; j++) {
      const cell = cells[j];
      const columnName = Object.keys(nameToCellIdMap)[j];
      const cellValue = cell.textContent.trim(); // Get the text content of the cell and remove any leading/trailing whitespace
      rowData[columnName] = cellValue; // Associate the column name with the cell value in the rowData object
    }
  
    table_list.push(rowData); // Add the rowData object to the data array
  }
  var payee = $('#payeeInput').val();
  var bank  = $('#draweeInput').val();
  // var bank  = $('#draweeInput').find('option:selected').text();
  var Entrylist = list_of_applied;
  var EntryTotal = list_of_applied_total;
  var totaldebit = $('#debittotal').val();
  var totalcredit = $('#credittotal').val();
  var doc_type = $('#doctype').find('option:selected').text()
  var docref = $('#docref').val();
  var Voucherdate = $('#Date').val();
  var Checkdate = $('#Dateidcheck').val();
  var checkNo = $('#checkNo').val();
  var remark = $('#remarks').val();
  var prepared = $('#prepared').find('option:selected').text()
  var reviewed =$('#reviewed').find('option:selected').text()
  var approved = $('#approved').find('option:selected').text()
  var transactionTypeID = $('#transactionTypeID').find('option:selected').text()

  totaldebit =parseFloat(totaldebit.replace(',', ''));
  totalcredit = parseFloat(totalcredit.replace(',', ''));

  const csrftoken = getCookie('csrftoken');
  const requestData = {
    formData: {
      payeeId: selectedId,
      payee: payee,
      bank: bank,
      doc_type: doc_type,
      docref: docref,
      Voucherdate: Voucherdate,
      Checkdate: Checkdate,
      checkNo: checkNo,
      totalcredit: totalcredit,
      totaldebit: totaldebit,
      remarks: remark,
      approved: approved,
      reviewed: reviewed,
      prepared: prepared,
      transactionTypeID: transactionTypeID,
    },
    tableData: table_list, // Include the table_list array in the requestData
  };
  
  fetch('/cvpr-report/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken,
    },
    body: JSON.stringify(requestData), // Convert the requestData object to a JSON string and send it in the request body
  })
  
  .then(data => {
    // Handle the response from the server
    window.open('/cvpr-html/', '_blank');
  })
  .catch(error => {
    // Handle any errors that occur during the fetch or processing
    console.error('Error:', error);
  });
});