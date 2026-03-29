from ultralytics import YOLO
from config import MODEL_PATHS, CONF_THRESHOLDS

class ModelRunner:
    def __init__(self):
        self.models = {}

    def load(self, name):
        if name not in self.models:
            print(f"[INFO] Loading {name}...")
            self.models[name] = YOLO(MODEL_PATHS[name])

    def predict(self, frame, model_name):
        self.load(model_name)
        model = self.models[model_name]

        detections = []
        results = model(frame, verbose=False)

        for r in results:
            boxes = r.boxes
            if boxes is None:
                continue

            for box in boxes:
                conf = float(box.conf[0])
                if conf < CONF_THRESHOLDS[model_name]:
                    continue

                x1, y1, x2, y2 = box.xyxy[0].tolist()

                detections.append({
                    "model": model_name,
                    "box": [int(x1), int(y1), int(x2), int(y2)],
                    "confidence": conf
                })

        return detections