import cv2

cam = cv2.VideoCapture(0)

print("Press s to save your face")
print("Press q to quit")

while True:
    ret, frame = cam.read()
    if not ret:
        continue

    cv2.imshow("Register Face", frame)

    key = cv2.waitKey(1)

    if key == ord('s'):
        cv2.imwrite("my_face.jpg",frame)
        print("Face saved succesfully")
        break
    if key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()