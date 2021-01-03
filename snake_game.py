import numpy as np
from graphics import *
import secrets as sec
class bruco:
    lunghezza=0
    al=0
    lx=2
    ly=2
    tex=1
    tey=1
    cox=1
    coy=1
    testax=1
    testay=1
    codax=1
    coday=1
    mc=list()
    def __init__(self,x,y,lx,ly):
        self.testax=x;
        self.testay=y;
        self.codax=x;
        self.coday=y;
        self.tex=x;
        self.tey=y;
        self.cox=x;
        self.coy=y;
        self.lx=lx
        self.ly=ly
    def svuota(self):
        self.al=0
        self.testax=self.tex
        self.testay=self.tey
        self.codax=self.cox
        self.coday=self.coy
        self.mc=[]
    def testa(self):
        return (self.testax, self.testay)
    def coda(self):
        return (self.codax,self.coday)
    def tx(self):
        return ((self.testax*lx, self.testay*ly),((self.testax*lx+lx, self.testay*ly+ly)))
    def cx(self):
        return ((self.codax * lx, self.coday * ly), ((self.codax * lx + lx, self.coday * ly + ly)))
    def destra(self):
        self.testax=self.testax+1
        self.mc.append(0)
        if self.al==0:
            app=self.mc.pop(0)
            if app==0:
                self.codax=self.codax+1
            if app == 1:
                self.codax = self.codax - 1
            if app==2:
                self.coday=self.coday+1
            if app == 3:
                self.coday= self.coday - 1
        self.al=0
    def sinistra(self):
        self.mc.append(1)
        self.testax = self.testax - 1
        if self.al==0:
            app=self.mc.pop(0)
            if app==0:
                self.codax=self.codax+1
            if app == 1:
                self.codax = self.codax - 1
            if app==2:
                self.coday=self.coday+1
            if app == 3:
                self.coday= self.coday - 1
        self.al=0
    def alto(self):
        self.mc.append(2)
        self.testay = self.testay + 1
        if self.al==0:
            app=self.mc.pop(0)
            if app==0:
                self.codax=self.codax+1
            if app == 1:
                self.codax = self.codax - 1
            if app==2:
                self.coday=self.coday+1
            if app == 3:
                self.coday= self.coday - 1
        self.al=0
    def basso(self):
        self.mc.append(3)
        self.testay = self.testay - 1
        if self.al==0:
            app=self.mc.pop(0)
            if app==0:
                self.codax=self.codax+1
            if app == 1:
                self.codax = self.codax - 1
            if app==2:
                self.coday=self.coday+1
            if app == 3:
                self.coday= self.coday - 1
        self.al=0
    def allunga(self):
        self.lunghezza=self.lunghezza+1
        self.al=1

class livello:
    sx=int
    sy=int
    liv=int
    def __init__(self, x, y):
        self.liv=0
        self.sx=x
        self.sy=y

    def live0(self, ped):
        self.schermo = np.full((self.sx, self.sy), 0)
        for i in range(0, self.sx):
            self.schermo[i][0] = 1
            self.schermo[i][self.sy - 1] = 1
        for i in range(0, self.sy):
            self.schermo[0][i] = 1
            self.schermo[self.sx - 1][i] = 1
        for i in range(int(self.sy / 5), int(4 * self.sy / 5)):
            self.schermo[int(self.sx / 4)][i] = 1
            self.schermo[self.sx - 1][i] = 1
        for i in range(int(self.sy / 5), int(4 * self.sy / 5)):
            self.schermo[int(3 * self.sx / 4)][i] = 1
            self.schermo[self.sx - 1][i] = 1
        for i in range(int(self.sx * (1 / 2 + 1 / 14)), int(self.sx * 3 / 4)):
            self.schermo[i][int(self.sy * 3 / 5)-1] = 1
            self.schermo[i][int(self.sy * 2 / 5)-1] = 1

        while ped>0:
            x=sec.randbelow(self.sx)
            y=sec.randbelow(self.sy)
            if self.schermo[x][y]==0:
                self.schermo[x][y]=2
                ped=ped-1
        return self.schermo

    def live1(self, ped):
        self.schermo = np.full((self.sx, self.sy), 0)
        for i in range(0, self.sx):
            self.schermo[i][0] = 1
            self.schermo[i][self.sy - 1] = 1
        for i in range(0, self.sy):
            self.schermo[0][i] = 1
            self.schermo[self.sx - 1][i] = 1
        for i in range(int(self.sy / 5), int(4 * self.sy / 5)):
            self.schermo[int(self.sx / 4)][i] = 1
            self.schermo[self.sx - 1][i] = 1
        for i in range(int(self.sy / 5), int(4 * self.sy / 5)):
            self.schermo[int(3 * self.sx / 4)][i] = 1
            self.schermo[self.sx - 1][i] = 1
        for i in range(int(self.sx / 4), int(self.sx*(1/2-1/14))):
            self.schermo[i][int(self.sy/5)]=1
        for i in range(int(self.sx * (1 / 2 + 1 / 14)), int(self.sx * 3/4)):
            self.schermo[i][int(self.sy / 5)] = 1
        for i in range(int(self.sx / 4), int(self.sx * (1 / 2 - 1 / 14))):
            self.schermo[i][int(self.sy * 4 / 5)-1] = 1
        for i in range(int(self.sx * (1 / 2 + 1 / 14)), int(self.sx * 3 / 4)):
            self.schermo[i][int(self.sy * 4 / 5)-1] = 1
        while ped>0:
            x=sec.randbelow(self.sx)
            y=sec.randbelow(self.sy)
            if self.schermo[x][y]==0:
                self.schermo[x][y]=2
                ped=ped-1
        return self.schermo
