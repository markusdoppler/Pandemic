"""
    environment.py
"""

import math, random
from functools import reduce
#from PIL import Image
#import numpy as np
from numpy import array, dot
from numpy.random import rand
import enum

from organisms import Organism, Health



class Environment:
	
    def __init__(self, size, restriction=0.25):
        self.width = size[0]
        self.height = size[1]
        self.organisms = []
        self.colour = (255,255,255)
        self.elasticity = 1.
        self.colliding = True
        self.time_elapsed = 0
        self.restriction = restriction

    def add_organisms(self,n=1,**kwargs):
        """  """
        #kwargs.get('x', ...)
        for i in range(n):
            space_occupied = True
            while space_occupied:
                o = Organism(random.uniform(0, self.width), random.uniform(0, self.height))
                space_occupied = False
                for j, o2 in enumerate(self.organisms):
                    if abs(o.x - o2.x) < 1.5*o.size and abs(o.y - o2.y) < 1.5*o.size:
                        #print(f"{i} is occupied at ({o.x}, {o.y} by particle {j}")
                        space_occupied = True
                #print(i, space_occupied)
            
            if i >= math.floor(n*(1.-self.restriction)):
                o.speed = 0
            #print(f"Created organism at ({o.x},{o.y})")
            self.organisms.append(o)
            self.organisms[0].infect(self.time_elapsed)


    def update(self):
        """ update all organisms' health and position """
        for i, o in enumerate(self.organisms):
            o.update_health(self.time_elapsed)
            o.update_position()
            self.bounce_off_wall(o)
            for j, o2 in enumerate(self.organisms[i+1:]):
                self.collide(o, o2)
        

    def remove_organism(self, organism):
       """  """
       pass


    def collide(self, organism1, organism2):
        """ check if organisms collide """
        distance = (organism1.x - organism2.x, organism1.y - organism2.y)
        r = reduce(lambda x,y: math.sqrt(x**2+y**2), distance)
        if r < organism1.size + organism2.size:
            # infect if either is sick
            if organism1.is_contageous(): organism2.infect(self.time_elapsed)
            if organism2.is_contageous(): organism1.infect(self.time_elapsed)

            if organism2.speed == 0:
                organism1.angle = 360.0 - organism1.angle
                #organism1.colour = (0,218,255)
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

    def health_overview(self):
        """ counts  """
        healthy, infected, contageous, sick, healed = 0,0,0,0,0
        for i, o in enumerate(self.organisms):
            if   o.health == Health.healthy:    healthy += 1
            elif o.health == Health.infected:   infected += 1
            elif o.health == Health.contageous: contageous += 1
            elif o.health == Health.sick:       sick += 1
            elif o.health == Health.healed:     healed += 1
        return {\
            Health.healthy: healthy,
            Health.infected: infected,
            Health.contageous: contageous,
            Health.sick: sick,
            Health.healed: healed}
