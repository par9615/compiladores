var matrix = {};
var childrenTable, childrenHeaders, realHeaders;

$(document).ready(function() {
	$('li.configure').addClass("active open");
	$('li.configure').find('a').append('<span class="selected"></span>');
	parseMatrix();
	setEvents();
});

function setEvents() {
	var data = matrix;
	$('btn.btn-transparent.red.btn-outline.btn-circle.btn-sm').on('click', function() {
		$.ajax({
			url: '/saveMatrix',
			method: 'POST',
			ContentType : 'application/json',
			data = data
		}).done(function(response) {
			console.log(response);
		}).fail( function(respose) {
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

function parseMatrix() {
	childrenTable = $('table tbody').children();
	childrenHeaders = $(childrenTable[0]).children();
	realHeaders = [];
	for (var i = 0; i < childrenHeaders.length; i++) {
		realHeaders.push($(childrenHeaders[i]).html().replace(/(<b>|<\/b>|<i>|<\/i>|<u>|<\/u>)/g, '').replace(/&gt;/g,'>').replace(/&lt;/g,'<').replace(/&amp;/g,'&'));
	}
	// Going through rows
	for (var i = 1; i < childrenTable.length; i++) {
		var row = $(childrenTable[i]).children();
		var rowNum = $(row[0]).html().replace(/\n|\s/g,'');
		matrix[rowNum] = {};
		// Going through cols
		for (var j = 1; j < row.length; j++) {
			var value = $(row[j]).html();
			if (value == '')	
				continue;
			value = value.replace(/\n|\s|<li>|<\/li>|<i>|<\/i>|<b>|<\/b>|<u>|<\/u>|<ul>|<\/ul>/g, '').replace(/&gt;/g,'>').replace(/&lt;/g,'<').replace(/&amp;/g,'&');
			matrix[rowNum][realHeaders[j]] = parseValue(value);
		}
	}
}

function parseValue(value) {
	if (!isNaN(value)) {
		value = "G" + value;
	}
	else if (value.includes('reduce')) {
		var arrowIndex = value.indexOf('→');
		var rule = value.substring(value.indexOf('(')+1,arrowIndex);
		var production = value.substring(arrowIndex+1,value.length-1);
		value = 'R' + rules[rule][production];
	}
	else if (value.includes('shift')) {
		value = "S" + value.substring(value.indexOf('(')+1, value.indexOf(')'));
	}
	else if (value.includes('acc')) {
		value = "AC";
	}
	return value;
}