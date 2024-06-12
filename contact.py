class Contact:
    db = {}

    def __init__(self, id_=None, first_=None, last_=None, email_=None, phone_=None):
        self.id = id_
        self.first = first_
        self.last = last_
        self.email = email_
        self.phone = phone_

    @staticmethod
    def all():
        return Contact.db