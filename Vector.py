
from math import hypot

class Vector :
    def  __init__(self,dx,dy):
        self.dx= dx
        self.dy=dy

    def getNormale( self, A, B, C): #A,B = obstacle , C = centre du cercle ou Impact ?
        u= Vector(B.x - A.x, B.y - A.y )
        AC = Vector( C.x - A.x, C.y - A.y )
        parenthesis = u.dx*AC.dy-u.dy*AC.dx; 
        N = Vector( -u.dy*parenthesis , u.dx*parenthesis )
        #Normalizeee
        norme = hypot(N.dx,N.dy)
        if norme == 0:
            return N
        else :
            N.dx= N.dx / norme
            N.dy=N.dy / norme
            return N