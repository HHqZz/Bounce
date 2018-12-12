
import arcade
import math
from  miscellaneous import Misc
import Constants

class Arrow:
    def __init__(self, x1, y1, x2, y2, x3, y3, color):
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2
            self.x3 = x3
            self.y3 = y3
            self.color = color

    def draw(self):
        arcade.draw_triangle_filled(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, self.color)

    def update(self,x,y):
        self.x1 = x
        self.y1 =y
    
        intersections = Misc.circle_intersection(self,(Constants.SCREEN_X/2, Constants.SCREEN_Y/2, Constants.CIRCLE_RADIUS), 
                                                                                                        (x,y,math.sqrt(pow(x-Constants.SCREEN_X/2,2)+ pow(y-Constants.SCREEN_Y/2,2)- pow(Constants.CIRCLE_RADIUS,2))))
        self.x2 = intersections[0]
        self.y2= intersections[1]
        self.x3 =  intersections[2]
        self.y3 =  intersections[3]
       