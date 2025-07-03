import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
# Data
y = np.array([10, 10, 15, 20, 12, 13, 20])
labels = ["Java", "Python", "C++", "SQL", "JavaScript", "C#", "Go"]
# Initial explode configuration
initial_explode = [0.0] * len(y)
# Create the figure and pie chart
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.3, bottom=0.4)  # Leave room for sliders
# Function to draw pie chart
def draw_pie(explode_vals):
    ax.clear()
    wedges, texts, autotexts = ax.pie(
        y,
        labels=labels,
        explode=explode_vals,
        autopct='%1.1f%%'
    )
    ax.legend(title="Languages:", loc="center left", bbox_to_anchor=(1, 0.5))
    fig.canvas.draw_idle()
# Draw initial chart
draw_pie(initial_explode)
# Create sliders for each slice
slider_axes = []
sliders = []
for i, label in enumerate(labels):
    ax_slider = plt.axes([0.25, 0.35 - i*0.04, 0.5, 0.02])  # [left, bottom, width, height]
    slider = Slider(ax_slider, label, 0.0, 0.5, valinit=0.0)
    slider_axes.append(ax_slider)
    sliders.append(slider)
# Update function for all sliders
def update(val):
    explode_vals = [slider.val for slider in sliders]
    draw_pie(explode_vals)
# Connect all sliders to update function
for slider in sliders:
    slider.on_changed(update)
plt.show()
