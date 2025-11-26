from ultralytics import YOLO

class HandDetector:
    def __init__(self, model_path="models/hand.pt", conf=0.6):
        self.model = YOLO(model_path)
        self.conf = conf

    def detect(self, frame):
        results = self.model.predict(frame, conf=self.conf)
        hands = []

        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                hands.append((x1, y1, x2, y2))

        return hands
