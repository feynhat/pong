import math

EPS = 1e-5

class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def norm(self):
        return norm(self.x,  self.y)

    def direction(self):
        M = self.norm()
        return Vec(float(self.x)/M, float(self.y)/M)

def vecDot(v1, v2):
    return v1.x*v2.x + v1.y*v2.y

def approx(x, y):
    return (abs(x-y) <= EPS)

def norm(a, b):
    return (a**2 + b**2)**.5

def dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p0[1] - p1[1])**2)

def rotate(o, p, a):
    x = p[0] - o[0]
    y = p[1] - o[1]
    rotx =  x*math.cos(a) - y*math.sin(a) + o[0]
    roty =  x*math.sin(a) + y*math.cos(a) + o[1]
    return [rotx, roty]

def angle(v1, v2):
    cos = float(vecDot(v1, v2))/(v1.norm()*v2.norm())
    if cos > 1:
        print("WTF COS>1 ?!?")
        sys.exit()
    sin = (1 - cos**2)**.5
    return [cos, sin]

def line2Points(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    a = (y2-y1)
    b = (x1-x2)
    c = x1*a + y1*b
    return [a, b, c]

def lineSlopePoint(m, p):
    x1, y1 = p
    a = -m
    b = 1
    c = -m*x1 + y1
    return [a, b, c]

def perpLinePoint(l, p):
    a1, b1, _ = l
    x1, y1 = p
    a = -b1
    b = a1
    c = a*x1 + b*y1
    return [a, b, c]

def solve2Lines(l1, l2):
    a1, b1, c1 = l1
    a2, b2, c2 = l2
    x = float(b2*c1 - b1*c2)/(a1*b2 - a2*b1)
    y = float(a1*c2 - a2*c1)/(a1*b2 - a2*b1)
    return [x, y]

def distPointLine(p, l):
    x, y = p
    a, b, c = l
    return abs(a*x + b*y - c)/norm(a, b)

def dist2Lines(l1, l2):
    a1, b1, c1 = l1
    a2, b2, c2 = l2
    if a1*a2 < 0 or b1*b2 < 0:
        c1 = -c1
    return float(abs(c1-c2))/norm(a1, b1)
