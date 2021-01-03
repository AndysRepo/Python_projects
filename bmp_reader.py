from graphics import *
f=open("path to the bmp file","rb")
f.seek(18)
lar=int.from_bytes(f.read(4), byteorder="little", signed=False)
alt=int.from_bytes(f.read(4), byteorder="little", signed=False)
f.seek(28)
size=int.from_bytes(f.read(2), byteorder="little", signed=False)
codifica=int.from_bytes(f.read(2), byteorder="little", signed=False)
win = GraphWin("Window", lar, alt)
if size==24:
    if codifica==0:
        f.seek(54)
        for j in range(alt):
            for i in range(lar):
                b = int.from_bytes(f.read(1), byteorder="little", signed=False)
                g = int.from_bytes(f.read(1), byteorder="little", signed=False)
                r = int.from_bytes(f.read(1), byteorder="little", signed=False)
                pix = Point(i, alt - j)
                pix.setFill(color_rgb(r, g, b))
                pix.draw(win)
f.close()

win.getMouse()
