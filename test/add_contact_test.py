# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    contact1 = Contact("Mykola", "Volodymyrovych", "Pysarev", "NA", "engineer", "EPAM", "city. street, house",
                       "0577778881", "0679876543", "", "", "mail@yandex.ua", "", "", "www.google.com",
                       14, 6, "1982", 1, 1, "", "", "1234567890", "")
    app.session.login(username="admin", password="secret")
    app.contact.add_information(contact1)
    app.session.logout()
