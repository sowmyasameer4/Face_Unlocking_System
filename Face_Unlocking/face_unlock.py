import cv2
import face_recognition
import os
import time

if not os.path.exists("my_face.jpg"):
    print("No registered face found")
    exit()

#Load the known face
known_image = face_recognition.load_image_file("my_face.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

#start camera
cam = cv2.VideoCapture(0)

print("Show your face to unlock")

#Variables to control show one-time("No matches")
no_match_flag = False
no_match_time = 0

while True:
    ret, frame = cam.read()
    if not ret:
        continue

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb)
    face_encodings = face_recognition.face_encodings(rgb, face_locations)
    
    match_found = False

    for face_encoding in face_encodings:
        match = face_recognition.compare_faces(
            [known_encoding],
            face_encoding,
            tolerance=0.5
        )

        if match[0]:
            print("Face matched. Access granted")
            cam.release()
            cv2.destroyAllWindows()
            exit()
        else:
            match_found = False
            if not no_match_flag:
                no_match_flag = True
                no_match_time = time.time()

    if no_match_flag and (time.time() - no_match_time < 2):
        cv2.putText(
            frame,
            "No Matches",
            (50,50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,0,255),
            2
        )
    elif no_match_flag:
        no_match_flag = False #reset flag after 2 seconds

    cv2.imshow("Face Unlock", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()