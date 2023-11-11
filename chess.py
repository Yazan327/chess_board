from colorama import init, Fore, Back, Style
from random import randint




def inbord(pos) ->tuple:
    return 0< pos[0]<=8 and 0< pos[1]<=8


# Rook sets
def rook_ther_are_movse(pos1,army) :      #tre

    return any([
                   all([(pos1[0]-1,pos1[1]) not in army.keys() , 0<(pos1[0]-1)<=8]), 
                   all([ (pos1[0]+1,pos1[1]) not in army.keys() , 0<(pos1[0]+1)<=8]),
                   all([ (pos1[0],pos1[1]-1) not in army.keys() , 0<(pos1[1]-1)<=8]),
                   all([(pos1[0],pos1[1]+1) not in army.keys() , 0<(pos1[1]+1)<=8])
                    ])
    

def rook_right_move(pos1,pos2):
        
        return any([pos1[0]==pos2[0],pos1[1]==pos2[1]])
    
def rook_can_move(pos1,pos2,army,army1)   :          
        if pos2 in army.keys():
            return False
        elif pos2[1]>pos1[1]:

            for i in range(pos1[1]+1,pos2[1]):
                if (pos1[0],i)in army.keys() or (pos1[0],i)in army1.keys():
                    return False
            return True
            
        elif pos2[1]<pos1[1]:
            for i in range(pos1[1]-1,pos2[1],-1):
                if (pos1[0],i)in army.keys() or (pos1[0],i)in army1.keys():
                    return False
            return True
        elif pos2[0]<pos1[0]:
            for i in range(pos1[0]-1,pos2[0]):
                if (i,pos1[1])in army.keys() or (i,pos1[1])in army1.keys():
                    return False
            return True
        else :
            for i in range(pos1[0]+1,pos2[0]):
                if (i,pos1[1])in army.keys() or (i,pos1[1])in army1.keys():
                    return False
            return True

                    
            
        

#Bishop Sets
def Bishop_ther_are_movse(pos1,army):
    x=pos1[0]
    y=pos1[1]
    return any([
        (x-1,y+1) not in army.keys() and inbord((x-1,y+1)),
        (x+1,y+1) not in army.keys() and inbord((x+1,y+1)),
        (x-1,y-1) not in army.keys() and inbord((x-1,y-1)),
        (x-1,y-1) not in army.keys() and inbord((x-1,y-1))

    ])

def Bishop_right_move(pos1,pos2) ->tuple:
    x1=pos1[0]
    y1=pos1[1]
    x2=pos2[0]
    y2=pos2[1]
    return any([x1-y1==x2-y2,x1+y1==x2+y2])
def Bishop_can_move(pos1,pos2,army,army1):
    x1=pos1[0]
    y1=pos1[1]
    x2=pos2[0]
    y2=pos2[1]
    if (x2,y2) in army.keys():
        return False
    elif y2<y1 and y2-x2 == y1 -x1:
        x=x1
        y=y1
        while x>x2 and y>y2:
            x-=1
            y-=1
            if (x,y)==(x2,y2):
                return True
            elif any([
                (x,y) in army.keys(),
                (x,y) in army1.keys()
                ]):
                return False
        return True
    elif y2<y1 and y2+x2 == y1 +x1:
        x=x1
        y=y1
        while x<x2 and y>y2:
            x+=1
            y-=1
            if (x,y)==(x2,y2):
                return True
            else:
                if any([
                 (x,y) in army.keys(),
                 (x,y) in army1.keys()
                 ]):
                 return False
        return True
    elif y2>y1 and y2+x2 == y1 +x1:
        x=x1
        y=y1
        while x>x2 and y<y2:
            x-=1
            y+=1
            if (x,y)==(x2,y2):
                return True
            elif any([
                (x,y) in army.keys(),
                (x,y) in army1.keys()
                ]):
                return False
        return True
    else    :        # y2>y1 and y2+x2 == y1 +x1:
        x=x1
        y=y1
        while x<x2 and y<y2:
            x+=1
            y+=1
            if (x,y)==(x2,y2):
                return True
            elif any([
                (x,y) in army.keys(),
                (x,y) in army1.keys()
                ]):
                return False
        return True



