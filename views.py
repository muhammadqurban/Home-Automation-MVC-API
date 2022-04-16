from flask_app import *
import endpoints


responseData = dict() #for storing data about user, priviliges, loads, cameras, doors, automation status etc.

@app.route('/')
def home():
	loggedInCookie = dict(session)
	if 'userData' in loggedInCookie:
		if 'isLoggedIn' in loggedInCookie['userData']:
			print("user ID: (from view)", loggedInCookie['userData']['userId'])
			resp = render_template('dashboard.html')
		else:
			resp = redirect('/login')
	else:
		print('I am here')
		resp = redirect('/login')
	return resp

@app.route('/login', methods= ['GET','POST'])
def loginUser():
	response = make_response(render_template('login.html'))
	response.set_cookie('loggedIn', str(1))
	return response


@app.route('/register')
def registerUser():
	return render_template('index.html')


@app.route('/logout')
def logoutUser():
	session['userData'] = dict()
	return redirect('/login')

@app.route('/about')
def aboutDevs():
	return "Developed by Hashir Shah"

@app.route('/profile')
def userProfile():
	return 'userProfile Page.'

@app.route('/dataset')
def dataset():
	return 'gather user images.'


@app.route('/manageUsers')
def manageUsers():
	print(session['userData'])

	loggedInCookie = dict(session)
	if 'userData' in loggedInCookie:
		
		if 'isLoggedIn' in loggedInCookie['userData']:
			from DBmodels import User
			blockedUsersData = db.session.query(User).filter(User.blockStatus == 1).all()
			db.session.commit()
			blockedUserList = []
			counter = 0
			for x in blockedUsersData:
				blockedUser = dict()
				blockedUser['userId'] = x.id
				blockedUser['name'] = x.firstName + " " + x.lastName
				counter += 1
				blockedUserList.append(blockedUser)

			return render_template('manageUsers.html', blockedUsers=blockedUserList)
		else:
			return redirect('/login')
	else:
		print('I am here')
		return redirect('/login')


@app.route('/manageLoads')
def manageLoads():
	loggedInCookie = dict(session)

	if 'userData' in loggedInCookie:
		if 'isLoggedIn' in loggedInCookie['userData']:
			return render_template('manageLoads.html')
		else:
			return redirect('/login')
	else:
		return redirect('/login')

@app.route('/manageAlerts')
def manageAlerts():
	return render_template('manageAlerts.html')

@app.route('/smartDoor')
def smartDoor():
	return render_template('manageDoor.html')

@app.route('/manageStream')
def manageStream():
	return render_template('manageStreams.html')

@app.route('/video')
def video():
	from classes1.Camera import Camera
	camera = Camera()
	return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/stopVideo')
def stopVideo():
	import cv2
	cv2.VideoCapture(0).release()
	cv2.destroyAllWindows()
	return 'streamStopped'

@app.route('/chats')
def userChats():
	return render_template('chats.html')

@app.route('/voiceControl')
def voiceControl():
	return render_template('voice.html')

@app.route('/systemSettings')
def settings():
	return render_template('systemSettings.html')

@app.route('/history')
def history():
	return render_template('actionsHistory.html')


