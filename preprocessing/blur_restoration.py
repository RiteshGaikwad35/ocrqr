import cv2
import numpy as np

def wiener_filter(img, kernel_size=5):
    kernel = np.ones((kernel_size, kernel_size)) / (kernel_size**2)

    img_fft = np.fft.fft2(img)
    kernel_fft = np.fft.fft2(kernel, s=img.shape)

    kernel_fft_conj = np.conj(kernel_fft)
    denominator = kernel_fft * kernel_fft_conj + 0.01

    result_fft = (kernel_fft_conj / denominator) * img_fft
    result = np.abs(np.fft.ifft2(result_fft))

    result = np.uint8(np.clip(result, 0, 255))

    return result
