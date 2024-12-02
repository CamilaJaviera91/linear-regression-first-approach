import numpy as np

#Function collect data
def collect_data():
    print("Collecting data for temperature and sales .... \n")

    #Collect temperature data
    temperature = []

    while True:
        num_temp = input("Enter a temperature (in celsius) value (or type 'exit' to finish): ")

        if num_temp.lower == 'exit': #Exit the loop if the user types the word 'exit'
            break
        try:
            num_temp = int(num_temp) #Convert input to an integer
            temperature.append(num_temp) #Append valir temperature to the list
        except:
            print("Invalid input. Please enter numbers only or type 'exit'")
    
    #Collect sales data

    ice_crea_sales = []

    while True:
        num_sales = input("Enter a sales value (or type 'exit to finish'): ")

        if num_sales == 'exit':
            break

        try:
            num_sales = int(num_sales)
            ice_crea_sales.append(num_sales)
        except:
            print("Invalid input. Please enter numbers only or type 'exit'")
    