from model.contact import Contact
__author__ = 'Pysarev'


def test_edit_first_contact(app):
    contact1 = Contact(firstname="Rodion4", work="Airport4", dropbox1_choise=5)
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="delete_test"))
    old_contacts = app.contact.get_contact_list()
    contact1.id = old_contacts[0].id
    app.contact.edit_first_contact(contact1)
    if not contact1.lastname:
        contact1.lastname = old_contacts[0].lastname
    if not contact1.firstname:
        contact1.firstname = old_contacts[0].firstname
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact1
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
