# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.initializer import HelperInitializer
__author__ = 'Pysarev'


class Application:
    def __init__(self):
        self.wd = WebDriver()
        initializer = HelperInitializer(self)
        initializer.initialize_helper()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()