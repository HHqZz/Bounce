
from math import   sqrt
from math import hypot
from Vector import Vector
import sys
from shapely import geometry
from Point import Point

class Misc(object):
    def circle_intersection(self, circle1, circle2):
        x1,y1,r1 = circle1
        x2,y2,r2 = circle2
        dx,dy = x2-x1,y2-y1
        d = sqrt(dx*dx+dy*dy)
        a = (r1*r1-r2*r2+d*d)/(2*d)
        h = sqrt(r1*r1-a*a)
        xm = x1 + a*dx/d
        ym = y1 + a*dy/d
        xs1 = xm + h*dy/d
        xs2 = xm - h*dy/d
        ys1 = ym - h*dx/d
        ys2 = ym + h*dx/d
        return [xs1,ys1,xs2,ys2]

    def isBetween(self,bot,top,value):
        return ((bot<=value) and (top>=value))

    def line_circle_intersection(self,center_x, center_y, radius, start, end):
        return geometry.Point(center_x,center_y).buffer(radius).boundary.intersects(geometry.LineString([(start.x,start.y),(end.x,end.y)]))


    def projectionCercleObstacle(self, A, B,C):
        u = Vector(B.x - A.x, B.y -A.y)
        AC = Vector(C.x - A.x, C.y - A.y) 
        ti = (u.dx*AC.dx + u.dy*AC.dy)/(u.dx*u.dx + u.dy*u.dy)
        I = Point(A.x + ti*u.dx ,A.y + ti*u.dy )
        return I
      

