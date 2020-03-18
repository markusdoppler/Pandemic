"""
    organisms.py
"""

import math, random
from math import sqrt
#from PIL import Image
#import numpy as np
from numpy import array, dot
from numpy.random import rand








class Organism:

    def __init__(self, x, y, infected=False, vulnerability=True, speed=4):
       self.x = x
       self.y = y
       self.health = 1 # healthy
       self.vulnerability = vulnerability
       self.time_since_infection = None
       self.speed = speed
       # representation
       self.size = 10
       self.thickness = self.size
       self.angle = random.uniform(0, 360)
       self.colour = (0,100,100)#color_for_health(self.health)
       
    def move(self):
       """
          Update position based on speed and angle
       """
 		
       self.x += math.sin(self.angle) * self.speed
       self.y -= math.cos(self.angle) * self.speed







class Environment:
	
    def __init__(self, size):
        self.width = size[0]
        self.height = size[1]
        self.organisms = []
        self.colour = (255,255,255)
        self.elasticity = 1.
        self.colliding = True
        self.time_elapsed = 0

    def addOrganisms(self,n=1,**kwargs):
        """  """
        #kwargs.get('x', ...)
        for i in range(n):
            o = Organism(random.uniform(0, self.width), random.uniform(0, self.height))
            #print(f"Created organism at ({o.x},{o.y})")
            self.organisms.append(o)
        self.update()

    def update(self):
        """  """
        for i, o in enumerate(self.organisms):
            o.move()
            self.bounce_off_wall(o)
            for j, o2 in enumerate(self.organisms[i+1:]):
                self.collide(o, o2)
        

    def removeOrganism(self, organism):
       """  """
       pass

#	def update(self):
#		''' Update the unique parameters of the organism '''
#		
#		for i, organism in enumerate(self.organisms):
#			organism.control(self)
#			organism.move()
#			self.bounce(organism)
#			self.track_bounce(organism)
#			if self.colliding:
#				for organism2 in self.organisms[i+1:]:
#					collide(organism, organism2)
#			self.distances(organism)
#			organism.update_score(self)
#
    def collide(self, organism1, organism2):
        """ check if organisms collide """
        
        cond1 = abs(organism1.x - organism2.x) < (organism1.size + organism2.size)/sqrt(2.)
        cond2 = abs(organism1.y - organism2.y) < (organism1.size + organism2.size)/sqrt(2.)
        if cond1 and cond2:
            # infect if either is sick
            organism1.colour = (255,0,0)
            organism2.colour = (255,0,0)
            # swap angles
            organism2.angle, organism1.angle = (organism1.angle, organism2.angle)


    def bounce_off_wall(self,organism):
        """ check if (x,y) is off the screen, bounce off limits"""

        if organism.x > self.width - organism.size:
            organism.x = 2*(self.width - organism.size) - organism.x
            organism.angle = - organism.angle
            organism.speed *= self.elasticity
        
        elif organism.x < organism.size:
            organism.x = 2*organism.size - organism.x
            organism.angle = - organism.angle
            organism.speed *= self.elasticity
        
        if organism.y > self.height - organism.size:
            organism.y = 2*(self.height - organism.size) - organism.y
            organism.angle = math.pi - organism.angle
            organism.speed *= self.elasticity
        
        elif organism.y < organism.size:
            organism.y = 2*organism.size - organism.y
            organism.angle = math.pi - organism.angle
            organism.speed *= self.elasticity

