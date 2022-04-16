class Massage:
    
    messageId = 0
    senderId = 0
    recieverId = 0
    chatId = 0
    messageText = ""

    def __init__(self, massageId, senderId, recieverId, chatId, massageText):
        self.massageId = massageId
        self.senderId = senderId
        self. recieverId = recieverId
        self.chatId = chatId
        self. massageText = massageText

    def get_massage_id(self):
        return self.massageId

    def set_massage_id(self, massageId):
        self.massageId=massageId

    def get_sender_id(self):
        return self.senderId

    def set_sender_id(self,senderId):
        self.senderId=senderId

    def get_reciever_id(self):
        return self.recieverId

    def set_reciever_id(self,recieverId):
        self.recieverId=recieverId

    def get_chat_id(self):
        return self.chatId

    def set_chat_id(self,chatId):
        self.chatId=chatId

    def get_massage_text(self):
        return self. massageText

    def set_massage_text(self, massageText):
        self. massageText= massageText


    def  is_seen(self): 
        tisSean = "massage is seen"
        fisSean = "massage is not seen"

        if tisSean==fisSean:
        print("condition was true")
        else:
        print("condision was faluse")


    def  is_replied(self): 
        tisReplied = "massage is Replied"
        fisReplied = "massage is not Replied"

        if tisReplied==fisReplied:
        print("condition was true")
        else:
        print("condision was faluse")


    def send_massage(self):
        usendMassage="To access your Massage"
        print("well come:",usendMassage)


    def get_all_massages(self):
        ugetAllMassage="To access your all Massage"
        print("well come:",ugetAllMassage)
 
      
# massage=Massage(1,2,3,4,"Hellow Hashir")

# massage.set_chatId(0)
# print(massage.get_chatId())

# massage.isSean()
# massage.getAllMassage () 
 
      

