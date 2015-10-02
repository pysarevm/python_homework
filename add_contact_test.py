# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest, random
# random.randomrange(1,14,1) from 1 to 14 with step 1

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class Contact:
    def __init__(self, firstname, middlename, lastname, nickname, title, company, address, home, mobile, work, fax,
                 email, email2, email3, homepage, dropbox1_choise, dropbox2_choise, byear, dropbox3_choise,
                 dropbox4_choise, ayear, address2, phone2, notes):
        self.firstname=firstname
        self.middlename=middlename
        self.lastname=lastname
        self.nickname=nickname
        self.title=title
        self.company=company
        self.address=address
        self.home=home
        self.mobile=mobile
        self.work=work
        self.fax=fax
        self.email=email
        self.email2=email2
        self.email3=email3
        self.homepage=homepage
        self.dropbox1_choise=dropbox1_choise
        self.dropbox2_choise=dropbox2_choise
        self.byear=byear
        self.dropbox3_choise=dropbox3_choise
        self.dropbox4_choise=dropbox4_choise
        self.ayear=ayear
        self.address2=address2
        self.phone2=phone2
        self.notes=notes




class add_contact_test(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.add_contact_information(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Вийти").click()

    def add_contact_information(self, wd):
        # init contact creation
        self.navigate_add_contact_page(wd)
        # Filling contact information
        self.fill_the_field(wd, field_name="firstname", field_content="Mykola")
        self.fill_the_field(wd, field_name="middlename", field_content="Volodymyrovych")
        self.fill_the_field(wd, field_name="lastname", field_content="Pysarev")
        self.fill_the_field(wd, field_name="nickname", field_content="NA")
        self.fill_the_field(wd, field_name="title", field_content="engineer")
        self.fill_the_field(wd, field_name="company", field_content="EPAM")
        self.fill_the_field(wd, field_name="address", field_content="city. street, house")
        self.fill_the_field(wd, field_name="home", field_content="0577778881")
        self.fill_the_field(wd, field_name="mobile", field_content="0679876543")
        self.fill_the_field(wd, field_name="work", field_content="")
        self.fill_the_field(wd, field_name="fax", field_content="")
        self.fill_the_field(wd, field_name="email", field_content="mail@yandex.ua")
        self.fill_the_field(wd, field_name="email2", field_content="")
        self.fill_the_field(wd, field_name="email3", field_content="")
        self.fill_the_field(wd, field_name="homepage", field_content="www.google.com")
        self.select_from_dropbox(wd, box_number=1, choice_number=14)
        self.select_from_dropbox(wd, box_number=2, choice_number=6)
        self.fill_the_field(wd, field_name="byear", field_content="1982")
        self.select_from_dropbox(wd, box_number=3, choice_number=1)
        self.select_from_dropbox(wd, box_number=4, choice_number=1)
        self.fill_the_field(wd, field_name="ayear", field_content="")
        self.fill_the_field(wd, field_name="address2", field_content="some address")
        self.fill_the_field(wd, field_name="phone2", field_content="0987654321")
        self.fill_the_field(wd, field_name="notes", field_content="")
        # Submit contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def select_from_dropbox(self, wd, box_number, choice_number):
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[%d]//option[%d]" % (box_number, choice_number)).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[%d]//option[%d]" % (box_number, choice_number)).click()

    def fill_the_field(self, wd, field_name, field_content):
        wd.find_element_by_name(field_name).click()
        wd.find_element_by_name(field_name).clear()
        wd.find_element_by_name(field_name).send_keys(field_content)

    def navigate_add_contact_page(self, wd):
        wd.find_element_by_link_text("Додати контакт").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
