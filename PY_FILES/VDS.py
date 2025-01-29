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

    def identify(self, Car_count):

        if car_count >= self.traffic_threshold:
            print("Vehicle detected")
        else:
            print("Vehicle not detected")

    def Monitor(self):
        print("Monitoring started")

        while True:

            self.pre_process(self.camera)













