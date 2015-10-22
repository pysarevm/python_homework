from model.group import Group
# -*- coding: utf-8 -*-
__author__ = 'Pysarev'


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
            wd = self.app.wd
            self.open_group_page()
            # init group creation
            wd.find_element_by_name("new").click()
            self.fill_group_form(group)
            # submit group creation
            wd.find_element_by_name("submit").click()
            self.return_to_groups_page()
            self.group_cache = None

    def fill_group_form(self, group):
        wd = self.app.wd
        self.fill_field("group_name", group.name)
        self.fill_field("group_header", group.header)
        self.fill_field("group_footer", group.footer)

    def fill_field(self, field_name, field_data):
        wd = self.app.wd
        if field_data is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(field_data)

    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len( wd.find_elements_by_name("new")) > 0):
            self.navigate_main_page()
            wd.find_element_by_link_text("Групи").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def edit_first_group(self, group):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    def navigate_main_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_name("searchstring"))>0 and wd.current_url.endswith("/addressbook/") > 0):
            wd.get("http://localhost/addressbook/")

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)