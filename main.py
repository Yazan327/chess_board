from colorama import init, Fore, Back, Style
from random import randint
import timeit



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
        (x+1,y-1) not in army.keys() and inbord((x+1,y-1))

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
      (x1,y1-1) not in army.keys() and (x1,y1-1) not in army1.keys()
            ])
    else:
      return any([
          
      (x1+1,y1+1) in army1.keys(),
      (x1-1,y1+1) in army1.keys(),
      (x1,y1+1) not in army.keys() and (x1,y1+1) not in army1.keys()
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

def  king_freeToMove(pos1,pos2,army,army1,black):
    """returns true if the king free to move"""
    army_=army
    
    new_key = pos2
    army_ = {new_key if k == pos1 else k: v for k, v in army.items()}  # need to study
    army1_= { k: v for k, v in army1.items()} 
    if pos2 in army1_.keys():
            del army1_[pos2]

    for location ,solder  in army1_.items():

        if solder[0:4]=='rook':
            if rook_right_move(location,pos2):
                if rook_can_move(location,pos2,army1_,army_):
                    return False
            
        elif solder[0:6]=='Bishop':    
            if Bishop_right_move(location,pos2):
                if Bishop_can_move(location,pos2,army1_,army_):
                    return False
        elif solder[0:6]=='Knight':    
            if Knight_right_move(location,pos2):
                
                 return False

        elif solder=='Queen':    
            if Queen_right_move(location,pos2):
                if Queen_can_move(location,pos2,army1_,army_):
                    return False
        elif solder=='king':
            if King_right_move(location,pos2):
                if King_can_move(location,pos2,army1_):
                    return False
        else:
            
           
            if pawn_can_move(location,pos2,black,army1_,army_):
                    
                        return False                   
    return True


#King's Protacter

def king_protected(pos1,pos2,army,army1,black,king):
    army2=army
    
    new_key = pos2
    army2 = {new_key if k == pos1 else k: v for k, v in army.items()}  # need to study


    for location ,solder  in army1.items():
        if solder[0:4]=='rook':
            if rook_right_move(location,king):
                if rook_can_move(location,king,army1,army2):
                    return False
            
        elif solder[0:6]=='Bishop':    
            if Bishop_right_move(location,king):
                if Bishop_can_move(location,king,army1,army2):
                    return False
                
        elif solder[0:6]=='Knight':    
            if Knight_right_move(location,king):
                
                 return False

        elif solder=='Queen':    
            if Queen_right_move(location,king):
                if Queen_can_move(location,king,army1,army2):
                    return False
                
        elif solder=='king':
            if King_right_move(location,king):
                if King_can_move(location,king,army2):
                    return False
                
        else:
            
            
            if pawn_right_move(location,king,1,black):
                     return False                   
    return True

def King_protector_allways(pos1,army,army1,black,king):
        """returns true if all the movse of this solder maks the king unsafe"""
        x=pos1[0]
        y=pos1[1]
        Solder=army[pos1]

        if Solder[0:4]=='rook':
               
               
                for y1 in range(y+1,9):
                    if (x,y1) not in army.keys() and king_protected(pos1,(x,y1),army,army1,black,king):
                        return False
                    
                    if (x,y1) in army.keys() or (x,y1) in  army1.keys()  :
                        break


                for y1 in range(y-1,0,-1):
                    if (x,y1) not in army.keys() and king_protected(pos1,(x,y1),army,army1,black,king):
                        return False
                    
                    if (x,y1) in army.keys() or (x,y1) in  army1.keys()  :
                        break



                for x1 in range(x+1,9):
                    if (x1,y) not in army.keys() and king_protected(pos1,(x1,y),army,army1,black,king):
                        return False
                    
                    if (x1,y) in army.keys() or (x1,y) in  army1.keys()  :
                        break                    

                for x1 in range(x-1,0,-1):
                    if (x1,y) not in army.keys() and king_protected(pos1,(x1,y),army,army1,black,king):
                        return False
                    
                    if (x1,y) in army.keys() or (x1,y) in  army1.keys()  :
                        break                    
                             
            
                return True
  
                    
     
        elif Solder[0:6]=='Bishop':    

                  
                x=pos1[0]
                y=pos1[1]
                x1=x
                y1=y
                while True:
                    x1+=1
                    y1+=1
                    if (x1,y1) in army.keys():
                        break
                    if (x1,y1) not in army.keys() and king_protected(pos1,(x1,y1),army,army1,black,king):
                        return False
                    if (x1,y1) in army1.keys():
                        break
                    if x1>=8 or y1>=8:
                        break

                x1=x
                y1=y
                while True:
                    x1-=1
                    y1-=1
                    if (x1,y1) in army.keys():
                        break
                    if (x1,y1) not in army.keys() and king_protected(pos1,(x1,y1),army,army1,black,king):
                        return False
                    if (x1,y1) in army1.keys():
                        break
                    if x1<=8 or y1<=1:
                        break                
                x1=x
                y1=y
                while True:
                    x1+=1
                    y1-=1
                    if (x1,y1) in army.keys():
                        break
                    if (x1,y1) not in army.keys() and king_protected(pos1,(x1,y1),army,army1,black,king):
                        return False
                    if (x1,y1) in army1.keys():
                        break
                    if x1>=8 or y1<=1:
                        break                
                x1=x
                y1=y
                while True:
                    x1-=1
                    y1+=1
                    if (x1,y1) in army.keys():
                        break
                    if (x1,y1) not in army.keys() and king_protected(pos1,(x1,y1),army,army1,black,king):
                        return False
                    if (x1,y1) in army1.keys():
                        break
                    if x1<=1 or y1>=8:
                        break                



                return True
                

        elif Solder[0:6]=='Knight':    
                x=pos1[0]
                y=pos1[1]

                if any([
                    (x+1,y+2) not in army.keys() and inbord((x+1,y+2))and king_protected(pos1,(x+1,y+2),army,army1,black,king),
                    (x-1,y+2) not in army.keys() and inbord((x-1,y+2))and king_protected(pos1,(x-1,y+2),army,army1,black,king),
                    (x-1,y-2) not in army.keys() and inbord((x-1,y-2))and king_protected(pos1,(x-1,y-2),army,army1,black,king),
                    (x+1,y-2) not in army.keys() and inbord((x+1,y-2))and king_protected(pos1,(x+1,y-2),army,army1,black,king),
                    (x-2,y+1) not in army.keys() and inbord((x-2,y+1))and king_protected(pos1,(x-2,y+1),army,army1,black,king),
                    (x-2,y-1) not in army.keys() and inbord((x-2,y-1))and king_protected(pos1,(x-2,y-1),army,army1,black,king),
                    (x+2,y-1) not in army.keys() and inbord((x+2,y-1))and king_protected(pos1,(x+2,y-1),army,army1,black,king),
                    (x+2,y+1) not in army.keys() and inbord((x+2,y+1))and king_protected(pos1,(x+2,y+1),army,army1,black,king)


                    ]):
                    return False
                else:
                    return True
            
        elif Solder=='Queen':    
    
                x=pos1[0]
                y=pos1[1]
                #take the rook sets
                for y1 in range(y+1,9):
                    if (x,y1) not in army.keys() and king_protected(pos1,(x,y1),army,army1,black,king):
                        return False
                    
                    if (x,y1) in army.keys() or (x,y1) in  army1.keys()  :
                        break


                for y1 in range(y-1,0,-1):
                    if (x,y1) not in army.keys() and king_protected(pos1,(x,y1),army,army1,black,king):
                        return False
                    
                    if (x,y1) in army.keys() or (x,y1) in  army1.keys()  :
                        break



                for x1 in range(x+1,9):
                    if (x1,y) not in army.keys() and king_protected(pos1,(x1,y),army,army1,black,king):
                        return False
                    
                    if (x1,y) in army.keys() or (x1,y) in  army1.keys()  :
                        break                    

                for x1 in range(x-1,0,-1):
                    if (x1,y) not in army.keys() and king_protected(pos1,(x1,y),army,army1,black,king):
                        return False
                    
                    if (x1,y) in army.keys() or (x1,y) in  army1.keys()  :
                        break         
               
                #take the bishop sets        
                x1=x
                y1=y
                while True:
                    x1+=1
                    y1+=1
                    if (x1,y1) in army.keys():
                        break
                    if (x1,y1) not in army.keys() and king_protected(pos1,(x1,y1),army,army1,black,king):
                        return False
                    if (x1,y1) in army1.keys():
                        break
                    if x1>=8 or y1>=8:
                        break

                x1=x
                y1=y
                while True:
                    x1-=1
                    y1-=1
                    if (x1,y1) in army.keys():
                        break
                    elif (x1,y1) not in army.keys() and king_protected(pos1,(x1,y1),army,army1,black,king):
                        return False
                    elif (x1,y1) in army1.keys():
                        break
                    if x1<=8 or y1<=1:
                        break                
                x1=x
                y1=y
                while True:
                    x1+=1
                    y1-=1
                    if (x1,y1) in army.keys():
                        break
                    if (x1,y1) not in army.keys() and king_protected(pos1,(x1,y1),army,army1,black,king):
                        return False
                    if (x1,y1) in army1.keys():
                        break
                    if x1<=8 or y1<=1:
                        break       



                x1=x
                y1=y
                while True:
                    x1-=1
                    y1+=1
                    if (x1,y1) in army.keys():
                        break
                    if (x1,y1) not in army.keys() and king_protected(pos1,(x1,y1),army,army1,black,king):
                        return False
                    if (x1,y1) in army1.keys():
                        break
                    if x1<=1 or y1<=8:
                        break       

                return True        

                
        else :#solder[0:4]=='pawn'
                x1=pos1[0]
                y1=pos1[1]

                if black:

                    if any([
                    
                        (x1+1,y1-1)     in army1.keys()   and  king_protected(pos1,(x1+1,y1-1),army,army1,black,king),
                        (x1-1,y1-1)     in army1.keys()   and  king_protected(pos1,(x1-1,y1-1),army,army1,black,king),
                        (x1,y1-1)   not in army.keys()    and  king_protected(pos1,(x1,y1-1),army,army1,black,king),
                        (x1,y1-1)   not in army.keys()    and
                        (x1,y1-1)   not in army1.keys()   and 
                        (x1,y1-2)   not in army.keys()    and
                        (x1,y1-2)   not in army1.keys()   and  king_protected(pos1,(x1,y1-2),army,army1,black,king)

                            ]):
                        return False
                    else:
                        return True
                else:
                    if any([
                        
                        (x1+1,y1+1)     in army1.keys()   and  king_protected(pos1,(x1+1,y1+1),army,army1,black,king),
                        (x1-1,y1+1)     in army1.keys()   and  king_protected(pos1,(x1-1,y1+1),army,army1,black,king),
                        (x1,y1+1)   not in army.keys()    and  king_protected(pos1,(x1,y1+1),army,army1,black,king),
                        (x1,y1+1)   not in army.keys()    and   
                        (x1,y1+1)   not in army1.keys()   and 
                        (x1,y1+2)   not in army.keys()    and   
                        (x1,y1+1)   not in army1.keys()   and  king_protected(pos1,(x1,y1+2),army,army1,black,king)

                            ]):
                        return False
 
                    else:
                        return True
        return False


def chekmate(army1,army2,king,black):                  
    """returns true if checkmate"""
    for location ,solder  in army2.items():
        if solder[0:4]=='rook':
            if rook_right_move(location,king):
                if rook_can_move(location,king,army2,army1):
                    return True
            
        elif solder[0:6]=='Bishop':    
            if Bishop_right_move(location,king):
                if Bishop_can_move(location,king,army2,army1):
                    return True
        elif solder[0:6]=='Knight':    
            if Knight_right_move(location,king):
                
                 return True

        elif solder=='Queen':    
            if Queen_right_move(location,king):
                if Queen_can_move(location,king,army2,army1):
                    return True
        elif solder=='king':
            if King_right_move(location,king):
                if King_can_move(location,king,army2):
                    return True
        else:
            
            
            if pawn_right_move(location,king,1,black):
                    
                    return True                
    return False



def king_checkmated(king,army,army1,black):
    """Returns True If Checkmated """
    x=king[0]
    y=king[1]
    black1=black
    black= abs(black-1)
    if any([
        (x-1,y+1) not in army.keys() and inbord((x-1,y+1)) and king_freeToMove(pos1,(x-1,y+1),army,army1,black),
        (x+1,y+1) not in army.keys() and inbord((x+1,y+1)) and king_freeToMove(pos1,(x+1,y+1),army,army1,black),
        (x-1,y-1) not in army.keys() and inbord((x-1,y-1)) and king_freeToMove(pos1,(x-1,y-1),army,army1,black),
        (x+1,y-1) not in army.keys() and inbord((x+1,y-1)) and king_freeToMove(pos1,(x+1,y-1),army,army1,black),
        (x,y-1)   not in army.keys() and inbord((x+1,y-1)) and king_freeToMove(pos1,(x,y-1),army,army1,black),
        (x,y+1)   not in army.keys() and inbord((x+1,y+1)) and king_freeToMove(pos1,(x,y+1),army,army1,black),
        (x-1,y)   not in army.keys() and inbord((x-1,y))   and king_freeToMove(pos1,(x-1,y),army,army1,black),
        (x+1,y)   not in army.keys() and inbord((x+1,y))   and king_freeToMove(pos1,(x+1,y),army,army1,black)
             ]):
        
        return False
    
    black=black1
    for solder in army.keys():
        if army[solder]=="king":
            continue
        if King_protector_allways(solder,army,army1,black,king):
            continue
        else:
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

def makechange(army,army1,solgers_out,black):
    """ To Make Changes After Every Move"""
    if black:
        black_army[army[pos1]]['posatios']=pos2
        black_army[army[pos1]]['Movements']+=1
        if pos2 in army1.keys():
            white_army[army1[pos2]]['active']=False
            solgers_out.append(army1[pos2])   
    else:
        white_army[army[pos1]]['posatios']=pos2
        white_army[army[pos1]]['Movements']+=1
        if pos2 in army1.keys():
            black_army[army1[pos2]]['active']=False
            solgers_out.append(army1[pos2])            

def rightPosSynt():
    try:
        pos2=(int(input()),int(input()))
        if inbord(pos2):

            return pos2
        else:
            print("The location Out The Borde,try again")
    except ValueError:
        False

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
    if round ==1:
        print("Black Round ")
        
        while round==1:
            kingpos=black_army['king']['posatios']
            chekmateblack=chekmate(blackposation,whiteposation,kingpos,0)
            king_checkmatedblack=king_checkmated(kingpos,blackposation,whiteposation,round)
            if chekmateblack and king_checkmatedblack:
                
                    print("------WHITE ARMY WINS------")
                    round=3    
                    break
            elif chekmateblack:
                    print("Check Meet !!!!!!!!!!!!!!!!!")
            print("Enter The Terrier Location:")
            #chose the right Solder
            
            while True:
                try:
                    pos1=(int(input()),int(input()))
                    if inbord(pos1):
                        break
                    else:
                        print("The location Out The Borde")
                except ValueError:
                    break 


            if pos1 in blackposation.keys():
                solder=blackposation[pos1]
                if solder[0:4]=='rook':
                    
                    if rook_ther_are_movse(pos1,blackposation) :
                       if King_protector_allways(pos1,blackposation,whiteposation,round,kingpos):
                           print("This Solder Can't Be Moves 'king protector'")
                           break
                       else:
                        
                        while True:
                            
                            while True:
                                print("Enter The New  Location ")
                                pos2=rightPosSynt()
                                if type(pos2)==tuple:
                                    break
                            if pos2== pos1:
                                break     

                            if rook_right_move(pos1,pos2):
                                if rook_can_move(pos1,pos2,blackposation,whiteposation):
                                    if king_protected(pos1,pos2,blackposation,whiteposation,round,kingpos):

                                        makechange(blackposation,whiteposation,white_out,round)   
                                        round=0                          
                                        break
                                    else:
                                        print("king protecter")
                                        
                                        
                                else:
                                    print("Wrong Move ,Try Again")    
                                    
                            else:
                                print("Wrong Move for The Rook ")

                    else:
                        print("there are no movse")
                elif solder[0:6]=='Bishop':
                    if Bishop_ther_are_movse(pos1,blackposation) :
                       if King_protector_allways(pos1,blackposation,whiteposation,round,kingpos):
                           print("This Solder Can't Be Moves 'king protector'")
                           break
                       else:                       
                        while True:
                            
                            
                            while True:
                                print("Enter The New  Location ")
                                pos2=rightPosSynt()
                                if type(pos2)==tuple:
                                    break
                            if pos2== pos1:
                                break       
                            if Bishop_right_move(pos1,pos2):
                                if Bishop_can_move(pos1,pos2,blackposation,whiteposation):
                                    if king_protected(pos1,pos2,blackposation,whiteposation,round,kingpos):

                                        makechange(blackposation,whiteposation,white_out,round)      
                                        round=0                          
                                        break
                                    else:
                                        print("king protecter")
                                        
                                        
                                else:
                                    print("Wrong Move ,Try Again")    
                                    
                            else:
                                print("Wrong Move for The Bishop ")

                    else:
                       print("there are no movse")
                elif solder[0:4]=='pawn':
                    if pawn_ther_are_movse(pos1,round,blackposation,whiteposation) :
                       if King_protector_allways(pos1,blackposation,whiteposation,round,kingpos):
                           print("This Solder Can't Be Moves 'king protector'")
                           break
                       else:                       

                        while True:
                            
                            while True:
                                print("Enter The New  Location ")
                                pos2=rightPosSynt()
                                if type(pos2)==tuple:
                                    break
                            if pos2== pos1:
                            
                                break     

                            movments=black_army[blackposation[pos1]]['Movements']
                            if pawn_right_move(pos1,pos2,movments,1):
                                if pawn_can_move(pos1,pos2,round,blackposation,whiteposation):
                                
                                    if king_protected(pos1,pos2,blackposation,whiteposation,round,kingpos):
                                
                                        makechange(blackposation,whiteposation,white_out,round)      
                                            
                                        round=0                          
                                        break
                                    else:
                                        print("king protecter")
                                        
                                    
                                else:
                                    print("Wrong Move ,Try Again")    
                            
                            
                            else:
                                print("Wrong Move for The Pawn ")
                    else:
                       print("there are no movse") 
                elif solder[0:6]=='Knight':
                    if Knight_ther_are_movse(pos1,blackposation) :
                       if King_protector_allways(pos1,blackposation,whiteposation,round,kingpos):
                           print("This Solder Can't Be Moves 'king protector'")
                           break
                       else:                       
                        while True:
                            
                            while True:
                                print("Enter The New  Location ")
                                pos2=rightPosSynt()
                                if type(pos2)==tuple:
                                    break
                            if pos2== pos1:
                                break     

                            if Knight_right_move(pos1,pos2):
                                
                                    if king_protected(pos1,pos2,blackposation,whiteposation,round,kingpos):

                                        makechange(blackposation,whiteposation,white_out,round)      
                                        round=0                          
                                        break
                                    else:
                                        print("king protecter")
                                        
                            
                            
                            else:
                                print("Wrong Move for The Knight ")
                    else:
                       print("there are no movse") 
                elif solder=='Queen':
                    if Queen_ther_are_movse(pos1,blackposation) :
                       if King_protector_allways(pos1,blackposation,whiteposation,round,kingpos):
                           print("This Solder Can't Be Moves 'king protector'")
                           break
                       else:                       
                        while True:
                            
                            while True:
                                print("Enter The New  Location ")
                                pos2=rightPosSynt()
                                if type(pos2)==tuple:
                                    break
                            if pos2== pos1:
                                break     

                            if Queen_right_move(pos1,pos2):
                                if Queen_can_move(pos1,pos2,blackposation,whiteposation):
                                    if king_protected(pos1,pos2,blackposation,whiteposation,round,kingpos):
                                        makechange(blackposation,whiteposation,white_out,round)
     
                                        round=0                          
                                        break
                                    else:
                                        print("king protecter")
                                    
                                else:
                                    print("Wrong Move ,Try Again")    
                                    
                            else:
                                print("Wrong Move for The Queen ")

                    else:
                       print("there are no movse")
                else:
                    if King_ther_are_movse(pos1,blackposation) :
             
                        while True:
                            
                            while True:
                                print("Enter The New  Location ")
                                pos2=rightPosSynt()
                                if type(pos2)==tuple:
                                    break
                            if pos2== pos1:
                                break     

                            if King_right_move(pos1,pos2):
                                if King_can_move(pos2,blackposation):
                                    if king_freeToMove(pos1,pos2,blackposation,whiteposation,0):

                                        makechange(blackposation,whiteposation,white_out,round)
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
            elif pos1 not in zip(white_army.keys(),black_army.keys()) and pos1 !=None:
                print("There Is No Pieces In This Place ")
               
            else:
                break
                




    


    # if white army
    elif round ==0:
        whiteposation=white_posation_chang(white_army)
        blackposation=black_posation_chang(black_army)
        print("White Round ") 

        while round ==0:
            kingpos=white_army['king']['posatios']
            chekmatewhite=chekmate(whiteposation,blackposation,kingpos,1)
            king_checkmatedwhite=king_checkmated(kingpos,whiteposation,blackposation,round)
            if  king_checkmatedwhite and  king_checkmatedwhite:
                
                print("------BLACK ARMY WINS------")

                round=3    

                break
                    
            elif king_checkmatedwhite :
                print("Check Meet !!!!!!!!!!!!!!!!!")
                
           
            print("Enter The Terrier Location:")
            #chose the right Solder

            while True:
                try:
                    pos1=(int(input()),int(input()))
                    if inbord(pos1):
                        break
                    else:
                        print("The location Out The Borde")
                except ValueError:
                    break 
            if pos1 in whiteposation.keys():
                solder=whiteposation[pos1]
                if solder[0:4]=='rook':
                    
                    if rook_ther_are_movse(pos1,whiteposation) :
                       if King_protector_allways(pos1,whiteposation,blackposation,round,kingpos):
                           print("This Solder Can't Be Moves 'king protector'")
                           break
                       else:                       
                        while True:
                            
                            while True:
                                print("Enter The New  Location ")
                                pos2=rightPosSynt()
                                if type(pos2)==tuple:
                                    break
                            if pos2== pos1:
                                break     

                            if rook_right_move(pos1,pos2):
                                if rook_can_move(pos1,pos2,whiteposation,blackposation):
                                    if king_protected(pos1,pos2,whiteposation,blackposation,round,kingpos):

                                        makechange(whiteposation,blackposation,black_out,round)      
                                        round=1                        
                                        break
                                    else:
                                        print("king protecter")
                                
                                else:
                                    print("Wrong Move ,Try Again")    
                                    
                            else:
                                print("Wrong Move for The Rook ")

                    else:
                       print("there are no movse")
                elif solder[0:6]=='Bishop':
                    if Bishop_ther_are_movse(pos1,whiteposation) :
                       if King_protector_allways(pos1,whiteposation,blackposation,round,kingpos):
                           print("This Solder Can't Be Moves 'king protector'")
                           break
                       else:                       
                        while True:
                            
                            while True:
                                print("Enter The New  Location ")
                                pos2=rightPosSynt()
                                if type(pos2)==tuple:
                                    break
                            if pos2== pos1:
                                break     

                            if Bishop_right_move(pos1,pos2):
                                if Bishop_can_move(pos1,pos2,whiteposation,blackposation):
                                    if king_protected(pos1,pos2,whiteposation,blackposation,round,kingpos):

                                        makechange(whiteposation,blackposation,black_out,round)       
                                        round=1                        
                                        break
                                    else:
                                        print("king protecter")
                                    
                                else:
                                    print("Wrong Move ,Try Again")    
                                    
                            else:
                                print("Wrong Move for The Bishop ")

                    else:
                       print("there are no movse")
                elif solder[0:4]=='pawn':
                    if pawn_ther_are_movse(pos1,0,whiteposation,blackposation) :
                       if King_protector_allways(pos1,whiteposation,blackposation,round,kingpos):
                           print("This Solder Can't Be Moves 'king protector'")
                           break
                       else:                            
                        while True:
                            
                            while True:
                                print("Enter The New  Location ")
                                pos2=rightPosSynt()
                                if type(pos2)==tuple:
                                    break
                            if pos2== pos1:
                                break     

                            movments=white_army[whiteposation[pos1]]['Movements']
                            if pawn_right_move(pos1,pos2,movments,0):
                                if pawn_can_move(pos1,pos2,0,whiteposation,blackposation):
                                    if king_protected(pos1,pos2,whiteposation,blackposation,round,kingpos):

                                        makechange(whiteposation,blackposation,black_out,round)       
                                        round=1                        
                                        break
                                    else:
                                        print("king protecter")
                                        
                                
                                        
                                else:
                                    print("Wrong Move ,Try Again")    
                            
                            
                            else:
                                print("Wrong Move for The Pawn ")
                    else:
                       print("there are no movse") 

                elif solder[0:6]=='Knight':
                    if Knight_ther_are_movse(pos1,whiteposation) :
                       if King_protector_allways(pos1,whiteposation,blackposation,round,kingpos):
                           print("This Solder Can't Be Moves 'king protector'")
                           break
                       else:                            
                        while True:
                            
                            while True:
                                print("Enter The New  Location ")
                                pos2=rightPosSynt()
                                if type(pos2)==tuple:
                                    break
                            if pos2== pos1:
                                break     
                            
                            if Knight_right_move(pos1,pos2):
                                
                                    if king_protected(pos1,pos2,whiteposation,blackposation,round,kingpos):

                                        makechange(whiteposation,blackposation,black_out,round)       
                                        round=1                        
                                        break
                                    else:
                                        print("king protecter")
                                    
                            else:
                                print("Wrong Move for The Knight ")
                    else:
                       print("there are no movse") 
                elif solder=='Queen':
                    if Queen_ther_are_movse(pos1,whiteposation) :
                       if King_protector_allways(pos1,whiteposation,blackposation,round,kingpos):
                           print("This Solder Can't Be Moves 'king protector'")
                           break
                       else:                            
                        while True:
                            
                            while True:
                                print("Enter The New  Location ")
                                pos2=rightPosSynt()
                                if type(pos2)==tuple:
                                    break
                            if pos2== pos1:
                                break     

                            if Queen_right_move(pos1,pos2):
                                if Queen_can_move(pos1,pos2,whiteposation,blackposation):
                                    if king_protected(pos1,pos2,whiteposation,blackposation,round,kingpos):

                                        makechange(whiteposation,blackposation,black_out,round)      
                                        round=1                        
                                        break
                                    else:
                                        print("king protecter")
                                        
                                    
                                else:
                                    print("Wrong Move ,Try Again")    
                                    
                            else:
                                print("Wrong Move for The Queen ")

                    else:
                       print("there are no movse")
                else:
                    if King_ther_are_movse(pos1,whiteposation) :
                       
                        while True:
                            
                            while True:
                                print("Enter The New  Location ")
                                pos2=rightPosSynt()
                                if type(pos2)==tuple:
                                    break
                            if pos2== pos1:
                                break     

                        if King_right_move(pos1,pos2):
                            if King_can_move(pos2,whiteposation):
                                if king_freeToMove(pos1,pos2,whiteposation,blackposation,1):
                                    makechange(whiteposation,blackposation,black_out,round) 
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
            elif pos1 not in white_army.keys() and pos1 not in black_army.keys() and pos1 !=None:
                print("There Is No Pieces In This Place ")
               
            else:
                break

    else:
        break    
    
    

   

