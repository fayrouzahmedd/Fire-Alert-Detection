from config import PRIMARY_MODEL, SECONDARY_MODELS, ALWAYS_ON_MODELS, ALERT_CLASSES
from detector import ModelRunner

class SmartPipeline:
    def __init__(self):
        self.runner = ModelRunner()

    def process(self, frame):
        all_detections = []

        # 1️⃣ Always-on models (cigarettes)
        for model in ALWAYS_ON_MODELS:
            detections = self.runner.predict(frame, model)
            all_detections.extend(detections)

        # 2️⃣ Primary model (smoke)
        primary_detections = self.runner.predict(frame, PRIMARY_MODEL)
        all_detections.extend(primary_detections)

        # 3️⃣ Trigger secondary ONLY if smoke detected
        if len(primary_detections) > 0:
            for model in SECONDARY_MODELS:
                detections = self.runner.predict(frame, model)
                all_detections.extend(detections)

        return all_detections