import tkinter as tk

rootpt1 = tk.Tk()
rootpt1.title("Assignment 5 Part 1")
rootpt1.geometry("500x500")

def part1Main():

    weight = tk.IntVar()
    height = tk.IntVar()

    weightLabel = tk.Label(rootpt1, text="Enter your weight in pounds: ")
    weightEntry = tk.Entry(rootpt1, textvariable=weight)

    heightLabel = tk.Label(rootpt1, text="Enter your height in inches: ")
    heightEntry = tk.Entry(rootpt1, textvariable=height)

    calculateButton = tk.Button(rootpt1, text="Calculate BMI", command = lambda: calculateBMI(weight, height))

    weightLabel.grid(row=0, column=0)
    weightEntry.grid(row=0, column=1)
    heightLabel.grid(row=1, column=0)
    heightEntry.grid(row=1, column=1)
    calculateButton.grid(row=2, column=0)

    rootpt1.mainloop()

def calculateBMI(weight, height):
    weight = weight.get()
    height = height.get()
    bmi = (weight * 703) / (height * height)

    bmiClass = ""
    if bmi < 18.5:
        bmiClass = "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        bmiClass = "Normal"
    elif bmi >= 25:
        bmiClass = "Overweight"
    
    bmi = round(bmi, 2)
    showBMI = tk.Label(rootpt1, text="Your BMI is: " + str(bmi) + " and you are " + bmiClass)
    showBMI.grid(row=3, column=0)
    return bmi

part1Main()