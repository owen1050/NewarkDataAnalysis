import pickle, sys
from PIL import Image, ImageDraw, ImageColor

#newark.png upper left = (40.79182, -74.27174) bottom right = (40.67641, -74.10332)
left = -74.251574
right = -74.112488
top = 40.79000
bot = 40.68022

file = open('data', 'rb')
data = pickle.load(file)
print(len(data))

im = Image.open("Newark.png")
wid = im.size[0]
hei = im.size[1]
r = 2
print(wid,hei)
draw = ImageDraw.Draw(im)
i = 0
for d in data:
    x = float(d[4]) 
    y = float(d[3])

    xP =(right - x) / (right - left)
    yP = (top - y) / (top - bot)
    l = 0
    pt = float(d[2])
    if( pt> 50000):
        l = 100
    else:
        l = int(0.0035*pt - 0.0044)

    if( xP > 0 and xP < 1 and yP > 0 and yP < 1):
        draw.ellipse(( wid - wid* xP-r, hei*yP-r, wid - wid* xP+r, hei*yP+r), "hsl(116, 96%, "+str(l)+"%)")
        i = i + 1
im.save("WithDots.png")
print(i)

