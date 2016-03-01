from django.test import LiveServerTestCase, Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from selenium.webdriver.firefox.webdriver import WebDriver


class UserProfileViewTestCase(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super(UserProfileViewTestCase, cls).setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(UserProfileViewTestCase, cls).tearDownClass()

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test1234', first_name='test', last_name='user')

    def test_user_profile_view(self):
        self.selenium.get("{}{}".format(self.live_server_url, reverse('accounts:user_profile_view', kwargs={
            'username': self.user.username
        })))
        self.assertEqual("test" in self.selenium.title, True)
        self.assertEqual("user" in self.selenium.title, True)
        self.assertEqual("test" in self.selenium.page_source, True)
        self.assertEqual("user" in self.selenium.page_source, True)
