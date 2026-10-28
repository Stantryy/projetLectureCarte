import cv2
from camera import open_camera, get_frame, save_frame, release_camera
from ocr import read_text

# --- Paramètres ROI par défaut ---
roi = {
    "x1": 100,
    "y1": 100,
    "x2": 400,
    "y2": 300,
    "step": 5
}

# --- Ouverture caméra ---
cap = open_camera(0)
print("Ajuste la ROI avec x/X, c/C, y/Y, u/U. ENTER pour capturer, ESC pour quitter.")

while True:
    try:
        frame = get_frame(cap)
    except RuntimeError as e:
        print(e)
        break

    # --- Dessine le rectangle ROI sur la frame ---
    display = frame.copy()
    cv2.rectangle(display, (roi["x1"], roi["y1"]), (roi["x2"], roi["y2"]), (0, 255, 0), 2)
    cv2.imshow("Camera", display)

    key = cv2.waitKey(1) & 0xFF

    # --- Quitter ---
    if key == 27:  # ESC
        break

    # --- Capturer et lancer OCR ---
    elif key == 13:  # ENTER
        cropped = frame[roi["y1"]:roi["y2"], roi["x1"]:roi["x2"]]
        save_frame(cropped, "capture_roi.jpg")
        text = read_text("capture_roi.jpg")
        print("RESULTAT OCR :")
        print(repr(text))

    # --- Ajustements ROI corrigés et fonctionnels ---
    elif key == ord('s'):  # augmenter x2 (droite)
        roi["x2"] = min(roi["x2"] + roi["step"], frame.shape[1])
    elif key == ord('x'):  # diminuer x2
        roi["x2"] = max(roi["x2"] - roi["step"], roi["x1"] + 1)
    elif key == ord('d'):  # augmenter x1 (gauche)
        roi["x1"] = min(roi["x1"] + roi["step"], roi["x2"] - 1)
    elif key == ord('c'):  # diminuer x1
        roi["x1"] = max(roi["x1"] - roi["step"], 0)
    elif key == ord('h'):  # augmenter y2 (bas)
        roi["y2"] = min(roi["y2"] + roi["step"], frame.shape[0])
    elif key == ord('y'):  # diminuer y2
        roi["y2"] = max(roi["y2"] - roi["step"], roi["y1"] + 1)
    elif key == ord('j'):  # augmenter y1 (haut)
        roi["y1"] = min(roi["y1"] + roi["step"], roi["y2"] - 1)
    elif key == ord('u'):  # diminuer y1
        roi["y1"] = max(roi["y1"] - roi["step"], 0)

release_camera(cap)
cv2.destroyAllWindows()