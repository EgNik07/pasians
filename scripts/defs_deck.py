d_x = 100
d_y = 100
import random
class d_card():
    def __init__(self,suit,n,id):
        if(suit == 0):
            self.suit = "spades"
        elif(suit == 1):
            self.suit = "hearts"
        elif(suit == 2):
            self.suit = "diamonds" 
        elif(suit == 3):
            self.suit = "clubs" 
        self.id=id
        self.n = n
        self.special = None
        self.x = d_x
        self.y = d_y
        
class s_card():
    def __init__(self,suit,special,id):
        if(suit == 0):
            self.suit = "spades"
        elif(suit == 1):
            self.suit = "hearts"
        elif(suit == 2):
            self.suit = "diamonds" 
        elif(suit == 3):
            self.suit = "clubs" 


        if(special == 0):
            self.special = "ace"
        elif(special == 1):
            self.special = "jack"
        elif(special == 2):
            self.special = "lady" 
        elif(special == 3):
            self.special = "king" 
        self.id=id
        self.n = None
        self.x = d_x
        self.y = d_y

def filling():
    d=[]
    f=[]  
    id = 0
    for j in range(4):
        f=[] 
        
        for i in range(8): 
            f.append(d_card(j,i+2,id))
            id+=1
        for k in range(4):
            f.append(s_card(j,k,id)) 
            id+=1
        d.append(f)
    dd=[]
    while True:
        for i in d:
            for j in i:
                if(random.randint(0,1)):
                    dd.append(j)
                    h=0
                    for ii in d:
                        w=0
                        for jj in ii:
                            if(j.id==jj.id):
                                d[h].pop(w)   
                            w+=1
                        h+=1

        if(len(d[0])==0 and len(d[1])==0 and len(d[2])==0 and len(d[3])==0):
            return dd

def show_deck(deck):
    for i in deck:
        
        print("[",i.x," ",i.y," | ", i.suit,"]",end="|")
        print("\n")
def refresh(deck,id):
    for i in deck:
        if (i.id == id):
            deck.append(i)
            deck.remove(i)