#pawn sets
def pawn_ther_are_movse(pos1,black,army,army1):
    x1=pos1[0]
    y1=pos1[1]

    if black:

      return any([
          
      (x1+1,y1-1) in army1.keys(),
      (x1-1,y1-1) in army1.keys(),
      (x1,y1-1) not in army.keys()
            ])
    else:
      return any([
          
      (x1+1,y1+1) in army1.keys(),
      (x1-1,y1+1) in army1.keys(),
      (x1,y1+1) not in army.keys()
            ])
def pawn_right_move(pos1,pos2,movments,black) :
    if black:
        return any([
              pos2[1]==pos1[1]-2 and pos2[0]==pos1[0] and not movments,
              pos2[1]==pos1[1]-1  and pos2[0]==pos1[0] ,
              pos2[0]==pos1[0]-1 and pos2[1]==pos1[1]-1,
              pos2[0]==pos1[0]+1 and pos2[1]==pos1[1]-1
               
                ])
    else:
        return any([
              pos2[1]==pos1[1]+2 and pos2[0]==pos1[0] and not movments,
              pos2[1]==pos1[1]+1  and pos2[0]==pos1[0] ,
              pos2[0]==pos1[0]-1 and pos2[1]==pos1[1]+1,
              pos2[0]==pos1[0]+1 and pos2[1]==pos1[1]+1
               
                ])
def pawn_can_move(pos1,pos2,black,army,army1):
    
    if black:
        return any([
              pos2[1]==pos1[1]-2 and pos2[0]==pos1[0]   and (pos1[0],pos1[1]-1) not in army.keys() and(pos1[0],pos1[1]-1) not in army1.keys() and pos2 not in army.keys() and pos2 not in army1.keys(),
              pos2[1]==pos1[1]-1 and pos2[0]==pos1[0]   and (pos1[0],pos1[1]-1) not in army.keys() and pos2 not in army.keys()and pos2 not in army1.keys(),
              pos2[0]==pos1[0]-1 and pos2[1]==pos1[1]-1 and (pos1[0]-1,pos1[1]-1) in army1.keys() ,
              pos2[0]==pos1[0]+1 and pos2[1]==pos1[1]-1 and (pos1[0]+1,pos1[1]-1) in army1.keys()          
        ])
    else:
        return any([
              pos2[1]==pos1[1]+2 and pos2[0]==pos1[0]   and (pos1[0],pos1[1]+1) not in army.keys() and(pos1[0],pos1[1]+1) not in army1.keys() and pos2 not in army.keys() and pos2 not in army1.keys(),
              pos2[1]==pos1[1]+1 and pos2[0]==pos1[0]   and (pos1[0],pos1[1]+1) not in army.keys() and pos2 not in army.keys() and pos2 not in army1.keys(),
              pos2[0]==pos1[0]-1 and pos2[1]==pos1[1]+1 and (pos1[0]-1,pos1[1]+1) in army1.keys() ,
              pos2[0]==pos1[0]+1 and pos2[1]==pos1[1]+1 and (pos1[0]+1,pos1[1]+1) in army1.keys()          
        ])

#Knight Sets
def Knight_ther_are_movse(pos1,army):
    x=pos1[0]
    y=pos1[1]

    return any([
        (x+1,y+2) not in army.keys() and inbord((x+1,y+2)),
        (x-1,y+2) not in army.keys() and inbord((x-1,y+2)),
        (x-1,y-2) not in army.keys() and inbord((x-1,y-2)),
        (x+1,y-2) not in army.keys() and inbord((x+1,y-2)),
        (x-2,y+1) not in army.keys() and inbord((x-2,y+1)),
        (x-2,y-1) not in army.keys() and inbord((x-2,y-1)),
        (x+2,y-1) not in army.keys() and inbord((x+2,y-1)),
        (x+2,y+1) not in army.keys() and inbord((x+2,y+1))


             ])

def Knight_right_move(pos1,pos2) ->tuple:
    x1=pos1[0]
    y1=pos1[1]
    x2=pos2[0]
    y2=pos2[1]
    return any([
        y2==y1+2 and any([x2==x1+1,x2==x1-1]),
        y2==y1-2 and any([x2==x1+1,x2==x1-1]),
        x2==x1-2 and any([y2==y1+1,y2==y1-1]),
        x2==x1+2 and any([y2==y1+1,y2==y1-1])


             ])

    


