from PIL import Image

def decode_lsb(image_path):
    img = Image.open(image_path)
    img = img.convert('RGB')
    width, height = img.size
    message_bits = ''

    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            message_bits += str(r & 1)
            message_bits += str(g & 1)
            message_bits += str(b & 1)

    chars = []
    for i in range(0, len(message_bits), 8):
        byte = message_bits[i:i+8]
        char = chr(int(byte, 2))
        if char == chr(0):  # Null karakter gelince dur
            break
        chars.append(char)
    message = ''.join(chars)
    print("📥 Çözülen gizli mesaj:")
    print(message)
    return message

if __name__ == "__main__":
    decode_lsb('ornek1_gizli.png')
