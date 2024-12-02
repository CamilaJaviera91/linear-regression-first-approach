from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

from collect_data import collect_data #Import the function to collect data
from prediction import get_prediction #Im port the function to get prediction

""" 
Step 1: Collect data
Collect temperature and sales data from the user
"""
temp, sales = collect_data()

"""
Step 2: Sort the datafor better visualization
Sorting ensures the data us ordered for clear plotting
"""
temp.sort(axis=0)  #Sort temperatures
sales.sort(axis=0) #Sort sales

"""Step 3: Create the linear regression model"""
model = LinearRegression()

#Train the model using the collected data
model.fit(temp, sales)

"""
Step 4: make a prediction
Get a temperature value from the user for prediction
"""
pred = get_prediction()

#Check if the predicted temperature is within the training data range
if pred < temp.min() or pred > temp.max():
    print(f"Warning! The entered {pred} is outside the range of training data")

#Use the model to predict sales for the given temperature
prediction = model.predict([[pred]])
print(f"If the temperature is {pred}ºC, approximately {prediction[0][0]:.0f} ice creams will be sold.")

"""
Step 5: Plot the results
Scatter plot for actual data points
"""
plt.scatter(temp, sales, color='blue', label='Actual data')

#Plot the regression line
plt.plot(temp, model.predict(temp), color='red', label='Model Line')

#Add labels and title for the plot
plt.xlabel("Temperature (ºC)")
plt.ylabel("Ice cream Sales")
plt.title("Linear Regression: Ice Cream Sales vs Temperature")
plt.legend

#Display the plot
plt.show()