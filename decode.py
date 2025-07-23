from PIL import Image

img = Image.open("output.png")
pixels = list(img.getdata())

bits = ""
for pixel in pixels:
    for val in pixel:
        bits += str(val & 1)

chars = [bits[i:i+8] for i in range(0, len(bits), 8)]
message = ""
for char in chars:
    if char == '11111111': 
        break
    message += chr(int(char, 2))

print("Hidden message:", message)
