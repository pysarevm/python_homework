from model.group import Group
__author__ = 'Pysarev'


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Edit_test"))
    app.group.edit_first_group(Group(name="edited1", footer="edited1"))
