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

    def random_choise(self, dropbox_number):
        if dropbox_number == 1:
            return random.randint(1, 33)
        elif dropbox_number == 2:
            return random.randint(1, 13)
        elif dropbox_number == 3:
            return random.randint(1, 33)
        elif dropbox_number == 4:
            return random.randint(1, 13)
        else:
            print("There is no ", dropbox_number, " dropbox number available. Please, chose between 1, 2, 3, 4")

class add_contact_test(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_add_contact(self):
        contact1 = Contact("Mykola", "Volodymyrovych", "Pysarev", "NA", "engineer", "EPAM", "city. street, house",
                           "0577778881", "0679876543", "", "", "mail@yandex.ua", "", "", "www.google.com",
                           14, 6, "1982", 1, 1, "", "", "1234567890", "")
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.add_contact_information(wd, contact1)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Вийти").click()

    def add_contact_information(self, wd, contact):
        # init contact creation
        self.navigate_add_contact_page(wd)
        # Filling contact information
        self.fill_the_field(wd, field_name="firstname", field_content=contact.firstname)
        self.fill_the_field(wd, field_name="middlename", field_content=contact.middlename)
        self.fill_the_field(wd, field_name="lastname", field_content=contact.lastname)
        self.fill_the_field(wd, field_name="nickname", field_content=contact.nickname)
        self.fill_the_field(wd, field_name="title", field_content=contact.title)
        self.fill_the_field(wd, field_name="company", field_content=contact.company)
        self.fill_the_field(wd, field_name="address", field_content=contact.address)
        self.fill_the_field(wd, field_name="home", field_content=contact.home)
        self.fill_the_field(wd, field_name="mobile", field_content=contact.mobile)
        self.fill_the_field(wd, field_name="work", field_content=contact.work)
        self.fill_the_field(wd, field_name="fax", field_content=contact.fax)
        self.fill_the_field(wd, field_name="email", field_content=contact.email)
        self.fill_the_field(wd, field_name="email2", field_content=contact.email2)
        self.fill_the_field(wd, field_name="email3", field_content=contact.email3)
        self.fill_the_field(wd, field_name="homepage", field_content=contact.homepage)
        self.select_from_dropbox(wd, box_number=1, choice_number=contact.random_choise(1))
        self.select_from_dropbox(wd, box_number=2, choice_number=contact.random_choise(2))
        self.fill_the_field(wd, field_name="byear", field_content=contact.byear)
        self.select_from_dropbox(wd, box_number=3, choice_number=contact.random_choise(3))
        self.select_from_dropbox(wd, box_number=4, choice_number=contact.random_choise(4))
        self.fill_the_field(wd, field_name="ayear", field_content=contact.ayear)
        self.fill_the_field(wd, field_name="address2", field_content=contact.address2)
        self.fill_the_field(wd, field_name="phone2", field_content=contact.phone2)
        self.fill_the_field(wd, field_name="notes", field_content=contact.notes)
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
