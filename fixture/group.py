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
        wd.find_element_by_link_text("Групи").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def edit_first_group(self, group):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()