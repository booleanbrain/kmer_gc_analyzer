import k_mer_plot

data = [1, 0, -1, -2, -1, 0, 2, 4, 3, 1]
result = k_mer_plot.plot_cumulative_skew(data, "test_plot2.png")

print(result)
