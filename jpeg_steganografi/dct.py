import cv2
import numpy as np
import scipy.fftpack as fft
import matplotlib.pyplot as plt

# DCT fonksiyonu
def apply_dct(image):
    # Görüntüyü gri tonlara çevir (görüntü renkli değilse atlanabilir)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Görüntüyü 8x8 bloklara ayır
    h, w = gray_image.shape
    blocks = []

    for i in range(0, h, 8):
        for j in range(0, w, 8):
            block = gray_image[i:i+8, j:j+8]
            blocks.append(block)

    # Her 8x8 blokta DCT uygula
    dct_blocks = [fft.dct(fft.dct(block.T, norm='ortho').T, norm='ortho') for block in blocks]

    return dct_blocks, gray_image

# DCT'yi geri çevirme (IDCT - ters DCT)
def inverse_dct(dct_blocks, h, w):
    idct_blocks = []

    # Her blok için ters DCT uygula
    for block in dct_blocks:
        idct_block = fft.idct(fft.idct(block.T, norm='ortho').T, norm='ortho')  # scipy.fftpack.idct kullan
        idct_blocks.append(idct_block)

    # Blokları yeniden birleştir
    idct_image = np.zeros((h, w), dtype=np.float32)
    block_idx = 0
    for i in range(0, h, 8):
        for j in range(0, w, 8):
            idct_image[i:i+8, j:j+8] = idct_blocks[block_idx]
            block_idx += 1

    # Görüntü verisini uint8'e çevir
    idct_image = np.clip(idct_image, 0, 255).astype(np.uint8)
    return idct_image

# Görüntü oku
image_path = 'ornek1.jpg'  # Kendi görüntü dosyanızın yolunu buraya yazın
image = cv2.imread(image_path)

# DCT uygula
dct_blocks, original_image = apply_dct(image)

# IDCT ile geri çöz
h, w = original_image.shape[:2]
reconstructed_image = inverse_dct(dct_blocks, h, w)

# Görüntüleri göster
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Reconstructed Image from DCT')
plt.imshow(cv2.cvtColor(reconstructed_image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.show()
