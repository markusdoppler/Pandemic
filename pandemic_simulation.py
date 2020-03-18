import pygame as pg
from organisms import Organism, Environment
import random, math, itertools, time, pickle

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
    environment.time_elapsed = int(round((current_time - start_time)*1000))



#pg.draw.line(screen, p.colour, (int(p.x), int(p.y)), (int(p.x)+p.distance_front*math.sin(angle),int(p.y)+p.distance_front*math.cos(angle)))
#screen.blit(header, headerRect)

#for i in range(0,10):
#
#    p = sorted_list[i]
#
#    leader_x = 800 + 75
#    leader_y = 80 + i*35
#
#    numberplate = basicfont.render(str(i+1), True, BLACK, WHITE)
#    numberRect = numberplate.get_rect()   
#    numberRect.center = (leader_x - 10, leader_y)
#    screen.blit(numberplate, numberRect)
#
#    pg.draw.circle(screen, p.colour, (leader_x + 20, leader_y), p.size, p.thickness)



# infinite loop that stops on key press
#def main():
#    while 1:
#        for event in pg.event.get():
#            if event.type in (pg.QUIT, pg.KEYDOWN):
#                return
#
#if __name__ == "__main__":
#    main()

