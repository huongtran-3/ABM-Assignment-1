#!/usr/bin/env python
# coding: utf-8

# In[23]:


import random
import matplotlib.pyplot
import matplotlib.animation
import agentframework_v2
import csv
#import sys

# Reading environment
f = open('data.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
environment = []
for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(value) 
    environment.append(rowlist)  
f.close() 


agents = []
wolves = []
num_of_agents = 50
num_of_wolves = 60
num_of_iterations = 100
neighbourhood = 20
scope = 10

# Setting Plots
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


# Creating sheeps and wolves
for i in range(num_of_agents):
    agents.append(agentframework_v2.Agent(environment, agents, neighbourhood))
    
for i in range(num_of_wolves):
    wolves.append(agentframework_v2.Wolf(agents, scope))    
    
    
       
#Moving, eating and sharing     
    
carry_on = True    
def update(frame_number):
    
    fig.clear()
    global carry_on
    
    if len(agents) == 0: 
        carry_on=False 
        print("stopping condition")
       
    for j in range(len(agents)):
        random.shuffle(agents)  
        for i in range(num_of_iterations): 
            agents[j].move()
            agents[j].eat()
            agents[j].share_with_neighbours(neighbourhood)   
                  
    for i in range(len(agents)):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, marker="*", color='yellow')           
        
    for j in range(num_of_wolves):
        random.shuffle(wolves)
        for i in range(num_of_iterations):
            wolves[j].move()
            wolves[j].hunt(agents)                      
        
    for i in range(num_of_wolves):
        matplotlib.pyplot.scatter(wolves[i].x,wolves[i].y, color='black')   
    matplotlib.pyplot.ylim(0, 300)
    matplotlib.pyplot.xlim(0, 300)
    matplotlib.pyplot.imshow(environment) 
   
    
# Creating the animation.                                              
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1000, frames=gen_function, repeat=False)
matplotlib.pyplot.show()
        
print(len(agents))

