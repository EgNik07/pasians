import pygame
def render_background(sc,W,H):
    pygame.display.flip()
    sc.fill(pygame.Color('black'))

    img_surf = pygame.image.load('img\\background.jpg')
    img_rect = img_surf.get_rect(bottomright=(W, H))
    sc.blit(img_surf, img_rect)
def render_deck(sc,deck,size,font,font_color):
    card_bakc =  pygame.transform.scale(pygame.image.load('img\\card_back.jpg'),size)
    for j in deck:
            sc.blit(card_bakc, (j.x, j.y))   
            # pygame.draw.rect(sc,pygame.Color(card_color),(j.x,j.y,*size))   
            if(j.special == "ace"):
                if(j.suit == "spades"):
                    sc.blit(font.render("T",2,pygame.Color("black")),(j.x+35,j.y+50))
                elif(j.suit == "hearts"):
                    sc.blit(font.render("T",2,pygame.Color("red")),(j.x+35,j.y+50))
                elif(j.suit == "diamonds"):
                        sc.blit(font.render("T",2,pygame.Color("red")),(j.x+35,j.y+50))
                elif(j.suit == "clubs"):
                        sc.blit(font.render("T",2,pygame.Color("black")),(j.x+35,j.y+50))
                
            elif(j.special == "jack"):
                if(j.suit == "spades"):
                    sc.blit(font.render("J",2,pygame.Color("black")),(j.x+35,j.y+50))
                elif(j.suit == "hearts"):
                    sc.blit(font.render("J",2,pygame.Color("red")),(j.x+35,j.y+50))
                elif(j.suit == "diamonds"):
                        sc.blit(font.render("J",2,pygame.Color("red")),(j.x+35,j.y+50))
                elif(j.suit == "clubs"):
                        sc.blit(font.render("J",2,pygame.Color("black")),(j.x+35,j.y+50))
                
            elif(j.special == "lady"):
                if(j.suit == "spades"):
                    sc.blit(font.render("L",2,pygame.Color("black")),(j.x+35,j.y+50))
                elif(j.suit == "hearts"):
                    sc.blit(font.render("L",2,pygame.Color("red")),(j.x+35,j.y+50))
                elif(j.suit == "diamonds"):
                        sc.blit(font.render("L",2,pygame.Color("red")),(j.x+35,j.y+50))
                elif(j.suit == "clubs"):
                        sc.blit(font.render("L",2,pygame.Color("black")),(j.x+35,j.y+50))
                
            elif(j.special == "king"):
                if(j.suit == "spades"):
                    sc.blit(font.render("K",2,pygame.Color("black")),(j.x+35,j.y+50))
                elif(j.suit == "hearts"):
                    sc.blit(font.render("K",2,pygame.Color("red")),(j.x+35,j.y+50))
                elif(j.suit == "diamonds"):
                        sc.blit(font.render("K",2,pygame.Color("red")),(j.x+35,j.y+50))
                elif(j.suit == "clubs"):
                        sc.blit(font.render("K",2,pygame.Color("black")),(j.x+35,j.y+50))
                
            

            suite_coo = [(j.x+20,j.y+35),(j.x+55,j.y+35),(j.x+20,j.y+70),(j.x+55,j.y+70)]
            if(j.special ==None and j.suit == "spades"):
                sc.blit(font.render(str(j.n),2,pygame.Color("black")),(j.x+10,j.y+5))
                sc.blit(font.render(str(j.n),2,pygame.Color("black")),(j.x+70,j.y+5))
                sc.blit(font.render(str(j.n),2,pygame.Color("black")),(j.x+10,j.y+95))
                sc.blit(font.render(str(j.n),2,pygame.Color("black")),(j.x+70,j.y+95))

                sc.blit(font.render("S",2,pygame.Color("black")),suite_coo[0])
                sc.blit(font.render("S",2,pygame.Color("black")),suite_coo[1])
                sc.blit(font.render("S",2,pygame.Color("black")),suite_coo[2])
                sc.blit(font.render("S",2,pygame.Color("black")),suite_coo[3])
               
            elif(j.special ==None and j.suit == "hearts"):
                sc.blit(font.render(str(j.n),2,pygame.Color("red")),(j.x+10,j.y+5))
                sc.blit(font.render(str(j.n),2,pygame.Color("red")),(j.x+70,j.y+5))
                sc.blit(font.render(str(j.n),2,pygame.Color("red")),(j.x+10,j.y+95))
                sc.blit(font.render(str(j.n),2,pygame.Color("red")),(j.x+70,j.y+95))

                sc.blit(font.render("H",2,pygame.Color("red")),suite_coo[0])
                sc.blit(font.render("H",2,pygame.Color("red")),suite_coo[1])
                sc.blit(font.render("H",2,pygame.Color("red")),suite_coo[2])
                sc.blit(font.render("H",2,pygame.Color("red")),suite_coo[3])
            elif(j.special ==None and j.suit == "diamonds"):
                sc.blit(font.render(str(j.n),2,pygame.Color("red")),(j.x+10,j.y+5))
                sc.blit(font.render(str(j.n),2,pygame.Color("red")),(j.x+70,j.y+5))
                sc.blit(font.render(str(j.n),2,pygame.Color("red")),(j.x+10,j.y+95))
                sc.blit(font.render(str(j.n),2,pygame.Color("red")),(j.x+70,j.y+95))

                sc.blit(font.render("D",2,pygame.Color("red")),suite_coo[0])
                sc.blit(font.render("D",2,pygame.Color("red")),suite_coo[1])
                sc.blit(font.render("D",2,pygame.Color("red")),suite_coo[2])
                sc.blit(font.render("D",2,pygame.Color("red")),suite_coo[3])
            elif(j.special ==None and j.suit == "clubs"):
                sc.blit(font.render(str(j.n),2,pygame.Color("black")),(j.x+10,j.y+5))
                sc.blit(font.render(str(j.n),2,pygame.Color("black")),(j.x+70,j.y+5))
                sc.blit(font.render(str(j.n),2,pygame.Color("black")),(j.x+10,j.y+95))
                sc.blit(font.render(str(j.n),2,pygame.Color("black")),(j.x+70,j.y+95))

                sc.blit(font.render("C",2,pygame.Color("black")),suite_coo[0])
                sc.blit(font.render("C",2,pygame.Color("black")),suite_coo[1])
                sc.blit(font.render("C",2,pygame.Color("black")),suite_coo[2])
                sc.blit(font.render("C",2,pygame.Color("black")),suite_coo[3])
                
                
