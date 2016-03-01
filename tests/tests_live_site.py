from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver


class LiveSiteTests(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super(LiveSiteTests, cls).setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(LiveSiteTests, cls).tearDownClass()

    def test_site(self):
        self.selenium.get(self.live_server_url)
