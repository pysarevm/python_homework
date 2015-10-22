from model.group import Group
from random import randrange
__author__ = 'Pysarev'


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Edit_test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="edited1", footer="edited1")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups,  key=Group.id_or_max)