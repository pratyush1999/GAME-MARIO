from lists import *
class Scenery:
	def __init__(self,x,y,l,w,c):
		self.l=l
		self.w=w
		self.startX=x
		self.startY=y
		self.char=c
class Tower(Scenery):
	def __init__(self,x,y,l,w,c):
		Scenery.__init__(self,x,y,l,w,c)
	def make(self):
		for i in range(self.l):
			for j in range(self.w):
				lists.mat[self.startY-i][self.startX+j]=self.char
class Mountain(Scenery):
	def __init__(self,x,y,l,w):
		Scenery.__init__(self,x,y,l,w,'w')
	def make(self):
		for i in range(self.l):
			lists.mat[self.startY-i][self.startX+i]='/'
		for i in range(self.l-1,-1,-1):
			lists.mat[self.startY-i][self.startX+self.l+self.l-1-i+self.w]='\\'
		for i in range(self.w):
			lists.mat[self.startY-self.l][self.startX+i+self.l-1+1]='_'
class Cloud(Scenery):
	def __init__(self,x,y,l,w):
		Scenery.__init__(self,x,y,l,w,'c')
	def make(self):
		for i in range(self.l):
			lists.mat[self.startY-i][self.startX+i]='/'
		for i in range(self.l):
			lists.mat[self.startY+i+1][self.startX+i]='\\'
		for i in range(self.w):
			lists.mat[self.startY-self.l][self.startX+i+self.l-1+1]='_'
		for i in range(self.l):
			lists.mat[self.startY-i][self.startX+self.l+self.l-1-i+self.w]='\\'
		for i in range(self.l):
			lists.mat[self.startY+i+1][self.startX+self.l+self.l-1-i+self.w]='/'
		for i in range(self.w):
			lists.mat[self.startY+self.l][self.startX+i+1]='_'
class bar(Scenery):
	def __init__(self,x,y,l,w,c):
		Scenery.__init__(self,x,y,l,w,c)
	def make(self):
		for i in range(self.l):
			for j in range(self.w):
				lists.mat[self.startY-i][self.startX+j]=self.char
class UgTower():
	def __init__(self,x,y,l,w):
		Scenery.__init__(self,x,y,l,w,'#')
	def make(self):
		for i in range(self.w):
			for j in range(self.l):
				lists.mat[j+self.startY][self.startX+i]=self.char