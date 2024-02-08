
import copy
import datetime
import math




def würfeln():
    p=(random.randint(1, 6),random.randint(1, 6),random.randint(1, 6),random.randint(1, 6),random.randint(1, 6))
    return p

def avil(List):
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
def get_reward (dice,action):
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

def simulate(state):
    List= copy.deepcopy(state[0])
    dice=state[1]
    action=state[2]
    sumall=get_reward(dice,action)
    r,c=action
    List[r][c] = 0
    n=0
    for _ in range(150):
        n +=1
        dice=würfeln()
        available=avil(List)
        if not available:
                break
        else:
            action=random.choice(available)
            sumall += get_reward(dice,action)
            r,c=action
            List[r][c] = 0
    return sumall

import random
import math


class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.value = 0

def mcts(root, iterations,l):
    l+=1
    for _ in range(iterations):
        node = select(root)
        reward = simulate(node.state)
        backpropagate(node, reward)
        



    best_child = best_child_ucb(root, 0)
    return best_child

def select(node):
    node = random.choice(node.children)
    return node

def backpropagate(node, reward):
    while node:
        node.visits += 1
        node.value += reward
        node = node.parent

def best_child_ucb(node, exploration_weight):
    children = sorted(node.children, 
                      
                    key=lambda x: 
                      
                    x.value / x.visits + exploration_weight * math.sqrt(math.log(node.visits) / x.visits), reverse=True)
    

    
    return children[0]
print('ok')










dice_all=[(6, 6, 4, 6, 3), (1, 2, 2, 4, 5), (6, 2, 4, 2, 3), (3, 3, 6, 2, 4), (5, 3, 2, 5, 2), (4, 3, 5, 6, 6), (5, 5, 2, 6, 3), (1, 3, 6, 2, 1), (5, 3, 4, 1, 2), (6, 3, 4, 4, 4), (5, 5, 5, 3, 1), (3, 4, 5, 6, 6), (4, 2, 3, 3, 4), (1, 1, 3, 1, 6), (2, 2, 4, 3, 3), (1, 6, 3, 4, 5), (4, 4, 6, 4, 1), (3, 3, 6, 2, 4), (1, 1, 2, 2, 4), (3, 6, 2, 3, 5), (4, 1, 3, 5, 2), (6, 2, 3, 2, 6), (1, 4, 5, 3, 4), (3, 4, 1, 1, 3), (1, 6, 3, 3, 2), (1, 4, 1, 3, 3), (2, 6, 5, 2, 6), (4, 1, 1, 1, 5), (6, 6, 5, 6, 2), (4, 3, 3, 6, 2), (1, 3, 2, 1, 6), (2, 6, 6, 4, 6), (3, 3, 4, 5, 2), (3, 1, 3, 5, 6), (3, 2, 3, 5, 1), (6, 3, 3, 3, 2), (4, 5, 6, 1, 4), (5, 5, 3, 2, 4), (4, 2, 2, 2, 6), (6, 5, 2, 1, 2), (1, 6, 5, 2, 6), (3, 4, 1, 2, 5), (3, 3, 2, 5, 4), (2, 6, 1, 6, 1), (2, 1, 4, 4, 3), (5, 5, 6, 5, 4), (2, 4, 1, 6, 1), (5, 3, 6, 6, 4), (4, 1, 1, 1, 4), (1, 1, 2, 1, 1), (4, 6, 2, 4, 1), (6, 2, 6, 6, 1), (2, 2, 6, 5, 6), (2, 1, 1, 2, 1), (2, 1, 4, 4, 3), (5, 5, 1, 6, 4), (5, 5, 1, 3, 5), (1, 1, 4, 6, 3), (3, 6, 6, 4, 6), (4, 2, 6, 2, 2), (3, 4, 4, 2, 5), (4, 4, 6, 5, 4), (4, 4, 4, 6, 3), (3, 4, 2, 4, 1), (4, 2, 4, 6, 3), (6, 2, 5, 1, 4), (5, 1, 6, 2, 3), (3, 5, 4, 4, 3), (2, 1, 1, 2, 5), (4, 3, 6, 5, 4), (4, 6, 6, 2, 2), (3, 3, 3, 5, 2), (4, 3, 2, 3, 5), (1, 1, 2, 4, 5), (4, 2, 6, 4, 6), (6, 3, 4, 3, 6), (5, 6, 5, 1, 2), (3, 4, 3, 5, 5), (3, 1, 4, 5, 3), (5, 6, 5, 1, 1), (2, 5, 3, 5, 1), (2, 3, 6, 5, 4), (4, 1, 5, 4, 3), (6, 2, 3, 1, 3), (1, 4, 3, 3, 5), (4, 5, 6, 5, 2), (5, 2, 3, 2, 1), (3, 2, 4, 6, 1), (5, 2, 1, 3, 6), (4, 1, 5, 1, 3), (3, 5, 3, 4, 6), (5, 3, 6, 6, 3), (5, 3, 5, 4, 3), (4, 3, 4, 2, 1), (5, 6, 2, 3, 1), (6, 6, 3, 3, 4), (5, 4, 4, 4, 1), (6, 1, 5, 4, 4), (3, 4, 1, 3, 3), (3, 1, 5, 1, 5)]
state=[[[1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1]],[1,3,2,6,5],[0,1]]
root=Node(state)
root.state[1]=dice_all[0]
List=state[0]
available=avil(List)
current_time = datetime.datetime.now()  
turns=0
sumall=0
for _ in range(150):
    turns +=1
    for child in available:
    # Create a deep copy of the state for each child node
        child_state = copy.deepcopy(root.state)
        child_state[2] = child
    
        child_node = Node(child_state)
        root.children.append(child_node)
    
    root.visits =1
    chosen_state = mcts(root, 200000,0)

    action=chosen_state.state[2]
    dice=root.state[1]
    root=Node(chosen_state.state)
    root.state[2]=action
    rewae=get_reward(dice,action)
    sumall +=rewae

    print(root.state,rewae, sumall)
    r,c=action
    
    List[r][c] = 0
    root.state[0]=List
    root.state[1]=dice_all[turns]
    available=avil(List)
    if not available:
         print(turns)
         break

current_time = datetime.datetime.now() - current_time
print('Game 1 is finished with total of:', sumall, 'and time is:',current_time)