#Queen Sets 
def Queen_ther_are_movse(pos1,army):
    x=pos1[0]
    y=pos1[1]
    return any([
        (x-1,y+1) not in army.keys(),
        (x+1,y+1) not in army.keys(),
        (x-1,y-1) not in army.keys(),
        (x-1,y-1) not in army.keys(),
        all([(pos1[0]-1,pos1[1]) not in army.keys() , 0<(pos1[0]-1)<=8]), 
        all([ (pos1[0]+1,pos1[1]) not in army.keys() , 0<(pos1[0]+1)<=8]),
        all([ (pos1[0],pos1[1]-1) not in army.keys() , 0<(pos1[1]-1)<=8]),
        all([(pos1[0],pos1[1]+1) not in army.keys() , 0<(pos1[1]+1)<=8])
    ])


def Queen_right_move(pos1,pos2) ->tuple:
    x1=pos1[0]
    y1=pos1[1]
    x2=pos2[0]
    y2=pos2[1]
    return any([
        pos1[0]==pos2[0],
        pos1[1]==pos2[1],
        y1-x1==y2-x2,
        x1+y1==x2+y2

        ])

def Queen_can_move(pos1,pos2,army,army1):
        x1=pos1[0]
        y1=pos1[1]
        x2=pos2[0]
        y2=pos2[1]
        if pos2 in army.keys():
            return False

        elif y2<y1 and y2-x2 == y1 -x1:
            x=x1
            y=y1
            while x>x2 and y>y2:
                x-=1
                y-=1
                if (x,y)==(x2,y2):
                    return True
                elif any([
                    (x,y) in army.keys(),
                    (x,y) in army1.keys()
                    ]):
                    return False
            return True
        elif y2<y1 and y2+x2 == y1 +x1:
            x=x1
            y=y1
            while x<x2 and y>y2:
                x+=1
                y-=1
                if (x,y)==(x2,y2):
                    return True
                else:
                    if any([
                    (x,y) in army.keys(),
                    (x,y) in army1.keys()
                    ]):
                     return False
            return True
        elif y2>y1 and y2+x2 == y1 +x1:
            x=x1
            y=y1
            while x>x2 and y<y2:
                x-=1
                y+=1
                if (x,y)==(x2,y2):
                    return True
                elif any([
                    (x,y) in army.keys(),
                    (x,y) in army1.keys()
                    ]):
                    return False
            return True
        elif y2>y1 and y2-x2 == y1 -x1:
            x=x1
            y=y1
            while x<x2 and y<y2:
                x+=1
                y+=1
                if (x,y)==(x2,y2):
                    return True
                elif any([
                    (x,y) in army.keys(),
                    (x,y) in army1.keys()
                    ]):
                    return False
            return True
        elif pos2[1]>pos1[1]:

            for i in range(pos1[1]+1,pos2[1]):
                if (pos1[0],i)in army.keys() or (pos1[0],i)in army1.keys():
                    return False
            return True
            
        elif pos2[1]<pos1[1]:
            for i in range(pos1[1]-1,pos2[1],-1):
                if (pos1[0],i)in army.keys() or (pos1[0],i)in army1.keys():
                    return False
            return True
        elif pos2[0]<pos1[0]:
            for i in range(pos1[0]-1,pos2[0]):
                if (i,pos1[1])in army.keys() or (i,pos1[1])in army1.keys():
                    return False
            return True
        elif pos2[0]>pos1[0]:
            for i in range(pos1[0]+1,pos2[0]):
                if (i,pos1[1])in army.keys() or (i,pos1[1])in army1.keys():
                    return False
            return True
        else:
            return False


#King Sets
def King_ther_are_movse(pos1,army):
    x=pos1[0]
    y=pos1[1]
    return any([
        (x-1,y+1)not in army.keys() and inbord((x-1,y+1)),
        (x+1,y+1)not in army.keys() and inbord((x+1,y+1)),
        (x-1,y-1)not in army.keys() and inbord((x-1,y-1)),
        (x+1,y-1)not in army.keys() and inbord((x+1,y-1)),
        (x,y-1)not in army.keys() and inbord((x+1,y-1)),
        (x,y+1)not in army.keys() and inbord((x+1,y+1)),
        (x-1,y)not in army.keys() and inbord((x-1,y)),
        (x+1,y)not in army.keys() and inbord((x+1,y))
  

    ])
