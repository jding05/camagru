// Send back data from front end to back end using Ajax

	// cookie
	function getCookie(name) {
		var cookieValue = null;
		if (document.cookie && document.cookie != '') {
					var cookies = document.cookie.split(';');
		for (var i = 0; i < cookies.length; i++) {
				 var cookie = jQuery.trim(cookies[i]);
		// Does this cookie string begin with the name we want?
		if (cookie.substring(0, name.length + 1) == (name + '=')) {
			cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			 }
		}
	}
	return cookieValue;
	}

	// ajax
	$(document).ready(function() {
    $("#merge").click(function(e) {
        e.preventDefault();
				data = $("#photo").attr('src');
				console.log("{ " + data + " }");
				var csrftoken = getCookie('csrftoken');
        $.ajax({
            "type": "POST",
						"dataType": "json",
            "url": "/webcam/",
						"data" : {
							"action" : "merge",
							"content" : data,
							"csrfmiddlewaretoken" : csrftoken,
						},
            "success": function(data) {
							$("#photo").attr('src', data.finish);
						},
						"error" : function() {console.log("error");},

						"failure" : function(result) {
							console.log("Failure " + result);
						}
        });
    });
	});

	$(document).ready(function() {
    $("#post").click(function(e) {
        e.preventDefault();
				data = $("#photo").attr('src');
				console.log("{ " + data + " }");
				var csrftoken = getCookie('csrftoken');
        $.ajax({
            "type": "POST",
						"dataType": "json",
            "url": "/webcam/",
						"data" : {
							"action" : "post",
							"content" : data,
							"csrfmiddlewaretoken" : csrftoken,
						},
            "success": function(data) {
							document.getElementById("post").disabled = true;
							alert("Post Succeed");
						},
						"error" : function() {console.log("error");},

						"failure" : function(result) {
							console.log("Failure " + result);
						}
        });
    });
	});