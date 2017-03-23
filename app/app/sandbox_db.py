from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///db.sqlite3')
Base = declarative_base()
Base.metadata.reflect(engine)

from sqlalchemy.orm import relationship, backref

class Skills(Base):
    __table__ = 'single_page_website_skill'

if __name__ == '__main__':
    from sqlalchemy.orm import scoped_session, sessionmaker, Query
    db_session = scoped_session(sessionmaker(bind=engine))
    for item in db_session.query(Skills.title, Skills.rating):
        print(item)