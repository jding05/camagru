
	$(document).ready(function() {
    $("#delete").click(function(e) {
        e.preventDefault();
				data = $("#photo").attr('src');
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
							// $("#finish").attr('src', data.finish);
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