from ezgraphics import GraphicsWindow
from time import sleep
vindu  = GraphicsWindow()
lerret = vindu.canvas()
x = 10
y = 10
while y<200:
    lerret.clear()
    lerret.drawRect(x,y,50,50)
    y +=1
    sleep(0.01)
