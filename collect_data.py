import numpy as np

#Function collect data
def collect_data():
    print("Collecting data for temperature and sales .... \n")

    #Collect temperature data
    temperature = []

    while True:
        num_temp = input("Enter a temperature (in celsius) value (or type 'exit' to finish): ")
      
        if num_temp.lower() == "exit": #exit the loop if the user types the word 'e'
            break
        else:
            try:
                num_temp = int(num_temp) #Convert input to an integer
                temperature.append(num_temp) #Append valir temperature to the list
            except:
                print("Invalid input. Please enter numbers only or type 'exit'")
        
    #Collect sales data
    ice_cream_sales = []
   
    while True:
        num_sales = input("Enter a sales value (or type 'e' to finish'): ")

        if num_sales.lower() == "exit":
            break
        else:
            try:
                num_sales = int(num_sales)
                ice_cream_sales.append(num_sales)
            except:
                print("Invalid input. Please enter numbers only or type 'e'")

    #Verify that both lists have the same lenght
    if len(temperature) != len(ice_cream_sales):
        print("\nThe temperature and sales lists MUST HAVE the same number of elements.")
        print("Please re-enter the data\n")
        return collect_data() #Recursively call the function to restart data collection
    
    #Convert lists to NumPy arrays for further processing
    temp = np.array(temperature).reshape(-1, 1).astype(int) #Reshape to a column vector
    sales = np.array(ice_cream_sales).reshape(-1, 1).astype(int) #Reshape to a column vector

    return temp, sales #Return the temperature and sales array