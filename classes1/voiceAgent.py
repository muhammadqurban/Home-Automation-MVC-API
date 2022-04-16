import OperationControl
class voiceAgent(OperationControl):

    def __init__(self, apiEndpoint, apikey):
        self.apiEndpoint = apiEndpoint
        self.apikey = apikey
      
    def getApiEndpoint(self):
        return self.apiEndpoint
    
    def setApiEndpoint(self,apiEndpoint):
        self.apiEndpoint=apiEndpoint

    def getAPIKey(self):
        return self.apikey
    
    def setAPIKey(self,apikey):
        self. apikey=apikey

    def setupRecognizer(self):
        usettupRecognizer=" Make sure that all words are spelled correctly."
        print("well come:",usettupRecognizer)

    def getVoiceCommand(self):
        ugetVoiceCommand="Under Microphone"
        print("well come:",ugetVoiceCommand)

    def performActions(self):
        uperformActions="command is used to execute complex user actions"
        print("well come:",uperformActions)
      

