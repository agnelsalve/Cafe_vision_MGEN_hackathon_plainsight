from openfilter import Filter
import cv2

class Camera(Filter):
    def __init__(self, source=0):
        super().__init__()
        self.cap = cv2.VideoCapture(source)

    def run(self, data):
        ret, frame = self.cap.read()
        if not ret:
            self.stop()
            return None
        return {"frame": frame}

    def close(self):
        self.cap.release()
