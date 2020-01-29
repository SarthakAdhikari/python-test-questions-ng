from . import db

class UsersModel(db.Model):
    __table__name = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    location = db.Column(db.String)
    salary = db.Column(db.Integer)
    position = db.Column(db.String)
    start_date = db.Column(db.Date)
    extension = db.Column(db.BigInteger)

    def serialize(self):
        return {"first_name": self.first_name, "last_name": self.last_name, "location": self.location,
                "salary": self.salary, "start_date": self.start_date, "position": self.position,
                "extension": self.extension}

    def __init__(self, first_name, last_name, location, salary, position, extension, start_date):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.salary = salary
        self.position = position
        self.extension = extension
        self.start_date = start_date

    def __repr__(self):
        return "<User {}>".format(self.first_name + " " + self.last_name)
