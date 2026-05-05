class PasswordRecord:
    def __init__(self, service, username, password, created_at):
        self.service = service
        self.username = username
        self.password = password
        self.created_at = created_at
