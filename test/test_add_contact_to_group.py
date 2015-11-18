from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="add_contact_to_group_test"))
    else:
        app.group.delete_groups_with_same_names()
    all_groups = db.get_group_list()
    group=random.choice(all_groups)
    print("group = ", group)
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="add_contact_to_group_test"))
    #print ("contacts_from_group: ",db.get_contacts_from_group(group))
    #print ("contacts not from group: ", db.get_contacts_not_from_group(group))
    contact=random.choice(db.get_contacts_not_from_group(group))
    app.contact.add_contact_to_group(contact, group)
    print("contact: ", contact)
    print("contacts in group: ", db.get_contacts_from_group(group))
    assert contact in db.get_contacts_from_group(group)
