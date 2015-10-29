# -*- coding: utf-8 -*-
from model.group import Group
import pytest
from data.groups import constant as testdata


@pytest.mark.parametrize("group_parameters", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group_parameters):
    old_groups = app.group.get_group_list()
    app.group.create(group_parameters)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group_parameters)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups,  key=Group.id_or_max)