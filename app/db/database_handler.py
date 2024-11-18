
#This module will handle all database related logic. It will be mostly used in the server side program A.K.A. in the boss machine. @Doni @Szabi
import pathlib
from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.exc import IntegrityError
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text, Float
from sqlalchemy.sql import func
from sqlalchemy.orm import (
    declarative_base,
    mapped_column,
    relationship,
    sessionmaker,
    Mapped,
    Session
)
from logger import logger
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy import select, delete, update, values

import datetime
from datetime import date, timedelta

def handle_exceptions(f):
    def wrapper(*args, **kw):
        try:
            return f(*args, **kw) # Call main function
        except IntegrityError as e:
            logger.error(e.orig)
            raise e.orig
        except SQLAlchemyError as e:
            logger.error(f"Unexpected error when creating item: {e}")
            raise e
    return wrapper


base_dir = pathlib.Path().cwd()
engine = sa.create_engine(fr"sqlite:///{base_dir}\app\db\test.db")
Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()


class BookingItem(Base):
    __tablename__ = "bookingitem"

    id  = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(Text, nullable=False)
    wbs = Column(Text, nullable=False)

    def __repr__(self):
        return f"<id={self.id}, name={self.name}, wbs={self.wbs}>"


class TimeTable(Base):
    __tablename__ = "timetable"

    id  = Column(Integer, primary_key=True, autoincrement="auto")
    booking_item_id = Column(Integer, ForeignKey("bookingitem.id"))
    date = Column(DateTime)
    hours = Column(Float)

    booking_item = relationship("BookingItem")

    def __repr__(self):
        return f"<id={self.id}, booking_item_id={self.booking_item_id}, date={self.date}, hours={self.hours}>"



Base.metadata.create_all(engine)

@handle_exceptions
def create_booking_item(session: Session, new_booking_item: BookingItem):
    exist = read_booking_item(session, new_booking_item)
    if exist is None:
        session.add(new_booking_item) 
        session.commit() 
        logger.info(f"Created user: {new_booking_item}")
    else:
        logger.warning(f"Booking item already exists in database: {exist}")
    return read_booking_item(session, new_booking_item)


@handle_exceptions
def read_booking_item(session: Session, bookingitem: BookingItem):
    item = session.scalars(select(BookingItem)
                            .where(BookingItem.name == bookingitem.name)
                            .where(BookingItem.wbs == bookingitem.wbs)).first()
    return item


@handle_exceptions
def update_booking_item(session: Session, bookingitem: BookingItem , modified_bookingitem: BookingItem):
    exist = read_booking_item(session, bookingitem)
    if exist is None:
        logger.info(f"No such item: {bookingitem}")
    else:
        stmt = (
            update(BookingItem)
            .where(BookingItem.name.is_(bookingitem.name))
            .where(BookingItem.wbs.is_(bookingitem.wbs))
            .values(name = modified_bookingitem.name))
        session.execute(stmt)
        session.commit()
        logger.info(f"Item modified from : {bookingitem}  to {exist}")


@handle_exceptions
def delete_booking_item(session: Session, bookingitem: BookingItem):
    exist = read_booking_item(session, bookingitem)
    if exist is None:
        logger.info(f"No such item: {bookingitem}")
    else:
        stmt = (
            delete(BookingItem)
            .where(BookingItem.name.is_(bookingitem.name))
            .where(BookingItem.wbs.is_(bookingitem.wbs)))
        session.execute(stmt)
        session.commit()
        logger.info(f"Item deleted from : {exist}")


@handle_exceptions
def create_time_table_item(session: Session, new_timetable_item: TimeTable):
    exist_booking_item = read_booking_item(session, new_timetable_item.booking_item)
    new_timetable_item.booking_item = exist_booking_item
    
    if new_timetable_item.date is None:
        new_timetable_item.date = date.today() 
        
    exist = read_time_table_item(session, new_timetable_item)
    if exist is None:
        session.add(new_timetable_item) 
        session.commit() 
        logger.info(f"Created new item: {new_timetable_item}")
    else:
        logger.warning(f"TimeTable item already exists in database: {exist}")
        #add hours to existing item
        stmt = (
            update(TimeTable)
            .where(TimeTable.id == exist.id)
            .values(hours = exist.hours + new_timetable_item.hours))
    return read_time_table_item(session, new_timetable_item)

@handle_exceptions
def read_time_table_item(session: Session, timetable: TimeTable):
    item = session.scalars(select(TimeTable)
                            .where(TimeTable.booking_item == timetable.booking_item) #itt miért nem primary key alapján keresünk?
                            .where(func.DATE(TimeTable.date) == timetable.date)).first()
    return item

@handle_exceptions
def update_time_table_item(session: Session, timetable: TimeTable): #itt a booking_itemnél volt modified meg prev is, de igazából elég csak a modified, mert az id fix
    exist = read_time_table_item(session, timetable)
    if exist is None:
        logger.info(f"No such item: {timetable}")
    else:
        stmt = (
            update(TimeTable)
            .where(TimeTable.id == exist.id)
            .values(date = timetable.date, hours = timetable.hours))
        session.execute(stmt)
        session.commit()
        logger.info(f"Item modified from : {exist}  to {timetable}")

@handle_exceptions
def delete_time_table_item(session: Session, timetable: TimeTable):
    exist = read_time_table_item(session, timetable)
    if exist is None:
        logger.info(f"No such item: {timetable}")
    else:
        stmt = (
            delete(TimeTable)
            .where(TimeTable.id == exist.id))
        session.execute(stmt)
        session.commit()
        logger.info(f"Item deleted from : {exist}")




# b1 = BookingItem(
#     name = "New1111",
#     wbs = "Hey",
# )
#
# b2 = BookingItem(
#     name = "Test1",
#     wbs = "Hey",
# )
#
# b3 = BookingItem(
#     name = "Test1",
#     wbs = "Heeey",
# )
#
# create_booking_item(session, b1)
#
# update_booking_item(session, b1, b2)
#
# delete_booking_item(session, b3)
#
# t1 = TimeTable(
#
#     hours = 6,
#     booking_item = b1
#
# )
#
# create_time_table_item(session, t1)