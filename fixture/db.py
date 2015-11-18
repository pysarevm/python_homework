__author__ = 'Pysarev'
import mysql.connector
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    def get_group_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name,header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3 "
                           "from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, homephone, mobilephone, workphone, phone2, email, email2, email3) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address, homephone=homephone,
                                    mobilephone=mobilephone, workphone=workphone, phone2=phone2, email=email,
                                    email2=email2, email3=email3))
        finally:
            cursor.close()
        return list

    def address_in_groups_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, group_id from address_in_groups where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, group_id) = row
                list.append(Contact(id=str(id), group_id=group_id,))

        finally:
            cursor.close()
        return list

    def get_contacts_from_group(self, group):
        list=[]
        contacts=[]
        cursor = self.connection.cursor()
        try:
            for c in (self.address_in_groups_list()):
                if str(c.group_id) == group.id:
                    contacts.append(c.id)
            a = str(contacts).strip('[]')
            if contacts != []:
                a = str(contacts).strip('[]')
                cursor.execute("select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3"
                           " from addressbook where deprecated='0000-00-00 00:00:00' and id in (%s)" % a)
                for row in cursor:
                    (id, firstname, lastname, address, homephone, mobilephone, workphone, phone2, email, email2, email3) = row
                    list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address, homephone=homephone,
                                    mobilephone=mobilephone, workphone=workphone, phone2=phone2, email=email,
                                    email2=email2, email3=email3))
        finally:
            cursor.close()
        return list

    def get_contacts_not_from_group(self, group):
        list=[]
        cursor = self.connection.cursor()
        try:
            all_contacts = self.get_contact_list()
            contacts_in_group = self.get_contacts_from_group(group)
            if contacts_in_group == []:
                list = all_contacts
            else:
                for c in all_contacts:
                    for cnt in contacts_in_group:
                        if c != cnt:
                            list.append(c)
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()