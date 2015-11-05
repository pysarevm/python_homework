from model.contact import Contact
import random
__author__ = 'Pysarev'


def test_edit_some_contact(app, db, check_ui):
    contact1 = Contact(firstname="Rodion4", company="Airport4", dropbox1_choise=5)
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="delete_test"))
    old_contacts = db.get_contact_list()
    old_contact = random.choice(old_contacts)
    contact1.id = old_contact.id
    app.contact.edit_contact_by_id(contact1.id, contact1)
    if not contact1.lastname:
        contact1.lastname = old_contact.lastname
    if not contact1.firstname:
        contact1.firstname = old_contact.firstname
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts_to_compare = [contact1 if contact.id == contact1.id else contact for contact in old_contacts]
    assert sorted(old_contacts_to_compare, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        def clean(contact):
            return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())
        ui_list = map(clean, new_contacts)
        assert sorted(ui_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)