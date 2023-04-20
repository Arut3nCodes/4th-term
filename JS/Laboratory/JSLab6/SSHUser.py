import datetime

class SSHUser:
    def __init__(self, name:str, lastLoginDate):
        self.name = name
        self.lastLoginDate = lastLoginDate

    def validate(self):
        if (self.name not in ['unknown']) and (6 <= len(self.name) <= 15):
            return True
        return False