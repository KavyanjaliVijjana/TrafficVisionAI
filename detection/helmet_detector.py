from ultralytics import YOLO

helmet_model = YOLO("models/helmet.pt")

def detect_helmet(image_path):

    results = helmet_model(image_path)

    helmets = 0
    no_helmets = 0

    for result in results:

        for box in result.boxes:

            cls = int(box.cls[0])

            class_name = helmet_model.names[cls]

            if class_name.lower() in [
                "helmet",
                "with_helmet"
            ]:
                helmets += 1

            elif class_name.lower() in [
                "without_helmet",
                "no_helmet"
            ]:
                no_helmets += 1

    return {
        "helmets": helmets,
        "no_helmets": no_helmets
    }