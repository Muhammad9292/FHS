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

def po(dice,available):
    move=[]
    Würfel=list(dice)
    Würfel.sort()

    eins = Würfel.count(1)
    zwei = Würfel.count(2)
    drei = Würfel.count(3)
    vier = Würfel.count(4)
    fünf = Würfel.count(5)
    sechs = Würfel.count(6)
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
    
    for row, col in available:
        if eins >= 1 and col == 0:
            move.append((row,col))
            
        elif zwei >= 1 and col == 1:
            move.append((row,col))
            
        elif drei >= 1 and col == 2:
            move.append((row,col))
            
        elif vier >= 1 and col == 3:
            move.append((row,col))
            
        elif fünf >= 1 and col == 4:
            move.append((row,col))
            
        elif sechs >= 1 and col == 5:
            move.append((row,col))

        elif col == 6 and (eins >= 3 or  zwei>= 3 or  drei>= 3 or  vier>= 3 or  fünf>= 3 or  sechs>= 3) :
            move.append((row,col))
        
        elif col == 7 and (eins >= 4 or  zwei>= 4 or  drei>= 4 or  vier>= 4 or  fünf>= 4 or  sechs>= 4) :
            move.append((row,col))
        
        elif col == 8 and ((eins >= 2 and (zwei>= 3 or  drei>= 3 or  vier>= 3 or  fünf>= 3 or  sechs>= 3))
                        or  (zwei >= 2 and (eins>= 3 or  drei>= 3 or  vier>= 3 or  fünf>= 3 or  sechs>= 3))
                        or  (drei >= 2 and (eins>= 3 or  zwei>= 3 or  vier>= 3 or  fünf>= 3 or  sechs>= 3))
                        or  (vier >= 2 and (eins>= 3 or  zwei>= 3 or  drei>= 3 or  fünf>= 3 or  sechs>= 3))
                        or  (fünf >= 2 and (eins>= 3 or  zwei>= 3 or  drei>= 3 or  vier>= 3 or  sechs>= 3))
                        or  (sechs >= 2 and (eins>= 3 or  zwei>= 3 or  drei>= 3 or  vier>= 3 or  fünf>= 3))):
            move.append((row,col))
                        
        elif col == 9 and straße == 1:
            move.append((row,col))
                           
        elif col == 10 and gasse == 1:
            move.append((row,col))                
        
        elif col == 11 and (eins >= 5 or  zwei>= 5 or  drei>= 5 or  vier>= 5 or  fünf>= 5 or  sechs>= 5) :
            move.append((row,col))
                           
        elif col == 12:
            move.append((row,col))
    return move

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
            decison=0
            rew=0
            possible=po(dice,available)
            if not possible:
                for go in available:
                    rew=get_reward(dice,go)
                    if rew>=decison:
                         action=go
            else:
                 for goo in possible:
                    rew=get_reward(dice,goo)
                    if rew>=decison:
                         action=goo
                 
      
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

def mcts(root_mcts, iterations,l):
    l+=1
    for _ in range(iterations):
        node = select(root_mcts)
        reward = simulate(node.state)
        backpropagate(node, reward)
        



    best_child = best_child_ucb(root_mcts, 0)
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
print('Start:')







def get_user_input():
    numbers = []
    
    while True:
        user_input = input("Enter five numbers of the dices separated by spaces: ")
        
        if user_input.lower() == 'finish':
            break
        
        # Split the input string by spaces
        input_numbers = user_input.split()
        
        # Check if the number of input numbers is not exactly five
        if len(input_numbers) == 5:
            
            try:
                for num_str in input_numbers:
                    number = int(num_str)
                    numbers.append(number)
      
                state=[[[1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1]],[1,3,2,6,5],[0,1]]
                root=Node(state)
                root.state[1]=numbers
                List=state[0]
                available=avil(List)
                current_time = datetime.datetime.now()  
                turns=0
                sumall=0
                replay=0
                for _ in range(150):
                    numbers = []
                    turns +=1
                    for child in available:
                    # Create a deep copy of the state for each child node
                        child_state = copy.deepcopy(root.state)
                        child_state[2] = child
                    
                        child_node = Node(child_state)
                        root.children.append(child_node)
                    
                    root.visits =1
                    chosen_state = mcts(root, 50000,0)

                    action=chosen_state.state[2]
                    dice=root.state[1]
                    
                    rewae=get_reward(dice,action)
                    if rewae==0 and replay<2:
                        replay+=1
                        print('skip')
                        

                        user_input = input("skip please! Enter five numbers of the dices separated by spaces: ")
        
                        if user_input.lower() == 'finish':
                             break
        
                        input_numbers = user_input.split()
        
                        if len(input_numbers) == 5:
                            for num_str in input_numbers:
                                number = int(num_str)
                                numbers.append(number)
                            root.state[1]=numbers


                    else:
                        replay=0
                        root=Node(chosen_state.state)
                        root.state[2]=action  
                        sumall +=rewae

                        print(root.state,rewae, sumall)
                        r,c=action
                        user_input = input("Enter five numbers of the dices separated by spaces: ")
        
        
                        input_numbers = user_input.split()
        
                        if len(input_numbers) == 5:
                            for num_str in input_numbers:
                                number = int(num_str)
                                numbers.append(number)
                        List[r][c] = 0
                        root.state[0]=List
                        root.state[1]=numbers
                        available=avil(List)
                        if not available:
                            print(turns)
                            break
                        

                current_time = datetime.datetime.now() - current_time
                print('/nGame 3 is finished with total of:', sumall, 'and time is:',current_time)





            except ValueError:
                print("Error: Please enter valid numbers.")
                continue
            print(numbers)
        else:
            print("Error: Please enter exactly five numbers separated by spaces.")
            continue
        

get_user_input()  # Start the loop



