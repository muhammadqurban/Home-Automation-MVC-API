import datetime
class Chat:
    
    chatid = 0
    user2ID = 0
    user1ID = 0

    def __init__(self, chatID,user2ID,user1ID):
       self.chatID= chatID
       self.user2ID=user2ID
       self.user1ID=user1ID
          

    def get_chatID(self):
       return self.chatID

    def set_chatID(self,chatID):
       self.chatID=chatID
           
    def get_user2ID(self):
       return self.user2ID
     
    def set_user2ID(self,user2ID):
       self.user2ID=user2ID
      
    def get_user1ID(self):
       return self.user1ID
     
    def set_user1ID(self,user1ID):
       self.user1ID=user1ID
           
    def getAllChats(self):
       ugetAllChats="To access your getAllChats"
       print("well come:",ugetAllChats)

    def StartChat(self, user1ID, user2ID):
       uStartChat="To access your StartChat"
       print("well come:",uStartChat)


    def deleteChat(self, user1ID, user2ID):
       udeletChate="To access your deletChate"
       print("well come:",udeletChate)
 

# x = datetime.datetime.now()
# print(x)

# chat=Chat(2,3,4)

# chat.set_chatID(1)
# print(chat.get_user2ID())

# chat.getAllChats() 
# chat.StartChat()  

