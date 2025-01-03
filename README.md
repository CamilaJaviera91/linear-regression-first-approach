# Ice Cream Sales Prediction Using Linear Regression

This project implements a simple linear regression model to predict ice cream sales based on temperature. It includes user interaction for collecting data, building the regression model, making predictions, and visualizing results.

---

## Features
- **Data Collection**: Interactive script for inputting temperature and sales data.
- **Linear Regression Model**: Uses `scikit-learn` to train a regression model on the collected data.
- **Prediction**: Allows users to input a temperature and predicts corresponding ice cream sales.
- **Visualization**: Generates a scatter plot of the data points and the regression line.

---

## Files Description
### `collect_data.py`
This script collects temperature and sales data from the user interactively. It ensures the data is consistent and converts it into NumPy arrays for further processing.

#### Key Functions:
- **`collect_data()`**:
  - Prompts the user to input temperature and sales values.
  - Ensures both lists have the same length.
  - Converts the data into NumPy arrays for model training.

### `linear_regression.py`
This script handles the creation and training of the linear regression model. It:
- Collects data using the `collect_data` module.
- Trains a regression model using the collected data.
- Makes predictions based on user input.
- Visualizes the results with a scatter plot and regression line.

#### Steps:
1. **Data Collection**: Uses `collect_data()` from `collect_data.py`.
2. **Data Sorting**: Sorts data for better visualization.
3. **Model Training**: Trains a linear regression model on the collected data.
4. **Prediction**: Prompts the user for a temperature value to predict sales.
5. **Visualization**: Plots actual data and the regression line.

### `prediction.py`
Contains a utility function to get a valid temperature input for predictions.

#### Key Functions:
- **`get_prediction()`**:
  - Prompts the user for a temperature value.
  - Ensures the input is a valid integer.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ice-cream-sales-prediction.git
   cd ice-cream-sales-prediction
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage
1. Run the `linear_regression.py` script:
   ```bash
   python linear_regression.py
   ```
2. Follow the prompts to:
   - Input temperature and sales data.
   - Input a temperature for sales prediction.
3. View the scatter plot and regression line for the data.

---

## Example
### Input Data:
```text
Temperature: 25, 30, 35
Sales: 200, 300, 400
```

### Prediction:
```text
Enter a temperature to predict sales: 28
Prediction: Approximately 240 ice creams will be sold.
```

### Visualization:
A plot showing the relationship between temperature and sales, along with the regression line.

---

## Requirements
- Python 3.7+
- NumPy
- Matplotlib
- scikit-learn
