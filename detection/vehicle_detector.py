from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

VEHICLE_CLASSES = [
    "car",
    "motorcycle",
    "bus",
    "truck",
    "person"
]

def detect_vehicles(image_path):

    results = model(image_path)

    detections = []

    for result in results:

        for box in result.boxes:

            class_id = int(box.cls[0])

            class_name = model.names[class_id]

            confidence = float(box.conf[0])

            if class_name in VEHICLE_CLASSES:

                detections.append({
                    "class": class_name,
                    "confidence": round(confidence, 2)
                })

    

    vehicle_counts = {}

    for detection in detections:

        cls = detection["class"]

        vehicle_counts[cls] = (
            vehicle_counts.get(cls, 0) + 1
        )
    results[0].save(filename="outputs/result.jpg")

    return detections, vehicle_counts