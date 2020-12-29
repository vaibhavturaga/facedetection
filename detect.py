import cv2, time

face_cascade = cv2.CascadeClassifier("C:\\Users\\b2rag\\Downloads\\FaceDetect-master\\FaceDetect-master\\haarcascade_frontalface_default.xml")

video = cv2.VideoCapture(0)

numOfFrames = 1

while True:
    numOfFrames += 1

    check,frame = video.read()
    print(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor = 2, minNeighbors = 5)

    for x,y,w,h in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
    
    cv2.imshow("Camera", frame)
    key = cv2.waitKey(1)

    if key == ord('x'):
        break


print(a)

video.release()
cv2.destroyAllWindows()
