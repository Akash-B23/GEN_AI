import numpy as np
import matplotlib.pyplot as plt

def heart_outline():
    """
    These are the steps i followed to create a heart-shaped function.

    1. I started by creating an array 't' with 300 numbers ranging from 0 to 2π. 
       This array acts as a guide for drawing the curve.
    
    2. Then, I used some trigonometry to calculate the x and y coordinates:
       i) For x, I used the formula: 16 * sin(t)^3. This helps shape the horizontal part of the heart.
       ii) For y, I combined several cosine functions: 13 * cos(t) - 5 * cos(2*t) - 2 * cos(3*t) - cos(4*t). 
         This gives the heart its vertical curves.
    
    3. Next, I set up a square plot (6x6 inches) so that the heart doesn’t look stretched.
    
    4. I then plotted the heart with a red line and set the line thickness to 2.
    
    5. To make the plot easier to understand, I added a grid with dashed lines, and drew the x and y axes at the center (0,0).
    
    6. I set the x and y limits from -20 to 20 so that the heart fits nicely in the view.
    
    7. Finally, I added a title and labels for the x-axis and y-axis, then displayed the plot.
    
    """
    
    # I created a list of 300 values from 0 to 2π.
    t = np.linspace(0, 2 * np.pi, 300)
    
    # calculated the x and y coordinates for the heart shape using trigonometry.
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    
    # a 6x6 inch figure to ensure the heart is proportionate.
    plt.figure(figsize=(6, 6))
    
    # plotted the heart in red with a thicker line.
    plt.plot(x, y, 'r', linewidth=2)
    
    # added a dashed grid to the background.
    plt.grid(True, linestyle='--', alpha=0.6)
    
    # drew the x and y axes in black to mark the center.
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    
    # set the axis limits so the heart fits nicely.
    plt.xlim(-20, 20)
    plt.ylim(-20, 20)
    
    # added a title and labels for clarity.
    plt.title("Heart Outline")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    
    # I displayed the plot here.
    plt.show()

# calling the function to draw the heart.
heart_outline()
