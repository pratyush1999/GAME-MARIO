from Scenery import *
from lists import *
xOfBoard = 137
yOfBoard = 28
lofBoard = 140
wofBoard = 30


def Screen2():
    Tower1 = Tower(xOfBoard-6, yOfBoard, 6, 3, '&')
    Tower1.make()
    Tower2 = Tower(15, yOfBoard, 7, 3, '#')
    Tower2.make()
    Mountain1 = Mountain(int(xOfBoard/2), yOfBoard, 3, 5)
    Mountain1.make()
    bar1 = bar(int(xOfBoard/2), yOfBoard-7, 2, 6, '%')
    bar1.make()
    Cloud1 = Cloud(4, 1, 1, 1)
    Cloud1.make()
    Mountain2 = Mountain(4, yOfBoard, 3, 0)
    Mountain2.make()
