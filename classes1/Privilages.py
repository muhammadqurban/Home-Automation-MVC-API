class Privileges:
    def __init__(self,privilegeName,prvilegeType,privilegeStatus,palertType):
        self.privilegeName=privilegeName
        self.prvilegeType=prvilegeType
        self.privilegeStatus=privilegeStatus
        self.palertType=palertType

    def get_privilegeName(self):
        return self.privilegeName

    def set_privilegeName(self,privilegeName):
        self.privilegeName=privilegeName

    def get_prvilegeType(self):
        return self.prvilegeType

    def set_prvilegeType(self,prvilegeType):
        self.prvilegeType=prvilegeType

    def get_prvilegeType(self):
        return self.privilegeStatus

    def set_prvilegeType(self,privilegeStatus):
        self.privilegeStatus=privilegeStatus

    def sendMassage(self):
        usendMassage="To access your Massage"
        print("well come:",usendMassage)

    def getAllMassage(self):
        ugetAllMassage="To access your all Massage"
        print("well come:",ugetAllMassage)


# privilages=Privilages("Hashir","Privileg Light","Kaffeemaschine")

# privilages.set_privilegeName("Shah")
# print(privilages.get_privilegeName())

# privilages.sendMassage() 
# privilages.getAllMassage() 

