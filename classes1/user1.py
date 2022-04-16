class User:
    def __init__(self,firstname,lastname,email,password):
        self.firstname=firstname
        self.lastname=lastname
        self.email=email
        self.password=password

    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname

    def get_email(self):
        return self.email
    
    def get_password(self):
        print(self.password)



    def set_firstname(self,name):
        self.firstname=name

    

user1=User("nayab","iqbal","iqbal@gmail.com","12345")

user1.set_firstname("haseb")
print(user1.get_firstname())