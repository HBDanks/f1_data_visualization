#### Imports ####
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from DataVisualizer import DataVisualizer

#Creates Selenium test class and extends testcase
class CompSciUnitTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def test_search(self):
        driver = self.driver

        driver.get("https://google.com")
        
        #Check if title contains compsci.
        self.assertIn("Google", driver.title)
        
        #Get the search bar
        search = driver.find_element_by_name("q")

        #Fill out search bar
        search.send_keys("formula 1 championship 2021 race results")

        # query
        search.send_keys(Keys.RETURN)
        
        
        #navigate to formula1 website
        # using xpath we can specify the value of the attribute we'd like to get
        desired_site = driver.find_element_by_xpath('//a[@href="https://www.formula1.com/en/results.html"]')

        desired_site.click()

        # todo: Get the table of data
        # Scrape the site
        # use the datavisualizer to print driver results

        # Pause so I can look at the result
        time.sleep(10)


if __name__ == "__main__":
    unittest.main()