import OperationControl
class DataBaseHandler:

    dbHost = '127.0.0.1'
    dbUser = 'rootUser'
    dbPassword = 'root'

    def __init__(self,dbHost, dbUser, dpPassword):
        self.dbHost = dbHost
        self.dbUser = dbUser
        self.dpPassword = dpPassword

    ### Getters and Setters Start ###

    def get_db_Host(self):
        return self.dbHost
       
    def set_db_Host(self,dbHost):
        self.dbHost = dbHost
       
    def get_db_Password(self):
        return self.dpPassword

    def set_db_Password(self,dpPassword):
        self.dpPassword = dpPassword

    def get_db_user(self):
        return self.dbUser

    def set_db_user(self, dbUser):
        self.dbUser = dbUser

    ### Getters and Setters End  ###

    def connect(self):          
        # database connection code here.
        # enclosed in try and catch
        return True


    def updating(self):
        updating="Updation is correct"
        print("well come:",updating)


    def Delete(self):
        uDelete="a command on a computer which erases text."
        print("well come:",uDelete)

# test codes.
# databasehandier=DataBaseHandier("database administration to us","bewafa na")

# databasehandier.set_dbHost("Db")
# print(databasehandier.get_dbHost())

# databasehandier.connected() 
# databasehandier.updating()

