$(window).load(function() {
  check("learning");
  check("email");
  setInterval(function() {
    check("learning");
    check("email");
  }, 10000);
});

function check(service) {
  $.ajax({url: "/check_service/" + service, statusCode: {
    200: function(data) {
      var data = $.parseJSON(data);
      var d = new Date(data["timestamp"] * 1000);
      var n = d.toLocaleString();
      $("#" + service + "_server_status").html(data["message"] + "  "+ n);
      $("#" + service + "_box").removeClass("fail");
      $("#" + service + "_box").addClass("success");
    },
    404: function() {
      $("#" + service + "_server_status").html("No..... status code 404");
      $("#" + service + "_box").removeClass("success");
      $("#" + service + "_box").addClass("fail");
    },
    500: function() {
      $("#" + service + "_server_status").html("No..... status code 500");
      $("#" + service + "_box").removeClass("success");
      $("#" + service + "_box").addClass("fail");
    }
  }});
}
