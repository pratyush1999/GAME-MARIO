from Scenery import *
from lists import *
xOfBoard = 137
yOfBoard = 28
lofBoard = 140
wofBoard = 30


def Screen1():
    Tower1 = Tower(xOfBoard-6, yOfBoard, 6, 2, '#')
    Tower1.make()
    Tower2 = Tower(15, yOfBoard, 10, 3, '#')
    Tower2.make()
    Mountain1 = Mountain(int(xOfBoard/2), yOfBoard, 3, 5)
    Mountain1.make()
    bar1 = bar(int(xOfBoard/2), yOfBoard-7, 2, 6, '$')
    bar1.make()
    bar2 = bar(xOfBoard-10, yOfBoard-8, 2, 6, '?')
    bar2.make()
    bar1 = bar(int(xOfBoard/2)-12, yOfBoard-17, 2, 6, '$')
    bar1.make()
    bar1 = bar(int(xOfBoard/2)+12, yOfBoard-12, 2, 6, '$')
    bar1.make()
    bar1 = bar(int(xOfBoard/2)-35, yOfBoard-13, 2, 6, '%')
    bar1.make()
    bar1 = bar(int(xOfBoard/2)+35, yOfBoard-13, 2, 6, '&')
    bar1.make()
    Cloud1 = Cloud(4, 1, 1, 5)
    Cloud1.make()
    Cloud1 = Cloud(24, 3, 1, 7)
    Cloud1.make()
    Cloud2 = Cloud(int(xOfBoard/2), 2, 1, 5)
    Cloud2.make()
    Cloud3 = Cloud(xOfBoard-10, 1, 1, 5)
    Cloud3.make()
    Cloud3 = Cloud(int(xOfBoard/2)+22, 3, 1, 5)
    Cloud3.make()
    Mountain2 = Mountain(4, yOfBoard, 3, 0)
    Mountain2.make()
