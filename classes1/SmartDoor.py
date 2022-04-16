import AlAgent
class SmartDoor(AlAgent):

   doorId = 0
   doorStatus = True # True means On, False means Off
   doorName = "Main Door"
   automationStatus = False

   def open():
      uopen="To access your door"
      print("well come:",uopen)

   def close():
      uclose="Don't access your door"
      print("well come:",uclose) 

   def enableAutomation():
      uenableautomation="To access your Massage"
      print("well come:",uenableautomation)
  
   def disableAutomation():
      udisapleAutomation="your Massage disapleAutomation"
      print("well come:",udisapleAutomation)
   
   def getAutomationStatus():
      ucheckAutomationStatus=" your Massage checkAutomationStatus"
      print("well come:",ucheckAutomationStatus)