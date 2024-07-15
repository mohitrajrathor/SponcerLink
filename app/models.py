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
        return f"<Industry - {self.name}>"


class Sponcers(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    username = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    company = db.Column(db.String)
    ind_id = db.Column(db.Integer, db.ForeignKey('industries.id'), nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    phone_num = db.Column(db.Integer, unique=True, nullable=False)
    address = db.Column(db.String)
    website = db.Column(db.String)
    joined_time = db.Column(db.String, nullable=False)
    update_time = db.Column(db.String)

    industries = db.relationship('Industries', backref=db.backref('sponcers', lazy=True))

    def __repr__(self) -> str:
        return f"<Sponcer {self.username}>"



# class Influencers(db.Model):
#     id: Mapped[int] = mapped_column(primary_key=True, unique=True, nullable=False, autoincrement=True)
#     username: Mapped[str] = mapped_column(unique=True, nullable=False)
#     name:Mapped[str] = mapped_column(nullable=False)
#     bio: Mapped[str] = mapped_column()
#     email: Mapped[str] = mapped_column(unique=True, nullable=False)
#     phone_num: Mapped[int] = mapped_column(unique=True, nullable=False)
#     joined_time: Mapped[str] = mapped_column(nullable=False)
#     updated_time: Mapped[str] = mapped_column()

#     def __repr__(self) -> str:
#         return f"<Influencer {self.username}>"

# class SocialPlatforms:
#     id: Mapped[int] = mapped_column(primary_key=True, unique=True, nullable=True, autoincrement=True)
#     name: Mapped[str] = mapped_column(unique=True, nullable=True)
#     description: Mapped[str] = mapped_column()
#     logo_url: Mapped[str] = mapped_column()

#     def __repr__(self) -> str:
#         return f"<Social Platform {self.name}>"

# class SocialAccounts(db.Model):
#     id: Mapped[int] = mapped_column(primary_key=True, nullable=False, unique=True, autoincrement=True)
#     influencer_id: Mapped["Influencers"] = ForeignKey(Influencers.id)
#     platform_id: Mapped['SocialPlatforms'] = ForeignKey(SocialPlatforms.id)
#     handle_url: Mapped[str] = mapped_column(nullable=False, unique=True)
#     follower_count: Mapped[int] = mapped_column(default=-1)
#     created_time: Mapped[str] = mapped_column(nullable=False)
#     updated_time: Mapped[str] = mapped_column()

#     def __repr__(self) -> str:
#         return f"<Social Acoount {self.handle_url}>"


# class Categories(db.Model):
#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     category: Mapped[str] = mapped_column(unique=True, nullable=False)

#     def __repr__(self) -> str:
#         return f"<Category {self.category}>"


# class Campaigns(db.Model):
#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     title: Mapped[str] = mapped_column(nullable=False)
#     description: Mapped[str] = mapped_column()
#     budget: Mapped[float] = mapped_column(nullable=False, default=0)
#     start_date: Mapped[str] = mapped_column(nullable=False)
#     end_date: Mapped[str] = mapped_column(nullable=False)
#     sponcer_id: Mapped["Sponcers"] = ForeignKey(Sponcers.id)
#     created_time:Mapped[str] = mapped_column(nullable=False)
#     updated_time: Mapped[str] = mapped_column()
#     privacy: Mapped[str] = mapped_column(nullable=False, default="public")
#     category_id: Mapped["Categories"] = ForeignKey(Categories.id)

#     def __repr__(self) -> str:
#         return f"<Campaign {self.title}>"
    

# class AdRequests(db.Model):
#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     sponcer_id: Mapped["Sponcers"] = ForeignKey(Sponcers.id)
#     influencer_id: Mapped["Influencers"] = ForeignKey(Influencers.id)
#     title: Mapped[str] = mapped_column(nullable=False)
#     description: Mapped[str] = mapped_column()
#     start_date: Mapped[str] = mapped_column(nullable=False)
#     end_date: Mapped[str] = mapped_column(nullable=False)
#     budget: Mapped[float] = mapped_column(default=0)
#     status: Mapped[str] = mapped_column(default="pending")
#     created_time: Mapped[str] = mapped_column(nullable=False)
#     updated_time: Mapped[str] = mapped_column()
#     camp_id: Mapped["Campaigns"] = ForeignKey(Campaigns.id)


# class SponcershipRequests(db.Model):
#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     influencer_id: Mapped["Influencers"] = ForeignKey(Influencers.id)
#     camp_id: Mapped["Campaigns"] = ForeignKey(Campaigns.id)
#     title: Mapped[str] = mapped_column(nullable=False)
#     description: Mapped[str] = mapped_column()
#     ask: Mapped[float] = mapped_column(default=0)
#     start_date: Mapped[str] = mapped_column(nullable=False)
#     end_date: Mapped[str] = mapped_column(nullable=False)
#     created_time: Mapped[str] = mapped_column(nullable=False)
#     updated_time: Mapped[str] = mapped_column()