import random


def test_phones_on_home_page(app):
    contacts_quantity = len(app.contact.get_contact_list())
    contact_number = random.randrange(contacts_quantity)
    contact_from_home_page = app.contact.get_contact_list()[contact_number]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(contact_number)
    print (contact_from_edit_page, contact_from_home_page)
    assert (contact_from_home_page.firstname == contact_from_edit_page.firstname and
        contact_from_home_page.lastname == contact_from_edit_page.lastname and
        contact_from_home_page.address == contact_from_edit_page.address and
        contact_from_home_page.all_emails == app.contact.merge_emails_like_on_home_page(contact_from_edit_page) and
        contact_from_home_page.all_phones_from_home_page == app.contact.merge_phones_like_on_home_page(contact_from_edit_page))