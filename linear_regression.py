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