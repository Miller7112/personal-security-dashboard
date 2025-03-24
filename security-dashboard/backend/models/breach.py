from datetime import datetime
from backend import db  

class BreachHistory(db.Model):
    """Model to store breach information for passwords."""
    
    __tablename__ = 'breach_history'
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each record
    password_hash = db.Column(db.String(64), nullable=False)  # The hashed password
    breach_count = db.Column(db.Integer, default=0, nullable=False)  # Number of breaches
    last_checked = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp of last check

    def __init__(self, password_hash, breach_count):
        self.password_hash = password_hash
        self.breach_count = breach_count
        self.last_checked = datetime.utcnow()

    @classmethod
    def get_breach_by_hash(cls, password_hash):
        """Fetch a breach record by the password hash."""
        return cls.query.filter_by(password_hash=password_hash).first()

    @classmethod
    def create_breach(cls, password_hash, breach_count):
        """Create a new breach record."""
        breach = cls(password_hash=password_hash, breach_count=breach_count)
        db.session.add(breach)
        db.session.commit()
        return breach

    @classmethod
    def update_breach(cls, password_hash, breach_count):
        """Update an existing breach record."""
        breach = cls.query.filter_by(password_hash=password_hash).first()
        if breach:
            breach.breach_count = breach_count
            breach.last_checked = datetime.utcnow()
            db.session.commit()
            return breach
        return None
