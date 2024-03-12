#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Equation: 
    """
    Object that cointains all variables needed for the newton's equation 
    and function calculating it. 
    """
    
    def __init__(self, mass_of_object1, mass_of_object2, distance, constant_of_gravitation = 6.674E-11):
        
        self.mass_of_object1 = mass_of_object1
        self.mass_of_object2 = mass_of_object2
        self.constant_of_gravitation = constant_of_gravitation
        self.distance = distance
    
    def calculate(self):
    
        force = (self.constant_of_gravitation * self.mass_of_object1 * self.mass_of_object2) / self.distance ** 2
        return force

