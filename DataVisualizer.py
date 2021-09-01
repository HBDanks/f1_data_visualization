#### Imports ####
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.close("all")

#Create data visualization tool.
class DataVisualizer():
    def __init__(self, _data):
        print("Initializing data visualizer...")
        self.data = pd.Series(_data)
        print("Data visualizer initialized.\n\n")

    def series_plotter(self):
        # generate pandas series
        series = self.data
        series = series.cumsum()
        series.plot()
        self.series = series

    def series_show(self):
        plt.show()


if __name__ == "__main__":
    dv = DataVisualizer(np.random.randn(1000))
    dv.series_plotter()
    dv.series_show()