class Alerts:
     alertID = 0
     alertName = ""
     alertText = ""
     palertType = "imageAlert"
     
     def __init__(self,alertID,alertName,alertText,palertType):
          self.alertID=alertID
          self.alertName=alertName
          self.alertText=alertText
          self.palertType=palertType

     def get_alertID(self):
          return self.alertID

     def set_alertID(self,alertID):
          self.alertID=alertID
           
     def get_alertName(self):
          return self.alertName

     def set_alertName(self,alertName):
        self.alertName=alertName
      
     def get_alertText(self):
          return self.alertText

     def set_alertText(self,alertText):
          self.alertText=alertText
           
     def get_palertType(self):
          print(self.palertType)

     def set_palertType(self,palertType):
          self.palertType=palertType
      
     def sandBroadcast(self):
          a = "massage Broadcast"
          b = " massage  is not Broadcast"
          if a==b:
               print("condition was true")
          else:
               print("condision was faluse")

     def sandprivate(self):
          a = "massage private"
          b = " massage  is not private"
           
          if a==b:
               print("condition was true")
          else:
               print("condision was faluse") 

