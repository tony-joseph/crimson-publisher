from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

from publisher.config import SITE_CONFIG


class IndexViewsTestCase(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super(IndexViewsTestCase, cls).setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(IndexViewsTestCase, cls).tearDownClass()

    def test_index_page(self):
        self.selenium.get(self.live_server_url)
        self.assertEqual(SITE_CONFIG['SITE_NAME'] in self.selenium.title, True)
