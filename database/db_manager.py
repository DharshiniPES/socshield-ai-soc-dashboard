import sqlite3


class DBManager:

    def __init__(self):

        self.conn = sqlite3.connect(
            "database/alerts.db",
            check_same_thread=False
        )

        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT,
            severity TEXT,
            protocol TEXT,
            action TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT,
            note TEXT
        )
        """)

        self.conn.commit()

    def alert_exists(
        self,
        ip,
        severity,
        protocol,
        action
    ):

        self.cursor.execute(
            """
            SELECT COUNT(*)
            FROM alerts
            WHERE ip = ?
            AND severity = ?
            AND protocol = ?
            AND action = ?
            """,
            (
                ip,
                severity,
                protocol,
                action
            )
        )

        return self.cursor.fetchone()[0] > 0

    def insert_alert(
        self,
        ip,
        severity,
        protocol,
        action
    ):

        if self.alert_exists(
            ip,
            severity,
            protocol,
            action
        ):
            return

        self.cursor.execute(
            """
            INSERT INTO alerts
            (
                ip,
                severity,
                protocol,
                action
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                ip,
                severity,
                protocol,
                action
            )
        )

        self.conn.commit()

    def get_alerts(self):

        self.cursor.execute(
            "SELECT * FROM alerts"
        )

        return self.cursor.fetchall()

    def insert_note(
        self,
        ip,
        note
    ):

        self.cursor.execute(
            """
            INSERT INTO notes
            (
                ip,
                note
            )
            VALUES (?, ?)
            """,
            (
                ip,
                note
            )
        )

        self.conn.commit()

    def get_notes(self):

        self.cursor.execute(
            "SELECT * FROM notes"
        )

        return self.cursor.fetchall()
