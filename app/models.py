from . import db

# Admin table
class Admins(db.Model):
    admin_id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    username = db.Column(db.String ,unique=True, nullable=False)
    email = db.Column(db.String ,unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    create_time = db.Column(db.String, nullable=False)
    update_time = db.Column(db.String)

    def __repr__(self) -> str:
        return f"<Admin - {self.username}>"


class Industries(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    title = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, nullable=True)

    def __repr__(self) -> str:
        return f"<Industry - {self.title}>"


class Sponcers(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    username = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    company = db.Column(db.String)
    ind_id = db.Column(db.Integer, db.ForeignKey('industries.id'), nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    website = db.Column(db.String)
    password = db.Column(db.String, nullable=False)
    balance = db.Column(db.Integer, default=0)
    joined_time = db.Column(db.String, nullable=False)
    update_time = db.Column(db.String)

    industries = db.relationship('Industries', backref=db.backref('sponcers', lazy=True))

    def __repr__(self) -> str:
        return f"<Sponcer {self.username}>"


class Influencers(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    username = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    balance = db.Column(db.Integer, default=0)
    joined_time = db.Column(db.String, nullable=False)
    update_time = db.Column(db.String)

    def __repr__(self) -> str:
        return f"<Sponcer {self.username}>"
    
class Campaigns(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    spo_id = db.Column(db.Integer, db.ForeignKey('sponcers.id'), nullable=False)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    budget = db.Column(db.Integer, nullable=False, default=0)
    niches = db.relationship('Niches', backref='campaigns', lazy=True)
    start_date = db.Column(db.String, nullable=False)
    end_date = db.Column(db.String, nullable=False)
    status = db.Column(db.String, default='pending', nullable=False)

class Niches(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    camp_id = db.Column(db.Integer, db.ForeignKey('campaigns.id'))
