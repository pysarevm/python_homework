from model.contact import Contact
from random import randrange
__author__ = 'Pysarev'


def test_edit_some_contact(app):
    contact1 = Contact(firstname="Rodion4", work="Airport4", dropbox1_choise=5)
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="delete_test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact1.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact1)
    if not contact1.lastname:
        contact1.lastname = old_contacts[index].lastname
    if not contact1.firstname:
        contact1.firstname = old_contacts[index].firstname
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact1
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
