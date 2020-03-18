"""
    organisms.py
"""

import math, random
from math import sqrt
#from PIL import Image
#import numpy as np
from numpy import array, dot
from numpy.random import rand
import enum




class Health(enum.Enum):
    healthy    = 0
    infected   = 1
    contageous = 2
    sick       = 3
    healed     = 4



class Organism:

    def __init__(self, x, y, infected=False, vulnerability=True, speed=5):
       self.x = x
       self.y = y
       self.health = Health.healthy
       self.is_contageous = False
       self.infection_time = None
       self.vulnerability = vulnerability
       self.speed = speed
       # representation
       self.size = 6 
       self.thickness = self.size
       self.angle = random.uniform(0, 360)
       self.colour = (0,100,100)#color_for_health(self.health)
       
    def move(self):
       """
          Update position based on speed and angle
       """
 		
       self.x += math.sin(self.angle) * self.speed
       self.y -= math.cos(self.angle) * self.speed

    def infect(self, infection_time):
        self.health = Health.infected
        self.infection_time = infection_time

    def updateHealth(self, time):
        if self.health != Health.healthy:
            if time - self.infection_time > 14*1000:
                #print("healthy again")
                self.colour = (0,200,200)
                self.health = Health.healed
                self.is_contageous = False
            elif time - self.infection_time > 7*1000:
                #print("getting sick")
                self.colour = (255,0,0)
                self.health = Health.sick
                self.is_contageous = True
            elif time - self.infection_time > 5*1000:
                #print("getting contageous")
                self.colour = (150,150,0)
                self.health = Health.contageous
                self.is_contageous = True





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
            if i > n*(1-1/4):
                o = Organism(random.uniform(0, self.width), random.uniform(0, self.height), speed=0)
            else:
                o = Organism(random.uniform(0, self.width), random.uniform(0, self.height))
            #print(f"Created organism at ({o.x},{o.y})")
            self.organisms.append(o)
        self.update()
        self.organisms[0].infect(self.time_elapsed)


    def update(self):
        """  """
        for i, o in enumerate(self.organisms):
            o.updateHealth(self.time_elapsed)
            o.move()
            self.bounce_off_wall(o)
            for j, o2 in enumerate(self.organisms[i+1:]):
                self.collide(o, o2)
        

    def removeOrganism(self, organism):
       """  """
       pass


    def collide(self, organism1, organism2):
        """ check if organisms collide """
        
        match_x = abs(organism1.x - organism2.x) < (organism1.size + organism2.size)
        match_y = abs(organism1.y - organism2.y) < (organism1.size + organism2.size)
        if match_x and match_y:
            # infect if either is sick
            if organism1.is_contageous: organism2.infect(self.time_elapsed)
            if organism2.is_contageous: organism1.infect(self.time_elapsed)

            if organism1.speed == 0 or organism2.speed == 0:
                organism1.angle, organism2.angle = (360-organism1.angle, 360-organism2.angle)
            else:
                # swap angles due to collision
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

