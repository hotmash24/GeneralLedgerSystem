var acct_code0= ''
var acct_code1= ''
var acct_code2= ''
var acct_code3= ''
var sl_type_per_acct_Title = ''
var sl_code_entry = ''

function GetAccountCodeIndividual(ACCOUNTTILTE) {
  $.ajax({
    url: '/api/AccoutCodeIndividual/',
    type: 'GET',
    dataType: 'json',
    data: {
      ACCOUNTTILTE: ACCOUNTTILTE
    },
    success: function(data) {
      data.forEach(function(codeslist) {
        localStorage.acct_code0 = codeslist.primary_code;
        localStorage.acct_code1 = codeslist.secondary_code;
        localStorage.acct_code2 = codeslist.acct_code;
        localStorage.acct_code3 = codeslist.subsidiary_code;
        localStorage.sl_type_per_acct_Title = codeslist.sl_type;


      });
    },
    error: function(xhr, status, error) {
      console.error('Error fetching data from server:', error);
    }
  });
}



function GetSLCodeEntry(c,slentry) {
  console.log('slentry:',slentry);
  console.log('sl--:',c);
  $.ajax({
    url: '/api/get-sl-code/',
    type: 'GET',
    dataType: 'json',
    data: {
      sl_type_per_acct_Title: c,
      slentry: slentry,
    },
    success: function(data) {
      localStorage.sl_id_code = data;
    },
    error: function(xhr, status, error) {
      console.error('Error fetching data from server:', error);
    }
  });
}