def pulisci(win):
    for item in win.items[:]:
        item.undraw()
    win.update()
x=100
y=100
lx=2
ly=2
pedine=10
liv=0
mx=int(x/lx)
my=int(y/ly)
l=livello(mx,my)
matrix=l.live0(pedine)
b=bruco (int(mx / 2),int(my / 2),lx,ly)
posx = int(mx / 2)
posy = int(my / 2)
win = GraphWin("Snake game by Andy", 800, 600)
win.setBackground("green")
win.setCoords(0, 0, x, y)

for i in range(0,mx):
    for j in range(0,my):
        if matrix[i][j]==1:
            r = Rectangle(Point(int(i*lx), int(j*ly)), Point(int(i*lx + lx), int(j*ly+ ly)))
            r.setFill(color_rgb(250,0, 0))
            r.draw(win)
        if matrix[i][j] == 2:
            r = Rectangle(Point(int(i * lx), int(j * ly)), Point(int(i * lx + lx), int(j * ly + ly)))
            r.setFill(color_rgb(37,40,80))
            r.setOutline(color_rgb(88, 255, 255))
            r.draw(win)
i=0
app=0
p = Rectangle(Point(b.tx()[0][0],b.tx()[0][1]),Point(b.tx()[1][0],b.tx()[1][1]))
p.setFill(color_rgb(0,255,0))
p.draw(win)
while i<10:
    j=0
    while j<5000:
        k=win.checkKey()
        if k == "Up": app = 2
        if k == "Down": app = 3
        if k == "Left": app = 1
        if k == "Right": app = 0
        j=j+1
    p = Rectangle(Point(b.cx()[0][0], b.cx()[0][1]), Point(b.cx()[1][0], b.cx()[1][1]))
    p.setFill(color_rgb(255, 255, 255))
    p.setOutline(color_rgb(255, 255, 255))
    p.draw(win)
    if app==0:
        b.destra()
    if app==1:
        b.sinistra()
    if app==2:
        b.alto()
    if app==3:
        b.basso()
    if matrix[b.testa()[0]][b.testa()[1]]==1:
        i=20
    if matrix[b.testa()[0]][b.testa()[1]]==2:
        matrix[b.testa()[0]][b.testa()[1]]==0
        pedine=pedine-1
        b.allunga()
    if pedine==0:
        if liv==0:
            liv=1
            pedine=15
            app=0
            matrix=l.live1(pedine)
            b.svuota()
            message = Text(Point(int(x / 2), int(y / 2) + 5), "MINCA MIA A TUI! GI SES PAGU BRAVU \n Fai click con il mouse per continuare")
            message.draw(win)
            message.setSize(30)
            win.getMouse()
            pulisci(win)
            for i in range(0, mx):
                for j in range(0, my):
                    if matrix[i][j] == 1:
                        r = Rectangle(Point(int(i * lx), int(j * ly)), Point(int(i * lx + lx), int(j * ly + ly)))
                        r.setFill(color_rgb(250, 0, 0))
                        r.draw(win)
                    if matrix[i][j] == 2:
                        r = Rectangle(Point(int(i * lx), int(j * ly)), Point(int(i * lx + lx), int(j * ly + ly)))
                        r.setFill(color_rgb(37, 70, 90))
                        r.setOutline(color_rgb(255, 255, 255))
                        r.draw(win)
            i=0
        else:
            liv=2
            i=20
    matrix[b.testa()[0]][b.testa()[1]]=1
    matrix[b.coda()[0]][b.coda()[1]]=0
    p = Rectangle(Point(b.tx()[0][0] , b.tx()[0][1]), Point(b.tx()[1][0], b.tx()[1][1]))
    p.setFill(color_rgb(0, 0, 0))
    p.setOutline(color_rgb(0, 0, 0))
    p.draw(win)

if liv<2:
    message= Text(Point(int(x/2), int(y/2)+5),"Game Over \n Fai click con il mouse per uscire")
else:
    message = Text(Point(int(x / 2), int(y / 2) + 5), "Hai vinto. \n Fai click con il mouse per uscire")
message.draw(win)
message.setSize(30)
win.getMouse()
win.close()
