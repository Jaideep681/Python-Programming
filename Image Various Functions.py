from PIL import Image as i,ImageFilter as f

#1.Open image
img=i.open("PHOTO.jpeg")
img.show()

#2.Rotate image
rotate=img.rotate(90)
rotate.save("Image Various Functions Output Images/rotate.jpg")

#3.Resize image
resize=img.resize((250,250))
resize.save("Image Various Functions Output Images/resize.jpg")

#4.Convert format
img.save("Image Various Functions Output Images/Photo_converted.png")

#5.Crop image
crop=img.crop((50,50,200,200))
crop.save("Image Various Functions Output Images/crop.jpg")

#6.Grayscale image
gray=img.convert("L")               #'L' Grayscale Mode
gray.save("Image Various Functions Output Images/grayscale.jpg")

#7.Flip image
flip=img.transpose(i.FLIP_LEFT_RIGHT)
flip.save("Image Various Functions Output Images/flip.jpg")

#8.Blur image
blur=img.filter(f.BLUR)
blur.save("Image Various Functions Output Images/blur.jpg")

print("Image processing completed successfully!!")
