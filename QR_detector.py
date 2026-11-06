
import cv2

# Initialize detectors
qr_detector = cv2.QRCodeDetector()

aruco_dict = cv2.aruco.getPredefinedDictionary(
    cv2.aruco.DICT_4X4_50
)
aruco_detector = cv2.aruco.ArucoDetector(aruco_dict)

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # --- QR Code Detection ---
    data, points, _ = qr_detector.detectAndDecode(frame)

    if points is not None:
        pts = points.astype(int).reshape(-1, 1, 2)
        cv2.polylines(frame, [pts], True, (0, 255, 0), 2)

        if data:
            cv2.putText(frame, data, tuple(pts[0, 0]),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                        (0, 255, 0), 2)

    # --- ArUco Detection ---
    corners, ids, _ = aruco_detector.detectMarkers(frame)

    if ids is not None:
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)

        for marker_id in ids.flatten():
            print("ArUco ID:", marker_id)

    cv2.imshow("QR + ArUco Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
