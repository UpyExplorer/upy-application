window.addEventListener("load", function () {	
	try {
		document.getElementById("btnSave").addEventListener("click", function() {
			$('.btn_save').trigger('click');
		});

		document.getElementById("btnDelete").addEventListener("click", function() {
			$('.btn_delete').trigger('click');
		});

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
	}
	
	function btnDisabled(object){
		if (object.disabled === true) {
			object.disabled = false;
		}else{
			object.disabled = true;
		}
	}

});

window.toastrDefaultSuccess = function(title, text){
	setMessage();
	toastr["success"](title, text)
}

window.toastrDefaultInfo = function(title, text){
	setMessage();
	toastr["info"](title, text)
}

window.toastrDefaultError = function(title, text){
	setMessage();
	toastr["error"](title, text)
}

window.toastrDefaultWarning = function(title, text){
	setMessage();
	toastr["warning"](title, text)
}

window.setMessage = function(type=null, title=null, text=null){
	toastr.options = {
		"closeButton": true,
		"debug": false,
		"newestOnTop": false,
		"progressBar": true,
		"positionClass": "toast-top-right",
		"preventDuplicates": true,
		"onclick": null,
		"showDuration": "300",
		"hideDuration": "1000",
		"timeOut": "5000",
		"extendedTimeOut": "1000",
		"showEasing": "swing",
		"hideEasing": "linear",
		"showMethod": "fadeIn",
		"hideMethod": "fadeOut"
	}
	if(type != null){
		toastr[type](title, text)
	}
}