import sqlite3
import os
import datetime as dt
from werkzeug.security import generate_password_hash


# list of industries with their names and descriptions
industries = [
    ("Individual", "Type for individual category."),
    ("Fashion and Beauty", "Brands showcase products, trends, and styles through influencers."),
    ("Fitness and Wellness", "Fitness brands and wellness products use influencers to promote services."),
    ("Travel and Hospitality", "Hotels, airlines, and travel agencies collaborate with influencers for promotions."),
    ("Technology", "Tech companies engage influencers to create awareness about gadgets and software."),
    ("Food and Beverage", "Restaurants and beverage brands promote menus and new dishes with influencers."),
    ("Entertainment and Media", "Movie studios and streaming platforms collaborate with influencers for promotions."),
    ("Automotive", "Car manufacturers and dealerships showcase new models and features through influencers."),
    ("Home and Lifestyle", "Furniture brands and lifestyle products use influencers to showcase offerings."),
    ("Finance and Investment", "Banks and fintech companies use influencers to promote financial products."),
    ("Gaming", "Gaming companies and esports organizations engage influencers to promote games and events."),
    ("Sports", "Sports brands and athletic wear companies use influencers to reach sports enthusiasts."),
    ("Healthcare", "Pharmaceutical companies and health clinics promote health products with influencers."),
    ("Education and E-learning", "Online courses and educational platforms use influencers to reach students."),
    ("Environmental Sustainability", "Eco-friendly brands and conservation organizations promote sustainability."),
    ("Charity and Non-profit", "Non-profit organizations use influencers to raise awareness and support for social causes."),
    ("Other", "Industry not listed.")
]

# list of sponcers for demo purpose
sponcers = [
    ('sponcer', 'sponcer', None, 1, 'sponcer@sponcer.com', None,  generate_password_hash('1'), dt.datetime.now().isoformat(), 0),
    ('raj', 'raj sahu', None, 1, 'raj@abc.com', None, generate_password_hash('123456789'), dt.datetime.now().isoformat(), 0),
    ('akash', 'akash', None, 1, 'akash@abc.com', None, generate_password_hash('10101010'), dt.datetime.now().isoformat(), 0),
    ('rohan', 'rohan', 'Agrotech', 5, 'rohan@agrotech.com', 'agrotech.com', generate_password_hash('abc'), dt.datetime.now().isoformat(), 0),
    ('tripti', 'tripti', 'beatutify', 2, 'tripti@beautify.com', 'beautify.com', generate_password_hash('xyz'), dt.datetime.now().isoformat(), 0)
]


# list of influecners for demo purpose
influencers = [
    (1, 'ajayr', 'Ajay Rao', 'ajayrao@example.com', generate_password_hash('password123'), 100, dt.datetime.now().isoformat(), None),
    (2, 'sunitap', 'Sunita Patel', 'sunitapatel@example.com', generate_password_hash('password456'), 200, dt.datetime.now().isoformat(), None),
    (3, 'rohitk', 'Rohit Kumar', 'rohitkumar@example.com', generate_password_hash('password789'), 300, dt.datetime.now().isoformat(), None),
    (4, 'priyap', 'Priya Sharma', 'priyasharma@example.com', generate_password_hash('password012'), 400, dt.datetime.now().isoformat(), None),
    (5, 'vikasp', 'Vikas Singh', 'vikassingh@example.com', generate_password_hash('password345'), 500, dt.datetime.now().isoformat(), None),
]

path = os.path.join("instance", 'db.sqlite3')

# Connect to SQLite database (create it if not exists)
conn = sqlite3.connect(path)
cursor = conn.cursor()


# insert data into sponcer table
cursor.executemany('''
    INSERT INTO sponcers (username, name, company, ind_id, email, website, password, joined_time, balance)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
''', sponcers)


# insert into influencer
cursor.executemany("""
    INSERT INTO influencers (id, username, name, email, password, balance, joined_time, update_time)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", influencers)


# Insert data into the industries table
cursor.executemany('''
    INSERT INTO industries (title, description)
    VALUES (?, ?)
''', industries)


# Commit changes and close connection
conn.commit()
conn.close()

print("Data has been successfully inserted into the industries table.")