def King_right_move(pos1,pos2) ->tuple:
    x1=pos1[0]
    y1=pos1[1]
    x2=pos2[0]
    y2=pos2[1]
    return any([x2==x1-1 and y2==y1+1,
                x2== x1+1 and y2==y1+1,
                x2==x1-1 and y2==y1-1,
                x2==x1+1 and y2==y1-1,
                x2==x1 and any([y2-y1==1,y1-y2==1]),
                y2==y1 and any([x2-x1==1,x1-x2==1])
                ])
def King_can_move(pos2,army):
    if pos2 in army.keys():
        return False
    else:
        return True

def king_freeToMove(pos2,army,army1,black):
    for location ,soljer  in army1.items():
        if soljer[0:4]=='rook':
            if rook_right_move(location,pos2):
                if rook_can_move(location,pos2,army1,army):
                    return False
            
        elif soljer[0:6]=='Bishop':    
            if Bishop_right_move(location,pos2):
                if Bishop_can_move(location,pos2,army1,army):
                    return False
        elif soljer[0:6]=='Knight':    
            if Knight_right_move(location,pos2):
                
                 return False

        elif soljer=='Queen':    
            if Queen_right_move(location,pos2):
                if Queen_can_move(location,pos2,army1,army):
                    return False
        elif soljer=='king':
            if King_right_move(location,pos2):
                if King_can_move(location,pos2,army1):
                    return False
        else:
            
            
            if pawn_right_move(location,pos2,1,black):
                    return False                
    return True

white_army={
        'pawn1':{
            'Movements':0,'posatios':(1,2),'active':True},
        'pawn2':{
            'Movements':0,'posatios':(2,2),'active':True},
        'pawn3':{
            'Movements':0,'posatios':(3,2),'active':True},
        'pawn4':{
            'Movements':0,'posatios':(4,2),'active':True},
        'pawn5':{
            'Movements':0,'posatios':(5,2),'active':True},
        'pawn6':{
            'Movements':0,'posatios':(6,2),'active':True},
        'pawn7':{
            'Movements':0,'posatios':(7,2),'active':True},
        'pawn8':{
            'Movements':0,'posatios':(8,2),'active':True},
        'rook1':{
            'Movements':0,'posatios':(1,1),'active':True},
        'rook2':{
            'Movements':0,'posatios':(8,1),'active':True},
        'Knight1':{
            'Movements':0,'posatios':(2,1),'active':True},
        'Knight2':{
            'Movements':0,'posatios':(7,1),'active':True},
        'Bishop1':{
            'Movements':0,'posatios':(3,1),'active':True},
        'Bishop2':{
            'Movements':0,'posatios':(6,1),'active':True},
        'Queen':{
            'Movements':0,'posatios':(4,1),'active':True},
        'king':{
            'Movements':0,'posatios':(5,1),'active':True}

}
black_army={
        'pawn1':{
            'Movements':0,'posatios':(1,7),'active':True},
        'pawn2':{
            'Movements':0,'posatios':(2,7),'active':True},
        'pawn3':{
            'Movements':0,'posatios':(3,7),'active':True},
        'pawn4':{
            'Movements':0,'posatios':(4,7),'active':True},
        'pawn5':{
            'Movements':0,'posatios':(5,7),'active':True},
        'pawn6':{
            'Movements':0,'posatios':(6,7),'active':True},
        'pawn7':{
            'Movements':0,'posatios':(7,7),'active':True},
        'pawn8':{
            'Movements':0,'posatios':(8,7),'active':True},
        'rook1':{
            'Movements':0,'posatios':(1,8),'active':True},
        'rook2':{
            'Movements':0,'posatios':(8,8),'active':True},
        'Knight1':{
            'Movements':0,'posatios':(2,8),'active':True},
        'Knight2':{
            'Movements':0,'posatios':(7,8),'active':True},
        'Bishop1':{
            'Movements':0,'posatios':(3,8),'active':True},
        'Bishop2':{
            'Movements':0,'posatios':(6,8),'active':True},
        'Queen':{
            'Movements':0,'posatios':(4,8),'active':True},
        'king':{
            'Movements':0,'posatios':(5,8),'active':True}

}

def is_empty(pos) ->tuple:
    status=True
    for key,value in black_army.items():
        if value['posatios']==pos:
            status=False
            return status
    for key,value in white_army.items():
        if value['posatios']==pos:
            status=False
            return status
           
    return status

