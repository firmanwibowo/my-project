from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.orm import relationship

from ksl import database


class Articles(database.Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    article = Column(String)
    datepost = Column(String)
    author = relationship("Users")
    author_id = Column(Integer, ForeignKey('users.id'))
