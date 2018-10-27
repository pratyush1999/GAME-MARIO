from inpu import *
import time
import os
from Mario import *
from Enemy import *
from Screen1 import Screen1
from Screen2 import Screen2
from UnderGround1 import UnderGround1
from UnderGround2 import UnderGround2
from lists import *
from Board import *


def main():
    start = True
    kb = KBHit()
    Board.r = 0
    while start:
        if kb.kbhit():
            x = kb.getch()
        else:
            x = 'd'
        Board.f = -1
        if x == 'q':
            start = False
        elif x == 'r':
            Board.f = 0
            Board.r -= 1
        elif x == 'l':
            Board.f = 1
            Board.r += 1
        if x == 'j' and MARIO.checkGr(MARIO.y+1, MARIO.x):
            MARIO.jump = 1
            MARIO.initSpeed()
        if lists.scenes[MARIO.y+1][MARIO.x] == 'y' and lists.scenes[MARIO.y+1][MARIO.x+1] == 'y':
            MARIO.jump = 1
            MARIO.speed = 8
        if MARIO.jump == 1:
            MARIO.jumpCount += 1
        if MARIO.jumpCount == MARIO.jumpMax:
            MARIO.jump = 0
            MARIO.jumpCount = 0
        Board.counter += 1
        os.system('clear')
        Board.printBoard()
        if MARIO.checkIfFound():
            print('Thank You MARIO!')
            print('Game Over')
            MARIO.score = MARIO.score+100+1000-MARIO.timePassed
            start = False
        print("Lives Remaining:", MARIO.lives, "Time Taken:", MARIO.timePassed)
        print("Score:", MARIO.score)
        print("?:", MARIO.coins)
        print("$:", MARIO.gems)
        MARIO.timePassed += 1
        if MARIO.lives <= 0:
            start = False
        time.sleep(0.05)
    MARIO.score = MARIO.score+int(MARIO.coins/10)+int(MARIO.gems/5)
    print(MARIO.score)


if __name__ == '__main__':
    main()
