# ReadMe

# Intro :
    This is an implementation of the classic game mario in python.The goal of mario is to rescue the princess by overcoming various hurdles.
#   Keys :

  - To quit-q
  - to move mario right-l
  - to move mario left-r
  - to jump - j    
  - to execute game type python3 main.py
### Symbols:
    Coin-'?'
    Gem-'$'
    Enemy is Represented by E s
    princess is represented by p s
    Mario is represented by 'M' s
    Spring is represented by 'y'
    All other symbols (except small hills and clouds) are obstacles through which Mario can't go
### Enemy:
    Each Enemy has 2 lives 
    On each lateral collision with Mario enemy reduces by 1 in     size and reduces Mario's life by one,If Mario
    jumps on it its width reduces by 1 
    Can be killed only by jumping on them 
    Boss Enemy:Bigger in Size,Has 3 lives,
    Has higher speed,On each lateral collision with Mario         reduces by 2 in size and decreases Mario's 
    life by 2
    Enemy at the end of board releases bullets  each of 
    which decrease Mario's life by 1.The bullets can be 
    blocked by other enemies and walls('#')
    On collision between 2 Enemies,both move in 
    opposite direction
### Score
    Coins and gems can be earned only if hit from bottom 
    by Mario
    If Mario jumps on or kills Enemy,it's score increses 
    by 1
    On killing enemy,life increases by 1
    final score is calculated as 1000-timeTaken             +gemsCollected/5+coinsCollected/10
    +scoreEarnedByKillingEnemies+100(for saving the princess) only if Mario completes the game
    otherwise its just the scoreEarnedByKillingEnemies








