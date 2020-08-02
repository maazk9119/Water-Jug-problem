import random
class State:
    
    def __init__(self, startsate):
        self.states = startsate
        self.jug_one = 6 # represent x
        self.jug_two = 4 #represent y 
        self.visited = [] #stop looping by using visited mark 
    
    #All operators
    #First
    def op_01(self):
        x = self.states[0]
        y = self.states[1]
        if x < self.jug_one and ([self.jug_one, y] not in self.visited):
            self.visited.append([self.jug_one, y])
            return [self.jug_one,y]
        else:
            return None

    #Second
    def op_02(self):
        x = self.states[0]
        y = self.states[1]
        if y < self.jug_two and([x, self.jug_two] not in self.visited):
            self.visited.append([x,self. jug_two])
            return [x, self.jug_two]
        else:
            return None

    #Third 
    def op_03(self):
        x = self.states[0]
        y = self.states[1]
        if x > self.jug_one and ([0, y] not in self.visited):
            self.visited.append([0, y])
            return [0, y]
        else:
            return None

    #Fourth
    def op_04(self):
        x = self.states[0]
        y = self.states[1]
        if y > self.jug_two and ([self.jug_one, 0] not in self.visited):
            self.visited.append([self.jug_one, 0])
            return [self.jug_one, 0]
        else:
            return None
        
    #fifth
    def op_05(self):
        x = self.states[0]
        y = self.states[1]
        if y > 0 and ([min(x+y, self.jug_one), max(0,x+y-self.jug_one)] not in self.visited):
            self.visited.append([min(x+y, self.jug_one), max(0,x+y-self.jug_one)])
            return [min(x+y, self.jug_one), max(0,x+y-self.jug_one)]
        else:
            return None

    #Sixth
    def op_06(self):
        x = self.states[0]
        y = self.states[1]
        if x > 0 and ([max(0, x+y-self.jug_two), min(x+y,self.jug_two)] not in self.visited):
            self.visited.append([max(0, x+y-self.jug_two), min(x+y,self.jug_two)])
            return [max(0, x+y-self.jug_two), min(x+y,self.jug_two)]
        else:
            return None

    #Seventh and Eight
    def op_07_08(self):
        x = self.states[0]
        y = self.states[1]
        if [x == self.jug_one and y == self.jug_two] not in self.visited:
            self.visited.append([x,y])
            var = random.randint(0,1)
            if var == 0:
                x = 0
            else:
                y = 0
            return [x, y]
        else:
            return None

    #Apply Operators
    def apply_operator(self):
        return [self.op_01(), self.op_02(),self.op_03(), self.op_04(), self.op_05(), self.op_06(), self.op_07_08()]        

    
   

#Algorithm to solve the problem
def BFS(state, goalnodeY):
    queue = []
    queue.append([state])

    while queue:
        path = queue.pop(0)
        node = path[-1]
        y = node[-1]

        if y == goalnodeY:
            return path
        else:
            mystateobj = State(node)
            list_of_lists = mystateobj.apply_operator()
            for one_list in list_of_lists:
                if one_list == None:
                    pass
                else:
                    new_path = list(path)
                    new_path.append(one_list)
                    queue.append(new_path)



#Drive code
print("---Enter the initial state State--")
x = int(input("Enter water initailly in JUG one:"))
y = int(input("Enter water initially in JUG two:"))
if x > 6 or y > 4:
    print("JUG is overflown")
else:
    goalnodeY = 2
    state = [x,y]
    path = BFS(state, goalnodeY)
    print("Succssors from initial to final according to Given operations are:")
    print(path)

