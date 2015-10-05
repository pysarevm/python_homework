from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
__author__ = 'Pysarev'


class HelperInitializer:
    def __init__(self, fixture):
        self.fixture = fixture

    def initialize_helper(self):
        self.fixture.session = SessionHelper(self.fixture)
        self.fixture.group = GroupHelper(self.fixture)
        self.fixture.contact = ContactHelper(self.fixture)