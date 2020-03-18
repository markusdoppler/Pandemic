import pygame as pg
from environment import Environment
from organisms import Organism, Health
import random, math, itertools, time, pickle

# plotting
import matplotlib.pyplot as plt
from scipy import asarray as ar,exp
import numpy as np

# size of window
(width, height) = (1000, 666)

# parameters
duration = 60 #60
population = 80 #1000
sick_initial = 1

# HEX-colours
RED = (255,0,0)
WHITE = (255,255,255)
GREY = (230,230,230)
BLUE = (0,0,255)
BLACK = (0,0,0)



environment = Environment((width, height))
environment.addOrganisms(population)

#pygame
pg.init()
screen = pg.display.set_mode((width, height))

# display text
pg.display.set_caption('Pandemic 1.0')
#basicfont = pg.font.Font(None, 32)
#text_string = ''
#header = basicfont.render(text_string, True, RED, WHITE)
#headerRect = header.get_rect()   
#headerRect.center = (50, 40)

pg.init()
start_time = time.time()
current_time = time.time()

i = 0
s = 0
x            = ar([])
y_contageous = ar([])
y_sick       = ar([])
y_healed     = ar([])
while current_time - start_time < duration:
    pg.init()

    # draw background
    screen.fill(environment.colour)
    environment.update()


    #print(f"{current_time} ({current_time}) {duration}") 
    for o in environment.organisms:
        #print(f"c:{o.colour}, ({o.x},{o.y}), {o.size}, {o.thickness}")
        pg.draw.circle(screen, o.colour, (int(o.x), int(o.y)), o.size, o.thickness)
        #pg.draw.circle(screen, )
    for event in pg.event.get():
        if event.type in (pg.QUIT, pg.KEYDOWN):
            print("Key pressed")
    #screen.blit()

    pg.display.flip()
    current_time = time.time()
    time_elapsed = int(round((current_time - start_time)*1000))
    environment.time_elapsed = time_elapsed

    if s < math.floor(current_time - start_time):
        # data for plotting
        x = np.append(x, s)
        ov = environment.health_overview()
        #print(ov)
        y_contageous = np.append(y_contageous, ov[Health.contageous])
        y_sick       = np.append(y_sick, ov[Health.sick])
        y_healed     = np.append(y_healed, ov[Health.healed])
            
    s = math.floor(current_time - start_time)
    i+=1
print(i)

fig, ax = plt.subplots()
plt.plot(x,y_contageous,'ro:',label='contageous')
plt.plot(x,y_sick,'bo:',label='sick')
plt.plot(x,y_healed,'go:',label='healed')
plt.legend()
plt.show()




#pg.draw.line(screen, p.colour, (int(p.x), int(p.y)), (int(p.x)+p.distance_front*math.sin(angle),int(p.y)+p.distance_front*math.cos(angle)))
#screen.blit(header, headerRect)


# infinite loop that stops on key press
#def main():
#    while 1:
#        for event in pg.event.get():
#            if event.type in (pg.QUIT, pg.KEYDOWN):
#                return
#
#if __name__ == "__main__":
#    main()

