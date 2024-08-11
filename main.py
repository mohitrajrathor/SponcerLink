from app import create_app, db
from data_inserter import insert_db


app = create_app()

# insert sample data
with app.app_context():
    insert_db(app, db)


app.run(debug=True)