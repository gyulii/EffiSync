
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



class DatabaseHandler:
    Base = declarative_base()

    class BookingItem(Base):
        __tablename__ = "bookingitem"

        id = Column(Integer, primary_key=True, autoincrement="auto")
        name = Column(Text, nullable=False)
        wbs = Column(Text, nullable=False)

        def __repr__(self):
            return f"<id={self.id}, name={self.name}, wbs={self.wbs}>"

    class TimeTable(Base):
        __tablename__ = "timetable"

        id = Column(Integer, primary_key=True, autoincrement="auto")
        booking_item_id = Column(Integer, ForeignKey("bookingitem.id"))
        date = Column(DateTime)
        hours = Column(Float)

        booking_item = relationship("BookingItem")

        def __repr__(self):
            return f"<id={self.id}, booking_item_id={self.booking_item_id}, date={self.date}, hours={self.hours}>"

    def __init__(self):
        base_dir = pathlib.Path().cwd()
        engine = sa.create_engine(fr"sqlite:///{base_dir}\app\db\test.db")
        Session = sessionmaker(bind=engine)
        self.session = Session()
        Base = declarative_base()

        Base.metadata.create_all(engine)

    @handle_exceptions
    def create_booking_item(self, new_booking_item: BookingItem):
        exist = self.read_booking_item(new_booking_item)
        if exist is None:
            self.session.add(new_booking_item)
            self.session.commit()
            logger.info(f"Created user: {new_booking_item}")
        else:
            logger.warning(f"Booking item already exists in database: {exist}")
        return self.read_booking_item(new_booking_item)


    @handle_exceptions
    def read_booking_item(self, bookingitem: BookingItem):
        item = self.session.scalars(select(self.BookingItem)
                            .where(self.BookingItem.name == bookingitem.name)
                            .where(self.BookingItem.wbs == bookingitem.wbs)).first()
        return item

    @handle_exceptions
    def read_all_booking_names(self):
        names = self.session.scalars(select(self.BookingItem.name)).all()
        return names

    @handle_exceptions
    def update_booking_item(self, bookingitem: BookingItem , modified_bookingitem: BookingItem):
        exist = self.read_booking_item(bookingitem)
        modified_exist = self.read_booking_item(modified_bookingitem)
        if exist is None:
            logger.info(f"No such item: {bookingitem}")
        else:
            if modified_exist is not None:
                logger.info(f"Item already exists in database: {modified_exist}")
            else:
                stmt = (
                    update(self.BookingItem)
                    .where(self.BookingItem.name.is_(bookingitem.name))
                    .where(self.BookingItem.wbs.is_(bookingitem.wbs))
                    .values(name = modified_bookingitem.name))
                self.session.execute(stmt)
                self.session.commit()
                logger.info(f"Item modified from : {bookingitem}  to {exist}") #NOTE: this log is not correct, bookingitem is getting modified along with the database object


    @handle_exceptions
    def delete_booking_item(self, bookingitem: BookingItem):
        exist = self.read_booking_item(bookingitem)
        if exist is None:
            logger.info(f"No such item: {bookingitem}")
        else:
            stmt = (
                delete(self.BookingItem)
                .where(self.BookingItem.name.is_(bookingitem.name))
                .where(self.BookingItem.wbs.is_(bookingitem.wbs)))
            self.session.execute(stmt)
            self.session.commit()
            logger.info(f"Item deleted from : {exist}")

    @handle_exceptions
    def clean_booking_data(self):
        stmt = delete(self.BookingItem)
        self.session.execute(stmt)
        self.session.commit()
        logger.info("All booking data deleted")

    @handle_exceptions
    def create_time_table_item(self, new_timetable_item: TimeTable):
        exist_booking_item = self.read_booking_item(new_timetable_item.booking_item)
        new_timetable_item.booking_item = exist_booking_item

        if new_timetable_item.date is None:
            new_timetable_item.date = date.today()

        exist = self.read_time_table_item(new_timetable_item)
        if exist is None:
            self.session.add(new_timetable_item)
            self.session.commit()
            logger.info(f"Created new item: {new_timetable_item}")
        else:
            logger.warning(f"TimeTable item already exists in database: {exist}")
            #add hours to existing item
            stmt = (
                update(self.TimeTable)
                .where(self.TimeTable.id == exist.id)
                .values(hours = exist.hours + new_timetable_item.hours))
            self.session.execute(stmt)
            self.session.commit()
            logger.info(f"Item modified to : {exist}")
        return self.read_time_table_item(new_timetable_item)

    @handle_exceptions
    def read_time_table_item(self, timetable: TimeTable):
        item = self.session.scalars(select(self.TimeTable)
                                .where(self.TimeTable.booking_item == timetable.booking_item) #itt miért nem primary key alapján keresünk?
                                .where(func.DATE(self.TimeTable.date) == timetable.date)).first()
        return item

    @handle_exceptions
    def update_time_table_item(self, timetable: TimeTable): #itt a booking_itemnél volt modified meg prev is, de igazából elég csak a modified, mert az id fix
        exist = self.read_time_table_item(timetable)
        if exist is None:
            logger.info(f"No such item: {timetable}")
        else:
            #TODO: check unique constraint
            stmt = (
                update(self.TimeTable)
                .where(self.TimeTable.id == exist.id)
                .values(date = timetable.date, hours = timetable.hours))
            self.session.execute(stmt)
            self.session.commit()
            logger.info(f"Item modified from : {exist}  to {timetable}")

    @handle_exceptions
    def delete_time_table_item(self, timetable: TimeTable):
        exist = self.read_time_table_item(timetable)
        if exist is None:
            logger.info(f"No such item: {timetable}")
        else:
            stmt = (
                delete(self.TimeTable)
                .where(self.TimeTable.id == exist.id))
            self.session.execute(stmt)
            self.session.commit()
            logger.info(f"Item deleted from : {exist}")

def mock_data():
    db=DatabaseHandler()
    db.clean_booking_data()
    b1 = db.BookingItem(
        name = "Project 1",
        wbs = "test1",
    )
    b2 = db.BookingItem(
        name = "Project 2",
        wbs = "test2",
    )
    b3 = db.BookingItem(
        name = "Project 3",
        wbs = "test3",
    )
    db.create_booking_item(b1)
    db.create_booking_item(b2)
    db.create_booking_item(b3)


if __name__ == "__main__":
    db = DatabaseHandler()
    b1 = db.BookingItem(
        name = "New1111",
        wbs = "Hey",
    )

    b2 = db.BookingItem(
        name = "Test1",
        wbs = "Hey",
    )

    b3 = db.BookingItem(
        name = "Test1",
        wbs = "Heeey",
    )

    db.create_booking_item(b1)

    db.update_booking_item(b1, b2)

    db.delete_booking_item(b3)

    t1 = db.TimeTable(
        hours = 6,
        booking_item = b1
    )

    db.create_time_table_item(t1)

    logger.info(db.read_all_booking_names())