def real_time_bord(white,black)->dict:
    for y in range(8,0,-1):
        
        for x in range(1,9):
            
            
            try:
                lenwhite=9-(len(white[(x,y)]))
                print(Fore.WHITE+Style.BRIGHT+white[(x,y)],lenwhite*" ",end="   ")
            except Exception:
                try:
                    lenblack=9-(len(black[(x,y)]))
                    print(Fore.BLACK+black[(x,y)],lenblack*" ",end="   ")
                except Exception:
                    if (y+x)%2==0:
                        print(f"{Fore.BLUE}{(x,y)}",3*" ",end="   ")
                    else:
                        print(f"{Fore.LIGHTGREEN_EX}{(x,y)}",3*" ",end="   ")
        print("\n\n\n")
    

#> POSATIONS CHANGE

def black_posation_chang(black) ->dict:
    #black army sort
    posatios_values= black.values()
    army_keys=black.keys()
    black_army_posatios={}
    for key,value in zip(army_keys,posatios_values):
        if value["active"]:
         black_army_posatios[value['posatios']]=key
    
    return black_army_posatios

def white_posation_chang(white) ->dict:
    #white army sort
    posatios_values= white.values()
    army_keys=white.keys()
    white_army_posatios={}
    for key,value in zip(army_keys,posatios_values):
        if value["active"]:
            white_army_posatios[value['posatios']]=key
    return white_army_posatios

