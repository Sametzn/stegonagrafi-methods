from PIL import Image

def encode_lsb(image_path, message, output_path):
    img = Image.open(image_path)
    img = img.convert('RGB')
    encoded = img.copy()
    width, height = img.size

    message += chr(0)
    message_bits = ''.join([format(ord(c), '08b') for c in message])
    data_index = 0

    for y in range(height):
        for x in range(width):
            if data_index >= len(message_bits):
                break
            r, g, b = img.getpixel((x, y))
            r = (r & ~1) | int(message_bits[data_index])
            data_index += 1
            if data_index < len(message_bits):
                g = (g & ~1) | int(message_bits[data_index])
                data_index += 1
            if data_index < len(message_bits):
                b = (b & ~1) | int(message_bits[data_index])
                data_index += 1
            encoded.putpixel((x, y), (r, g, b))
        if data_index >= len(message_bits):
            break

    encoded.save(output_path)
    print(f"✅ Mesaj başarıyla '{output_path}' dosyasına gizlendi!")

if __name__ == "__main__":
    message = input("Lütfen 160 karaktere kadar bir mesaj girin: ")
    if len(message) > 160:
        print("⚠️ 160 karakterden uzun mesaj girdiniz, otomatik kısaltılıyor.")
        message = message[:160]

    encode_lsb('ornek1.jpg', message, 'ornek1_gizli.png')
