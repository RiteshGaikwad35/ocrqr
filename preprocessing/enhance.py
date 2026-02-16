import cv2
import numpy as np

def enhance_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    cl = clahe.apply(gray)

    bilateral = cv2.bilateralFilter(cl, 9, 75, 75)

    gaussian = cv2.GaussianBlur(bilateral, (9,9), 10.0)
    sharp = cv2.addWeighted(bilateral, 1.5, gaussian, -0.5, 0)

    return sharp
