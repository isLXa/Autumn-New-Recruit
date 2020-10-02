from app.extensions import db,Model

class Admin(Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.VARCHAR(255))
    password = db.Column(db.VARCHAR(255))
    def __repr__(self):
        return "Admin: %s %s %s"%(self.id, self.username, self.password)