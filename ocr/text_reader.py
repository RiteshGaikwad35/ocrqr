import cv2
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def read_text(image, offset=80, config="--psm 7"):


    if image is None:
        return ""

    if image.size == 0:
        return ""

    # Convert to grayscale safely
    try:
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image.copy()
    except:
        return ""

    h, w = gray.shape

    if h < 20 or w < 20:
        return ""

    y_start = int(h * 0.65)

    if y_start >= h:
        y_start = int(h * 0.5)

    y_end = min(h, y_start + offset)

    if y_end <= y_start:
        return ""

    text_roi = gray[y_start:y_end, 0:w]

    if text_roi is None or text_roi.size == 0:
        return ""

    try:
        text_roi = cv2.resize(
            text_roi,
            None,
            fx=2,
            fy=2,
            interpolation=cv2.INTER_CUBIC
        )
    except:
        return ""

    try:
        text_roi = cv2.GaussianBlur(text_roi, (3, 3), 0)
    except:
        return ""

    try:
        text_roi = cv2.adaptiveThreshold(
            text_roi,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            11,
            2
        )
    except:
        return ""


    custom_config = config + " -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    try:
        text = pytesseract.image_to_string(text_roi, config=custom_config)
    except:
        return ""

    text = text.strip().replace(" ", "").replace("\n", "")

    return text
