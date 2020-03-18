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
       self.infection_time = None
       self.vulnerability = vulnerability
       self.speed = speed
       # representation
       self.size = 6 
       self.thickness = self.size
       self.angle = random.uniform(0, 360)
       self.colour = (0,100,100)#color_for_health(self.health)


    def move(self):
       """ Update position based on speed and angle """
 		
       self.x += math.sin(self.angle) * self.speed
       self.y -= math.cos(self.angle) * self.speed


    def infect(self, infection_time):
        """ Infect the organism with the decease """
        self.health = Health.infected
        self.infection_time = infection_time


    def updateHealth(self, time):
        """ Update the health """

        if self.health != Health.healthy:

            if time - self.infection_time > 14*1000:
                #print("healthy again")
                self.colour = (0,200,200)
                self.health = Health.healed

            elif time - self.infection_time > 7*1000:
                #print("getting sick")
                self.colour = (255,0,0)
                self.health = Health.sick

            elif time - self.infection_time > 5*1000:
                #print("getting contageous")
                self.colour = (150,150,0)
                self.health = Health.contageous


    def is_contageous(self):
        """ Is the organism contageous to others? """
        return (self.health == Health.contageous or self.health == Health.sick)
