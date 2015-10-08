# -*- coding: utf-8 -*-
import random
__author__ = 'Pysarev'


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def add_information(self, contact):
        wd = self.app.wd
        # init contact creation
        self.navigate_add_contact_page()
        # Filling contact information
        self.fill_the_field(field_name="firstname", field_content=contact.firstname)
        self.fill_the_field(field_name="middlename", field_content=contact.middlename)
        self.fill_the_field(field_name="lastname", field_content=contact.lastname)
        self.fill_the_field(field_name="nickname", field_content=contact.nickname)
        self.fill_the_field(field_name="title", field_content=contact.title)
        self.fill_the_field(field_name="company", field_content=contact.company)
        self.fill_the_field(field_name="address", field_content=contact.address)
        self.fill_the_field(field_name="home", field_content=contact.home)
        self.fill_the_field(field_name="mobile", field_content=contact.mobile)
        self.fill_the_field(field_name="work", field_content=contact.work)
        self.fill_the_field(field_name="fax", field_content=contact.fax)
        self.fill_the_field(field_name="email", field_content=contact.email)
        self.fill_the_field(field_name="email2", field_content=contact.email2)
        self.fill_the_field(field_name="email3", field_content=contact.email3)
        self.fill_the_field(field_name="homepage", field_content=contact.homepage)
        self.select_from_dropbox(box_number=1, choice_number=contact.get_random_date())
        self.select_from_dropbox(box_number=2, choice_number=contact.get_random_month())
        self.fill_the_field(field_name="byear", field_content=contact.byear)
        self.select_from_dropbox(box_number=3, choice_number=contact.get_random_date())
        self.select_from_dropbox(box_number=4, choice_number=contact.get_random_month())
        self.fill_the_field(field_name="ayear", field_content=contact.ayear)
        self.fill_the_field(field_name="address2", field_content=contact.address2)
        self.fill_the_field(field_name="phone2", field_content=contact.phone2)
        self.fill_the_field(field_name="notes", field_content=contact.notes)
        # Submit contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def select_from_dropbox(self, box_number, choice_number):
        wd = self.app.wd
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[%d]//option[%d]" % (box_number, choice_number)).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[%d]//option[%d]" % (box_number, choice_number)).click()

    def update_the_dropbox(self, box_number, choice_number):
        wd = self.app.wd
        if choice_number == 0:
            pass
        else:
           wd.find_element_by_xpath("//div[@id='content']/form/select[%d]//option[%d]" % (box_number, choice_number)).click()

    def fill_the_field(self, field_name, field_content):
        wd = self.app.wd
        if field_content:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(field_content)

    def update_the_field(self, field_name, field_content):
        wd = self.app.wd
        if field_content == "":
            pass
        else:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(field_content)

    def navigate_add_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Додати контакт").click()

    def navigate_edit_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("img[alt=\"Редагувати\"]").click()

    def navigate_main_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Головна").click()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.navigate_main_page()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.navigate_edit_contact_page()
        # Filling contact information
        self.update_the_field(field_name="firstname", field_content=contact.firstname)
        self.update_the_field(field_name="middlename", field_content=contact.middlename)
        self.update_the_field(field_name="lastname", field_content=contact.lastname)
        self.update_the_field(field_name="nickname", field_content=contact.nickname)
        self.update_the_field(field_name="title", field_content=contact.title)
        self.update_the_field(field_name="company", field_content=contact.company)
        self.update_the_field(field_name="address", field_content=contact.address)
        self.update_the_field(field_name="home", field_content=contact.home)
        self.update_the_field(field_name="mobile", field_content=contact.mobile)
        self.update_the_field(field_name="work", field_content=contact.work)
        self.update_the_field(field_name="fax", field_content=contact.fax)
        self.update_the_field(field_name="email", field_content=contact.email)
        self.update_the_field(field_name="email2", field_content=contact.email2)
        self.update_the_field(field_name="email3", field_content=contact.email3)
        self.update_the_field(field_name="homepage", field_content=contact.homepage)
        self.update_the_dropbox(box_number=1, choice_number=contact.dropbox1_choise)
        self.update_the_dropbox(box_number=2, choice_number=contact.dropbox2_choise)
        self.update_the_field(field_name="byear", field_content=contact.byear)
        self.update_the_dropbox(box_number=3, choice_number=contact.dropbox3_choise)
        self.update_the_dropbox(box_number=4, choice_number=contact.dropbox4_choise)
        self.update_the_field(field_name="ayear", field_content=contact.ayear)
        self.update_the_field(field_name="address2", field_content=contact.address2)
        self.update_the_field(field_name="phone2", field_content=contact.phone2)
        self.update_the_field(field_name="notes", field_content=contact.notes)
        # Update contact
        wd.find_element_by_name("update").click()