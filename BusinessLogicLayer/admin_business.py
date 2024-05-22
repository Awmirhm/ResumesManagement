from DataAccessLayer.admin_data_access import AdminDataAccess
from passlib.hash import pbkdf2_sha256


class AdminBusiness:
    def __init__(self):
        self.admin_data_access = AdminDataAccess()

        self.user = None

    def login(self, username, password):
        passwords = self.admin_data_access.return_all_password()

        if len(username) < 3 or len(password) < 3:
            return [None, "Invalid Request"]

        for item in passwords:
            if pbkdf2_sha256.verify(password, item):
                self.user = self.admin_data_access.get_user(username, item)
                break
            self.user = None

        if self.user:
            return [self.user, None]
        else:
            return [None, "Invalid Username or Password"]
