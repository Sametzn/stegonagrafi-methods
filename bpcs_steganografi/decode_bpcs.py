import cv2
import numpy as np

# 1. Görüntüyü yükle ve gri tonlamaya çevir
def load_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(f"Resim yolu {image_path} bulunamadı!")
    return image

# 2. Bit Düzeylerine Ayırma
def bit_plane_decomposition(image):
    bit_planes = []
    for i in range(8):  # 8 bit düzeyi var
        bit_plane = (image >> i) & 1
        bit_planes.append(bit_plane)
    return bit_planes

# 3. Gizli Mesajı Çıkartma
def extract_message(image, bit_planes):
    extracted_bits = []
    # Her bit düzeyinden piksel değerlerini çıkarıyoruz
    for i in range(8):
        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                extracted_bits.append(str((image[x, y] >> i) & 1))  # Doğrudan piksel bitini al

    # Çıkarılan bitleri birleştir
    extracted_message = ''.join(extracted_bits)

    # Mesajı ASCII formatına dönüştür
    message = ''
    for i in range(0, len(extracted_message), 8):
        byte = extracted_message[i:i+8]
        # Eğer 8 bit tamamlanmışsa (yani mesaj bitsiz değilse)
        if len(byte) == 8:
            message += chr(int(byte, 2))

    # Null byte (\x00) kontrolü: mesajın sonu geldiğinde ekstra byte'ları temizle
    message = message.split('\x00')[0]  # Mesajı temizle ve sonlandırıcı karakteri kaldır
    return message

# Ana Fonksiyon
def main(image_path):
    # Görüntüyü yükle
    image = load_image(image_path)

    # Bit düzeylerine ayır
    bit_planes = bit_plane_decomposition(image)

    # Mesajı çıkart
    extracted_message = extract_message(image, bit_planes)

    # Çıkarılan mesajı yazdır
    print("Çıkarılan Mesaj:")
    print(extracted_message)  # Mesajın çıkarılması

# Örnek
image_path = 'hidden_image.jpg'  # Gizlenmiş görüntünün yolu
main(image_path)
