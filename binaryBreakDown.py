import binascii
from PIL import Image
def string2bits(s=""):
    return [bin(ord(x))[2:].zfill(8) for x in s]
f = open("test.txt","r")
if f.mode == "r":
    file = f.read()

lines = []
binary=string2bits(file)
binString = ''.join(binary)
wid = 90
lengh = int(len(binString)/wid)

img = Image.new('RGB', (wid,lengh), (0, 0, 0))
img.save("image.png", "PNG")
img = Image.open('image.png')
sz = lengh*2
# Process every pixel
itr = 0
print(len(binString),wid,lengh, end = " ")
for x in range(wid):
    for y in range(lengh):
        if itr != len(binString):
            if binString[itr] == "1":
                img.putpixel((x,y),(0,255,255))
            elif binString[itr] == "0":
                img.putpixel((x,y),(255,255,0))
            itr = itr + 1
print(itr)
img.save('image.png')
