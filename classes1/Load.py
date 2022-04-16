class Load:

    id = 0
    name = 0
    Type = ""
    pinNumber = 0

    def get_load_id(self):
        return self.loadId

    def set_load_id(self,loadId):
        self.loadId=loadId
     
    def get_load_name(self):
        return self.loadName

    def set_load_name(self,loadName):
        self.loadName=loadName

    def get_load_type(self):
        return self.loadType

    def set_load_type(self, loadType):
        self.loadType = loadType

    def set_load_pin(self, pinNumber):
        self.pinNumber = pinNumber

    def get_load_pin(self):
        return self.pinNumber

    def on(self, id):
        import RPi.GPIO as GPIO
        from DBmodels import Loads

        loadsList = db.session.query(Loads).filter_by(id=id).first()

        pinNumber = loadsList.pinNumber
        
        GPIO.output(pinNumber,1)
        return True

    def off(self, id):
        import RPi.GPIO as GPIO
        from DBmodels import Loads

        pinNumber = 2

        #this will not print any bugs to GPIO related on python shell
        GPIO.setwarnings(False)
        #this means that we are using GPIO pin and not using board numbers
        GPIO.setmode(GPIO.BCM)
        #All these pins are output thats why we are setting here GPIO.OUT
        GPIO.setup(pinNumber, GPIO.OUT)
        
        GPIO.output(pinNumber,0)

        return True

    def viewStatus(self):
        uof="The information displayed in the Status Log"
        print("well come:",uof)

    def isSensor(self):
        TisSensor = "Load at the end of a PagingData."
        FisSensor = "Load at the end of a PagingData."

        if TisSensor==FisSensor:
            print("isSensor was True")
        else:
            print("isSensor was faluse")

    def add(self, db):
        from DBmodels import Loads
        record = Loads(self.get_load_name(), self.get_load_type(), self.get_load_pin())
        try:
            db.session.add(record)
            if not (db.session.commit()):
                return record.id
            else:
                return 0  
        except Exception as e:
            return 0

    def setupAll():
        # Setup pins
        import RPi.GPIO as GPIO
        from DBmodels import Loads
        #this will not print any bugs to GPIO related on python shell
        GPIO.setwarnings(False)
        #this means that we are using GPIO pin and not using board numbers
        GPIO.setmode(GPIO.BCM)
        #All these pins are output thats why we are setting here GPIO.OUT

        loadsList = db.session.query(Loads).all()
        for each in loadsList:
            GPIO.setup(each.loadPin, GPIO.OUT)