black_out=[]
white_out=[]
round= randint(0,1)
while True:
    
    whiteposation=white_posation_chang(white_army)
    blackposation=black_posation_chang(black_army)
    print("White Out :", white_out,'\n')
    real_time_bord(whiteposation,blackposation)
    print("Black Out :",black_out)
    #if black round
    pos1=None
    pos2=None 
    if round:
        print("Black Round ")

        while round:
            print("Enter The Terrier Location:")
            #chose the right solger
            while True:
                pos1=(int(input()),int(input()))
                if inbord(pos1):
                    break
                else:
                    print("The location Out The Borde")
            if pos1 in blackposation.keys():
                soljer=blackposation[pos1]
                if soljer[0:4]=='rook':
                    
                    if rook_ther_are_movse(pos1,blackposation) :
                       
                       while True:
                        print("Enter The New  Location ")
                        while True:
                            pos2=(int(input()),int(input()))
                            if inbord(pos2):
                                break
                            else:
                                print("The location Out The Borde,try again")

                        if rook_right_move(pos1,pos2):
                            if rook_can_move(pos1,pos2,blackposation,whiteposation):
                                black_army[blackposation[pos1]]['posatios']=pos2
                                if pos2 in whiteposation.keys():
                                    white_army[whiteposation[pos2]]['active']=False
                                    white_out.append(whiteposation[pos2])
                                round=0
                                break
                            else:
                                print("Wrong Move ,Try Again")    
                                  
                        else:
                            print("Wrong Move for The Rook ")

                    else:
                       print("there are no movse")
                elif soljer[0:6]=='Bishop':
                    if Bishop_ther_are_movse(pos1,blackposation) :
                       
                       while True:
                        print("Enter The New  Location ")
                        while True:
                            pos2=(int(input()),int(input()))
                            if inbord(pos2):
                                break
                            else:
                                print("The location Out The Borde,try again")

                        if Bishop_right_move(pos1,pos2):
                            if Bishop_can_move(pos1,pos2,blackposation,whiteposation):
                                black_army[blackposation[pos1]]['posatios']=pos2
                                if pos2 in whiteposation.keys():
                                    white_army[whiteposation[pos2]]['active']=False
                                    white_out.append(whiteposation[pos2])
                                round=0
                                break
                            else:
                                print("Wrong Move ,Try Again")    
                                  
                        else:
                            print("Wrong Move for The Bishop ")

                    else:
                       print("there are no movse")
                elif soljer[0:4]=='pawn':
                    if pawn_ther_are_movse(pos1,1,blackposation,whiteposation) :
                       
                       while True:
                        print("Enter The New  Location ")
                        while True:
                            pos2=(int(input()),int(input()))
                            if inbord(pos2):
                                break
                            else:
                                print("The location Out The Borde,try again")
                        movments=black_army[blackposation[pos1]]['Movements']
                        if pawn_right_move(pos1,pos2,movments,1):
                            if pawn_can_move(pos1,pos2,1,blackposation,whiteposation):
                                black_army[blackposation[pos1]]['posatios']=pos2
                                if pos2 in whiteposation.keys():
                                    white_army[whiteposation[pos2]]['active']=False
                                    white_out.append(whiteposation[pos2])
                                round=0
                                break
                             
                            else:
                                 print("Wrong Move ,Try Again")    
                        
                           
                        else:
                            print("Wrong Move for The Pawn ")
                    else:
                       print("there are no movse") 
                elif soljer[0:6]=='Knight':
                    if Knight_ther_are_movse(pos1,blackposation) :
                       
                       while True:
                        print("Enter The New  Location ")
                        while True:
                            pos2=(int(input()),int(input()))
                            if inbord(pos2):
                                break
                            else:
                                print("The location Out The Borde,try again")

                        if Knight_right_move(pos1,pos2):
                            
                            black_army[blackposation[pos1]]['posatios']=pos2
                            if pos2 in whiteposation.keys():
                                white_army[whiteposation[pos2]]['active']=False
                                white_out.append(whiteposation[pos2])
                            round=0
                            break
                             
                            
                        
                           
                        else:
                            print("Wrong Move for The Knight ")
                    else:
                       print("there are no movse") 
                elif soljer=='Queen':
                    if Queen_ther_are_movse(pos1,blackposation) :
                       
                       while True:
                        print("Enter The New  Location ")
                        while True:
                            pos2=(int(input()),int(input()))
                            if inbord(pos2):
                                break
                            else:
                                print("The location Out The Borde,try again")

                        if Queen_right_move(pos1,pos2):
                            if Queen_can_move(pos1,pos2,blackposation,whiteposation):
                                black_army[blackposation[pos1]]['posatios']=pos2
                                if pos2 in whiteposation.keys():
                                    white_army[whiteposation[pos2]]['active']=False
                                    white_out.append(whiteposation[pos2])
                                round=0
                                break
                            else:
                                print("Wrong Move ,Try Again")    
                                  
                        else:
                            print("Wrong Move for The Queen ")

                    else:
                       print("there are no movse")
                else:
                    if King_ther_are_movse(pos1,blackposation) :
                       
                       while True:
                        print("Enter The New  Location ")
                        while True:
                            pos2=(int(input()),int(input()))
                            if inbord(pos2):
                                break
                            else:
                                print("The location Out The Borde,try again")

                        if King_right_move(pos1,pos2):
                            if King_can_move(pos2,blackposation):
                                if king_freeToMove(pos2,blackposation,whiteposation,0):
                                    black_army[blackposation[pos1]]['posatios']=pos2
                                    if pos2 in whiteposation.keys():
                                        white_army[whiteposation[pos2]]['active']=False
                                        white_out.append(whiteposation[pos2])
                                    round=0
                                    break
                                else:
                                    print("Subscription patch")
                            else:
                                print("Wrong Move ,Try Again")    
                                  
                        else:
                            print("Wrong Move for The king ")

                    else:
                       print("there are no movse")                    
            elif pos1 in whiteposation.keys():
                print("You cannot move white pieces")
            else:
                print("There Is No Pieces In This Place ")




    


    # if white army
    else:
        print("White Round ")   
        while not round:
            print("Enter The Terrier Location:")
            #chose the right solger
            while True:
                pos1=(int(input()),int(input()))
                if inbord(pos1):
                    break
                else:
                    print("The location Out The Borde")
            if pos1 in whiteposation.keys():
                soljer=whiteposation[pos1]
                if soljer[0:4]=='rook':
                    
                    if rook_ther_are_movse(pos1,whiteposation) :
                       
                       while True:
                        print("Enter The New  Location ")
                        while True:
                            pos2=(int(input()),int(input()))
                            if inbord(pos2):
                                break
                            else:
                                print("The location Out The Borde,try again")

                        if rook_right_move(pos1,pos2):
                            if rook_can_move(pos1,pos2,whiteposation,blackposation):
                                white_army[whiteposation[pos1]]['posatios']=pos2
                                if pos2 in blackposation.keys():
                                    black_army[blackposation[pos2]]['active']=False
                                    black_out.append(blackposation[pos2])
                                round=1
                                break
                            else:
                                print("Wrong Move ,Try Again")    
                                  
                        else:
                            print("Wrong Move for The Rook ")

                    else:
                       print("there are no movse")
                elif soljer[0:6]=='Bishop':
                    if Bishop_ther_are_movse(pos1,whiteposation) :
                       
                       while True:
                        print("Enter The New  Location ")
                        while True:
                            pos2=(int(input()),int(input()))
                            if inbord(pos2):
                                break
                            else:
                                print("The location Out The Borde,try again")

                        if Bishop_right_move(pos1,pos2):
                            if Bishop_can_move(pos1,pos2,whiteposation,blackposation):
                                white_army[whiteposation[pos1]]['posatios']=pos2
                                if pos2 in blackposation.keys():
                                    black_army[blackposation[pos2]]['active']=False
                                    black_out.append(blackposation[pos2])
                                round=1
                                break
                            else:
                                print("Wrong Move ,Try Again")    
                                  
                        else:
                            print("Wrong Move for The Bishop ")

                    else:
                       print("there are no movse")
                elif soljer[0:4]=='pawn':
                    if pawn_ther_are_movse(pos1,0,whiteposation,blackposation) :
                       
                       while True:
                        print("Enter The New  Location ")
                        while True:
                            pos2=(int(input()),int(input()))
                            if inbord(pos2):
                                break
                            else:
                                print("The location Out The Borde,try again")
                        movments=white_army[whiteposation[pos1]]['Movements']
                        if pawn_right_move(pos1,pos2,movments,0):
                            if pawn_can_move(pos1,pos2,0,whiteposation,blackposation):
                               white_army[whiteposation[pos1]]['posatios']=pos2
                               if pos2 in blackposation.keys():
                                    black_army[blackposation[pos2]]['active']=False
                                    black_out.append(blackposation[pos2])
                               round=1
                               break
                             
                            else:
                                 print("Wrong Move ,Try Again")    
                        
                           
                        else:
                            print("Wrong Move for The Pawn ")
                    else:
                       print("there are no movse") 
                elif soljer[0:6]=='Knight':
                    if Knight_ther_are_movse(pos1,whiteposation) :
                       
                       while True:
                        print("Enter The New  Location ")
                        while True:
                            pos2=(int(input()),int(input()))
                            if inbord(pos2):
                                break
                            else:
                                print("The location Out The Borde,try again")
                        
                        if Knight_right_move(pos1,pos2):
                            
                            white_army[whiteposation[pos1]]['posatios']=pos2
                            if pos2 in blackposation.keys():
                                black_army[blackposation[pos2]]['active']=False
                                black_out.append(blackposation[pos2])
                            round=1
                            break
                             
                            
                        
                           
                        else:
                            print("Wrong Move for The Knight ")
                    else:
                       print("there are no movse") 
                elif soljer=='Queen':
                    if Queen_ther_are_movse(pos1,whiteposation) :
                       
                       while True:
                        print("Enter The New  Location ")
                        while True:
                            pos2=(int(input()),int(input()))
                            if inbord(pos2):
                                break
                            else:
                                print("The location Out The Borde,try again")

                        if Queen_right_move(pos1,pos2):
                            if Queen_can_move(pos1,pos2,whiteposation,blackposation):
                                white_army[whiteposation[pos1]]['posatios']=pos2
                                if pos2 in whiteposation.keys():
                                    black_army[blackposation[pos2]]['active']=False
                                    black_out.append(blackposation[pos2])
                                round=1
                                break
                            else:
                                print("Wrong Move ,Try Again")    
                                  
                        else:
                            print("Wrong Move for The Queen ")

                    else:
                       print("there are no movse")
                else:
                    if King_ther_are_movse(pos1,whiteposation) :
                       
                       while True:
                        print("Enter The New  Location ")
                        while True:
                            pos2=(int(input()),int(input()))
                            if inbord(pos2):
                                break
                            else:
                                print("The location Out The Borde,try again")

                        if King_right_move(pos1,pos2):
                            if King_can_move(pos2,whiteposation):
                                if king_freeToMove(pos2,whiteposation,blackposation,1):
                                    white_army[whiteposation[pos1]]['posatios']=pos2
                                    if pos2 in blackposation.keys():
                                        black_army[blackposation[pos2]]['active']=False
                                        black_out.append(blackposation[pos2])
                                    round=1
                                    break
                                else:
                                    print("Subscription patch")
                            else:
                                print("Wrong Move ,Try Again")    
                                  
                        else:
                            print("Wrong Move for The king ")
            elif pos1 in blackposation.keys():
                print("You cannot move black pieces")
            else:
                print("There Is No Pieces In This Place ")
          
    
    

   

