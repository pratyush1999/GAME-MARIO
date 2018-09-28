from Person import Person
from Mario import *
xOfBoard=137
yOfBoard=28
from lists import *
class Enemy(Person):
	def __init__(self,l,w,c,s,lives,x,y,hspeed,f,jump=0):
		Person.__init__(self,l,w,c,s,lives,x,y,hspeed,0,0)
		self.right=1-f
		self.left=f
		self.chase=0
	def move(self):
		if self.right :
			if self.mvRchk(self.x,self.y):
				self.moveRight()
			else:
				self.right=0
				self.left=1
				self.moveLeft()
		elif self.left:
			if self.mvLchk(self.x,self.y):
				self.moveLeft()
			else:
				self.right=1
				self.left=0
				self.moveRight()
		elif self.chase:
			self.Chase()
	def Chase(self):
		if MARIO.x<self.x :
			self.moveLeft()
		else :
			self.moveRight()
	def CollwithMario(self,f):
		for i in range(self.length):
			for j in range (self.width):
				if self.check(self.x+i,self.y-j):
					if self.checkIfHit(self.x+i,self.y-j,f):
						return 1
		return 0
	def checkIfJmp(self):
		if MARIO.y<self.y-1:
			return 1
		return 0
	def hitByMario(self):
		self.width-=1
		if self.width==0:
			self.lives-=1
	def checkIfHit(self,x,y,f):
		if x>=MARIO.x and x<=MARIO.NxtX(f) and MARIO.NxtY()==y:
			return 1
		if y>=MARIO.y and y<=MARIO.NxtY() and MARIO.NxtX(f)==x:
			return 1
		return 0
class Weapon(Person):
	def __init__(self):
		Person.__init__(self,1,1,'*',5,5,xOfBoard-5,yOfBoard,4,0,0)
	def moveLeftOfThis(self):
		s=self.hspeed
		while s>0 and self.mvLchk(self.x,self.y):
			if self.x==MARIO.x and self.y==MARIO.y:
				return 1
			self.x-=1
			s-=1
		return 0