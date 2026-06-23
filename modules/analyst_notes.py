class AnalystNotes:

    def __init__(self, db):
        self.db = db

    def save_note(self, ip, note):
        self.db.insert_note(ip, note)

    def get_notes(self):
        return self.db.get_notes()