import unittest
import os
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.touch_actions import TouchActions
from time import sleep
from math import floor


class Unique(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': '/Users/bogdanbucur/PycharmProjects/Unique/Unique.app',
                'automationName': 'XCUITest',
                'platformName': 'iOS',
                'platformVersion': '10.3',
                'deviceName': 'iPhone 7',
                'noReset': True,
                'fullReset': False
            })

    def tearDown(self):
        self.driver.quit()

    def test_001(self):
        sleep(2)

        # Allow notifications
        try:
            self.driver.find_element_by_accessibility_id('Allow').click()
            sleep(1)
        except:
            pass

        tocList = self.driver.find_elements_by_class_name('XCUIElementTypeStaticText')
        length = len(tocList)

        # Iterate ToC list and Scroll to bottom
        for i in range(int(floor(length / 4))):
            xI = 180
            yI = 90
            xI2 = 180
            yI2 = 550

            self.driver.swipe(xI2, yI2, xI - xI2, yI - yI2, 100)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Unique)
    unittest.TextTestRunner(verbosity=2).run(suite)
