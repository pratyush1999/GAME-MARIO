from Person import *
from Mario import *
from Enemy import *
from Scenery import Scenery
from Screen1 import Screen1
from Screen2 import Screen2
from UnderGround1 import UnderGround1
from UnderGround2 import UnderGround2
from lists import *
class Board:
	def __init__(self):
		self.first=' '
		self.length=140
		self.width=30
		self.middle='|'
		self.spaces='|'
		self.y=self.width-2
		self.x=self.length-3
		for i in range(self.length):
			self.first+="-"
		self.counter=0
	def getOutline(self):
		self.spaces='|'
		for i in range(self.length):
			self.spaces+=' '
		self.spaces+='|'
	def printBoard(self,f,r):
		self.getOutline()
		move(r,f,1)
		for e in lists.Enemies:
			e.move()
			if e.CollwithMario(f):
				if not e.checkIfJmp():
					MARIO.lives-=1
				else:
					MARIO.score+=1
					MARIO.lives+=1
				e.hitByMario()	
				if e.lives==0:
					lists.Enemies.remove(e)
		move(r,f,0)
		make_mat()
		for e in lists.Enemies:
			e.get()	
		MARIO.jumpp()
		MARIO.get()	
		if self.counter%5==0 and r>=3*Board.length:
			lists.bullets.append(Weapon())
		if r>=3*Board.length:
			for b in lists.bullets :
				if b.mvLchk(b.x,b.y)==0 :
					lists.bullets.remove(b)
				else:
					if b.moveLeftOfThis():
						MARIO.lives-=1
						lists.bullets.remove(b)	
					else:
						b.get()
		print(self.first)
		for i in range(Board.width):
			print('|',end='')
			for j in range(Board.length-1):
				print(lists.mat[i][j],end='')
			print('|')
		print(self.spaces)
		print(self.first)
def moveRight(v,x):
	if  v<=int(Board.x/2) or v>=3*Board.length+int(Board.x/2)  and MARIO.mvRchk(MARIO.x,MARIO.y):
		if x==0:
			MARIO.moveRight()
	elif x==1 and MARIO.mvRchk(MARIO.x,MARIO.y):
		for i in range(Board.width):
			prev[i].append(lists.scenes[i][0])
			for j in range(4*Board.length-1):
				lists.scenes[i][j]=lists.scenes[i][j+1]
		for e in lists.Enemies:
			e.moveLeftByOne()
			#lists.scenes[i][2*Board.length-1]=temp
def moveLeft(v,x):
	if  v<=int(Board.x/2) or v>=3*Board.length+int(Board.x/2)  and MARIO.mvLchk(MARIO.x,MARIO.y):
		if x==0:
			MARIO.moveLeft()
	elif x==1 and MARIO.mvLchk(MARIO.x,MARIO.y):
		for i in range(Board.width):
			for j in range(4*Board.length-1,0,-1):
				lists.scenes[i][j]=lists.scenes[i][j-1]
			lists.scenes[i][0]=prev[i][-1]
			prev[i].pop()
		for e in lists.Enemies:
			e.moveRightbyOne()
			#lists.scenes[i][0]=temp
def move(v,f,x):
	if f==1:
		moveRight(v,x)
	elif f==0:
		moveLeft(v,x)
Board=Board();
###########################
def make_mat():
	for i in range(Board.width):
		for j in range(Board.length):
			lists.mat[i][j]=lists.scenes[i][j]
lists.mat[Board.width-1]=['-' for x in range(Board.length)]
lists.mat[Board.width-1][int(Board.length/2)]='y'
lists.mat[Board.width-1][int(Board.length/2)+1]='y'
lists.mat[Board.width-1][int(Board.length/2)+2]='y'
Enemy1=Enemy(4,3,'E',0,3,Board.x-6,Board.y,2,1)
lists.Enemies.append(Enemy1)
Enemy2=Enemy(2,2,'E',0,2,int(Board.x/2),Board.y,1,0)
lists.Enemies.append(Enemy2)
Enemy2=Enemy(3,2,'E',0,2,Board.x,Board.y,1,1)
lists.Enemies.append(Enemy2)
Enemy2=Enemy(3,2,'E',0,2,2*Board.length+int(Board.x/2)+2,Board.y,1,1)
lists.Enemies.append(Enemy2)
Enemy2=Enemy(4,3,'E',0,2,2*Board.length+int(Board.x/2),Board.y,1,1)
lists.Enemies.append(Enemy2)
lists.mat=[[' 'for i in range(Board.length)]for j in range(Board.width)]
lists.mat[Board.width-1]=['-' for x in range(Board.length)]
Screen1()
for j in range(Board.width):
	lists.scenes[j]=[x for x in lists.mat[j]]
lists.mat=[[' 'for i in range(Board.length)]for j in range(Board.width)]
lists.mat[Board.width-1]=['-' for x in range(Board.length)]
Screen2()
for j in range(Board.width):
	for x in lists.mat[j]:
		lists.scenes[j].append(x)
prev=[[]for j in range(Board.width)]
lists.mat=[[' 'for i in range(Board.length)]for j in range(Board.width)]
lists.mat[Board.width-1]=['-' for x in range(Board.length)]
UnderGround2()
for j in range(Board.width):
	for x in lists.mat[j]:
		lists.scenes[j].append(x)
lists.mat=[[' 'for i in range(Board.length)]for j in range(Board.width)]
lists.mat[Board.width-1]=['-' for x in range(Board.length)]
UnderGround1()
for j in range(Board.width):
	for x in lists.mat[j]:
		lists.scenes[j].append(x)
