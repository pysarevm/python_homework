# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, db, check_ui, json_contacts):
    contact_parameters = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(contact_parameters)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact_parameters)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts,  key=Contact.id_or_max)
    if check_ui:
        def clean(contact):
            return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())
        ui_list = map(clean, new_contacts)
        print("!!!", ui_list)
        assert sorted(ui_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)