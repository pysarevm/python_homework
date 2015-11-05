from model.contact import Contact
import random
__author__ = 'Pysarev'


def test_del_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="delete_test"))
    old_contacts = db.get_contact_list()
    old_contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(old_contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(old_contact)
    assert old_contacts == new_contacts
    if check_ui:
        def clean(contact):
            return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())
        ui_list = map(clean, new_contacts)
        assert sorted(ui_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)