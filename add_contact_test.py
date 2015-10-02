# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture=Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    contact1 = Contact("Mykola", "Volodymyrovych", "Pysarev", "NA", "engineer", "EPAM", "city. street, house",
                       "0577778881", "0679876543", "", "", "mail@yandex.ua", "", "", "www.google.com",
                       14, 6, "1982", 1, 1, "", "", "1234567890", "")
    app.login(username="admin", password="secret")
    app.add_contact_information(contact1)
    app.logout()