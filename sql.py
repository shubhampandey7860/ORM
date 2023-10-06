from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a SQLite database file named 'example.db'
engine = create_engine('sqlite:///user.db', echo=True)


Base = declarative_base()

# Define a Python class as a model for a database table
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(100))

# Create the database tables
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Insert a new user into the 'users' table
new_user = User(username='john_doe', email='john@example.com')
session.add(new_user)
session.commit()

# Query the 'users' table
user = session.query(User).filter_by(username='john_doe').first()
print(f'User ID: {user.id}, Username: {user.username}, Email: {user.email}')

# Update a user's email
user.email = 'new_email@example.com'
session.commit()

# Delete a user
session.delete(user)
session.commit()

# Close the session
session.close()
