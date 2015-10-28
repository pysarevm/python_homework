# -*- coding: utf-8 -*-
from model.contact import Contact
import string
import random
import pytest
import re


def random_string(prefix="", maxlen=0):
    symbols = re.sub("'", "", string.ascii_letters + string.digits + string.punctuation + " "*10)
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])

def random_phone(prefix="",maxlen=0):
    symbols = re.sub("'", "", string.digits*5 + string.punctuation + " ")
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])

def random_email(prefix="", maxlen=0):
    symbols = re.sub("'", "", string.ascii_letters + string.digits + string.punctuation + " "*10)
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen/2))])+ "@" +\
           "".join([random.choice(symbols) for i in range (random.randrange(maxlen/2))])

testdata = [Contact(firstname="", lastname="")] + [Contact(firstname=random_string(maxlen=12),
            middlename=random_string(maxlen=18),
            lastname=random_string(maxlen=20),
            nickname=random_string(maxlen=20),
            title=random_string(maxlen=20),
            company=random_string(maxlen=30),
            address=random_string(maxlen=40),
            homephone=random_phone(maxlen=20),
            mobilephone=random_phone(maxlen=20),
            workphone=random_phone(maxlen=20),
            faxphone=random_phone(maxlen=20),
            email=random_email(maxlen=30),
            email2=random_email(maxlen=30),
            email3=random_email(maxlen=30),
            homepage=random_string(prefix="www.", maxlen=30),
            dropbox1_choise=Contact.get_random_date,
            dropbox2_choise=Contact.get_random_month,
            byear=[random.randint(0,9) for i in range (0,4)],
            dropbox3_choise=Contact.get_random_date,
            dropbox4_choise=Contact.get_random_month,
            ayear=[random.randint(0,9) for i in range (0,4)],
            address2=random_string(maxlen=40),
            phone2=random_phone(maxlen=20),
            notes=random_string(maxlen=200)) for i in range(3)]


@pytest.mark.parametrize("contact_parameters", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact_parameters):
   # contact1 = Contact("Rodion", "Mykolayovych", "Pysarev", "NA", "engineer", "Buran", "city. street, house",
   #                    "0577778881", "0679876543", "", "", "mail@yandex.ua", "", "", "www.google.com",
   #                    14, 6, "1982", 1, 1, "", "", "1234567890", "", None)
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact_parameters)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact_parameters)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts,  key=Contact.id_or_max)