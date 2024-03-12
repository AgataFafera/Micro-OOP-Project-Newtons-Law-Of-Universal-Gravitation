#!/usr/bin/env python
# coding: utf-8

from equation import Equation
from report import PdfReport
  

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
