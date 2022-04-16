$('#userRegistrationForm').on('submit', function (event) {
	event.preventDefault()

	formData = $(this).serialize();

	$.ajax({
		url: '/api/registerUser',
		method: 'POST',
		data: formData,
		success: function (data) {
			alert(data);
			window.locaton = window.origin+'/login';
		},
		error: function (msg){
			alert(msg);
		}
	});
});


$('#usersList').on('click', function(){
	$.ajax({
		url: '/api/userList',
		method: 'GET',
		success: function(data){
			console.log(data.length);
			console.log(data[1]);
			var counter = 1;
			var row = ""
			$.each(data, function (key, value) {

				console.log('Key: '+key+" value: "+value.userId);

				var loggedInState = "<td><span class='bg-success' style='padding: 10px 4px;'>Active</span></td>";
				var offlineState = "<td><span class='bg-warning' style='padding: 10px 4px;'>Offline</span></td>";
				var currentState = "";

				if (value.isLoggedIn) {
					currentState = loggedInState;
				}else{
					currentState = offlineState;
				}

				row += "<tr><td>"+value.userId+"</td><td style='width: 200px;'>"+value.userfirstName+' '+value.userLastName+"</td><td>"+value.userEmail+"</td>"+currentState+"<td style='width: 400px;'><a class='btn btn-sm bg-success' href='#'> <i class='fab fa-accessible-icon'></i> Previliges</a><a class='btn btn-sm  bg-warning' href='#'> <i class='fas fa-comments'></i> chat</a><a class='btn btn-sm bg-danger' href='#'> <i class='fas fa-user-lock'></i> Block</a> &nbsp;</td></tr>";

			});
			$('#usersTable').html(row);



			var table = $('#example').DataTable({
              "columnDefs": [{
                  "visible": true,
                  "targets": 2
              }],
              "displayLength": 5,
          	});
		},
		error: function (argument) {
			alert('an unknown error occured.');
		}
	});
});

$('#addLoadForm').on('submit', function(event){
	event.preventDefault();
	formData = $(this).serialize();
	$.ajax({
		url: '/api/addLoad',
		method: 'POST',
		data: formData,
		success: function(data){
			alert(data);
		},
		error: function(msg){
			alert(msg);
		}
	});
});



$('#viewLoadsBtn').on('click', function(){
	$.ajax({		
		url: '/api/listLoads',
		method: 'GET',
		success: function(data){
			console.log(data);

			$.each(data, function(key, value){
				console.log("Key :"+key+" "+value.isSensor);
				if (parseInt(value.loadType) == 1) {
					var imageLink = '';
				}else if(parseInt(value.loadType) == 2){
					var imageLink = '';
				}else if(parseInt(value.loadType) == 3){
					var imageLink = '';
				}else{
					var imageLink = '';
				}
				
				var column = '<div class="col"><div class="card" onclick="onClick();"><div class="card-body"><div class="card-img-top"><img src="'+imageLink+'" class="img img-responsive"></div></div><div class="card-footer">'+value.loadName+' <br><div><button class="btn bg-primary" onclick="loadTurnOn('+value.loadId+');">Turn ON</button> &nbsp; &nbsp; <button class="btn btn-lg bg-primary" onclick="loadTurnOff('+value.loadId+');">Turn Off</button></div></div></div></div>';
				$('#loadsContainer').html(column);

			});
		},
		error: function(msg){
			alert('Some error has occured.');
		}
	});
});


