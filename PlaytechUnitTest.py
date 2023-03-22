import unittest 
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PlaytechQATesting(unittest.TestCase):
    def test_firstTest(self):
        self.driver = webdriver.Chrome()
        self.actions = ActionChains(self.driver)
        self.driver.get("https://www.playtech.ee/")
        # Maximizing the window because the test is run under the assummption we can see the Navbar ontop
        self.driver.maximize_window()
        
        # Finding the location of the internship button. The click option is available as an alternative to not using cordinates
        internshipButton = self.driver.find_element(By.XPATH, "//a[@class='menu-item font-size-sm text-uppercase font-weight-bold'][normalize-space()='Internship']")
        location = internshipButton.location
        print(location)
        # internshipButton.click()
        self.actions.move_by_offset(1192,0).click().perform()

        # Waiting until the presence of the Internship logo in the Internship page is present
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='display-1']")))

        get_source = self.driver.page_source
        # Text we want to find in the page
        search_text1 = "Summer Internship 2023"
        search_text2 = "Development QA Engineer (Intern)"
        # print True if text is present else False
        print(search_text1 in get_source)
        print(search_text2 in get_source)
        f = open('results.txt' , 'w')
        lines = ["'Summer Internship 2023' was found in the page "+ str(search_text1 in get_source)+"\n", "'Development QA Engineer (Intern)' was found in the page "+str(search_text2 in get_source)]
        f.writelines(lines)


if __name__ == "__main__":
    unittest.main()
