import pygame, sys, time,math
from pygame.locals import *

import geometry

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

class Entity(object):
    cx = 0
    cy = 0
    vx = 0
    vy = 0
    ax = 0
    ay = 0
    jx = 0
    jy = 0
    av = 0

    def getRect(self):
        pass

    def logic(self, o):
        pass

    def preUpdate(self):
        pass
    
    def postUpdate(self):
        pass
    
    def draw(self, o):
        pass

class Shape(Entity):
    color = BLACK

class Poly(Shape):
    def __init__(self, p, color, fill = True):
        self.p = p
        self.prevp = p
        self.color = color
        self.cx = float(sum(q[0] for q in p))/len(p)
        self.cy = float(sum(q[1] for q in p))/len(p)
        self.fill = fill
   
    def preUpdate(self):
        self.prevp = self.p

    def translateX(self, x):
        self.cx += x
        for q in self.p:
            q[0] += x

    def translateY(self, y):
        self.cy += y
        for q in self.p:
            q[1] += y

    def rotate(self, ang):
        o = (self.cx, self.cy)
        for i in range(len(self.p)):
            self.p[i] = geometry.rotate(o, self.p[i], ang)

    def draw(self, wSurface):
        pygame.draw.aalines(wSurface, self.color, True, self.p)
        if self.fill:
            pygame.draw.polygon(wSurface, self.color, self.p)

class Rect(Poly):
    def __init__(self, top, left, w, h, color, fill = True):
        self.top = top
        self.left = left 
        self.w = w
        self.h = h
        p = [[left, top], [left+w, top], [left+w, top+h], [left, top+h]]
        super(Rect, self).__init__(p, color, fill)
    
    def getRect(self):
        return pygame.Rect(self.left, self.top, self.w, self.h)
    
class Circle(Shape):
    def __init__(self, cx, cy, rad, color):
        self.cx = cx
        self.cy = cy
        self.rad = rad
        self.color = color
    
    def getRect(self):
        return pygame.Rect(self.cx - self.rad, self.cy - self.rad, 2*self.rad, 2*self.rad)

    def translateX(self, x):
        self.cx += x
    
    def translateY(self, y):
        self.cy += y
    
    def rotate(self, ang):
        pass

    def preUpdate(self):
        self.prevCX = self.cx
        self.prevCY = self.cy

    def postUpdate(self):
        pass

    def draw(self, wSurface):
        pygame.draw.circle(wSurface, self.color, (int(round(self.cx)), int(round(self.cy))), self.rad)

class Game:
    def __init__(self, w, h, bg, title):
        pygame.init()
        self.w_width = w
        self.w_height = h
        self.bg = bg
        self.title = title
        self.entities = []
        self.keyUpActions = []
        self.keyDownActions = []
        self.wSurface = pygame.display.set_mode((w, h), 0, 32)
        self.wSurface.fill(bg)
        pygame.display.set_caption(title)

    def start(self):
        while True:
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if e.type == KEYUP:
                    keyUpActions[chr(e.key)]()
                
                if e.type == KEYDOWN:
                    keyDownActions[chr(e.key)]()

            self.wSurface.fill(self.bg)

            for e in self.entities:
                e.preUpdate()
                
                e.translateX(e.vx)
                e.translateY(e.vy)
                e.vx += e.ax
                e.vy += e.ay
                e.ax += e.jx
                e.ay += e.jy
                e.rotate(e.av)
                
                e.logic(e)
                e.postUpdate()
                e.draw(self.wSurface)

            pygame.display.update()
            time.sleep(1.0/120)
