$(document).ready(function() {
    $('#newButton').click(function() {
      $('#mytranstype').modal('show');
    });
  
    $('#mytranstype').on('show.bs.modal', function() {
      // AJAX request to fetch the trans_type_list data
      $.ajax({
        url: '/api/trans-type/',
        method: 'GET',
        success: function(data) {
          var select = $('#activityid');
          select.empty(); // Clear existing options
          select.append('<option selected disabled>--------Select--------</option>'); // Add default option
          $.each(data, function(index, trans_type) {
            select.append('<option value="' + trans_type.line_number + '">' + trans_type.cf_desc + '</option>');
          });
        },
        error: function(xhr, textStatus, errorThrown) {
          console.log('Error:', errorThrown);
        }
      });
    });
  });
  