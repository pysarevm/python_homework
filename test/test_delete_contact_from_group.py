from model.contact import Contact
from model.group import Group
import random


def test_delete_contact_to_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="delete_contact_from_group_test"))
    else:
        app.group.delete_groups_with_same_names()
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="delete_contact_from_group_test"))
    if len(db.address_in_groups_list()) == 0:
        group=random.choice(db.get_group_list())
        contact=random.choice(db.get_contact_list())
        app.contact.add_contact_to_group(contact, group)
    else:
        c = db.address_in_groups_list()[random.randint(0, len(db.address_in_groups_list())-1)]
        contact = db.get_contact_by_id(c.id)
        group = db.get_group_by_id(c.group_id)
        print("contact: ", contact)
        print("Gropu: ", group)
        print("PRE contacts in group:", db.get_contacts_from_group(group))
    app.contact.delete_contact_from_group(contact, group)
    print("POST contacts in group:", db.get_contacts_from_group(group))
    assert contact not in db.get_contacts_from_group(group)