# object_detection/object_detector.py
from ultralytics import YOLO
import cv2

# Load the pretrained YOLOv8 model (nano for speed, you can use v8s or v8m for accuracy)
model = YOLO("yolov8n.pt")  # You can change to yolov8s.pt or yolov8m.pt for better accuracy


def detect_objects_from_camera():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Could not open webcam")
        return

    print("📷 Starting real-time object detection...")
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Perform detection
        results = model(frame)

        # Draw the results on the frame
        annotated_frame = results[0].plot()

        # Show frame
        cv2.imshow("YOLOv8 Object Detection", annotated_frame)

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

