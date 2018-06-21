from PIL import Image

img = Image.open('dice.png')
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        # not sure what x is but unpacks with 4 items.
        r, g, b, x = pixels[i, j]
        r *= 0.299
        g *= 0.587
        b *= 0.114
        pixels[i, j] = (int(r), int(g), int(b), x)

img.show()
