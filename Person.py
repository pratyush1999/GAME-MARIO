from lists import *
lofBoard = 140
wofBoard = 30
xOfBoard = 137
yOfBoard = 28


class Person:
    def __init__(self, l, w, c, s, lives, x, y, hspeed, j, acc):
        self.length = l
        self.width = w
        self.char = c
        self.speed = s
        self.lives = lives
        self.x = x
        self.y = y
        self.jumpCount = 0
        self.hspeed = hspeed
        self.jump = j
        self.acceler = acc

    def decLives(self):
        self.lives -= 1

    def getLives(self):
        return self.lives

    def check(self, x, y):
        if x < 0 or x > lofBoard-1 or y < 0 or y > yOfBoard:
            return 0
        else:
            return 1

    def moveLeft(self):
        s = self.hspeed
        while s > 0 and self.mvLchk(self.x, self.y):
            self.x -= 1
            s -= 1

    def moveRight(self):
        s = self.hspeed
        while s > 0 and self.mvRchk(self.x, self.y):
            self.x += 1
            s -= 1

    def moveLeftByOne(self):
        self.x -= 1

    def moveRightbyOne(self):
        self.x += 1

    def get(self):
        for i in range(self.length):
            for j in range(self.width):
                if self.check(self.x+i, self.y-j):
                    lists.mat[self.y-j][self.x+i] = self.char
                    lists.class_instances[self.y-j][self.x+i] = self

    def checkGr(self, y, x):
        for i in range(self.length):
            if self.checkGR2(lists.scenes[y][x+i]) or self.chkSpring(lists.scenes[y][x+i]):
                return 1
        return 0

    def chkSpring(self, c):
        if c == 'y':
            return 1
        return 0

    def checkGr3(self, y, x):
        for i in range(self.width):
            if self.checkGR2(lists.scenes[y-i][x]):
                return 0
            if lists.class_instances[y][x] != self and self.checkGR2(lists.mat[y-i][x]):
                return 0
        return 1

    def checkGR2(self, c):
        if c == '-' or c == '#' or c == '$' or c == '?' or c == '%' or c == '&' or c == 'E':
            return 1
        return 0

    def mvRchk(self, x, y):
        if self.check(x+self.length, y) and self.checkGr3(y, x+self.length):
            return 1
        return 0

    def mvLchk(self, x, y):
        if self.check(x-1, y) and self.checkGr3(y, x-1):
            return 1
        return 0
