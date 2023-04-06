import pygame
import random

from scripts.render import *
from scripts.defs_deck import *
from scripts.start import *
from scripts.mouse import *

pygame.init()
W,H,sc,clock,fps,font=start()

deck = filling()


up = 1.5
size = (60*up,90*up)


font_color = "black"

g = 0
flRunning = True
while flRunning: 
         

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            flRunning = False
        elif event.type == pygame.KEYDOWN:
            pass
    


    render_background(sc,W,H)
    render_deck(sc,deck,size,font,font_color)  
    
    if(id !=None):
        deck_mouse(pygame.mouse.get_pos(),deck,id)
        refresh(deck,id)
        if(pygame.mouse.get_pressed()[0] != True):
            id = None
        
        
    if(pygame.mouse.get_pressed()[0] and id == None):
        # print("pressed...")
        id = click(deck,pygame.mouse.get_pos(),size)
        
  
#   sc.blit(font.render(str(appleCount)+" apple",1,pygame.Color("white")),(50,50))

        
    
    clock.tick(fps)
    ##print(x,y)
print("end program")
