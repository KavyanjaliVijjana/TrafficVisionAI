from ultralytics import YOLO

helmet_model = YOLO(
    "models/helmet.pt"
)

print(helmet_model.names)

def detect_helmet(image_path):

    results = helmet_model(image_path)

    detections = []

    for result in results:

        for box in result.boxes:

            cls_id = int(box.cls[0])

            cls_name = helmet_model.names[
                cls_id
            ]

            confidence = float(
                box.conf[0]
            )

            detections.append({

                "class":
                cls_name,

                "confidence":
                round(confidence, 2)
            })
    # SAVE ANNOTATED IMAGE
    results[0].save(
        filename="outputs/helmet_result.jpg"
    )

    return detections