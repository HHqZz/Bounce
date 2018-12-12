
import Constants
import arcade
from miscellaneous import Misc
from Point import Point
from shapely import geometry


class Cible :
    """
    This class describe cible the user has to hit with the ball
    - cible should only be on edges =  (x =0 ; y = any)  (x = edge ; y = any)  ( x =  any ; y= 0)   (x = any ; y = edge)
    - cible are green, when hit they become red
    - We should add a cible only by giving a single point, size is always the same
    - if the cible cant fit on the edge, it should continue on the crossing edge
"""

    def __init__(self, position):
        self.size = Constants.CIBLE_size
        self.color = Constants.GREEN
        self.position = position
        self.left = [0, 600]
        self.top = [600, 1200]
        self.right =[1200, 1800]
        self.bot =[1800,2400]
        self.drawLeft =[]
        self.drawTop=[]
        self.drawBot=[]
        self.drawRight=[]
        self.interiorLines = []
        self.retrieveAllPixelToDraw()
        self.getInteriorLines()

    def draw(self,ball):
        self.drawNeededEdges()

    def update(self,ball):
        self.checkForCollision(ball)

    def drawNeededEdges(self):
        if  len(self.drawLeft ) != 0   :
            self.draw_left() 
        if  len(self.drawRight ) != 0:
            self.draw_right() 
        if  len(self.drawTop ) != 0 :
            self.draw_top()
        if  len(self.drawBot ) != 0 :
            self.draw_bot()

    def retrieveAllPixelToDraw(self):
        pixelMin = self.position - Constants.CIBLE_size
        pixelMax = self.position+ Constants.CIBLE_size
        for pixel  in range(pixelMin,pixelMax):
            if pixel > 2400:
                pixel = pixel % 2400
            while pixel <0 :
                pixel = pixel+2400
            if Misc.isBetween(self,self.left[0],self.left[1], pixel) :
                self.drawLeft.append(pixel)
            if Misc.isBetween(self,self.top[0],self.top[1],pixel):
                self.drawTop.append(pixel)
            if Misc.isBetween(self,self.right[0],self.right[1],pixel):
                self.drawRight.append(pixel)
            if Misc.isBetween(self,self.bot[0],self.bot[1],pixel) or pixel<0:
                self.drawBot.append(pixel)

    def getInteriorLines(self):
        if len(self.drawLeft)!=0:
            point1 = geometry.Point(Constants.obstacle_width, min(self.drawLeft))
            point2 = geometry.Point(Constants.obstacle_width, max(self.drawLeft))
            line =  geometry.LineString((point1,point2))
            self.interiorLines.append(line)

        if  len(self.drawRight ) != 0:
            point1 = geometry.Point(Constants.SCREEN_X-Constants.obstacle_width,1800 - min(self.drawRight))
            point2 = geometry.Point(Constants.SCREEN_X -Constants.obstacle_width,1800 - max(self.drawRight))
            line =  geometry.LineString((point1,point2))
            self.interiorLines.append(line)

        if  len(self.drawTop ) != 0 :
            point1 = geometry.Point(min(self.drawTop)  - Constants.SCREEN_X,Constants.SCREEN_Y-Constants.obstacle_width )
            point2 = geometry.Point( max(self.drawTop)  - Constants.SCREEN_X,Constants.SCREEN_Y-Constants.obstacle_width )
            line =  geometry.LineString((point1,point2))
            self.interiorLines.append(line)

        if  len(self.drawBot ) != 0 :
            point1 = geometry.Point(2400-max(self.drawBot), Constants.obstacle_width)
            point2 = geometry.Point(2400-min(self.drawBot), Constants.obstacle_width)
            line =  geometry.LineString((point1,point2))
            self.interiorLines.append(line)

    def checkForCollision(self,ball):
        for line in self.interiorLines:
            if geometry.Point(ball.centre.x,ball.centre.y).buffer(ball.radius).boundary.intersects(line) :
                self.hit()

    def draw_left(self):
        arcade.draw_commands.draw_lrtb_rectangle_filled(0, Constants.obstacle_width,  max(self.drawLeft) ,min(self.drawLeft), self.color)

    def draw_top(self):
        arcade.draw_commands.draw_lrtb_rectangle_filled(min(self.drawTop)  - Constants.SCREEN_X,max(self.drawTop)-600, Constants.SCREEN_Y, Constants.SCREEN_Y-Constants.obstacle_width, self.color)

    def draw_right(self):
        arcade.draw_commands.draw_lrtb_rectangle_filled(Constants.SCREEN_X-Constants.obstacle_width, Constants.SCREEN_X,1800 - min(self.drawRight), 1800 -max(self.drawRight),self.color)

    def draw_bot(self):
        arcade.draw_commands.draw_lrtb_rectangle_filled(2400-max(self.drawBot),2400- min(self.drawBot), Constants.obstacle_width,0,self.color)

    def hit(self):
        self.color = Constants.RED
