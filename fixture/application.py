# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.initializer import HelperInitializer
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
__author__ = 'Pysarev'



class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        initializer = HelperInitializer(self)
        initializer.initialize_helper()
       # self.session = SessionHelper(self)
       # self.group = GroupHelper(self)
       # self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()