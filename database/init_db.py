from database.connection import engine
from database.models import Base

# print("Dropping existing tables...")
# Base.metadata.drop_all(engine)

print("Creating tables from current models...")
Base.metadata.create_all(engine)

print("Database reset successfully!")