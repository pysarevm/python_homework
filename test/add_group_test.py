# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    for group_parameters in [Group("Group1", "Group1_header", "Group1_footer"), Group("", "", "")]:
        app.group.create(group_parameters)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 2 == len(new_groups)