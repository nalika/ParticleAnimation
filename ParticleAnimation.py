# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 21:30:00 2019

@author: akilan
"""

import string
import numpy as np


class ParticleAnimation:
    def __init__(self, speed, init):
        self.speed = speed
        self.init = init
  

    def animate(self):
        total_pos = len(self.init)
        dir_dic = "RL"
        temp = list(self.init)
        directions = list(self.init)
        directions_now = list(directions)
        
        
        ani_out = []
        
   
        # Initial cell content
        for pos in range(total_pos):
            if self.init[pos] in dir_dic:
                temp[pos] = "X"
         
        ani_out.append(''.join(temp))
        #print(ani_out)
        #print(ani_out)
        #print(temp)
        #print(directions)
       
        
        #i = 0
        
        # track the directino map 
        while "X" in temp:
            
            #print(directions)    
            directions_now = list(["." for x in range(len(temp))]) # to hold the new direction map
            
            for pos in range(total_pos):
               # print(pos)                
                #print(champer_now)
                
                curr_dir = list(directions[pos]) # all possibel direction associated to the cell
                #print(curr_dir)
                #curr_dir_temp = curr_dir
                
                for char in curr_dir:                
                
                    if char == 'R':
                        if (pos + self.speed) < total_pos:                            
                            #champer_now[pos + self.speed] = "X"                                 
                            directions_now[pos + self.speed] += "R"
                           # print("R: = move right")          
                            
                    if char == 'L':
                        if (pos - self.speed) >= 0:
                            #champer_now[pos - self.speed] = "X"                            
                            directions_now[pos - self.speed] += "L"
                            #print("L: = move left")
                
                champer_now = ["." for x in range(len(temp))]# to hold the new champer
                    
                for pos in range(total_pos):
                    xx = list(directions_now[pos])
                    
                    for char in xx:
                       # print(pos, char)
                        if char == "R" or char == "L":
                            champer_now[pos] = "X"
                            #print(champer_now)
                        else:
                             champer_now[pos] = "."
                
          
                
                
            #print(champer_now)
            ani_out.append(''.join(champer_now)) # update the champer with the initial condition
            #print(np.reshape(ani_out, (len(ani_out),1)))
                
            directions = directions_now # update the cell direction map
            #print(directions)
            '''i +=1
            if i > 4:
                break 
                '''
               
                
            # update the current champer & the cell movement
            temp = champer_now            #print(temp)


        #print(np.reshape(ani_out, (len(ani_out),1)))
        return np.reshape(ani_out, (len(ani_out),1))
  
            

        

# Test cases  
p1 = ParticleAnimation(2,  "..R....")
print("\n"+"*"*5+"Case 1"+"*"*5+"\n")
print(p1.animate())
 
print("\n"+"*"*5+"Case 2:"+"*"*5+"\n")          
p1 = ParticleAnimation(2, "LRLR.LRLR")
print(p1.animate())

print("\n"+"*"*5+"Case 3:"+"*"*5+"\n") 
p1 = ParticleAnimation(3,  "RR..LRL")
print(p1.animate())


p1 = ParticleAnimation(10,  "RLRLRLRLRL")
print("\n"+"*"*5+"Case 4"+"*"*5+"\n")
print(p1.animate())
 
print("\n"+"*"*5+"Case 5:"+"*"*5+"\n")          
p1 = ParticleAnimation(1,  "LRRL.LR.LRR.R.LRRL.")
print(p1.animate())

print("\n"+"*"*5+"Case 6:"+"*"*5+"\n")          
p1 = ParticleAnimation(10,  "RLRLRLRLRL")
print(p1.animate())
