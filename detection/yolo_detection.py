from ultralytics import YOLO
import cv2
import numpy as np

# Load the YOLO model
model = YOLO("models/fire_smoke_yolov8m.pt")  

# Class names
class_names = ['fire',  'other', 'smoke']


def run_detection(frame):
    """
    Runs YOLO detection on the input frame and returns the detections.
    """
    results = model(frame)
    detections = []
    for r in results[0].boxes.data.tolist():
        x1, y1, x2, y2, conf, cls = r
        detections.append({
            "x1": int(x1),
            "y1": int(y1),
            "x2": int(x2),
            "y2": int(y2),
            "confidence": conf,
            "class_id": int(cls),
            "label": class_names[int(cls)],  
        })
    return detections
