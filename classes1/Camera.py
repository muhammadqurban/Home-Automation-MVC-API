class Camera():

     id = 0
     CameraLocation = ""
     CameraName = "My Initial cam"
     Status = True #True means on, false means off.

     def get_id(self):
          return self.id

     def set_id(self,id):
          self.id=id
      
     def get_CameraLocation(self):
          return self.CameraLocation

     def set_CameraLocation(self,CameraLocation):
          self.CameraLocationalertName=CameraLocation

     def get_CameraName(self):
          return self.CameraName

     def set_CameraName(self,CameraName):
          self.CameraName=CameraName
      
     def get_Status(self):
          return self.Status

     def set_Status(self,Status):
          self.Status=Status

     def stopStream(self):
          ustopStrram=" your stopStrram"
          print("well come:",ustopStrram)

     def startStream(self, camIndex):
          import cv2
          camera=cv2.VideoCapture(camIndex)
          return camera

     def generate_frames(self):
         while True:
             ## read the camera frame
             success,frame=camera.read()
             if not success:
                 break
             else:
                 ret,buffer=cv2.imencode('.jpg',frame)
                 frame=buffer.tobytes()

             yield(b'--frame\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
