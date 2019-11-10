#!/usr/bin/env python
# coding: utf-8

# In[ ]:



# Agent Framework
import random 

#Create the agents
class Agent:
    def __init__(self, environment, agents,x,y):
        self.x = random.randint(0,300) 
        self.y = random.randint(0,300)
        
        self.environment = environment
        self.agents = agents
        self.store = 0 

#Allow agents move randomly            
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 300
        else:
            self.y = (self.y - 1) % 300

        if random.random() < 0.5:
            self.x = (self.x + 1) % 300
        else:
            self.x = (self.x - 1) % 300
            
#Allow agents to eat in their environment and share food with their neighbors
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
                    #print("sharing " + str(distance) + " " + str(ave))

# Distance function                            
    def distance_between(self, other_agent):
        return ((self.y - other_agent.y)**2 + 
                ((self.x - other_agent.x)**2))**0.5
                
# Creating the wolfs    
class Wolf:
    def __init__(self, agents, scope) :
        self.x = random.randint(0,300) 
        self.y = random.randint(0,300)
        self.agents = agents
        self.scope = scope
 
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 2) % 300
        else:
            self.y = (self.y - 2) % 300
            
        if random.random() < 0.5:
            self.x = (self.x + 2) % 300
        else:
            self.x = (self.x - 2) % 300
    
    def distance_between(self, other_agents):
        return ((self.y - other_agents.y)**2 + 
                ((self.x - other_agents.x)**2))**0.5
                
# Function that hunts sheeps              
    def hunt(self, agents):
        for i in agents:
            distance = self.distance_between(i) 
            if distance <= self.scope:
                agents_list.remove(i)
                #print("sharing " + str(distance) + " " + str(ave))


