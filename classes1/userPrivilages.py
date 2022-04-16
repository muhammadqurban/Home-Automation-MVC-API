import Privilages
class userPrivillages(Privilages):

    def __init__(self, userId, privilegeId):
        self.userId = userId
        self.privilegeId = privilegeId
          
     
    def getUserId(self):
        return self.userId

    def setUserId(self,userId):
        self.userId=userId
     
    def getPrivilegeID(self):
        return self.privilegeID

   
    def getUserprivillages(self):
        ugetUserprivillages="Retrieving all user privileges"
        print("well come:",ugetUserprivillages)
     

    def restricPrivillages(self):
        urestricPrivillages=" used to be continuously unable to updateS"
        print("well come:",urestricPrivillages)
