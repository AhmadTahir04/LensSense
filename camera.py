import cv2 as cv

# pip install opencv-python ot install modulde

class Camera:

    # Opens camera
    def __init__(self):
        self.camera = cv.VideoCapture(0)
        if not self.camera.isOpened():
            raise ValueError("Unable to open the camera!")

        self.width = self.camera.get(cv.CAP_PROP_FRAME_WIDTH)
        self.height = self.camera.get(cv.CAP_PROP_FRAME_HEIGHT)


    # Closes camera
    def __del__(self):
        if self.camera.isOpened():
            self.camera.release()

    # Gets frames (Data)
    def get_frame(self):
        if self.camera.isOpened():
            ret, frame = self.camera.read()

            # Resize the frame to fit the canvas size
            if ret:
                frame = cv.resize(frame, (640, 480))
                return (ret, cv.cvtColor(frame, cv.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return None


