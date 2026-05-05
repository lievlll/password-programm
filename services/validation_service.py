class ValidationService:

    def not_empty(self, text):
        if text.strip() == "":
            return False
        return True
