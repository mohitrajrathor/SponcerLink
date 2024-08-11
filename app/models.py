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
    campaigns = db.relationship('Campaigns', backref='campaigns', lazy=True)
    requests =  db.relationship('AddRequests', backref='sponcers', lazy=True)

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

    niches = db.relationship('Niches', backref='influencers', lazy=True)
    requests = db.relationship('AddRequests', backref='influencers', lazy=True)

    def __repr__(self) -> str:
        return f"<Sponcer username : {self.username}, id: {self.id}>"
    
class Campaigns(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    spo_id = db.Column(db.Integer, db.ForeignKey('sponcers.id'), nullable=False)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    budget = db.Column(db.Integer, nullable=False, default=0)
    start_date = db.Column(db.String, nullable=False)
    end_date = db.Column(db.String, nullable=False)
    post_time = db.Column(db.String, nullable=False)
    status = db.Column(db.String, default='pending', nullable=False)

    requests = db.relationship('AddRequests', back_populates='campaign', lazy=True)
    niches = db.relationship('Niches', backref='campaigns', lazy=True)


    def __repr__(self) -> str:
        return f"<Campaign {self.title} by {self.spo_id}>"

class Niches(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    camp_id = db.Column(db.Integer, db.ForeignKey('campaigns.id'), nullable=True)
    inf_id = db.Column(db.Integer, db.ForeignKey('influencers.id'), nullable=True)


    def __repr__(self) -> str:
        return f"<Niches {self.name}>"


class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sponcer_id = db.Column(db.Integer, db.ForeignKey('sponcers.id'), nullable=False)
    influencer_id = db.Column(db.Integer, db.ForeignKey('influencers.id'), nullable=False)
    amount = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"<Transaction between {self.sponcer_id} & {self.influencer_id}>"
    
class AddRequests(db.Model):
    '''
    sponcer send request for adrequest to influencer
    '''
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    inf_id = db.Column(db.Integer, db.ForeignKey('influencers.id'), nullable=False)
    spo_id = db.Column(db.Integer, db.ForeignKey('sponcers.id'), nullable=False)
    camp_id = db.Column(db.Integer, db.ForeignKey('campaigns.id'), nullable=False)
    requirements = db.Column(db.String, nullable=False)
    message = db.Column(db.String)
    payment = db.Column(db.Integer, default=0, nullable=False)
    status = db.Column(db.String, default='pending', nullable=False)
    req_time = db.Column(db.String, nullable=False)


    # one one relationship with campaign
    campaign = db.relationship('Campaigns', back_populates='requests', lazy=True)
    sponcer = db.relationship('Sponcers', back_populates='requests', lazy=True, overlaps="sponcers")
    influencer = db.relationship('Influencers', back_populates='requests', lazy=True, overlaps="influencers")


    def __repr__(self) -> str:
        return f"<Add Request {self.id} | details send by {self.sponcer.username} to {self.influencer.username}>"
    

class SponcerRequests(db.Model):
    '''
    influencer sent sponcer request to ask for sponcership for a posted campaign
    '''
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    inf_id = db.Column(db.Integer, db.ForeignKey('influencers.id'), nullable=False)
    spo_id = db.Column(db.Integer, db.ForeignKey('sponcers.id'), nullable=False)
    camp_id = db.Column(db.Integer, db.ForeignKey('campaigns.id'), nullable=False)
    message = db.Column(db.String)
    payment = db.Column(db.Integer, default=0, nullable=False)
    status = db.Column(db.String, default='pending', nullable=False)
    req_time = db.Column(db.String, nullable=False)

    # one one relationship with campaign
    campaign = db.relationship('Campaigns', backref='sponcer_requests', lazy=True)
    sponcer = db.relationship('Sponcers', backref='sponcer_requests', lazy=True)
    influencer = db.relationship('Influencers', backref='sponcer_requests', lazy=True)

    def __repr__(self) -> str:
        return f"<Sponcership Request between {self.spo_id} & {self.inf_id}>"