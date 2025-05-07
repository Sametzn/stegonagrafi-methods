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

# 3. Komplekslik Hesaplama
def calculate_complexity(bit_planes):
    complexities = []
    for bit_plane in bit_planes:
        # Komplekslik, bit düzeyindeki değişkenliği ölçer
        complexity = np.sum(np.abs(np.diff(bit_plane.astype(int), axis=0))) + np.sum(np.abs(np.diff(bit_plane.astype(int), axis=1)))
        complexities.append(complexity)
    return complexities

# 4. Mesajı Gizleme
def hide_message(image, message, bit_planes, complexities):
    # Mesajı ikili formata dönüştür
    message_bits = ''.join(format(ord(c), '08b') for c in message)

    # Düşük komplekslikli bit düzeylerine mesajı ekleyin
    message_index = 0
    for i in range(8):
        if complexities[i] < np.mean(complexities):  # Düşük komplekslikli bit düzeyini seç
            for x in range(image.shape[0]):
                for y in range(image.shape[1]):
                    if message_index < len(message_bits):
                        # Mesaj bitini gizle
                        bit_planes[i][x, y] = int(message_bits[message_index])
                        message_index += 1

    # Yeni görüntüyü yeniden oluştur
    new_image = np.zeros_like(image)
    for i in range(8):
        new_image |= (bit_planes[i] << i)
    return new_image

# 5. Mesajı Çıkartma
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
def main(image_path, output_image_path):
    # Kullanıcıdan maksimum 160 karakterlik mesajı al
    message = input("Lütfen gizlemek istediğiniz mesajı girin (Maksimum 160 karakter): ")

    # Mesajın uzunluğunu kontrol et ve 160 karakterden fazla girildiyse kes
    if len(message) > 160:
        message = message[:160]
        print("Mesajınız 160 karakteri aştığı için fazla kısımlar kesildi.")

    # Görüntüyü yükle
    image = load_image(image_path)

    # Bit düzeylerine ayır
    bit_planes = bit_plane_decomposition(image)

    # Komplekslik hesapla
    complexities = calculate_complexity(bit_planes)

    # Mesajı gizle
    hidden_image = hide_message(image, message, bit_planes, complexities)

    # Yeni görüntüyü dosyaya kaydet
    cv2.imwrite(output_image_path, hidden_image)

    # Mesajı çıkart
    extracted_message = extract_message(hidden_image, bit_planes)

    # Sonuçları yazdır
    print(f"Gizli görüntü şu dosyada kaydedildi: {output_image_path}")
    print("\nÇıkarılan Mesaj:")
    print(extracted_message)  # Mesajın çıkarılması

# Örnek
image_path = 'ornek1.jpg'  # Görselin yolu
output_image_path = 'hidden_image.jpg'  # Çıktı görselinin kaydedileceği yer
main(image_path, output_image_path)
