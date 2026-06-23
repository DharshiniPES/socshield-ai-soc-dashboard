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

        self.conn.commit()

    def insert_alert(
        self,
        ip,
        severity,
        protocol,
        action
    ):

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