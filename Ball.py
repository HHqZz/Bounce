
import math
from Point import Point
import arcade
import Constants
from Vector import Vector
from CollisionHandler import CollisionHandler

class Ball:
    def __init__(self, position_x, position_y, vitesse_x, vitesse_y, radius, color):
        self.centre = Point(position_x,position_y)
        self.vitesse = Vector(vitesse_x,vitesse_y)
        self.radius = radius
        self.color = color

    def getActualSpeed(self):
        return math.sqrt(math.pow(self.vitesse.dx, 2) + math.pow(self.vitesse.dy, 2))
    
    def resetPosition(self):
        self.centre = Point(Constants.SCREEN_X/2, Constants.SCREEN_Y/2)
        
    def draw(self):
        arcade.draw_circle_filled(
            self.centre.x, self.centre.y, self.radius, self.color)

    def update(self):
        self.centre.y += self.vitesse.dy
        self.centre.x += self.vitesse.dx
        CollisionHandler.ballCollision(self)
        # Stop the ball smoothly when speed is too low
        self.smoothSlow()

    def slowBall(self,pos):
        if pos == "x":
            self.vitesse.dx = self.vitesse.dx * Constants.BOUNCINESS
        if pos == "y":
            self.vitesse.dy = self.vitesse. dy * Constants.BOUNCINESS


    def smoothSlow(self):
        if self.getActualSpeed() < Constants.MIN_SPEED and self.getActualSpeed() > 1:
            if self.vitesse.dx < 0:  
                self.vitesse.dx = self.vitesse.dx + 0.01
            else:
                self.vitesse.dx = self.vitesse.dx - 0.01
            if self.vitesse.dy < 0:  
                self.vitesse.dy = self.vitesse.dy + 0.01
            else:
                self.vitesse.dy -= 0.01
        if self.getActualSpeed() < 1:
            self.vitesse.dx = 0
            self.vitesse.dy = 0

    def launch(self,x,y):
        self.vitesse.dx =  (x - self.centre.x)/10
        self.vitesse.dy = ( y - self.centre.y)/10