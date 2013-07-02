$(window).load(function() {
  check_learning();
  check_email();
  setInterval(function() {
    check_learning();
    check_email();
  }, 5000);
});

function check_learning() {
  $.ajax({url: "/check_learning_service", statusCode: {
    200: function(data) {
      console.log($.parseJSON(data));
      var data = $.parseJSON(data);
      var d = new Date(data["timestamp"] * 1000);
      var n = d.toLocaleString();
      $("#learning_server_status").html(data["message"] + "  "+ n);
      $("#learning_box").removeClass("fail");
      $("#learning_box").addClass("success");
    },
    404: function() {
      $("#learning_server_status").html("No..... status cod 404");
      $("#learning_box").removeClass("success");
      $("#learning_box").addClass("fail");
    },
    500: function() {
      $("#learning_server_status").html("No..... status code 500");
      $("#learning_box").removeClass("success");
      $("#learning_box").addClass("fail");
  }});
}

function check_email() {
  $.ajax({url: "/check_email_service", statusCode: {
    200: function(data) {
      console.log($.parseJSON(data));
      var data = $.parseJSON(data);
      var d = new Date(data["timestamp"] * 1000);
      var n = d.toLocaleString();
      $("#email_server_status").html(data["message"] + "  "+ n);
      $("#email_box").removeClass("fail");
      $("#email_box").addClass("success");
    },
    404: function() {
      $("#email_server_status").html("No..... status cod 404");
      $("#email_box").removeClass("success");
      $("#email_box").addClass("fail");
    },
    500: function() {
      $("#email_server_status").html("No..... status code 500");
      $("#email_box").removeClass("success");
      $("#email_box").addClass("fail");
    },
  }});
}
