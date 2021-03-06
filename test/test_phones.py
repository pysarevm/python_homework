__author__ = 'Pysarev'

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == app.contact.merge_phones_like_on_home_page(contact_from_edit_page)


#def test_phones_on_contact_view_page(app):
#    contact_from_view_page = app.contact.get_contact_from_view_page(0)
#    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#    assert clear(contact_from_view_page.homephone) == clear(contact_from_edit_page.homephone)
#    assert clear(contact_from_view_page.workphone) == clear(contact_from_edit_page.workphone)
#    assert clear(contact_from_view_page.mobilephone) == clear(contact_from_edit_page.mobilephone)
#    assert clear(contact_from_view_page.phone2) == clear(contact_from_edit_page.phone2)
