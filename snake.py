#自动寻路的贪吃蛇
#基于 pygame
#算法 BFS
'''
创建时间2019.7.20
创建人 geticsen
最后修订时间 2019.7.21
版本修订：
1 2019.7.20 图形界面以及 键盘控制完成
2 2019.7.21 自动寻路算法完成 有bug

'''

import pygame
import random
import pygame.font
from pygame.locals import *
class Point:
    row = 0
    col = 0

    def __init__(self,row,col):
        self.row = row
        self.col = col
    def copy(self):
        return Point(self.row, self.col)

class snakeGame():
    #窗口的宽度
    width=0
    #窗口的高度
    height=0
    #每个蛇方块的大小
    cell=0
    #速度 默认20
    speed=20
    window=""
    clock=""
    head=""
    body=""
    headColor = (0, 128, 128)
    foodColor = (255, 255, 0)
    backGroundColor = (0, 0, 0)
    bodyColor = (200, 200, 200)
    ROW=0
    COL=0
    food=""
    #蛇的方向
    direct="left"
    #字体
    font=""
    #BFS的矩阵
    arrayBFS=""
    #文字
    Text=""
    #自动寻路找到的路径
    way=[]
    def __init__(self,width,height,cell,speed):
        self.height = height
        self.width = width
        self.cell = cell
        self.speed = speed
        self.ROW = int(self.height/self.cell)
        self.COL = int(self.width/self.cell)
    def gameInit(self,title):
        self.head = Point(int(self.ROW / 2), int(self.COL / 2))
        self.body = [   Point(self.head.row, self.head.col + 1),
                        Point(self.head.row, self.head.col + 2),
                        Point(self.head.row, self.head.col + 3)]
        self.food=self.randomFood()#Point(self.ROW-1,self.COL-1)
        pygame.init()
        self.window = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("贪吃蛇")
        self.font =   pygame.font.Font('./msyhbd.ttc',int(self.cell*0.5))
        self.clock = pygame.time.Clock()
        self.arrayBFS = [([0] * (self.COL)) for i in range(self.ROW)]
        print(self.arrayBFS)
    def BFSfindWay(self):
        self.InitarrayBFS()
        isFind = False
        quene = []
        quene.append(Point(self.head.row,self.head.col))
        #如果找到食物  或者遍历完成就结束
        while len(quene) > 0:
            vertex = quene.pop(0)
            node = self.arrayBFS[vertex.row][vertex.col]
            if self.food.row <= 5 or self.food.row >= self.ROW - 5:

                #左
                if (vertex.col -1)>=0and (self.arrayBFS[vertex.row][vertex.col-1] ==0):
                    self.arrayBFS[vertex.row][vertex.col-1]= node+1
                    quene.append(Point(vertex.row,vertex.col-1))
                    if (vertex.row == self.food.row and (vertex.col-1) == self.food.col):
                        isFind = True
                        break;
                #右
                if (vertex.col +1)<self.COL and (self.arrayBFS[vertex.row][vertex.col+1] ==0):
                    self.arrayBFS[vertex.row ][vertex.col+1]= node+1
                    quene.append(Point(vertex.row,vertex.col+1))
                    if (vertex.row == self.food.row and (vertex.col+1) == self.food.col):
                        isFind = True
                        break;
                # 上
                if (vertex.row - 1) >= 0 and (self.arrayBFS[vertex.row - 1][vertex.col] == 0):
                    self.arrayBFS[vertex.row - 1][vertex.col] = node + 1
                    quene.append(Point(vertex.row - 1, vertex.col))
                    if ((vertex.row - 1) == self.food.row and vertex.col == self.food.col):
                        isFind = True
                        break;
                 # 下
                if (vertex.row + 1) < self.ROW and (self.arrayBFS[vertex.row + 1][vertex.col] == 0):
                    self.arrayBFS[vertex.row + 1][vertex.col] = node + 1;
                    quene.append(Point(vertex.row + 1, vertex.col))
                    if ((vertex.row + 1) == self.food.row and vertex.col == self.food.col):
                        isFind = True
                        break;
            else:
                # 上
                if (vertex.row - 1) >= 0 and (self.arrayBFS[vertex.row - 1][vertex.col] == 0):
                    self.arrayBFS[vertex.row - 1][vertex.col] = node + 1
                    quene.append(Point(vertex.row - 1, vertex.col))
                    if ((vertex.row - 1) == self.food.row and vertex.col == self.food.col):
                        isFind = True
                        break;
                # 下
                if (vertex.row + 1) < self.ROW and (self.arrayBFS[vertex.row + 1][vertex.col] == 0):
                    self.arrayBFS[vertex.row + 1][vertex.col] = node + 1;
                    quene.append(Point(vertex.row + 1, vertex.col))
                    if ((vertex.row + 1) == self.food.row and vertex.col == self.food.col):
                        isFind = True
                        break;
                # 左
                if (vertex.col - 1) >= 0 and (self.arrayBFS[vertex.row][vertex.col - 1] == 0):
                    self.arrayBFS[vertex.row][vertex.col - 1] = node + 1
                    quene.append(Point(vertex.row, vertex.col - 1))
                    if (vertex.row == self.food.row and (vertex.col - 1) == self.food.col):
                        isFind = True
                        break;
                # 右
                if (vertex.col + 1) < self.COL and (self.arrayBFS[vertex.row][vertex.col + 1] == 0):
                    self.arrayBFS[vertex.row][vertex.col + 1] = node + 1
                    quene.append(Point(vertex.row, vertex.col + 1))
                    if (vertex.row == self.food.row and (vertex.col + 1) == self.food.col):
                        isFind = True
                        break;
        #根据矩阵找到路
        if isFind:
            vertex=Point(self.food.row,self.food.col)
            for i in range(0,self.arrayBFS[self.food.row][self.food.col]):
                node = self.arrayBFS[vertex.row][vertex.col]
                if self.food.row<=5 or self.food.row>=self.ROW-5:
                    # 左搜
                    if (vertex.col - 1) >= 0 and (self.arrayBFS[vertex.row][vertex.col - 1] == (node - 1)):
                        vertex.col -= 1
                        self.way.append("right")
                        continue
                    # 右搜
                    if (vertex.col + 1) < self.COL and (self.arrayBFS[vertex.row][vertex.col + 1] == (node - 1)):
                        vertex.col += 1
                        self.way.append("left")
                        continue
                    # 上搜
                    if (vertex.row - 1) >= 0 and (self.arrayBFS[vertex.row - 1][vertex.col] == (node - 1)):
                        vertex.row -= 1
                        self.way.append("down")
                        continue
                    # 下搜
                    if (vertex.row + 1) < self.ROW and (self.arrayBFS[vertex.row + 1][vertex.col] == (node - 1)):
                        vertex.row += 1
                        self.way.append("up")
                        continue
                else:
                    # 上搜
                    if (vertex.row - 1) >= 0 and (self.arrayBFS[vertex.row - 1][vertex.col] == (node - 1)):
                        vertex.row -= 1
                        self.way.append("down")
                        continue
                    # 下搜
                    if (vertex.row + 1) < self.ROW and (self.arrayBFS[vertex.row + 1][vertex.col] == (node - 1)):
                        vertex.row += 1
                        self.way.append("up")
                        continue
                    # 左搜
                    if (vertex.col - 1) >= 0 and (self.arrayBFS[vertex.row][vertex.col - 1] == (node - 1)):
                        vertex.col -= 1
                        self.way.append("right")
                        continue
                    # 右搜
                    if (vertex.col + 1) < self.COL and (self.arrayBFS[vertex.row][vertex.col + 1] == (node - 1)):
                        vertex.col += 1
                        self.way.append("left")
                        continue

        #print(self.way)
    def InitarrayBFS(self):
        self.way=[]
        self.arrayBFS = [([0] * (self.COL)) for i in range(self.ROW)]
        try:
            self.arrayBFS[self.head.row][self.head.col]=1
        except:
            print("数组越界")
        for snake in self.body:
            self.arrayBFS[snake.row][snake.col]=-1
    def drawWay(self):
        for i in range(0,len(self.arrayBFS)):
            for j in range(0,len(self.arrayBFS[0])):
                self.Text = self.font.render(str(self.arrayBFS[i][j]), 1, (255, 255, 255))
                self.window.blit(self.Text, (j*self.cell, i*self.cell-self.cell/8))

    def drawGame(self,debug=False):
        pygame.draw.rect(self.window, self.backGroundColor, (0, 0, self.width, self.height))
        self.rect(self.head, self.headColor)
        self.rect(self.food, self.foodColor)
        # 生成蛇身体
        for snake in self.body:
            self.rect(snake, self.bodyColor)
        #调试模式下面画出道路
        if debug:
            self.drawWay()
        pygame.display.update()

    def rect(self,point, color):
        left = point.col * self.cell
        top = point.row * self.cell
        pygame.draw.rect(self.window, color, (left, top, self.cell, self.cell))

    def isGameOver(self):
        isOver=False
        if (self.head.row < 0 or self.head.col < 0 or self.head.row > self.ROW-1 or self.head.col > self.COL-1):
            print("游戏结束 1")
            isOver = True
        for snake in self.body:
            if (self.head.row == snake.row and self.head.col == snake.col):
                print("游戏结束二2")
                isOver = True
        return isOver
    def snakeMove(self,auto=False,move=True):
        if auto:
            self.BFSfindWay()
            if move:
                if len(self.way) >0:
                    self.keyEvent(debug=True,dir=self.way.pop())
        if move:
            #是否吃到食物
            eat = (self.head.row == self.food.row and self.head.col == self.food.col)
            self.body.insert(0, self.head.copy())
            #注意位置关系
            if eat:
                self.food = self.randomFood()
            else:
                self.body.pop()
            if self.direct == "left":
                self.head.col -= 1
            if self.direct == "down":
                self.head.row += 1
            if self.direct == "up":
                self.head.row -= 1
            if self.direct == "right":
                self.head.col += 1

    def randomFood(self):
        isRepeat=False
        pos = Point(random.randint(1, self.ROW - 2), random.randint(1, self.COL - 2))
        if (pos.row == self.head.row and pos.col == self.head.col):
            isRepeat=True
        for snake in self.body:
            if (pos.row == snake.row and pos.col == snake.col):
                isRepeat=True
        if isRepeat:
            pos=self.randomFood()
        return pos
    def keyEvent(self,debug=False,dir=""):
        isQuit = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isQuit = True
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_LEFT:
                    if (self.direct == "up" or self.direct == "down"):
                        self.direct = "left"
                        self.way = []
                elif event.key == pygame.K_RIGHT:
                    if (self.direct == "up" or self.direct == "down"):
                        self.direct = "right"
                        self.way = []
                elif event.key == pygame.K_UP:
                    if (self.direct == "right" or self.direct == "left"):
                        self.direct = "up"
                        self.way = []
                elif event.key == pygame.K_DOWN:
                    if (self.direct == "right" or self.direct == "left"):
                        self.direct = "down"
                        self.way = []
        if debug:
            if dir == "left":
                if (self.direct == "up" or self.direct == "down"):
                    self.direct = "left"
            elif dir == "right":
                if (self.direct == "up" or self.direct == "down"):
                    self.direct = "right"
            elif dir == "up":
                if (self.direct == "right" or self.direct == "left"):
                    self.direct = "up"
            elif dir == "down":
                if (self.direct == "right" or self.direct == "left"):
                    self.direct = "down"
        return isQuit
    def gameOver(self):
        Text = self.font.render("游戏结束",1,(255,255,255))
        self.window.blit(Text,(self.width/2,self.height/2))
        pygame.display.update()
    def gameMain(self):
        #游戏初始化
        self.gameInit("贪吃蛇")
        #游戏没有结束
        while not self.isGameOver() and not self.keyEvent():
            self.drawGame(debug=False)
            self.snakeMove(auto=True,move=True)
            self.clock.tick(self.speed)

        #游戏结束
        while  not self.keyEvent():
            #self.gameOver()
            self.clock.tick(self.speed)
snake=snakeGame(800,600,10,2000)
snake.gameMain()
