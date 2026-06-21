from detection.vehicle_detector import detect_vehicles

result = detect_vehicles(
    "test_images/test1.jpg"
)

print(result)