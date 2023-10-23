import tkinter as tk

root = tk.Tk()
root.title("Assignment 5")
root.minsize(500, 500)
root.maxsize(1920, 1080)
root.geometry("500x500")

def main():

    annualPercentageRate=tk.DoubleVar()
    years=tk.IntVar()
    price = tk.IntVar()
    downpayment = tk.IntVar()
    


    percentageLabel = tk.Label(root, text = 'Annual Percentage', font=('roman',20, 'bold'))
    percentageEntry = tk.Entry(root,textvariable = annualPercentageRate, font=('roman',20,'normal'))

    yearsLabel = tk.Label(root, text = 'Years', font=('roman',20, 'bold'))
    yearsEntry = tk.Entry(root,textvariable = years, font=('roman',20,'normal'))

    priceLabel = tk.Label(root, text = 'Price', font=('roman',20, 'bold'))
    priceEntry = tk.Entry(root,textvariable = price, font=('roman',20,'normal'))

    downpaymentLabel = tk.Label(root, text = 'Down Payment', font=('roman',20, 'bold'))
    downpaymentEntry = tk.Entry(root,textvariable = downpayment, font=('roman',20,'normal'))

    calculateButton = tk.Button(root, text = 'Calculate', font=('roman',20, 'bold'), command = (lambda: calculate(years, annualPercentageRate, price, downpayment)))

    monthlyPaymentLabel = tk.Label(root, text = 'Monthly Payment:', font=('roman',20, 'bold'))


    percentageLabel.grid(row=0,column=0)
    percentageEntry.grid(row=0,column=1)

    yearsLabel.grid(row=1,column=0)
    yearsEntry.grid(row=1,column=1)

    priceLabel.grid(row=2,column=0)
    priceEntry.grid(row=2,column=1)

    downpaymentLabel.grid(row=3,column=0)
    downpaymentEntry.grid(row=3,column=1)

    calculateButton.grid(row=4,column=0)
    monthlyPaymentLabel.grid(row=5,column=0)

    root.mainloop()

def calculate(years, annualPercentageRate, price, downpayment):
    months = years.get() * 12
    interest = annualPercentageRate.get() / 1200
    monthlyPayment = (((price.get() - downpayment.get()) * interest * ((1 + interest) ** months))/(((1 + interest) ** months) - 1))
    monthlyPayment = round(monthlyPayment, 2)
    monthlyPaymentDisplay = tk.Label(root, text = monthlyPayment, font=('roman',20, 'bold'))
    monthlyPaymentDisplay.grid(row=5,column=1)
    return monthlyPayment

if __name__ == "__main__":
    main()