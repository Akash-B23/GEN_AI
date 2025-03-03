import numpy as np
import matplotlib.pyplot as plt

# Generating some random data points around a linear equation y = 4x + 3
x = np.random.normal(12, 5, 10)  # 10 random numbers with mean=12 and std=5
noise = np.random.normal(0, 1, 10)  # Mean as 0 and Standard deviation as 1
y = 4 * x + 3  # Defining the actual relationship

# Initial guesses for slope (m1) and intercept (m2)
m1_current = 0  
m2_current = 0  

# List to store the mean squared error (cost) and the updated m1 and m2 values
mse_List =[]
m1_Values=[]
m2_Values=[]

def gradient_descent(x, y, m1_current, m2_current):
    learning_rate = 0.001  # Small steps to prevent overshooting
    iterations = 20  # We will update our values 10,000 times
    n = len(x)  # Number of data points

    for i in range(iterations):
        # Calculate predicted y values using the current guess for m1 and m2
        y_predicted = m1_current * x + m2_current 
        
        # Compute the mean squared error (cost function)
        cost = (1/n) * sum((y - y_predicted) ** 2)
        mse_List.append(cost)
        m1_Values.append(m1_current)
        
        # Calculate gradients (how much we need to adjust m1 and m2)
        m1_d = -(2/n) * sum(x * (y - y_predicted))  # Partial derivative w.r.t. m1
        m2_d = -(2/n) * sum(y - y_predicted)  # Partial derivative w.r.t. m2
        
        # Update m1 and m2 by moving in the opposite direction of the gradient
        m1_current -= learning_rate * m1_d
        m2_current -= learning_rate * m2_d

        # Print the progress
        print(f"Iteration {i}: m1 = {m1_current:.4f}, m2 = {m2_current:.4f}, Cost = {cost:.4f}")
    
    return m1_current, m2_current  # Return the final values of m1 and m2

# Running the gradient descent function and plotting the graph
m1_finalValue,m2_finalValue = gradient_descent(x, y, m1_current, m2_current)
plt.scatter(x, y, color='blue', label='Data Points')  # Scatter plot of actual data
plt.plot(x, m1_finalValue * x + m2_finalValue, color='red', label=f'Best Fit Line: y = {m1_finalValue:.2f}x + {m2_finalValue:.2f}')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Linear Regression using Gradient Descent')
plt.show()

# Plotting the graph for MSE Vs No of Iterations

plt.plot(range(len(mse_List)),mse_List, color='blue')
plt.xlabel('No of iterations')
plt.ylabel('Mean Squared Error (MSE)')
plt.title('MSE vs No of Iterations')
plt.grid(True)
plt.show()

# Ploting the graph for Loss (MSE) vs. m1

plt.plot(m1_Values, mse_List, color='blue')
plt.xlabel('m1 (Slope)')
plt.ylabel('Mean Squared Error (MSE)')
plt.title('Loss (MSE) vs. m1')
plt.grid(True)
plt.show()

