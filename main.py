#!/usr/bin/env python
# coding: utf-8

from fpdf import FPDF

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
        

# While loop to ask user for variables and file name
while True: 
    try:
        print("Please type all variables needed for equation.")
        mass1 = float(input("Type mass of first object: "))
        mass2 = float(input("Type mass of second object: "))
        dist = float(input("Type the distance between two objects: "))  
        file_name = input("Please type the file name (.pdf extension will be added automatically): ")

        provided_eq = Equation(mass_of_object1 = mass1, mass_of_object2 = mass2, distance = dist)
        pdf_report = PdfReport(filename = file_name+".pdf")
        pdf_report.generate(equation = provided_eq)
        break

    except ValueError: 
        print("Provide a valid input. Try again.")
        
    

