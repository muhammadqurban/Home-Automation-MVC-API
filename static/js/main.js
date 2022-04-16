function loadTurnOn(id) {
	$.ajax({
		url: '/api/loadTurnOn/'+id,
		method: 'GET',
		success: function(data){
			alert(data);
		},
		error: function(msg){
			alert(msg);
		}
	});
}


function loadTurnOff(id){
	$.ajax({
		url: '/api/loadTurnOff/'+id,
		method: 'GET',
		success: function(data){
			alert(data);
		},
		error: function(msg){
			alert(msg);
		}
	});
}