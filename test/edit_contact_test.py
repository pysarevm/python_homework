from model.contact import Contact
__author__ = 'Pysarev'


def test_edit_first_contact(app):
    contact1 = Contact(firstname="Rodion3", work="Airport2", dropbox1_choise=5)
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(contact1)
    app.session.logout()

