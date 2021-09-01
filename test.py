#### Imports ####
import unittest
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Creates Selenium test class and extends testcase
class CompSciUnitTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def test_search(self):
        driver = self.driver

        driver.get("https://www.compscillc.com")
        
        #Check if title contains compsci.
        self.assertIn("CompSci", driver.title)

        mobile_button = driver.find_element_by_

def pandas_test(self):
    s = pd.Series([1, 2, 4, 8, np.nan, 32])

    print(s)


if __name__ == "__main__":
    unittest.main()
    pandas_test()