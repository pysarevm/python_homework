from model.group import Group
__author__ = 'Pysarev'


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="edited1", footer="edited1"))
    app.session.logout()