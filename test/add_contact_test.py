# -*- coding: utf-8 -*-
from model.contact import Contact



def test_add_contact(app):
    contact1 = Contact("Rodion", "Mykolayovych", "Pysarev", "NA", "engineer", "Buran", "city. street, house",
                       "0577778881", "0679876543", "", "", "mail@yandex.ua", "", "", "www.google.com",
                       14, 6, "1982", 1, 1, "", "", "1234567890", "", None)
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact1)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact1)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts,  key=Contact.id_or_max)