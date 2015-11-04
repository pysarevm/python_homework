from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys
import re


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number fo groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix="", maxlen=0):
    symbols = re.sub("'", "", string.ascii_letters + string.digits + string.punctuation + " "*10)
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])


def random_phone(prefix="",maxlen=0):
    symbols = re.sub("'", "", string.digits*5 + string.punctuation + " ")
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])


def random_email(prefix="", maxlen=0):
    symbols = re.sub("'", "", string.ascii_letters + string.digits + string.punctuation + " "*10)
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen/2))]) + "@" +\
           "".join([random.choice(symbols) for i in range (random.randrange(maxlen/2))])


testdata = [Contact(firstname="", lastname="")] + [
    Contact(firstname=random_string(maxlen=12),
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
            notes=random_string(maxlen=200)
           ) for i in range(n)
   ]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
