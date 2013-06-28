$(window).load(function() {
  check_learning();
  setInterval(function() {
    check_learning();
  }, 5000);
});

function check_learning() {
  var d = new Date();
  var n = d.toLocaleString();
  $.ajax({url: "/test", statusCode: {
    200: function() {
      $("#learning_server_status").html("Yes, as of " + n.toLocaleString());
    },
    404: function() {
      $("#learning_server_status").html("No..... status cod 404");
    },
    500: function() {
      $("#learning_server_status").html("No..... status code 500");
    },
  }});
}
