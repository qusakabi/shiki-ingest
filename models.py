from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Anime(Base):
    """
     SQLAlchemy model for the 'anime' table.

     Attributes:
         id (int): Unique identifier for the anime.
         title (str): Title of the anime.
         score (str): Rating of the anime.
         episodes (int): Number of episodes.
         status (str): Status of the anime (e.g., "released", "ongoing").
     """
    __tablename__ = "anime"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    score = Column(String)
    episodes = Column(Integer)
    status = Column(String)