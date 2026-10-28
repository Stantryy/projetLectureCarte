import cv2
from camera import save_frame
from pytesseract import image_to_string

def preprocess_for_ocr(img, threshold_value):
    """
    Prétraite une image pour l'OCR :
    - Conversion en niveaux de gris
    - Amélioration du contraste
    - Seuillage global simple
    """
    # Convertir en gris
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Ajustement automatique du contraste
    gray = cv2.equalizeHist(gray)

    # Seuillage global simple
    _, thresh = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)
    
    # Sauvegarde pour debug si besoin
    save_frame(thresh, "testPreprocess.jpg")
    
    return thresh


def read_text(image_path):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Impossible de charger l'image : {image_path}")
    
    preprocessed = preprocess_for_ocr(img,200)
    text = image_to_string(preprocessed, config='--psm 6')
    return text