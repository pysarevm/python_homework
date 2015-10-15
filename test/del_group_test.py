from model.group import Group
__author__ = 'Pysarev'

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="delete_test"))
    app.group.delete_first_group()
