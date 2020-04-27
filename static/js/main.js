
// Check if passwords match
$('#pw2').on('input', function(e){
	var pw1 = $('#pw1').val();
	if (pw1 != $(this).val()){
		$('#pw_err').text('Passowrds do not match');
		$('#btn_reg').attr('disabled', 'disabled');
	}
	else{
		$('#pw_err').text('');
		$('#btn_reg').attr('disabled', false);
	}
});
$('#pw1').on('input', function(e){
	var pw2 = $('#pw2').val();
	if (pw2 != $(this).val()){
		$('#pw_err').text('Passowrds do not match');
		$('#btn_reg').attr('disabled', 'disabled');
	}
	else{
		$('#pw_err').text('');
		$('#btn_reg').attr('disabled', false);
	}
});

// Fadeout message automatically
setTimeout(function(e){
    $('#message').fadeOut();
},4000);
