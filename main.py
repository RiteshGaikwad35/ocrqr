import cv2
from config import *
from preprocessing.enhance import enhance_image
from preprocessing.blur_restoration import wiener_filter
from decoding.code128_decoder import decode_code128
from ocr.text_reader import read_text


def detect_barcode_classic(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gradX = cv2.Sobel(gray, cv2.CV_32F, 1, 0, ksize=3)
    gradX = cv2.convertScaleAbs(gradX)

    _, thresh = cv2.threshold(
        gradX, 0, 255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 5))
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(
        closed,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    if not contours:
        return []

    c = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(c)

    return [(x, y, x + w, y + h)]



def main():

    cap = cv2.VideoCapture(CAMERA_INDEX)
    qr_detector = cv2.QRCodeDetector()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        display_frame = frame.copy()

     
        qr_data, qr_bbox, _ = qr_detector.detectAndDecode(frame)

        if qr_bbox is not None and qr_data != "":
            qr_bbox = qr_bbox.astype(int)

            x1 = qr_bbox[0][0][0]
            y1 = qr_bbox[0][0][1]
            x2 = qr_bbox[0][2][0]
            y2 = qr_bbox[0][2][1]

            cv2.rectangle(display_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # OCR text below QR (if printed)
            text_roi = frame[y2:y2+BARCODE_HEIGHT_OFFSET, x1:x2]
            text_value = read_text(text_roi, BARCODE_HEIGHT_OFFSET, OCR_CONFIG)

            cv2.putText(display_frame,
                        f"QR: {qr_data}",
                        (x1, y1 - 20),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (0, 255, 0),
                        2)

            cv2.putText(display_frame,
                        f"Text: {text_value}",
                        (x1, y1 - 40),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (0, 255, 0),
                        2)

        else:
            
            boxes = detect_barcode_classic(frame)

            for (x1, y1, x2, y2) in boxes:

                roi = frame[y1:y2, x1:x2]

                if roi.size == 0:
                    continue

                enhanced = enhance_image(roi)
                restored = wiener_filter(enhanced)

                barcode_value = decode_code128(restored)

                text_value = read_text(
                    restored,
                    BARCODE_HEIGHT_OFFSET,
                    OCR_CONFIG
                )

                cv2.rectangle(display_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                cv2.putText(display_frame,
                            f"Barcode: {barcode_value}",
                            (x1, y1 - 20),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6,
                            (0, 255, 0),
                            2)

                cv2.putText(display_frame,
                            f"Text: {text_value}",
                            (x1, y1 - 40),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6,
                            (0, 255, 0),
                            2)

        cv2.imshow("Industrial Barcode System", display_frame)

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
