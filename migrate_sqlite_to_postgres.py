import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Database import db, User, Resource, Employee, Roster, Event, ResourcePreset, QualificationType, Qualification

# Set your SQLite and Postgres URLs
SQLITE_URL = 'sqlite:///rostering.db'  # or your actual path
POSTGRES_URL = os.getenv('DATABASE_URL')
if POSTGRES_URL and POSTGRES_URL.startswith('postgres://'):
    POSTGRES_URL = POSTGRES_URL.replace('postgres://', 'postgresql://', 1)

# Create engines
sqlite_engine = create_engine(SQLITE_URL)
postgres_engine = create_engine(POSTGRES_URL)

# Create sessions
SqliteSession = sessionmaker(bind=sqlite_engine)
PostgresSession = sessionmaker(bind=postgres_engine)
sqlite_session = SqliteSession()
postgres_session = PostgresSession()

def copy_table(Model):
    print(f"Migrating {Model.__tablename__}...")
    rows = sqlite_session.query(Model).all()
    for row in rows:
        # Detach from SQLite session
        sqlite_session.expunge(row)
        db.make_transient(row)
        postgres_session.merge(row)
    postgres_session.commit()
    print(f"Done: {Model.__tablename__}")

def main():
    # Create tables in Postgres if not exist
    db.metadata.create_all(postgres_engine)
    # Order matters for foreign keys
    for Model in [User, Resource, Employee, QualificationType, Qualification, ResourcePreset, Event, Roster]:
        copy_table(Model)
    print("Migration complete!")

if __name__ == "__main__":
    main()
