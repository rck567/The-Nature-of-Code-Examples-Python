# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
# 
# Python port: Abhik Pal

class Mover(object):
    def __init__(self):
        self.position = PVector(400, 50)
        self.velocity = PVector(1, 0)
        self.acceleration = PVector(0,0)
        self.mass = 1
        
    def applyForce(self, force):
        f = PVector.div(force, self.mass)
        self.acceleration.add(f)
    
    def update(self):
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.acceleration.mult(0)
    
    def display(self):
        stroke(0)
        strokeWeight(2)
        fill(127)
        ellipse(self.position.x, self.position.y, 16, 16)
    
    def checkEdges(self):
        if (self.position.x > width):
            self.position.x = 0
        elif (self.position.x < 0):
            self.position.x = width


        if (self.position.y > height):
            self.position.y = height

            self.velocity.y *= -1