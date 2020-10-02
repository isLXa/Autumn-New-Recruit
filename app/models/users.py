from app.extensions import db, Model


class User(Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(255), nullable=False)
    tel = db.Column(db.VARCHAR(255), nullable=False, unique=True)
    sex = db.Column(db.VARCHAR(255), nullable=False)
    grade = db.Column(db.VARCHAR(255), nullable=False)
    college = db.Column(db.VARCHAR(255), nullable=False)
    dormitory = db.Column(db.VARCHAR(255), nullable=False)
    first = db.Column(db.VARCHAR(255), nullable=False)
    second = db.Column(db.VARCHAR(255), nullable=False)
    adjust = db.Column(db.Integer, nullable=False)
    description = db.Column(db.VARCHAR(255), nullable=False)

    def __repr__(self):
        return "User: %s %s %s %s %s %s %s %s %s %s %s" % (
        self.id, self.name, self.tel, self.sex, self.grade, self.college,
        self.dormitory, self.first, self.second, self.adjust, self.description)
