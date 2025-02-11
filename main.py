import time_series_visualizer

# Generate and save the line plot
line_fig = time_series_visualizer.draw_line_plot()
line_fig.savefig("line_plot.png")

# Generate and save the bar chart
bar_fig = time_series_visualizer.draw_bar_plot()
bar_fig.savefig("bar_plot.png")

# Generate and save the box plots
box_fig = time_series_visualizer.draw_box_plot()
box_fig.savefig("box_plot.png")

print("Plots saved successfully.")
