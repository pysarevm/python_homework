from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, db):
    #contact_without_group = []
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="add_contact_to_group_test"))
    #all_groups = db.get_group_list()
    #group=random.choice(all_groups)
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="add_contact_to_group_test"))
    all_groups = db.get_group_list()
    print("all_groups PRE: ", all_groups)
    app.group.delete_groups_with_same_names()
    print("all_groups POST: ", db.get_group_list())
    #for c in db.get_contact_list:
    #    for address_in_groups in (db.address_in_groups_list()):
    #        if c.id != address_in_groups.id:





   # contact_parameters = json_contacts
   # old_contacts = db.get_contact_list()
   # app.contact.create(contact_parameters)
   # new_contacts = db.get_contact_list()
   # assert len(old_contacts) + 1 == len(new_contacts)
   # old_contacts.append(contact_parameters)
    #assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts,  key=Contact.id_or_max)
    #if check_ui:
   #     def clean(contact):
   #         return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())
    #    ui_list = map(clean, new_contacts)
    #    assert sorted(ui_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)