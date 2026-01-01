import cv2 
from win32com.client import Dispatch
import time
speaker = Dispatch("SAPI.SpVoice")

def speak(text):
    speaker.Speak(text)
capture=cv2.VideoCapture(0) 

speak("recording started")
time.sleep(5)
while True:
    
    
    ret,frame=capture.read()
    
    if not ret:
        print("Error:  could not read frame")
        break
    cv2.imshow("**video started recording**",frame)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
speak("recording ended")
time.sleep(5)        
capture.release()
cv2.destroyAllWindows()    
