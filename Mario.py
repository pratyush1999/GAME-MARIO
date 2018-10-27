from lists import *
from Person import *


class Mario(Person):
    def __init__(self):
        Person.__init__(self, 2, 2, 'M', 5, 100, 0, yOfBoard, 1, 1, 1)
        self.jumpMax = 9
        self.score = 0
        self.coins = 0
        self.gems = 0
        self.timePassed = 0

    def initSpeed(self):
        self.speed = 5

    def jumped(self):
        if self.y < yOfBoard:
            return 1
        else:
            return 0

    def jumpp(self):
        if self.jump == 1:
            s = self.speed
            while s > 0 and not self.checkGr(self.y-2, self.x):
                self.y -= 1
                s -= 1
            self.speed -= self.acceler
            self.checkScorbl(self.y-2, self.x)
        elif self.jump == 0 and not self.checkGr(self.y+1, self.x):
            s = self.speed
            while s > 0 and not self.checkGr(self.y+1, self.x):
                self.y += 1
                s -= 1
            self.speed += self.acceler

    def checkScorbl(self, y, x):
        for i in range(self.length):
            if lists.scenes[y][x+i] == '?':
                lists.scenes[y][x+i] = ' '
                lists.mat[y][x+i] = ' '
                self.coins += 1
            if lists.scenes[y][x+i] == '$':
                lists.scenes[y][x+i] = ' '
                lists.mat[y][x+i] = ' '
                self.gems += 1
        return 0

    def NxtY(self):
        if self.jump == 1:
            return self.y-self.speed
        if self.jump == 0 and not self.checkGr(self.y+1, self.x):
            return self.y+self.speed
        return self.y

    def NxtX(self, f):
        if f == 1:
            return self.x+self.hspeed
        elif f == 0:
            return self.x-self.hspeed
        else:
            return self.x

    def checkIfFound(self):
        for i in range(self.length):
            for j in range(self.width):
                if self.check(self.x+i, self.y-j):
                    if lists.scenes[self.y-j][self.x+i] == 'p':
                        return 1
        return 0


MARIO = Mario()
