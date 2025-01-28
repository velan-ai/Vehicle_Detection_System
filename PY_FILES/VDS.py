import cv2
import imutils  # Helps in resizing

class VDS:
    def __init__(self, cascade_file, camera_index, frame_width, traffic_threshold):
        # Initializing the objects for vehicle tracking
        self.cascade_file = cascade_file
        self.camera_index = camera_index
        self.frame_width = frame_width
        self.traffic_threshold = traffic_threshold

        # Loading the cascade classifier

        self.car_cascade = cv2.CascadeClassifier(cascade_file)
        if self.car_cascade.empty():
            print("Unable to find the Carcascade classifier empty")

        # Initializing the camera value
        self.camera = cv2.VideoCapture(camera_index)
        if not self.camera.isOpened():
            print("Unable to open camera device")

    def pre_process(self, frame):
        # Reading the frame
        frame = self.camera.read()[1]
        # Resizing
        frame = imutils.resize(frame, width=self.frame_width)
        # Converting the image into grey color
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detecting the Vehicle
        veh = self.car_cascade.detectMultiScale(grey, 1.05, 5)







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




