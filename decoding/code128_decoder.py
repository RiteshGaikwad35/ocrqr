import numpy as np
import cv2


# 
CODE128_PATTERNS = {
    "11011001100": 104,  
    "11010010000": 0,
    "11010011100": 1,
   
}

START_CODES = {
    103: 'A',
    104: 'B',
    105: 'C'
}

def extract_signal(barcode_img):
    resized = cv2.resize(barcode_img, None, fx=2, fy=2)
    signal = np.mean(resized, axis=0)
    threshold = np.mean(signal)
    binary = (signal < threshold).astype(int)
    return binary

def run_length_encoding(signal):
    runs = []
    current = signal[0]
    count = 1

    for val in signal[1:]:
        if val == current:
            count += 1
        else:
            runs.append(count)
            current = val
            count = 1
    runs.append(count)

    return runs

def normalize_widths(widths):
    min_width = min(widths)
    normalized = [round(w / min_width) for w in widths]
    return normalized

def decode_code128(barcode_img):
    signal = extract_signal(barcode_img)
    widths = run_length_encoding(signal)
    normalized = normalize_widths(widths)

    pattern = ''.join(str(w) for w in normalized)

    decoded = []

    i = 0
    while i + 11 <= len(pattern):
        chunk = pattern[i:i+11]
        if chunk in CODE128_PATTERNS:
            code = CODE128_PATTERNS[chunk]
            decoded.append(chr(code + 32))
        i += 11

    return ''.join(decoded)
