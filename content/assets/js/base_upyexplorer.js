window.addEventListener("load", function () {
	try {
		document.getElementById("btnEdit").addEventListener("click", function() {
			var inputs = document.getElementsByTagName("input");
			var selects = document.getElementsByTagName("select");
			var textareas = document.getElementsByTagName("textarea");

			for (var i = 0; i < inputs.length; i++) {
				btnDisabled(inputs[i]);
			}
			for (var i = 0; i < selects.length; i++) {
				btnDisabled(selects[i]);
			}
			for (var i = 0; i < textareas.length; i++) {
				btnDisabled(textareas[i]);
			}
		});

	}catch (e) {
		console.log(e);
	}
	
	function btnDisabled(object){
		if (object.disabled === true) {
			object.disabled = false;
		}else{
			object.disabled = true;
		}
	}

});