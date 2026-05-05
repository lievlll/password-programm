import json
from models.password_record import PasswordRecord

class StorageService:

    def load(self):
        try:
            with open("data/passwords.json", "r") as f:
                data = json.load(f)
                records = []
                for item in data:
                    record = PasswordRecord(
                        item["service"],
                        item["username"],
                        item["password"],
                        item["created_at"]
                    )
                    records.append(record)
                return records
        except:
            return []

    def save(self, records):
        data = []
        for r in records:
            data.append({
                "service": r.service,
                "username": r.username,
                "password": r.password,
                "created_at": r.created_at
            })

        with open("data/passwords.json", "w") as f:
            json.dump(data, f, indent=4)
