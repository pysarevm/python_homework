from model.group import Group
import random
import string

constant = [
    Group(name="Name1", header="header1", footer="footer1"),
    Group(name="Name2", header="header2", footer="footer2")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])


testdata = [Group("", "", "")]+[
    Group(name=random_string("Name", 10), header=random_string("Header", 20), footer=random_string("Footer", 20))
    for i in range(3)
]