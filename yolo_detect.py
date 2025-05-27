from ultralytics import YOLO
import cv2

# Load a pre-trained YOLOv8 model
model = YOLO("yolov8n.pt")  # 'n' = nano (lightweight version)

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Can't receive frame. Exiting ...")
        break

    # Run YOLOv8 inference
    results = model(frame, imgsz=640)

    # Visualize the results
    annotated_frame = results[0].plot()
    cv2.imshow("YOLOv8 Object Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
