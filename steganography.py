from PIL import Image

img = Image.open("dog.webp")  
pixels = list(img.getdata())

msg = "This code is made by Durjoy!"
binary_msg = ''.join(format(ord(c), '08b') for c in msg)
delimiter = '11111111'
binary_msg += delimiter

msg_index = 0
new_pixels = []

for pixel in pixels:
    new_pixel = []
    for val in pixel:
        if msg_index < len(binary_msg):
            val = (val & ~1) | int(binary_msg[msg_index])
            msg_index += 1
        new_pixel.append(val)
    new_pixels.append(tuple(new_pixel))

img.putdata(new_pixels)
img.save("output.png")
print("Message hidden in output.png")
