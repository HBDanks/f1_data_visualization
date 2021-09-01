import numpy as np
import pandas as pd

class PandasTest():
    def __init__(self):
        self.test_array = [1,2,3,4,5]

    def pandas_test(self):
        series = pd.Series(self.test_array)

        print(series)

    def pandas_main(self):
        self.pandas_test()

if __name__ == "__main__":
    pt = PandasTest()
    pt.pandas_main()