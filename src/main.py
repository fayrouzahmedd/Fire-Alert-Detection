import cv2
from camera import get_camera
from pipeline import SmartPipeline
from utils import draw_boxes, is_alert
from tracker import AlertTracker

def main():
    cap = get_camera(0)
    pipeline = SmartPipeline()
    tracker = AlertTracker(cooldown=5)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        detections = pipeline.process(frame)

        draw_boxes(frame, detections)

        if is_alert(detections) and tracker.should_alert():
            print("🚨 FIRE ALERT CONFIRMED!")
            cv2.putText(frame, "FIRE ALERT!", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 255), 3)

        cv2.imshow("SMART FIRE SYSTEM", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()