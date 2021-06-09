# QRcode-FaceRecognition-Door-Lock-system-Arduino-IOT
Door lock system using Arduino and Python with 2 step authentication(Face Recognition and QR code).


<b>Important files</b>:<br>
* <b>faces.py</b> : script that contains only face recognition code(just to detect the face and recognize it if the face is trained with the model)<br><br>
* <b>faces_train.py</b> : script that creates the face classification model by training upon the images stored in the images folder and creates a pickle file with the label ids (i.e. name of the user is label encoded for training the model)<br><br>
* <b>qr_face_recogntion.py</b> : main file that takes care of the 2 step authentication using QR code and face recognition, communication with Arduino(Open or Close the door), user interaction using text to speech etc.<br><br>
* <b>The authentication process</b> : <br><br>
![](qr_face_detection_flowchart.png)
