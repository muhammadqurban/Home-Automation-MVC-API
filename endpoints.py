from flask_app import *
@app.route('/api/registerUser', methods=['POST'])
def registerUserAPI():
	if request.method == "POST":
		
		firstName = request.form['firstName']
		lastName = request.form['lastName']
		email = request.form['userEmail']
		password = request.form['userPassword']

		from user import User
		newUser = User()
		newUser.setFirstName(firstName)
		newUser.setLastName(lastName)
		newUser.setEmail(email)
		newUser.setPassword(password)

		userId = newUser.register(db)
		if userId > 0:
			return 'User has been added.'
		else:
			return 'Error! Maybe try with a different email.'


@app.route('/api/login', methods=['POST'])
def loginUserAPI():

	userEmail = request.form['userEmail']
	userPass = request.form['userPassword']

	userData = dict()

	from user import User
	userData = User().login(db, userEmail, userPass)
	
	print(type(userData))

	if (len(userData) > 0) and (userData['isLoggedIn']):
		session['userData'] = userData
		return jsonify(userData)
	else:
		userData = dict()
		userData['ErrorMessage'] = 'login failed! check details.'

	return jsonify(userData)


@app.route('/api/userList')
def listUsers():

	if session["userData"]['isLoggedIn']:
		from DBmodels import User
		userList = db.session.query(User).all()
		userListDict = dict()
		counter = 0
		for x in userList:
			print(x)
			user = dict()
			user['userId'] = x.id
			user['userfirstName'] = x.firstName
			user['userLastName'] = x.lastName
			user['userEmail'] = x.Email
			user['userRegDate'] = x.reg_date
			user['isLoggedIn'] = True
			counter += 1
			userListDict[counter] = user

		return jsonify(userListDict)
	else:
		userData = dict()
		userData['ErrorMessage'] = 'You need to be logged In first.'
		return userData


@app.route('/api/blockUser/<id>')
def blockUser(id):
	if session['userData']['isLoggedIn']:
		from DBmodels import User
		a_user = db.session.query(User).filter(User.id == id).one()
		a_user.blockStatus = 0
		db.session.commit()
		return 'user has been blocked.'
	else:
		return redirect('/login')


@app.route('/api/deleteUser/<id>')
def deleteUser(id):
	id = int(id)
	if session['userData']['isLoggedIn']:
		from DBmodels import User
		deleteUser = db.session.query(User).filter(User.id == id).one()
		db.session.delete(deleteUser)
		db.session.commit()
	else:
		return redirect('/login')

@app.route('/api/addLoad', methods=['POST'])
def addLoad():
	loadName = request.form['loadName']
	loadType = request.form['loadType']
	loadPin = request.form['loadPin']

	from classes1.Load import Load
	newLoad = Load()
	newLoad.set_load_name(loadName)
	newLoad.set_load_type(loadType)
	newLoad.set_load_pin(loadPin)

	loadId = newLoad.add(db)
	if loadId > 0:
		return 'Load has been added.'
	else:
		return 'Error! Kindly try again.'


@app.route('/api/listLoads')
def listLoads():
	if session["userData"]['isLoggedIn']:

		from DBmodels import Loads
		loadsList = db.session.query(Loads).all()
		loadsListDict = dict()
		counter = 0
		for each in loadsList:
			print(each)
			load = dict()
			load['loadId'] = each.id
			load['loadName'] = each.loadName
			load['loadType'] = each.loadType
			load['loadStatus'] = each.loadStatus
			load['loadPin'] = each.loadPin
			load['isSensor'] = each.isSensor
			counter += 1
			loadsListDict[counter] = load
		return jsonify(loadsListDict)

	else:
		loadData = dict()
		loadData['ErrorMessage'] = 'You need to be logged In first.'
		return loadData




@app.route('/api/loadTurnOn/<id>')
def loadTurnOn(id):
	loadId = id
	if session["userData"]['isLoggedIn']:
		from classes1.Load import Load
		load = Load()
		load.on(loadId);
		return "Turned On"
	else:
		return redirect('/login')


@app.route('/api/loadTurnOff/<id>')
def loadTurnOff(id):
	loadId = id
	if session["userData"]['isLoggedIn']:
		from classes1.Load import Load
		load = Load()
		load.off(loadId);
		return "Turned On"
	else:
		return redirect('/login')


@app.route('/api/cameraStream/<camIndex>')
def cameraStream(cameraIndex):
	from classes1.Camera import Camera
	camera = Camera()
	camera.startStream(camIndex)
	return Response(camera.generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
