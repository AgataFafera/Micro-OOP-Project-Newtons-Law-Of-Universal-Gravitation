#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from fpdf import FPDF

class PdfReport: 
    """
    Object that creates a pdf file with all variables and the result. 
    """
    
    def __init__(self, filename): 
        self.filename = filename
        
    def generate(self, equation):
        
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        
        # Insert the icon
        pdf.image("saturn.png", w=60, h=30)
        
        # Insert the title 
        pdf.set_font(family='Times', size=18, style='B')
        pdf.cell(w=0, h=80, txt='Newton\'s law of universal gravitation', border=0, align='C', ln=1)
        
        # Insert the variables 
        pdf.cell(w=100, h=40, txt='Mass of the first object [kg]: ', border=0)
        pdf.cell(w=0, h=40, txt=str(round(equation.mass_of_object1, 2)), border=0, align='R', ln=1)
        
        pdf.cell(w=100, h=40, txt='Mass of the second object [kg]: ', border=0)
        pdf.cell(w=0, h=40, txt=str(round(equation.mass_of_object2, 2)), border=0, align='R', ln=1)
        
        pdf.cell(w=100, h=40, txt='Constant of gravitation [m^3·kg^-1·s^-2]: ', border=0)
        pdf.cell(w=0, h=40, txt=str(round(equation.constant_of_gravitation, 10)), border=0, align='R', ln=1)
        
        pdf.cell(w=100, h=40, txt='The distance between the objects [m]: ', border=0)
        pdf.cell(w=0, h=40, txt=str(round(equation.distance, 2)), border=0, align='R', ln=1) 
        
        # Insert the solution
        pdf.cell(w=0, h=40, txt='Force is equal to [N]: ', border=0)
        pdf.cell(w=0, h=40, txt=str(round(equation.calculate(), 2)), border=0, align='R', ln=1) 
        
        
        pdf.output(self.filename)

