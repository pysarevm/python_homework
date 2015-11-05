# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, db, check_ui, json_groups):
    group_parameters = json_groups
    old_groups = db.get_group_list()
    app.group.create(group_parameters)
    new_groups = db.get_group_list()
    old_groups.append(group_parameters)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups,  key=Group.id_or_max)
    if check_ui:
        def clean(group):
            return Group(id=group.id, name=group.name.strip())
        ui_list = map(clean, new_groups)
        assert sorted(ui_list, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)