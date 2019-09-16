
// upload image

function readURL(input) {
  if (input.files && input.files[0]) {
		console.log("readURL");
    var reader = new FileReader();
    
    reader.onload = function(e) {
			$('#photo').attr('src', e.target.result);
    }
    
		document.getElementById("merge").disabled = false;
		document.getElementById("post").disabled = false;
		reader.readAsDataURL(input.files[0]);
	}
	
}

$(document).ready(function() {
	$("#imgInp").change(function() {
		readURL(this);
	});
});