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
def UnderGround2():
	UgTower1=UgTower(0,0,2,lofBoard);
	UgTower1.make();
	UgTower1=UgTower(int(xOfBoard/2)-3,0,10,10);
	UgTower1.make();
	UgTower1=UgTower(int(xOfBoard/2)-13,9,10,10);
	UgTower1.make();
	UgTower1=UgTower(int(xOfBoard/2)-3,18,7,7);
	UgTower1.make();
	UgTower1=UgTower(xOfBoard-10,0,10,10);
	UgTower1.make();
	UgTower1=UgTower(xOfBoard,0,15,3);
	UgTower1.make();
	UgTower1=UgTower(xOfBoard-13,14,6,16);
	UgTower1.make();
	UgTower1=UgTower(int(xOfBoard/2)+24,11,9,2);
	UgTower1.make();
	UgTower1=UgTower(int(xOfBoard/2)+26,14,1,7);
	UgTower1.make();
	UgTower1=UgTower(int(xOfBoard/2)+33,11,9,2);
	UgTower1.make();
	UgTower1=UgTower(int(xOfBoard/4),10,9,3);
	UgTower1.make();
	lists.mat[wofBoard-1][int(xOfBoard/4)]='y'
	lists.mat[wofBoard-1][int(xOfBoard/4)+1]='y'
	lists.mat[wofBoard-1][int(xOfBoard/4)+2]='y'
	lists.mat[wofBoard-1][int(xOfBoard/4)+3]='y'
	lists.mat[wofBoard-1][int(xOfBoard/4)+4]='y'
	lists.mat[wofBoard-1][int(xOfBoard/4)+5]='y'
	bar1=bar(int(xOfBoard/4)-14,5,2,6,'?')
	bar1.make()
	UgTower1=UgTower(int(xOfBoard/4)-3,16,3,3);
	UgTower1.make();
	UgTower1=UgTower(int(xOfBoard/4)-6,10,9,3);
	UgTower1.make();
	UgTower1=UgTower(int(xOfBoard/4)-15,10,3,9);
	UgTower1.make();
	UgTower1=UgTower(int(xOfBoard/4)-18,10,9,3);
	UgTower1.make();
	UgTower1=UgTower(int(xOfBoard/4)-23,16,3,6);
	UgTower1.make();
	UgTower1=UgTower(int(xOfBoard/4)-24,10,9,3);
	UgTower1.make();
	lists.mat[wofBoard-1][int(xOfBoard/2)+21]='y'
	lists.mat[wofBoard-1][int(xOfBoard/2)+22]='y'
	lists.mat[wofBoard-1][int(xOfBoard/2)+23]='y'
	lists.mat[wofBoard-1][int(xOfBoard/2)+24]='y'
	lists.mat[wofBoard-1][int(xOfBoard/2)+29]='y'
	lists.mat[wofBoard-1][int(xOfBoard/2)+30]='y'
	UgTower1=UgTower(0,0,19,3);
	UgTower1.make();
	bar2=bar(int(xOfBoard/2)+26,8,2,7,'?')
	bar2.make()