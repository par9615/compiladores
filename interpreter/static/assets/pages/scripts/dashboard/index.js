$(document).ready(function() {
	$('li.dashboard').addClass('active open');
	$('li.dashboard').find('a').append('<span class="selected"></span>');
});