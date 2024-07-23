import sqlite3
import os

# Define the list of industries with their names and descriptions
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

path = os.path.join("instance", 'db.sqlite3')

# Connect to SQLite database (create it if not exists)
conn = sqlite3.connect(path)
cursor = conn.cursor()

# Create industries table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS industries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL
    )
''')

# Insert data into the industries table
cursor.executemany('''
    INSERT INTO industries (title, description)
    VALUES (?, ?)
''', industries)

# Commit changes and close connection
conn.commit()
conn.close()

print("Data has been successfully inserted into the industries table.")

