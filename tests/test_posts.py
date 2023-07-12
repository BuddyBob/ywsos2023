import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#run server
#run client
class Test(unittest.TestCase):
    def setUp(self):
        self.options = Options()
        self.options.add_experimental_option("detach",True)
        self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=self.options)
        self.driver.get("http://localhost:5173/posts")
    def test_click(self):
        WebDriverWait(self.driver, 10)#.until(EC.presence_of_element_located(("xpath","//div[contains(@class, 'col btn btn-primary button float-right')]")))
        btns = self.driver.find_elements("xpath","//div[contains(@class, 'col btn btn-primary button float-right')]")
        for btn in btns:
            btn.click()
    def test_href(self):
        WebDriverWait(self.driver, 10)
        links = self.driver.find_elements("xpath","//div[contains(@href, '#')]")
        for link in links:
            link.click()
    def tearDown(self):
        self.driver.close()
if __name__=="__main__":
    unittest.main()
##check if register works
#exaustivly check it