# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture=Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    for group_parameters in [Group("Group1", "Group1_header", "Group1_footer"), Group("", "", "")]:
        app.login(username="admin", password="secret")
        app.group_creation(group_parameters)
        app.logout()



