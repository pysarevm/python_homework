from model.contact import Contact
# -*- coding: utf-8 -*-
import random
import re
__author__ = 'Pysarev'


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
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
        self.fill_the_field(field_name="home", field_content=contact.homephone)
        self.fill_the_field(field_name="mobile", field_content=contact.mobilephone)
        self.fill_the_field(field_name="work", field_content=contact.workphone)
        self.fill_the_field(field_name="fax", field_content=contact.faxphone)
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
        self.contact_cache = None

    def select_from_dropbox(self, box_number, choice_number):
        wd = self.app.wd
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[%d]//option[%d]" % (box_number, choice_number)).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[%d]//option[%d]" % (box_number, choice_number)).click()

    def update_the_dropbox(self, box_number, choice_number):
        wd = self.app.wd
        if choice_number:
           wd.find_element_by_xpath("//div[@id='content']/form/select[%d]//option[%d]" % (box_number, choice_number)).click()

    def fill_the_field(self, field_name, field_content):
        wd = self.app.wd
        if field_content:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(field_content)

    def update_the_field(self, field_name, field_content):
        wd = self.app.wd
        if field_content:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(field_content)

    def navigate_add_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("middlename")) > 0):
            self.navigate_main_page()
            wd.find_element_by_link_text("Додати контакт").click()

    #def navigate_edit_contact_page(self):
    #    wd = self.app.wd
    #    if not (len(wd.find_elements_by_name("update")) > 0 and len(wd.find_elements_by_name("middlename")) > 0):
    #        self.navigate_main_page()
    #        wd.find_elements_by_css_selector("img[alt=\"Редагувати\"]").click()

    def navigate_edit_contact_page_by_index(self, index):
        wd = self.app.wd
        if not (len(wd.find_elements_by_name("update")) > 0 and len(wd.find_elements_by_name("middlename")) > 0):
            self.navigate_main_page()
            row = wd.find_elements_by_name("entry")[index]
            cell = row.find_elements_by_tag_name("td")[7]
            cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.navigate_main_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def navigate_main_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_name("searchstring"))>0 and wd.current_url.endswith("/addressbook/") > 0):
            wd.get("http://localhost/addressbook/")
            #wd.find_element_by_link_text("Головна").click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.navigate_main_page()
        self.select_contact_by_index(index)
        #wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.navigate_main_page()
        self.contact_cache = None

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(0, contact)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.navigate_edit_contact_page_by_index(index)
        # Filling contact information
        self.update_the_field(field_name="firstname", field_content=contact.firstname)
        self.update_the_field(field_name="middlename", field_content=contact.middlename)
        self.update_the_field(field_name="lastname", field_content=contact.lastname)
        self.update_the_field(field_name="nickname", field_content=contact.nickname)
        self.update_the_field(field_name="title", field_content=contact.title)
        self.update_the_field(field_name="company", field_content=contact.company)
        self.update_the_field(field_name="address", field_content=contact.address)
        self.update_the_field(field_name="home", field_content=contact.homephone)
        self.update_the_field(field_name="mobile", field_content=contact.mobilephone)
        self.update_the_field(field_name="work", field_content=contact.workphone)
        self.update_the_field(field_name="fax", field_content=contact.faxphone)
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
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.navigate_main_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.navigate_main_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                firstname = element.find_elements_by_tag_name("td")[2].text
                lastname = element.find_elements_by_tag_name("td")[1].text
                id = element.find_element_by_name("selected[]").get_attribute("id")
                all_phones = element.find_elements_by_tag_name("td")[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  all_phones_from_home_page = all_phones))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.navigate_edit_contact_page_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, phone2=phone2)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("Домашній телефон: (.*)", text).group(1)
        workphone = re.search("Робочий телефон: (.*)", text).group(1)
        mobilephone = re.search("Мобільний телефон: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, phone2=phone2)