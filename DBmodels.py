from flask_app import app
from flask_sqlalchemy import *
import datetime
from sqlalchemy import Column, Integer, DateTime

db = SQLAlchemy(app)

# Alerts Model.
class Alerts(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	alertName = db.Column(db.String(int(150)), unique=True)
	alertType = db.Column(db.String(150))
	alertText = db.Column(db.String(200))

	def __init__(self, alertName, alertType, alertText):
		self.alertName = alertName
		self.alertType = alertType
		self.alertText = alertText

# Camera Model..
class Camera(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	cameraName = db.Column(db.String(150))
	cameraLocation = db.Column(db.String(150))
	cameraStatus = db.Column(db.Boolean, unique=False, default=True)

	def __init__(self, cameraName, cameraLocation, cameraStatus):
		self.cameraName = cameraName
		self.cameraLocation = cameraLocation
		self.cameraStatus = cameraStatus

# Chat Model.
class chat(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_1_id = db.Column(db.Integer, unique=False , default=0)
	user_2_id = db.Column(db.Integer, unique=False, default=0)
	chatDate = db.Column(db.DateTime, unique=False)


	def __init__(self, user_1_id,user_2_id, chatDate):
		self.user_1_id = user_1_id
		self.user_2_id = user_2_id
		self.chatDate = chatDate

# Messages Model.
class Messages(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	senderId = db.Column(db.Integer, nullable=False)
	receiverId = db.Column(db.Integer, nullable=False)
	messageText = db.Column(db.String(200))


	def __init__(self, senderId, receiverId, messageText):
		self.senderId = senderId
		self.receiverId = receiverId
		self.messageText = messageText
		

# Loads Model.
class Loads(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	loadName = db.Column(db.String(120), unique=True, nullable=False)
	loadType = db.Column(db.String(50), nullable=False)
	loadPin = db.Column(db.Integer, nullable=False)
	loadStatus = db.Column(db.Boolean, default=False, nullable=False)
	isSensor = db.Column(db.Boolean, default=False)
	def __init__(self, loadName, loadType, loadPin):
		self.loadName = loadName
		self.loadType = loadType
		self.loadPin = loadPin

# User Model.
class User(db.Model):

	id = db.Column(db.Integer, primary_key=True)

	firstName = db.Column(db.String(150), nullable=False)
	lastName = db.Column(db.String(150), nullable=False)
	Email = db.Column(db.String(189), nullable=False, unique=True)
	password = db.Column(db.String(255))
	reg_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
	accountStatus = db.Column(db.Integer, default=0)
	blockStatus = db.Column(db.Integer, default=0)
	isAdmin = db.Column(db.Boolean, default=False)

	# userPreviliges = db.relationship('userPreviliges', backref='User', lazy=True)

	def __init__(self, firstName, lastName, Email, password):
		self.Email = Email
		self.password = password
		self.firstName = firstName
		self.lastName = lastName
		
	
# Smart Door Model.
class SmartDoor(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	status = db.Column(db.Integer, nullable=False)
	name = db.Column(db.String(150), nullable=False)
	automationStatus = db.Column(db.String(150), nullable=False)

	def __init__(self, status, name):
		self.status = status
		self.name = name


# Privileges Model.
class Privileges(db.Model):
	
	id=db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(150), unique=True)
	status = db.Column(db.Boolean, default=False, nullable=False)
	privilegeEndPoint = db.Column(db.String(150), nullable=False)

	# userPreviliges = db.relationship('userPreviliges', backref='Privileges', lazy=True)

	def __init__(self, name, status):
		self.name = name
		self.status = status



# User Privileges Model.
class userPreviliges(db.Model):

	id= db.Column(db.Integer, primary_key=True)
	# privilegeType = db.Column(db.String(180), nullable=False)
	# privilegeName = db.Column(db.String(180), nullable=False)

	privilegeId = db.Column(db.Integer, nullable=False)	
	userId = db.Column(db.Integer, nullable=False)

	def __init__(self, userId, privilegeId):
		self.userId = userId
		self.privilegeId = privilegeId
		# self.privilegeName = privilegeName
		# self.privilegeType = privilegeType



if __name__ == "__main__":
    db.create_all()
    # user1 = User(
    #     name="Paul John",email="pj@gmail.com",
    #     password="pjmaxson2020#"
    # )
    # user2 = User(
    #     name="John Doe",email="JD@gmail.com",
    #     password="jdmaxson2020#"
    # )
    # db.session.add_all([user1,user2])
    # db.session.commit()
