# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    for group_parameters in [Group("Group1", "Group1_header", "Group1_footer"), Group("", "", "")]:
        app.session.login(username="admin", password="secret")
        app.group.create(group_parameters)
        app.session.logout()