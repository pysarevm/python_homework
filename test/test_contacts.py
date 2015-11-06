import random
from model.contact import Contact


def test_contacts_on_home_page(app, db):
    contacts_from_home_page = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list()
    assert len(contacts_from_home_page) == len(contacts_from_db)
    for contact in contacts_from_db:
        contact.all_phones_from_home_page = app.contact.merge_phones_like_on_home_page(contact)
        contact.all_emails = app.contact.merge_emails_like_on_home_page(contact)
        if contact.firstname:
            contact.firstname= contact.firstname.strip()
        else:
            contact.firstname = ''
        if contact.lastname:
            contact.lastname= contact.lastname.strip()
        else:
            contact.lastname = ''
        if contact.address:
            contact.address = contact.address.strip()
        else:
            contact.address = ''
    print("from home page: ", contacts_from_home_page)
    print("from DB: ", contacts_from_db)
    sorted_contacts_from_home_page = sorted(contacts_from_home_page, key=Contact.id_or_max)
    sorted_contacts_from_db = sorted(contacts_from_db,  key=Contact.id_or_max)
    for i in range(0, len(contacts_from_db)-1):
        print("iteration: ",i)
        assert (sorted_contacts_from_home_page[i] == sorted_contacts_from_db[i] and
                sorted_contacts_from_home_page[i].address == sorted_contacts_from_db[i].address and
                sorted_contacts_from_home_page[i].all_phones_from_home_page == sorted_contacts_from_db[i].all_phones_from_home_page and
                sorted_contacts_from_home_page[i].all_emails == sorted_contacts_from_db[i].all_emails)
