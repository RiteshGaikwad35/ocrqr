

#  Industrial Barcode & QR Label Capture System

##  Overview

This project implements a **real-time computer vision–based label capture system** capable of:

* Detecting QR codes
* Detecting 1D Code128 barcodes
* Decoding embedded data
* Extracting printed text below labels using OCR
* Operating in real-time using a webcam

The system simulates an **industrial label inspection solution** suitable for manufacturing and production environments.

---

##  Project Requirements

The system is designed to:

1. Detect QR codes and decode embedded data.
2. Detect 1D Code128 barcodes.
3. Extract human-readable text printed below the barcode.
4. Operate in real-time using a camera feed.
5. Handle blur and low-contrast imaging conditions.
6. Maintain stable performance without runtime crashes.

---

##  Technologies Used

* Python 3.10+
* OpenCV
* NumPy
* pytesseract (Python OCR wrapper)
* Tesseract OCR Engine
* Pillow
* python-barcode
* qrcode

---

##  Project Structure

```
barcode_system/
│
├── main.py
├── config.py
│
├── preprocessing/
│   ├── enhance.py
│   └── blur_restoration.py
│
├── decoding/
│   └── code128_decoder.py
│
├── ocr/
│   └── text_reader.py
│
├── generate_test_barcode.py
└── generate_test_qr.py
```

---

##  Installation & Setup

### Clone the Repository

```bash
git clone <https://github.com/RiteshGaikwad35/ocrqr>
cd barcode_system
```

---

###  Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### Install Python Dependencies

```bash
pip install opencv-python numpy pytesseract pillow python-barcode qrcode
```

---

##  Install Tesseract OCR Engine (Important)

This project requires the **Tesseract OCR Engine** (separate from pytesseract).

###  Windows Installation

Download the official Windows installer from:

👉 [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)

Install using the default path:

```
C:\Program Files\Tesseract-OCR
```

After installation, verify:

```bash
tesseract --version
```

You should see output similar to:

```
tesseract v5.x.x
```

If needed, manually add the following path to your system environment variables:

```
C:\Program Files\Tesseract-OCR
```

Restart your terminal after updating PATH.

---

##  Running the System

Start the real-time scanner:

```bash
python main.py
```

Press **ESC** to exit the application.

---

##  Testing

### Generate Test QR Code

```bash
python generate_test_qr.py
```

### Generate Test Barcode

```bash
python generate_test_barcode.py
```

Display the generated image on your screen and show it to your webcam for testing.

---

##  Features

✔ Real-time camera-based scanning
✔ QR decoding using OpenCV
✔ Code128 barcode detection
✔ OCR text extraction using Tesseract
✔ Blur restoration using Wiener filter
✔ Contrast enhancement using CLAHE
✔ Crash-safe OCR handling

---

##  Industrial Use Cases

Designed for:

* Label inspection systems
* Manufacturing line barcode verification
* QR-based tracking systems
* Small text recognition under blur and lighting variation

---

##  Future Improvements

* Full industrial-grade Code128 decoder
* YOLO-based barcode detection
* Super-resolution for small text
* Confidence scoring system
* Docker deployment
* REST API integration

---

##  Author

**Ritesh Gaikwad**
Computer Vision & AI Developer

---

If you'd like, I can now:

* Add architecture diagram section
* Add performance metrics section
* Make it internship-submission ready
* Add screenshots section for GitHub
* Optimize it for portfolio presentation 
