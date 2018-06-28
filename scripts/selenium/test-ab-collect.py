import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ABCollectLoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_third_party_login(self):
        driver = self.driver
        driver.get("http://abcollect.service.dev.africanbank.net")
        self.assertIn("Login", driver.title)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys("trace@collections.co.za")
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("Password012")
        elem.send_keys(Keys.RETURN)
        self.assertIn("Project Lulu", driver.title)
        driver.implicitly_wait(30)  # seconds




    def tearDown(self):
        self.driver.close()
        # self.driver.quit()

if __name__ == "__main__":
    unittest.main()



# for a in ['200356002','9989971E003','9948165006']:
#     acc = Account.objects.get(loan_ref=a)
#     acc.closed_date = datetime(2018, 5, 10)
#     acc.closed_by = 'African Bank - TEST'
#     acc.status = 'Closed'
#     acc.save()

acc = Account.objects.get(loan_ref='9948165006')
acc.closed_date = datetime(2018, 5, 28)
acc.closed_by = 'African Bank - TEST'
acc.status = 'Closed'
acc.save()