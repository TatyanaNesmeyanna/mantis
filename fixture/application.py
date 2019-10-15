from selenium import webdriver
from fixture.session import SessionHelper
from selenium.common.exceptions import NoSuchElementException
from fixture.project import ProjectHelper
from fixture.james import JamesHelper
from fixture.signup import SignupHelper
from fixture.mail import MailHelper


class Application:
    def __init__(self, browser, config):
        if browser=="firefox":
            self.wd = webdriver.Firefox()
        elif browser=="Chrome":
            self.wd = webdriver.Chrome()
        elif browser=="ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.james = JamesHelper(self)
        self.signup = SignupHelper(self)
        self.mail = MailHelper(self)
        self.config = config
        self.base_url = config['web']['baseUrl']
        self.project = ProjectHelper(self)

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("/login_page.php")):
            wd.get(self.base_url)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def is_login_page(self):
        try:
            self.wd.find_element_by_name("pass")
            return True
        except NoSuchElementException:
            return False

    def destroy(self):
        self.wd.quit()
