$(document).ready(function() {
	
	$('.contacto').tooltip({
		placement: 'bottom'
	});
	
	$('.more-oom').tooltip({
		placement: 'right'
	});
	
	$('a[rel*=external]').click( function() {
        window.open(this.href);
        return false;
    });
  
});
