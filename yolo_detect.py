from ultralytics import YOLO
import cv2

# Load the model
model = YOLO("yolov8s.pt")
model.conf = 0.4
model.iou = 0.5

# Animal class IDs from COCO dataset
animal_classes = {14, 15, 16, 17, 18, 19, 20, 21, 22, 23}

# Start webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame")
        break

    # Run inference
    results = model(frame, imgsz=640)[0]

    # Copy the frame for annotation
    annotated = frame.copy()

    for box in results.boxes:
        cls_id = int(box.cls[0])
        if cls_id not in animal_classes:
            continue  # Skip non-animal classes

        label = model.names[cls_id]
        conf = box.conf[0]
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        # Draw bounding box
        cv2.rectangle(annotated, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(annotated, f"{label} {conf:.2f}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("Animal Detection", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
