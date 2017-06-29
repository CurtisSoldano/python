#investment future value calculator

#import graphics library
import graphics

def intro():
    #give a brief intro to what the program does 
    print("This program computes the future value of a 10 year investment")
    print("by entering a starting value and an annual percentage rate(APR)")

def main():
    #Prompt the user for input, record input values
    principal = eval(input("Enter starting investment value "))
    apr = eval(input("Enter the annual percentage rate "))
    years = eval(input("Enter the number of years the investment will grow "))

    #Create the graphics window with labels
    window = windows.GraphWin("Investment Growth Chart", 320, 240)
    graphics.window.setBackground("white")
    Text(Point(20,230), ' 0.0K').draw.window
    Text(Point(20,180), ' 2.5K').draw.window
    Text(Point(20,130), ' 5.0K').draw.window
    Text(Point(20,80), ' 7.5K').draw.window
    Text(Point(20,30), ' 10.0K').draw.window

    #Draw bar for initial principal
    height = principal * 0.02
    bar = Rectangle(Point(40, 230), Point(65, 230-height))
    graphics.bar.setfill("green")
    
   
    
    for i in range(years):
        principal = principal * (1 + apr)

    print("The value in ", years, " years is ", principal)

intro()

main()
