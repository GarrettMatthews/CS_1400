from cImage import *
wn = ImageWin("Image Processing",300,300)

img = FileImage("/home/pi/.local/lib/python3.5/site-packages/bear_fish.jpg")
nimg = EmptyImage(300,300)
img.setPosition(0,0)
img.draw(wn)
height = img.getHeight()
width = img.getWidth()
for row in range(int(height)):
    for col in range(int(width)):
        p = img.getPixel(col,row)
        gray = (((p.getRed()) + (p.getGreen()) + (p.getBlue()))) / 3
        nimg.setPixel(col,row,Pixel(int(gray),int(gray),int(gray)))
wn1 = ImageWin("Image Processing",300,300)        
nimg.setPosition(0,0)
nimg.draw(wn1)
