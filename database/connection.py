from sqlalchemy import create_engine,text
import os 
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

database_host = os.getenv('DATABASE_HOST')
database_port = os.getenv('DATABASE_PORT')
database_name = os.getenv('DATABASE_NAME')
database_user = os.getenv('DATABASE_USER')
database_password = os.getenv('DATABASE_PASSWORD')
DATABASE_URL= (f"postgresql+psycopg://{database_user}:{database_password}"
               f"@{database_host}:{database_port}/{database_name}")


# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Test the connection
try:
    with engine.connect() as connection:
        result = connection.execute(text("""
            SELECT
                current_database(),
                current_user,
                inet_server_addr(),
                inet_server_port();
        """))

        row = result.fetchone()

        print("Connected successfully!")
        print("Database:", row[0])
        print("User:", row[1])
        print("Server:", row[2])
        print("Port:", row[3])
except Exception as e:
    print("Connection failed:", e)