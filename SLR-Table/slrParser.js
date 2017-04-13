$(document).ready(function() {
	var childrenTable = $('table tbody').children();
	var childrenHeaders = $(childrenTable[0]).children();
	var realHeaders = [];
	for (var i = 0; i < childrenHeaders.length; i++) {
		realHeaders.push($(childrenHeaders[i]).html().replace(/(<b>|<\/b>|<i>|<\/i>|<u>|<\/u>)/g, '').replace(/&gt;/g,'>').replace(/&lt;/g,'<').replace(/&amp;/g,'&'));
	}
	console.log(realHeaders);
});