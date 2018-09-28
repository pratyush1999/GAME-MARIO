from Scenery import Scenery
from Scenery import	bar
from Scenery import Tower
from Scenery import Mountain
from Scenery import Cloud
from Scenery import UgTower
from lists import *
xOfBoard=137
yOfBoard=28
lofBoard=140
wofBoard=30
def UnderGround1():
	UgTower1=UgTower(0,0,14,5);
	UgTower1.make();
	UgTower1=UgTower(int(xOfBoard/4),0,19,5);
	UgTower1.make();
	UgTower1=UgTower(int(xOfBoard/12),8,2,15);
	UgTower1.make();
	UgTower1=UgTower(int(xOfBoard/12)+7,8,10,3);
	UgTower1.make();
	bar1=bar(int(xOfBoard/12)+4,5,2,6,'?')
	bar1.make()
	for i in range(18):
		lists.mat[wofBoard-1][int(xOfBoard/12)+i]='y'
	UgTower1=UgTower(0,0,2,lofBoard);
	UgTower1.make();
	UgTower1=UgTower(int(xOfBoard/2),4,2,15);
	UgTower1.make();
	UgTower1=UgTower(int(xOfBoard/2)-3,0,15,3);
	UgTower1.make();
	UgTower1=UgTower(int(3*xOfBoard/8)-3,0,25,3);
	UgTower1.make();
	UgTower1=UgTower(int(xOfBoard/2)+20,4,2,35);
	UgTower1.make();
	UgTower1=UgTower(lofBoard-4,2,wofBoard-6,4);
	UgTower1.make();
	UgTower1=UgTower(int(xOfBoard/2)+12,int(yOfBoard/2),2,56);
	UgTower1.make();
	bar1=bar(int(xOfBoard/2)+12,yOfBoard-18,2,6,'$')
	bar1.make()
	UgTower1=UgTower(int(xOfBoard/2)-10,10,2,8);
	UgTower1.make()
	bar2=bar(xOfBoard-10,yOfBoard-8,2,6,'?')
	bar2.make()
	Tower1=Tower(xOfBoard-24,yOfBoard,6,3,'E')
	Tower1.make()
	Tower1=Tower(xOfBoard-24,3,2,3,'p')
	Tower1.make()
	UgTower1=UgTower(xOfBoard-20,yOfBoard-13,10,5);
	UgTower1.make()
	UgTower1=UgTower(xOfBoard-30,yOfBoard-13,12,3);
	UgTower1.make()
