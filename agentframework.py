import random 
# Agent Framework

# Defining agents (sheep)
class Agent:
    def __init__(self, environment, agents, neighbourhood):
        self.x = random.randint(0,300) 
        self.y = random.randint(0,300)
        self.environment = environment
        self.agents = agents
        self.neighbourhood = neighbourhood
        self.store = 0 

# Randomly moving      
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 300 
        else:
            self.y = (self.y - 1 ) % 300
            
        if random.random() < 0.5:
            self.x = (self.x + 1 ) % 300
        else:
            self.x = (self.x - 1 ) % 300
            
# Eating and sharing in the environment
    def eat(self): 
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else: 
            self.environment[self.y][self.x] < 10
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] -= self.environment[self.y][self.x]
            
    def share_with_neighbours(self, neighbourhood):
        for i in self.agents: 
            if i != self: 
                distance = self.distance_between(i) 
                if distance <= neighbourhood: 
                    ave = (self.store + i.store)/2 
                    self.store = ave
                    i.store = ave
                    
#Distance function                             
    def distance_between(self, other_agent):
        return ((self.y - other_agent.y)**2 + 
                ((self.x - other_agent.x)**2))**0.5
                
# Defining the wolf class    
class Wolf:
    def __init__(self, agents, zone) :
        self.x = random.randint(0,300) 
        self.y = random.randint(0,300)
        self.agents = agents
        self.zone = zone
 
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 2) % 300
        else:
            self.y = (self.y - 2) % 300
            
        if random.random() < 0.5:
            self.x = (self.x + 2) % 300
        else:
            self.x = (self.x - 2) % 300
    
    def distance_between(self, other_agent):
        return ((self.y - other_agent.y)**2 + 
                ((self.x - other_agent.x)**2))**0.5
                
# Function that hunts (eliminate) sheeps              
    def hunt(self, agents):
        for i in agents:
            distance = self.distance_between(i) 
            if distance <= self.zone:
               agents.remove(i)
          
