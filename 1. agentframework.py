#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random 
# Agent Framework

# Defining the first agents (sheep)
class Agent:
    def __init__(self, environment, agents_list, neighbourhood):
        self.x = random.randint(0,300) # initial position adjusted to the total environment
        self.y = random.randint(0,300)
        self.environment = environment
        self.agents_list = agents_list
        self.neighbourhood = neighbourhood
        self.store = 0 # Food storage for every agent set to 0 when created

# Each sheep speed will depend on the amount of food they have eaten. The more they eat, the faster they go        
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1 + int(0.005 * self.store)) % 300 
        else:
            self.y = (self.y - 1 - int(0.005 * self.store)) % 300
            
        if random.random() < 0.5:
            self.x = (self.x + 1 + int(0.005 * self.store)) % 300
        else:
            self.x = (self.x - 1 - int(0.005 * self.store)) % 300
 
# If there are more than 10 units in a specific position, each agent will eat and store 10 units.
# If there is less than 10, the agent will what is left and store it.
    def eat(self): 
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else: 
            self.environment[self.y][self.x] < 10
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] -= self.environment[self.y][self.x]
            
    def share_with_neighbours(self, neighbourhood):
        for i in self.agents_list: #This is going to be executed for every agent in the list
            if i != self: # Only for those agents that are not itself
                distance = self.distance_between(i) #Calling distance function
                if distance <= neighbourhood: # This will happen if they are within a certain distance from themselves
                    ave = (self.store + i.store)/2 #Both agents share units by getting the average of both store values
                    self.store = ave
                    i.store = ave
                    #print("sharing " + str(distance) + " " + str(ave))
 
# Distance function                             
    def distance_between(self, other_agent):
        return ((self.y - other_agent.y)**2 + 
                ((self.x - other_agent.x)**2))**0.5
                
# Defining the wolf class    
class Wolf:
    def __init__(self, agents_list, scope) :
        self.x = random.randint(0,300) 
        self.y = random.randint(0,300)
        self.agents_list = agents_list
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
    
    def distance_between(self, other_agent):
        return ((self.y - other_agent.y)**2 + 
                ((self.x - other_agent.x)**2))**0.5
                
# Function that hunts (eliminate) sheeps when a sheep is at a certain distance                
    def hunt(self, agents_list):
        for i in agents_list:
            distance = self.distance_between(i) #Calling distance function
            if distance <= self.scope:
               agents_list.remove(i)
                #print("sharing " + str(distance) + " " + str(ave))


# In[ ]:




