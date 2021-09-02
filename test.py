#### Imports ####
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
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
        desired_site = driver.find_element_by_xpath('//a[contains(@href,"www.formula1.com")]')

        desired_site.click()
        # driver.implicitly_wait(1)
        #accept cookies
        try:
            cookies_accept = WebDriverWait(driver,10).until(ec.presence_of_element_located((By.ID, "truste-consent-button")))
            cookies_accept.click()
        except:
            print("Couldn't find the cookies accept button")
            driver.quit()

        # todo: Get the table of data
        # Scrape the site
        race_links = driver.find_elements_by_css_selector('a.ArchiveLink')
        for race in race_links:
            race.click()
            # find table

            # get data from table
            # - Driver name, position, points scored
            
            # pass data off to data visualizer.
            driver.implicitly_wait(10)
        print(race_links)
        # use the datavisualizer to print driver results

        # Pause so I can look at the result
        time.sleep(10)


if __name__ == "__main__":
    unittest.main()