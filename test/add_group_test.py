# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])


testdata = [Group("", "", "")]+[
    Group(name=random_string("Name", 10), header=random_string("Header", 20), footer=random_string("Footer", 20))
    for i in range(3)
]

@pytest.mark.parametrize("group_parameters", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group_parameters):
    old_groups = app.group.get_group_list()
    app.group.create(group_parameters)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group_parameters)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups,  key=Group.id_or_max)