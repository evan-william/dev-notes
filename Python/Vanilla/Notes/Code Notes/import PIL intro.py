import sys

from PIL import image

images = []

for arg in sys.argv[1:]:
    image = Image.opem(arg)
    images.append(image)
    
images[0].save(
    "costumes.gif", save_all=True, append_image=[images[1]], duration = 200, loop= 0
)
