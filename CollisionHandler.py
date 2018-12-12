
from miscellaneous import Misc
from Vector import Vector
import Constants
import math
# pylint: skip-file

class CollisionHandler :
    def collisionResolution(self,V_incident, N):# Vecteur incident a lobstacle et normale de lobstacle
        pscal = (V_incident.dx*N.dx +  V_incident.dy*N.dy)
        if Misc.isBetween(self,-0.5,0.5,pscal):
            print("PSCAL  = ", pscal)
            return  Vector(-V_incident.dx, -V_incident.dy)
        print("PSCAL @@@@ = ", pscal)
        v2 = Vector(V_incident.dx -2*pscal*N.dx, V_incident.dy -2*pscal*N.dy)
        return v2
                
    def ballCollision(self):
        # left
        if self.centre.x < self.radius:
            self.centre.x = self.radius
            self.vitesse.dx = -self.vitesse.dx
            self.slowBall("x")
 
         # right
        if self.centre.x > Constants.SCREEN_X-self.radius:
            self.centre.x = Constants.SCREEN_X - self.radius
            self.vitesse.dx = -self.vitesse.dx 
            self.slowBall("x")

        # bot
        if self.centre.y < self.radius:
            self.centre.y = self.radius
            self.vitesse.dy = -self.vitesse.dy
            self.slowBall("y")


         # top
        if self.centre.y > Constants.SCREEN_Y - self.radius:
            self.centre.y = Constants.SCREEN_Y - self.radius
            self.vitesse.dy = -self.vitesse.dy
            self.slowBall("y")

