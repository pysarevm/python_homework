import random


class Contact:
    def __init__(self, firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home="", mobile="", work="", fax="",
                 email="", email2="", email3="", homepage="", dropbox1_choise=0, dropbox2_choise=0, byear="", dropbox3_choise=0,
                 dropbox4_choise=0, ayear="", address2="", phone2="", notes=""):
        self.firstname=firstname
        self.middlename=middlename
        self.lastname=lastname
        self.nickname=nickname
        self.title=title
        self.company=company
        self.address=address
        self.home=home
        self.mobile=mobile
        self.work=work
        self.fax=fax
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

    def get_random_date(self):
        return random.randint(1, 33)

    def get_random_month(self):
        return random.randint(1, 13)