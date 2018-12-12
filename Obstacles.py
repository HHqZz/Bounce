
import arcade
from miscellaneous import Misc
from  Constants import CIRCLE_RADIUS
from Point import Point
from CollisionHandler import CollisionHandler
from Vector import Vector
import math

class Obstacle:
    def __init__(self, A,B, color, width):
        self.pointDepart = A
        self.pointFinal = B
        self.color = color
        self.width = width
        self.isHit = False

    def draw(self):
        arcade.draw_line(self.pointDepart.x, self.pointDepart.y, self.pointFinal.x, self.pointFinal.y, self.color, self.width)

    def update(self, ball):
        self.checkforCollision(ball)

    def checkforCollision(self, ball):
       if Misc.line_circle_intersection(self,ball.centre.x, ball.centre.y, CIRCLE_RADIUS, self.pointDepart, self.pointFinal) and not self.isHit:
            normale = Vector.getNormale(self, self.pointDepart, self.pointFinal, ball.centre)
            impact = Misc.projectionCercleObstacle(self, self.pointDepart,self.pointFinal,ball.centre)
            incident = ball.vitesse 
            Vf = CollisionHandler.collisionResolution(self, incident , normale)
            ball.vitesse.dx = Vf.dx 
            ball.vitesse.dy = Vf.dy 
            self.isHit = True
            print("COLLISION")

       if not Misc.line_circle_intersection(self,ball.centre.x, ball.centre.y, CIRCLE_RADIUS, self.pointDepart, self.pointFinal) and self.isHit :
            self.isHit = False
