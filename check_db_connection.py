#from fixture.db import DbFixture
#from fixture.orm import ORMFixture

#db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

#try:
 #   l = db.get_contact_in_group()
#   for item in l:
 #       print(item)
 #   print(len(l))

#finally:
#    pass #db.destroy()
contacts = [5, 12, 33, 59]
print("len: ", len(contacts))
print(contacts[4])
a = str(contacts).strip('[]')
print (a)
print ("select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3"
                           " from addressbook where deprecated='0000-00-00 00:00:00' and id in (%s)" % a)