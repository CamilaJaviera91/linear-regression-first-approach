def get_prediction():
    """
    Prompt the user to input a temperature value for prediction.
    Ensures the input is a valid integer
    """

    while True: #Infinite loop to handle invalid inputs
        try:
            #Prompt the user to enter a temperature
            pred = int(input("Please enter a temperature to predict sales: "))
            break #Exit the loop if the input is a valir integer
        except ValueError:
            #Handle cases where the input is not a valir integer
            print("That's not a valid number. Please try again.")
    
    return pred