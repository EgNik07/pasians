import pygame
def start():
    W = 1600
    H = 900
    sc =pygame.display.set_mode((W,H))
    pygame.display.set_caption("Пасьянц")
    pygame.display.set_icon(pygame.image.load("img\\solitaire.jpg"))

    clock = pygame.time.Clock()
    fps = 30
    font = pygame.font.SysFont('Times New Roman',  32)       
    return W,H,sc,clock,fps,font
