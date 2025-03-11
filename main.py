from extract import fetch_anime
from transform import transform_data
from config import SessionLocal, engine
from models import Base, Anime
from utils import logger
from sqlalchemy.dialects.postgresql import insert

def create_tables():
    """
    Creates all tables in the database as defined in the SQLAlchemy models.
    """
    Base.metadata.create_all(bind=engine)

def load_data():
    """
    Fetches anime data from an external source, transforms it, and saves it to the database.
    If a record with the same ID already exists, it will be updated.
    """
    session = SessionLocal()
    data = fetch_anime()
    transformed_data = transform_data(data)

    for item in transformed_data:
        stmt = insert(Anime).values(
            id=item["id"],
            title=item["title"],
            score=item["score"],
            episodes=item["episodes"],
            status=item["status"]
        ).on_conflict_do_update(
            index_elements=["id"],
            set_={
                "title": item["title"],
                "score": item["score"],
                "episodes": item["episodes"],
                "status": item["status"]
            }
        )
        session.execute(stmt)

    session.commit()
    session.close()
    logger.info("Data loaded and updated successfully!")

if __name__ == "__main__":
    create_tables()
    load_data()
