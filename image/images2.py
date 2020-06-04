from PIL import Image, ImageDraw, ImageFont
import os

canvas = Image.new('RGB', (1500, 700), (0, 0, 0))

idraw = ImageDraw.Draw(canvas)

images = []
path_images = 'images2/'

for path in os.listdir(path_images):
    if os.path.isfile(path_images + path):
        images.append(Image.open(path_images + path))

images = sorted(images, key=lambda x: x.getexif().get(34665))

for i, image in enumerate(images):
    images[i] = image
    image = image.rotate(0)
    image = image.resize((image.size[0] // 2, image.size[1] // 2))

    canvas.paste(image, (300 * i, 0))
    idraw.text(
        (300 * i + 100, 655),
        f'ISO:{image.getexif().get(34665)}',
        font=ImageFont.truetype("arial.ttf", size=22),
        fill=(220, 255, 0)
    )

canvas.show()
canvas.save(path_images + 'out/img.jpg')