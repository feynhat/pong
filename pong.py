import sys, math
import game
from geometry import *
import pygame

W_WIDTH = 512
W_HEIGHT = 512
g = game.Game(W_WIDTH, W_HEIGHT, game.WHITE, "Pong")

BATMS = 5
BALLMS = 7
BATX = 72
PAD = 12
G_WIDTH = W_WIDTH - 2*PAD
G_HEIGHT = W_HEIGHT - 2*PAD
G_TOP = PAD
G_BOT = G_HEIGHT + PAD
G_LEFT = PAD
G_RIGHT = G_WIDTH + PAD

BATL = 42
BATW = 8
bat1 = game.Rect((G_HEIGHT - BATL)/2, BATX - BATW/2, 8, 42, game.BLACK)
bat2 = game.Rect((G_HEIGHT - BATL)/2, G_WIDTH - BATX + BATW/2, 8, 42, game.BLACK)
ball = game.Circle(G_WIDTH/2, G_HEIGHT/2 + 20, 5, game.RED)
gbox = game.Rect(PAD, PAD, G_WIDTH, G_HEIGHT, game.BLACK, False)

ball.vx = 2
ball.vy = 2

def ballLogic(ball):
    if ball.cy - ball.rad <= G_TOP or ball.cy + ball.rad >= G_BOT:
        ball.vy = -ball.vy
    if ball.cx - ball.rad <= G_LEFT or ball.cx + ball.rad >= G_RIGHT:
        ball.vx = -ball.vx
    bv = Vec(ball.vx, ball.vy)
    M = bv.norm()
    print(M)
    if M > BALLMS:
        ball.vx = ball.vx*(BALLMS/M)
        ball.vy = ball.vy*(BALLMS/M)
    ball.ax = -(ball.vx)*0.0008
    ball.ay = -(ball.vy)*0.0008

bat1.blockUp = False
bat1.blockDown = False
bat1.blockLeft = False
bat1.blockRight = False
bat2.blockUp = False
bat2.blockDown = False
bat2.blockLeft = False
bat2.blockRight = False

def batLogic(bat):
    if abs(bat.vy) >= BATMS:
        bat.ay = 0
        bat.vy = (bat.vy/abs(bat.vy))*BATMS
    
    block = False
    for q in bat.p:
        if q[1] <= G_TOP:
            bat.translateY(G_TOP - q[1])
            if round(q[0]) > BATX:
                if not bat.blockLeft:
                    bat.av = 0
                bat.blockLeft = True
                bat.blockRight = False
            elif round(q[0]) < BATX:
                if not bat.blockRight:
                    bat.av = 0
                bat.blockLeft = False
                bat.blockRight = True
            else:
                bat.blockLeft = False
                bat.blockRight = False
            if not bat.blockUp:
                bat.ay = 0
                bat.vy = 0
            bat.blockUp = True
            block = True
        
        if q[1] >= G_BOT:
            #print q[1], q[1]-G_BOT
            bat.translateY(G_BOT - q[1])
            if round(q[0]) < BATX:
                if not bat.blockLeft:
                    bat.av = 0
                bat.blockLeft = True
                bat.blockRight = False
            elif round(q[0]) > BATX:
                if not bat.blockRight:
                    bat.av = 0
                bat.blockLeft = False
                bat.blockRight = True
            else:
                bat.blockLeft = False
                bat.blockRight = False
            if not bat.blockDown:
                bat.ay = 0
                bat.vy = 0 
            bat.blockDown = True
            block = True
    if not block:
        bat.blockUp = False
        bat.blockDown = False
        bat.blockLeft = False
        bat.blockRight = False

    a, b, c = line2Points(bat.p[0], bat.p[3])
    #print a, b
    sin = abs(float(a))/(a**2 + b**2)**.5
    cos = abs(float(b))/(a**2 + b**2)**.5
    perp = [sin, cos]
    for i in range(4):
        l = line2Points(bat.p[i], bat.p[(i+1)%4])
        d = distPointLine([ball.cx, ball.cy], l)

        l1 = line2Points(bat.p[(i-1)%4], bat.p[i])
        l2 = line2Points(bat.p[(i+1)%4], bat.p[(i+2)%4])
        
        s = dist2Lines(l1, l2)
        s1 = distPointLine([ball.cx, ball.cy], l1)
        s2 = distPointLine([ball.cx, ball.cy], l2)
        
        if d <= ball.rad and approx(s, s1+s2):
            print("-"*80)
            print("Collision with line: ", l)
            print("Initial Velocity: ", ball.vx, ball.vy)
            a, b, c = l
            perpLine = perpLinePoint(l, (ball.cx, ball.cy))
            pointOfAction = solve2Lines(l, perpLine)
            x, y = pointOfAction
            perp = Vec(ball.cx - x, ball.cy - y).direction()

            bVec = Vec(ball.vx, ball.vy)
            bVecM = bVec.norm()

            cos = abs(angle(perp, bVec)[0])
            deltaV = Vec(2*cos*bVecM*perp.x, 2*cos*bVecM*perp.y)
            ball.vx += deltaV.x
            ball.vy += deltaV.y
            print(cos)
            print("Normal: ", perp.x, perp.y)
            print("Change in Velocity: ", deltaV.x, deltaV.y)
            print("Final Velocity: ", ball.vx, ball.vy)
            print("-"*80)
            #sys.exit()
            break

def actionKeyDownW():
    if not bat1.blockUp:
        bat1.ay = -0.25
        #bat1.vy = -10

def actionKeyDownS():
    if not bat1.blockDown:
        #bat1.vy = 10
        bat1.ay = 0.25

def actionKeyUp():
    bat1.vy = 0
    bat1.ay = 0

def rotateLeft():
    if not bat1.blockLeft:
        bat1.av = -math.pi/60.0

def rotateRight():
    if not bat1.blockRight:
        bat1.av = +math.pi/60.0

def stopRotate():
    bat1.av = 0

game.keyDownActions = {'w': actionKeyDownW, 's': actionKeyDownS, 'a': rotateLeft, 'd': rotateRight}
game.keyUpActions = {'w': actionKeyUp, 's': actionKeyUp, 'a': stopRotate, 'd': stopRotate}
ball.logic = ballLogic
bat1.logic = batLogic
bat2.logic = batLogic

g.entities = [ball, bat1, bat2, gbox]

g.start()
