src_cascade = 'cars.xml'

car_cascade = cv2.CascadeClassifier('cars.xml')

# initialising the camera value
camera = cv2.VideoCapture(1)

while True:
    detect = 0
    _, img = camera.read()  # read the frames

    img = imutils.resize(img, width=300)  # resize the image to 300

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Grayscaling the image

    cars = car_cascade.detectMultiScale(gray, 1.1, 1)  # coordinates of vehicle in a frame

    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow("Frame", img)
    b = str(len(cars))
    a = int(b)
    detect = a
    n = detect
    print("------------------------------------------------")
    print("North: %d " % (n))
    if n >= 2:
        print("There is more traffic in North")
    else:
        print("no traffic")
    if cv2.waitKey(33) == 27:
        break

camera.release()
cv2.destroyAllWindows()