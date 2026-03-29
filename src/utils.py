import cv2
from config import ALERT_CLASSES

def draw_boxes(frame, detections):
    for det in detections:
        x1, y1, x2, y2 = det["box"]
        label = det["model"]
        conf = det["confidence"]

        if label in ["fire", "flames"]:
            color = (0, 0, 255)
        elif label == "smoke":
            color = (255, 0, 0)
        elif label == "cigarettes":
            color = (0, 255, 255)
        else:
            color = (0, 255, 0)

        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(frame, f"{label} {conf:.2f}",
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, color, 2)

def is_alert(detections):
    return any(det["model"] in ALERT_CLASSES for det in detections)