from model.contact import Contact
__author__ = 'Pysarev'

def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="delete_test"))
    app.contact.delete_first_contact()
