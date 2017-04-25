$(document).ready(function() {
	$('li.configure').addClass("active open");
	$('li.configure').find('a').append('<span class="selected"></span>');

	setEvents();
});

function setEvents() {
	$('button.btn.blue').on('click', function() {
		$.ajax({
			url: '/parseGrammar',
			method: 'GET'
		}).done({
			console.log('done');
		}).fail({
			console.log('fail');
		});
	});

	$('button.btn.green').on('click', function() {
		$.ajax({
			url: '/generateMatrix',
			method: 'GET'
		}).done({
			console.log('done');
		}).fail({
			console.log('fail');
		});
	});
}