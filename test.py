#### Imports ####
import unittest
import time
import dataset
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import exceptions as Excpt
from DataVisualizer import DataVisualizer
import sys

#Creates Selenium test class and extends testcase
class CompSciUnitTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.db = dataset.connect('sqlite:///./testdb.db')
    
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
            # Cookies popup isn't immediately present so we wait for it to show up.
            # WebDriverWait repeatedly checks for the condition listed in the until function.
            # In this case we've also added a timeout limit of 20 seconds
            cookies_accept = WebDriverWait(driver,20).until(ec.presence_of_element_located((By.ID, "truste-consent-button")))
            cookies_accept.click()
        except:
            print("Couldn't find the cookies accept button")
            driver.quit()

        # todo: Get the table of data
        # Scrape the site
        race_links = driver.find_elements_by_xpath('//li[@class="resultsarchive-filter-item"]//a[contains(@href,"2021/races/")]')
        # print("Race Links \n\n")
        # print(race_links)
        # print("\n\n")
        races_table = self.db['races']
        race_count = len(race_links)
        for i in range(race_count):
            # Is there a better way to get this without them going stale?
            # Currently when a link is clicked it refreshes the whole section including the filter
            # causing the links to go stale over time.
            r_links = driver.find_elements_by_xpath('//li[@class="resultsarchive-filter-item"]//a[contains(@href,"2021/races/")]')
            # WebDriverWait(driver, 10).until(ec.element_to_be_clickable(race)).click()
            # race.send_keys(Keys.RETURN)
            race_name = r_links[i].text

            r_links[i].click()
            # is there a better method to wait on an asynchronous call?
            # Potentially try out
            # currently this just hard pauses all steps
            time.sleep(3)
            # find table
            # races_table.insert(dict(name=race.text))
            # WebDriverWait(driver,10).until(ec.element_to_be_clickable((By.XPATH,'//table[contains(@class,"resultsarchive-table")]/tbody/tr')))

            results = driver.find_elements_by_xpath('//table[contains(@class,"resultsarchive-table")]/tbody/tr')
            
            for result in results:
                columns = result.find_elements_by_tag_name('td')
                db_set = dict()
                db_set['name'] = columns[3].text
                db_set[race_name] = columns[7].text
                races_table.insert(db_set)
                # if races_table.find(name=db_set['name']):
                #     races_table.update(db_set, ['name'])
                # else:
                #     races_table.insert(db_set)
            # get data from table
            # - Driver name, position, points scored
            
            # pass data off to data visualizer.
        # Custom query
        results = self.db.query('SELECT * FROM races')
        db_table = self.db.load_table('races')
        table = {}
        for row in db_table:
            table[row['name']] = []
            for col in races_table.columns:
                if col != 'id' or col != 'name':
                    table[row['name']].append(row[col])
        print(table)
        print(pd.DataFrame(table), races_table.columns)
        # print(db_table)
        print(races_table.columns)
        # use the datavisualizer to print driver results
        # find users with points at azerbaijan
        # azb_scorers = races_table.find(azerbaijan>0)

        # Pause so I can look at the result
        time.sleep(10)
    
    def test_compsci(self):
        driver = self.driver

        driver.get('https://www.compscillc.com/')

        self.assertIn('CompSci', driver.title)

        try:
            WebDriverWait(driver,5).until(ec.element_to_be_clickable((By.XPATH, '//a[@href="/about"]')))
            print("The About button is clickable")
        except:
            print("The about button did not become clickable within 5 seconds.")
            #Prints the last most recent exception. In this case it should be a timeout exception
            print(sys.exc_info()[0])

        try:
            print("Testing about button for clickability...\n\n")
            driver.find(By.XPATH, '//a[@href="/about"]').click()
            print("Found and clicked about button")
        except Excpt.ElementClickInterceptedException:
            print("About button was not clickable, click intercepted")
            print(Excpt.ElementClickInterceptedException.msg)
        except Excpt.NoSuchElementException:
            print("Element not found")
            print(Excpt.NoSuchElementException.msg)
        except:
            print("Error when trying to find and click about button")
            print(sys.exc_info()[0])
        finally:
            print("About button clickability test finished.")


if __name__ == "__main__":
    unittest.main()