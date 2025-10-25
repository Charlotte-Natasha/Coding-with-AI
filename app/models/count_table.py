from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class CountTable(Base):
    __tablename__ = 'count_table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    count_number = Column(Integer, nullable=False)

engine = create_engine('sqlite:///count_database.db', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def get_count():
    session = Session()
    row = session.query(CountTable).first()
    if row is None:
        row = CountTable(count_number=0)
        session.add(row)
        session.commit()
    count = row.count_number
    session.close()
    return count

def increment_count():
    session = Session()
    row = session.query(CountTable).first()
    if row is None:
        row = CountTable(count_number=1)
        session.add(row)
    else:
        row.count_number += 1
    session.commit()
    count = row.count_number
    session.close()
    return count

# Initialize table with a row of count 0 if empty on module load
session = Session()
if session.query(CountTable).count() == 0:
    session.add(CountTable(count_number=0))
    session.commit()
session.close()
