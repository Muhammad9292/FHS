
import copy
import datetime
import math
import random




def würfeln1():
    p=(random.randint(1, 6),random.randint(1, 6),random.randint(1, 6),random.randint(1, 6),random.randint(1, 6))
    return p

def avil1(List):
    avail=[]
    for col, z in enumerate(List[0][0:13:1]):
        if z != 0:
            avail.append((0, col))
        
    for col, z in enumerate(List[1][0:13:1]):
        if z != 0:
            avail.append((1, col))
            break
            
    for col, z in zip(range(12, -1, -1), List[2][::-1]):
        if z != 0:
            avail.append((2, col))
            break
    return avail
def get_reward1 (dice,action):
    Würfel=list(dice)
    Würfel.sort()

    eins = Würfel.count(1)
    zwei = Würfel.count(2)
    drei = Würfel.count(3)
    vier = Würfel.count(4)
    fünf = Würfel.count(5)
    sechs = Würfel.count(6)
    row, col =action
    straße = 0
    gasse = 0
    count_straße = 1
    
    for i in range(1, len(Würfel)):
        if Würfel[i] == Würfel[i - 1] + 1:
            count_straße += 1
        else:
            count_straße = 1

        if count_straße >= 4:
            straße = 1
            break 
            
    count_gasse = 1
    
    for i in range(1, len(Würfel)):
        if Würfel[i] == Würfel[i - 1] + 1:
            count_gasse += 1
        else:
            count_gasse = 1

        if count_gasse >= 5:
            gasse = 1
            break 
            

    if col == 0:
            return eins*1
            
    elif col == 1:
            return zwei*2
            
    elif col == 2:
            return drei*3
            
    elif col == 3:
            return vier*4
            
    elif col == 4:
            return fünf*5
            
    elif col == 5:
            return sechs*6
        
    elif col == 6 and eins >= 3:
            return 3
        
    elif col == 6 and zwei >= 3:
            return 6
        
    elif col == 6 and drei >= 3:
            return 9
        
    elif col == 6 and vier >= 3:
            return 12
        
    elif col == 6 and fünf >= 3:
            return 15
        
    elif col == 6 and sechs >= 3:
            return 18
        
    elif col == 7 and eins >= 4: 
            return 4
                
    elif col == 7 and zwei >= 4: 
            return 8
                
    elif col == 7 and drei >= 4: 
            return 12
                
    elif col == 7 and vier >= 4: 
            return 16
                
    elif col == 7 and fünf >= 4: 
            return 20
                
    elif col == 7 and sechs >= 4: 
            return 24
        
    elif col == 8 and ((eins >= 2 and (zwei>= 3 or  drei>= 3 or  vier>= 3 or  fünf>= 3 or  sechs>= 3))
                        or  (zwei >= 2 and (eins>= 3 or  drei>= 3 or  vier>= 3 or  fünf>= 3 or  sechs>= 3))
                        or  (drei >= 2 and (eins>= 3 or  zwei>= 3 or  vier>= 3 or  fünf>= 3 or  sechs>= 3))
                        or  (vier >= 2 and (eins>= 3 or  zwei>= 3 or  drei>= 3 or  fünf>= 3 or  sechs>= 3))
                        or  (fünf >= 2 and (eins>= 3 or  zwei>= 3 or  drei>= 3 or  vier>= 3 or  sechs>= 3))
                        or  (sechs >= 2 and (eins>= 3 or  zwei>= 3 or  drei>= 3 or  vier>= 3 or  fünf>= 3))):
            return 25
                        
    elif col == 9 and straße == 1:
            return 30
                           
    elif col == 10 and gasse == 1:
            return 40                
        
    elif col == 11 and (eins >= 5 or  zwei>= 5 or  drei>= 5 or  vier>= 5 or  fünf>= 5 or  sechs>= 5) :
            return 50  
                           
    elif col == 12:
            return sum(Würfel)
        
    else:
            return 0

def simulate1(state):
    List= copy.deepcopy(state[0])
    dice=state[1]
    action=state[2]
    sumall=get_reward1(dice,action)
    r,c=action
    List[r][c] = 0
    n=0
    for _ in range(150):
        n +=1
        dice=würfeln1()
        available=avil1(List)
        if not available:
                break
        else:
            action=random.choice(available)
            sumall += get_reward1(dice,action)
            r,c=action
            List[r][c] = 0
    return sumall







