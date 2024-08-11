from app import db
from app.models import Admins, Industries, Sponcers, Influencers, Campaigns, Niches, Transactions, AddRequests
from datetime import datetime
from werkzeug.security import generate_password_hash

def insert_db(app, db):
    # Clear existing data
    db.drop_all()
    db.create_all()

    # Add Admins
    admin1 = Admins(
        username="admin1",
        email="admin1@example.com",
        password=generate_password_hash("password123"),
        create_time=str(datetime.now()),
        update_time=str(datetime.now())
    )

    admin2 = Admins(
        username="admin2",
        email="admin2@example.com",
        password=generate_password_hash("password123"),
        create_time=str(datetime.now()),
        update_time=str(datetime.now())
    )

    db.session.add_all([admin1, admin2])

    # Add Industries
    industry1 = Industries(
        title="Tech",
        description="Technology and gadgets"
    )

    industry2 = Industries(
        title="Fashion",
        description="Fashion and lifestyle"
    )

    db.session.add_all([industry1, industry2])

    # Add Sponcers
    sponcer1 = Sponcers(
        username="rajivtech",
        name="Rajiv Kumar",
        company="TechVision",
        ind_id=1,  # Tech
        email="rajiv@techvision.com",
        website="http://techvision.com",
        password=generate_password_hash("password123"),
        balance=1000,
        joined_time=str(datetime.now()),
        update_time=str(datetime.now())
    )

    sponcer2 = Sponcers(
        username="sneha_fashion",
        name="Sneha Gupta",
        company="StyleSphere",
        ind_id=2,  # Fashion
        email="sneha@stylesphere.com",
        website="http://stylesphere.com",
        password=generate_password_hash("password123"),
        balance=2000,
        joined_time=str(datetime.now()),
        update_time=str(datetime.now())
    )

    db.session.add_all([sponcer1, sponcer2])

    # Add Influencers
    influencer1 = Influencers(
        username="priya_influencer",
        name="Priya Sharma",
        email="priya@influencer.com",
        password=generate_password_hash("password123"),
        balance=500,
        joined_time=str(datetime.now()),
        update_time=str(datetime.now())
    )

    influencer2 = Influencers(
        username="arjun_creator",
        name="Arjun Verma",
        email="arjun@creator.com",
        password=generate_password_hash("password123"),
        balance=800,
        joined_time=str(datetime.now()),
        update_time=str(datetime.now())
    )

    db.session.add_all([influencer1, influencer2])

    # Add Campaigns
    campaign1 = Campaigns(
        spo_id=1,  # Sponcer1
        title="Tech Launch Campaign",
        description="Launching a new tech product",
        budget=5000,
        start_date=str(datetime.now()),
        end_date=str(datetime.now()),
        post_time=str(datetime.now()),
        status="active"
    )

    campaign2 = Campaigns(
        spo_id=2,  # Sponcer2
        title="Spring Fashion Collection",
        description="Promoting the new spring collection",
        budget=3000,
        start_date=str(datetime.now()),
        end_date=str(datetime.now()),
        post_time=str(datetime.now()),
        status="active"
    )

    db.session.add_all([campaign1, campaign2])

    # Add Niches
    niche1 = Niches(
        title="Tech Reviews",
        description="Reviews of the latest tech products",
        camp_id=1  # Campaign1
    )

    niche2 = Niches(
        title="Fashion Tips",
        description="Daily fashion tips",
        camp_id=2  # Campaign2
    )

    db.session.add_all([niche1, niche2])

    # Add Transactions
    transaction1 = Transactions(
        sponcer_id=1,  # Sponcer1
        influencer_id=1,  # Influencer1
        amount=500
    )

    transaction2 = Transactions(
        sponcer_id=2,  # Sponcer2
        influencer_id=2,  # Influencer2
        amount=800
    )

    db.session.add_all([transaction1, transaction2])

    # Add AddRequests
    add_request1 = AddRequests(
        inf_id=1,  # Influencer1
        spo_id=1,  # Sponcer1
        camp_id=1,  # Campaign1
        requirements="Create a video review of our latest product",
        message="Please deliver by next week",
        payment=500,
        status="approved",
        req_time=str(datetime.now())
    )

    add_request2 = AddRequests(
        inf_id=2,  # Influencer2
        spo_id=2,  # Sponcer2
        camp_id=2,  # Campaign2
        requirements="Post a series of photos wearing our new collection",
        message="Include the brand hashtags",
        payment=800,
        status="approved",
        req_time=str(datetime.now())
    )

    db.session.add_all([add_request1, add_request2])

    # Commit all the changes
    db.session.commit()

    print("Database populated with sample data.")

if __name__ == '__main__':
    insert_db()
