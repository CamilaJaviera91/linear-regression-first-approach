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

    #Verify that both lists have the same lenght
    if len(temperature) != len(ice_crea_sales):
        print("\nThe temperature and sales lists MUST HAVE the same number of elements.")
        print("Please re-enter the data\n")
        return collect_data() #Recursively call the function to restart data collection
    
    #Convert lists to NumPy arrays for further processing
    temp = np.array(temperature).reshape(-1, 1).astype(int) #Reshape to a column vector
    sales = np.array(ice_crea_sales).reshape(-1, 1).astype(int) #Reshape to a column vector

    return temp, sales #Return the temperature and sales array