lOfBoard = 140
wOfBoard = 30
xOfBoard = 137
yOfBoard = 28


class LISTS:
    def __init__(self):
        self.Enemies = []
        self.bullets = []
        self.class_instances = [
            [' 'for i in range(lOfBoard)]for j in range(wOfBoard)]
        self.mat = [[' 'for i in range(lOfBoard)]for j in range(wOfBoard)]
        self.mat[wOfBoard-1] = ['-' for x in range(lOfBoard)]
        self.scenes = [[]for j in range(wOfBoard)]


lists = LISTS()
