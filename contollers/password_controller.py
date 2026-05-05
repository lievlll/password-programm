import datetime
from models.password_record import PasswordRecord

class PasswordController:

    def __init__(self, storage):
        self.storage = storage
        self.records = self.storage.load()

    def add(self, service, username, password):
        now = str(datetime.datetime.now())
        record = PasswordRecord(service, username, password, now)
        self.records.append(record)

    def show_all(self):
        return self.records

    def delete(self, index):
        if index >= 0 and index < len(self.records):
            self.records.pop(index)

    def save(self):
        self.storage.save(self.records)
