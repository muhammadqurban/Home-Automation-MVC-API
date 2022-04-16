
class User():
    
    def getFirstName(self):
      return self.firstName
    
    def setFirstName(self,FirstName):
      self.firstName=FirstName

    def getLastName(self):
      return self.lastName
    
    def setLastName(self,LastName):
      self.lastName=LastName

    def getEmail(self):
      return self.email
    
    def setEmail(self,email):
      self.email=email

    def setPassword(self,password):
       self.password= password

    def getPassword(self):
       return self.password

    def register(self, db):
        from DBmodels import User
        # add registration code here.
        record = User(self.getFirstName(), self.getLastName(), self.getEmail(), self.getPassword())
        
        try:
            db.session.add(record)
            if not (db.session.commit()):
                return record.id
            else:
                return 0
                
        except Exception as e:
            return 0
        # db.session.add(record)
        # return db.session.commit()

    def login(self, db, userEmail, userPass):
        
        from DBmodels import User
        from DBmodels import Loads
        #fetch data.
        no_of_users = db.session.query(User).all()
        no_of_loads = db.session.query(Loads).all()

        print("No of users: ",len(no_of_users))
        print('No of loads: ', len(no_of_loads))

        record = db.session.query(User).filter_by(Email=userEmail).first()
        
        if record is not None:
            # print("The id is: ",record.id)
            # print('the password is: ', record.password)
            
            if record.password == userPass:
                userData = dict()
                userData['totalUsers'] = len(no_of_users)
                userData['totalLoads'] = len(no_of_loads)
                userData['userId'] = record.id
                userData['userfirstName'] = record.firstName
                userData['userLastName'] = record.lastName
                userData['userEmail'] = record.Email
                userData['userRegDate'] = record.reg_date
                userData['isLoggedIn'] = True

                return userData
            else:
                print("passwords don't match")
                return dict()
        else:
            return dict()

        
        return ulogin

    def logout(self):
        ulogout="To not access your account"
        print("well come:",ulogout)

    def updateProfile(self ):
        pass
        
    def verifyUser(self):
        uvarify="verified users into your apps "
        print("well come",uvarify)