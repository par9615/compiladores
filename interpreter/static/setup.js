var matrix = {}, rules;
var childrenTable, childrenHeaders, realHeaders;

$(document).ready(function() {
	getRules();
});

function getRules() {
	$.ajax({
		url: 'interpreter/getRules',
		method: 'GET',
	}).done(function(response) {
		parseMatrix(response);
		sendMatrix();
	}).fail(function(response) {
		console.log(response);
	});
}

function sendMatrix() {
	$.ajax({
		url: 'interpreter/setMatrix',
		method: 'POST',
		headers: {'X-CSRFToken': $('[name="csrfmiddlewaretoken"]').val()},
		ContentType: 'application/json',
		dataType: 'json',
		data: {
			json: JSON.stringify(matrix)
		}
	}).done(function(response) {
		console.log("The matrix ");
		console.log(response);
	}).fail(function(response) {
		console.log(response);
	});
}

function parseMatrix(parsedRules) {
	rules = parsedRules;
	childrenTable = $('table tbody').children();
	childrenHeaders = $(childrenTable[0]).children();
	realHeaders = [];
	for (var i = 0; i < childrenHeaders.length; i++) {
		realHeaders.push($(childrenHeaders[i]).html().replace(/(<b>|<\/b>|<i>|<\/i>|<u>|<\/u>)/g, '').replace(/&gt;/g,'>').replace(/&lt;/g,'<').replace(/&amp;/g,'&').replace(' o ', ' | ').replace('oo', '||').replace('o=', '|='));
	}
	// Going through rows
	for (var i = 1; i < childrenTable.length; i++) {
		var row = $(childrenTable[i]).children();
		var rowNum = $(row[0]).html().replace(/\n|\s/g,'').replace(' o ', ' | ').replace('oo', '||').replace('o=', '|=');
		matrix[rowNum] = {};
		// Going through cols
		for (var j = 1; j < row.length; j++) {
			var value = $(row[j]).html();
			if (value == '')	
				continue;
			value = value.replace(/\n|<li>|<\/li>|<i>|<\/i>|<b>|<\/b>|<u>|<\/u>|<ul>|<\/ul>/g, '').replace(/&gt;/g,'>').replace(/&lt;/g,'<').replace(/&amp;/g,'&').replace(' o ', ' | ').replace('oo', '||').replace('o=', '|=');
			value = value.replace(/\s/g, '');
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
		indexRule = rules[rule][production];
		if (indexRule == undefined) {
			console.log(rules[rule]);
			console.log(production);
		}
		value = 'R' + indexRule;
	}
	else if (value.includes('shift')) {
		value = "S" + value.substring(value.indexOf('(')+1, value.indexOf(')'));
	}
	else if (value.includes('acc')) {
		value = "AC";
	}
	return value;
}