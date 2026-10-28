import cv2

def open_camera(index=0):
    cap = cv2.VideoCapture(index)
    if not cap.isOpened():
        raise RuntimeError("Impossible d'ouvrir la caméra")
    return cap

def get_frame(cap):
    ret, frame = cap.read()
    if not ret:
        raise RuntimeError("Erreur lecture caméra")
    return frame

def show_frame(frame, window_name="Camera"):
    cv2.imshow(window_name, frame)

def save_frame(frame, path="capture.jpg"):
    cv2.imwrite(path, frame)

def release_camera(cap):
    cap.release()
    cv2.destroyAllWindows()

# -----------------------
# ROI clavier uniquement
def select_roi(frame):
    """
    Sélection de la zone à découper via le clavier.
    Entrez x1, y1, x2, y2
    """
    print("Sélection ROI au clavier.")
    h, w = frame.shape[:2]
    print(f"Taille image : largeur={w}, hauteur={h}")
    
    while True:
        try:
            x1 = int(input("x1 (gauche): "))
            y1 = int(input("y1 (haut): "))
            x2 = int(input("x2 (droite): "))
            y2 = int(input("y2 (bas): "))
            
            if 0 <= x1 < x2 <= w and 0 <= y1 < y2 <= h:
                return frame[y1:y2, x1:x2]
            else:
                print("Coordonnées invalides, réessayez.")
        except ValueError:
            print("Entrée invalide, veuillez entrer des nombres entiers.")