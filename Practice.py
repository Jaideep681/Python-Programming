from PIL import Image
img=Image.open("MY PHOTO.jpg")
img.show()
rotate=img.rotate(90)
rotate.save("rotate.jpeg")
