$(document).ready(function() {
      var reviewed = 'CV - Reviewed By'
      $.ajax({
        url: '/api/reviewed/',
        method: 'GET',
        data: { reviewed: reviewed },
        success: function(data) {
          var select = $('#reviewed');
          select.empty(); // Clear existing options
          data.forEach(function(reviewed_list) {
            select.append('<option value="' + reviewed_list.autonum + '">' + reviewed_list.acct_title + '</option>');
          });
        },
        error: function(xhr, textStatus, errorThrown) {
          console.log('Error:', errorThrown);
        }
      });

    //   var approved = 'CV - Approved By'
    //   $.ajax({
    //     url: '/api/approved/',
    //     method: 'GET',
    //     data: { approved: approved },
    //     success: function(data) {
    //       var select = $('#approved');
    //       select.empty(); // Clear existing options
    //       data.forEach(function(approved_list) {
    //         select.append('<option value="' + approved_list.autonum + '">' + approved_list.acct_title + '</option>');
    //       });
    //     },
    //     error: function(xhr, textStatus, errorThrown) {
    //       console.log('Error:', errorThrown);
    //     }
    //   });

  });


  $(document).ready(function() {
    var approved = 'CV - Approved By'
    $.ajax({
      url: '/api/approved/',
      method: 'GET',
      data: { approved: approved },
      success: function(data) {
        var select = $('#approved');
        select.empty(); // Clear existing options
        data.forEach(function(approved_list) {
          select.append('<option value="' + approved_list.autonum + '">' + approved_list.acct_title + '</option>');
        });
      },
      error: function(xhr, textStatus, errorThrown) {
        console.log('Error:', errorThrown);
      }
    });

});



