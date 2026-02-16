from ultralytics import YOLO
import cv2

class YOLODetector:
    def __init__(self, model_path, conf=0.5):
        self.model = YOLO(model_path)
        self.conf = conf

    def detect(self, frame):
        results = self.model(frame)[0]

        boxes = []

        for box in results.boxes:
            if box.conf[0] >= self.conf:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                boxes.append((x1, y1, x2, y2))

        return boxes
