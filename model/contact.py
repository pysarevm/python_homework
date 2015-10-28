import random
from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, homephone=None, mobilephone=None, workphone=None, faxphone=None, email=None, email2=None, email3=None,
                 homepage=None, dropbox1_choise=None, dropbox2_choise=None, byear=None, dropbox3_choise=None,
                 dropbox4_choise=None, ayear=None, address2=None, phone2=None, notes=None, id=None, all_phones_from_home_page=None,
                 all_emails=None):
        self.firstname=firstname
        self.middlename=middlename
        self.lastname=lastname
        self.nickname=nickname
        self.title=title
        self.company=company
        self.address=address
        self.homephone=homephone
        self.mobilephone=mobilephone
        self.workphone=workphone
        self.faxphone=faxphone
        self.email=email
        self.email2=email2
        self.email3=email3
        self.homepage=homepage
        self.dropbox1_choise=dropbox1_choise
        self.dropbox2_choise=dropbox2_choise
        self.byear=byear
        self.dropbox3_choise=dropbox3_choise
        self.dropbox4_choise=dropbox4_choise
        self.ayear=ayear
        self.address2=address2
        self.phone2=phone2
        self.notes=notes
        self.id=id
        self.all_phones_from_home_page=all_phones_from_home_page
        self.all_emails = all_emails

    def get_random_date(self):
        return random.randint(1, 33)

    def get_random_month(self):
        return random.randint(1, 13)

    def __repr__(self):
        return "%s:%s, %s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname \
               and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize