import cv2
from ultralytics import YOLO

# Load smaller & faster model
model = YOLO("yolov8n.pt")

# Use IP Webcam URL
url = "http://192.168.29.21:8080/video"

# Use FFMPEG backend (better for streams)
cap = cv2.VideoCapture(url, cv2.CAP_FFMPEG)

if not cap.isOpened():
    print("❌ Error: Could not open IP camera")
    exit()

print("✅ Camera connected successfully!")

# Reduce resolution directly from capture
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

frame_skip = 2   # Process every 2nd frame
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame")
        break

    frame_count += 1

    # Skip frames to increase FPS
    if frame_count % frame_skip != 0:
        continue

    # Resize smaller (BIG FPS boost)
    frame = cv2.resize(frame, (480, 360))

    # YOLO inference (faster settings)
    results = model(frame, conf=0.5, imgsz=320, verbose=False)

    annotated_frame = results[0].plot()

    cv2.imshow("YOLOv8 Object Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()