$(window).load(resizeAllColumns);
$(window).resize(resizeAllColumns);

function resizeAllColumns() {
	var tallestColumn = Math.max($('#column-twitter').height(), $('#column-picture').height(), $('#column-definition').height());
	$('#column-twitter').height(tallestColumn);
	$('#column-picture').height(tallestColumn);
	$('#column-definition').height(tallestColumn);
}