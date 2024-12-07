from django.shortcuts import render
from django.http import StreamingHttpResponse
from .yolo_detection import run_detection
import cv2


def index(request):
    """
    Renders the home page.
    """
    return render(request, 'index.html')


def video_feed():
    """
    Captures video from webcam, runs YOLO detection, and streams frames.
    """
    camera = cv2.VideoCapture(0)

    while True:
        success, frame = camera.read()
        if not success:
            break

        # Run YOLO Detection
        detections = run_detection(frame)

        # Initialize statuses
        fire_status = "No"
        smoke_status = "No"

        # Check detections and update statuses
        for detection in detections:
            label = detection["label"]
            if "fire" in label:
                fire_status = "Yes"
            elif "smoke" in label:
                smoke_status = "Yes"

            # Draw Bounding Boxes
            x1, y1, x2, y2 = detection["x1"], detection["y1"], detection["x2"], detection["y2"]
            color = (0, 255, 0) if "Yes" in label else (0, 0, 255)  # Green for detection, Red otherwise
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, f"{label} ({detection['confidence']:.2f})", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        # Display the status in the top-right corner
        status_texts = [
            f"Fire: {fire_status}",
            f"Smoke: {smoke_status}",
        ]
        for i, text in enumerate(status_texts):
            color = (0, 255, 0) if "Yes" in text else (0, 0, 255)
            cv2.putText(frame, text, (10, 30 + i * 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

        # Encode the frame and yield it
        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


def stream_view(request):
    """
    Serves the video stream.
    """
    return StreamingHttpResponse(video_feed(), content_type='multipart/x-mixed-replace; boundary=frame')
