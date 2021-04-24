#qr and face recognition authentication as two different independent modules

from cv2 import cv2
import numpy as np 
from pyzbar.pyzbar import decode   #pyzbar helps in detection and decoding of the qrcode
from faces import face_recognition

cap=cv2.VideoCapture(0)



while(True):
    success,frame=cap.read()

    for i in decode(frame):
        decoded_data=i.data.decode("utf-8")   #converts bytes to string value
        print(decoded_data)

        #Drawing polygon on frame (tilts w.r.t orientation)
        pts=np.array([i.polygon],np.int32)

        pts=pts.reshape((-1,1,2))  
        cv2.polylines(frame,[pts],True,(0,0,255),2)
        # print(pts)
     
        #Display text
        rect_pts=i.rect #using rect point as origin for text as we don't want the text to tilt with the qrcode
        fontScale=0.8
        thickness=1
        cv2.putText(frame,decoded_data,(rect_pts[0],rect_pts[1]),cv2.FONT_HERSHEY_SIMPLEX,fontScale,(255,0,0),thickness)
        # print(rect_pts)

        if(decoded_data.lower()=="barcelona"):
            cap.release()
            cv2.destroyAllWindows()
            face_recognition()

    cv2.imshow('Result',frame)

    ch=cv2.waitKey(1) #delay of 1ms    
    if(ch==113):
        break
      