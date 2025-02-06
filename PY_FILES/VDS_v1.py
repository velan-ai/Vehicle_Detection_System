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

    def pre_process(self):
        # Reading the frame
        ret, frame = self.camera.read()

        if not ret:
            print("Unable to read camera device")

            return None, 0

        # Resizing
        frame = imutils.resize(frame, width=self.frame_width)
        # Converting the image into grey color
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detecting the Vehicle
        veh = self.car_cascade.detectMultiScale(grey, 1.05, 5)
        return frame, veh

    def identify(self, car_count):

        if car_count >= self.traffic_threshold:
            print("Vehicle detected")
        else:
            print("Vehicle not detected")

    def Monitor(self):
        print("Monitoring started")

        while True:
            frame, veh = self.pre_process()

            if frame is None:
                break

            for (x, y, w, h) in veh:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            # Displaying the pre-processed frame
            cv2.imshow("Frame", frame)
            self.identify(len(veh))

            # Exit function
            if cv2.waitKey(33) == 27:
                break

        self.camera.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    cascade_file = "cars.xml"
    print("Enter the parameters")

    try:
        camera_index = int(input("Enter the camera index ('0' OR '1'): "))
        frame_width = int(input("Enter the frame width (600 OR 1200) : "))
        traffic_threshold = int(input("Enter the traffic threshold (1,2,3,4,5): "))
    except ValueError:
        print("Invalid input")
        exit()


    # Initializing the traffic Monitor
    VDS = VDS(cascade_file, camera_index, frame_width, traffic_threshold)

    # Starting the application
    VDS.Monitor()