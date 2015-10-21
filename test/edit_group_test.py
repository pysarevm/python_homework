from model.group import Group
__author__ = 'Pysarev'


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Edit_test"))
    old_groups = app.group.get_group_list()
    group = Group(name="edited1", footer="edited1")
    group.id = old_groups[0].id
    app.group.edit_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups,  key=Group.id_or_max)