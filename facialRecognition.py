import cv2 

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

camera =  cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors = 5, minSize =(30, 30))

    num_people = len(faces)
    print(f"Numero de pessoas: {num_people}")

    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow('Detecção de pessoas', frame)

        if cv2.imshow(1) & 0xFF == ord('q'):
            break
        camera.release()
        cv2.destroyAllWindows() 