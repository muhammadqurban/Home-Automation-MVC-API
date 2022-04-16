class Syestem:
    def __init__(self,NetworkType,ServerAddress,ServerName):
        self.NetworkType=NetworkType
        self.ServerAddress=ServerAddress
        self.ServerName=ServerName

    def getNetworkType(self):
        return self.NetworkType

    def setNetworkType(self,NetworkType):
        self.NetworkType=NetworkType
      
    def getServerAddress(self):
        return self.ServerAddress
           
    def setServerAddress(self,ServerAddress):
        self.ServerAddress=ServerAddress

    def getServerName(self):
        return self.ServerName
           
    def setServerName(self,ServerName):
        self.ServerName=ServerName

    def isNetworkConnected():
        pass

    def run():
        pass
        
    def stop():
        pass


# syestem=Syestem("A metered network connection is required for this work.","com.mongodb.ServerAddress","Free Vps Server")

# syestem.set_ServerName("Shah")
# print(syestem.get_ServerName)

# syestem.update()
# syestem.update() 

#      