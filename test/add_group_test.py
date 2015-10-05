# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture=Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    for group_parameters in [Group("Group1", "Group1_header", "Group1_footer"), Group("", "", "")]:
        app.session.login(username="admin", password="secret")
        app.group_creation(group_parameters)
        app.session.logout()



