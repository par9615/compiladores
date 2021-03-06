var rules = {
	'Sx' : {
		'A_aug;Sx' : 0,
		'A_sim;Sx' : 1,
		'A_dro;Sx' : 2,
		'A_aug;' : 3,
		'A_sim;' : 4,
		'A_dro;' : 5,
		'CtrlSx' : 6,
		'Ctrl' : 7
	},
	'A_aug' : {
		'IDAoEx': 8
	},
	'A_sim' : {
		'ID=Ex' : 9
	},
	'A_dro' : {
		'IDDc' : 10
	},
	'Ao' : {
		'+=' : 11,
		'-=' : 12,
		'*=' : 13,
		'/=' : 14,
		'%=' : 15,
		'>>=' : 16,
		'<<=' : 17,
		'&=' : 18,
		'o=' : 19,
		'^=' : 20,
		'**=' : 21
	},
	'Ex' : {
		'Or_l' : 22
	},
	'Or_l' : {
		'Or_looAnd_l' : 23,
		'And_l' : 24
	},
	'And_l' : {
		'And_l&&Not_l' : 25,
		'Not_l' : 26
	},
	'Not_l' : {
		'!Not_l' : 27,
		'Lx' : 28
	},
	'Lx' : {
		'LxLoOr_b' : 29,
		'Or_b' : 30
	},
	'Lo' : {
		'<' : 31,
		'>' : 32,
		'<=' : 33,
		'>=' : 34,
		'==' : 35,
		'!=' : 36
	},
	'Or_b' : {
		'Or_boXor_b' : 37,
		'Xor_b' : 38
	},
	'Xor_b' : {
		'Xor_b^And_b' : 39,
		'And_b' : 40
	},
	'And_b' : {
		'And_b&Shift' : 41,
		'Shift' : 42
	},
	'Shift': {
		'Shift>>Ax' : 43,
		'Shift<<Ax' : 44,
		'Ax' : 45
	},
	'Ax' : {
		'Ax+Af' : 46,
		'Ax-Af' : 47,
		'Af' : 48
	},
	'Af' : {
		'Af*Ap' : 49,
		'Af%Ap' : 50,
		'Af/Ap' : 51,
		'Ap' : 52
	},
	'Ap' : {
		'At**Ap' : 53,
		'At' : 54
	},
	'At' : {
		'-NUMBER' : 55,
		'NUMBER' : 56,
		'STRING' : 57,
		'-ID': 58,
		'ID' : 59,
		'-(Ex)': 60,
		'(Ex)' : 61,
	},
	'Dc' : {
		'=**(STRING,NUMBER)**' : 62,
		'-<(Ex,Ex,Ex)' : 63,
		'-)(Ex,Ex,Ex)' : 64
	},
	'Ctrl' : {
		'For' : 65,
		'While' : 66,
		'If' : 67
	},
	'For' : {
		'for(ID:(Ex,Ex)){Sx}' : 68
	},
	'While' : {
		'while(Ex){Sx}' : 69
	},
	'If' : {
		'if(Ex){Sx}' : 70,
		'if(Ex)else{Sx}' : 71
	}
};
var matrix = {};
var childrenTable, childrenHeaders, realHeaders;

$(document).ready(function() {
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
	var keys = Object.keys(matrix);
	var lastKey = keys[keys.length-1];
	console.log('matrix = {');
	for(var stateIndex in matrix) {
		var headers = Object.keys(matrix[stateIndex]);
		var lastHeader = headers[headers.length-1];
		console.log('\t' + stateIndex + ' : {');
		for (var columnHeader in matrix[stateIndex]) {
			var closeValue = '\t\t"' + columnHeader + '":\t"' + matrix[stateIndex][columnHeader] + '"';
			if (columnHeader != lastHeader)
				closeValue += ',';
			console.log(closeValue);
		}
		var closeString = '\t}';
		if (stateIndex != lastKey)
			closeString += ',';
		console.log(closeString);
	}
	console.log('}');
});

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

function getCell(header,state) {
	var indexCol = realHeaders.indexOf(header);
	var row = $(childrenTable[state+1]).children();
	return $(row[indexCol]);
}