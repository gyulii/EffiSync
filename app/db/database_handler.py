
#This module will handle all database related logic. It will be mostly used in the server side program A.K.A. in the boss machine. @Doni @Szabi
import pathlib
from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.exc import IntegrityError
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text, Float, Date
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

    class Location(Base):
        __tablename__ = "location"

        id = Column(Integer, primary_key=True, autoincrement="auto")
        country = Column(Text, unique=True, nullable=False)
        wbs = Column(Text, nullable=False)

        def __repr__(self):
            return f"<id={self.id}, country={self.country}, wbs={self.wbs}>"

    class BookingItem(Base):
        __tablename__ = "bookingitem"

        id = Column(Integer, primary_key=True, autoincrement="auto")
        name = Column(Text, unique=True, nullable=False)  #are num

        def __repr__(self):
            return f"<id={self.id}, name={self.name}, active={self.active}>"

    class Topic(Base):
        __tablename__ = "topic"

        id = Column(Integer, primary_key=True, autoincrement="auto")
        booking_item_id = Column(Integer, ForeignKey("bookingitem.id"))
        name = Column(Text, unique=True, nullable=False)
        active = Column(Boolean, default=True)

        booking_item = relationship("BookingItem")

        def __repr__(self):
            return f"<id={self.id}, booking_item_id={self.booking_item_id}, name={self.name}, active={self.active}>"

    class TimeTable(Base):
        __tablename__ = "timetable"

        id = Column(Integer, primary_key=True, autoincrement="auto")
        topic_id = Column(Integer, ForeignKey("topic.id"))
        location_id = Column(Integer, ForeignKey("location.id"))
        date = Column(Date)
        hours = Column(Float)

        topic = relationship("Topic")
        location = relationship("Location")

        def __repr__(self):
            return f"<id={self.id}, project_id={self.topic_id}, location_id={self.location_id}, date={self.date}, hours={self.hours}>"


    def __init__(self):
        base_dir = pathlib.Path().cwd()
        engine = sa.create_engine(fr"sqlite:///{base_dir}\app\db\test.db")
        Session = sessionmaker(bind=engine)
        self.session = Session()

        self.Base.metadata.create_all(engine)

    #Location CRUD, +readall, +clean

    @handle_exceptions
    def create_location(self, new_location: Location):
        exist = self.read_location(new_location)
        if exist is None:
            self.session.add(new_location)
            self.session.commit()
            logger.info(f"Created location: {new_location}")
        else:
            logger.warning(f"Location already exists in database: {exist}")
        return self.read_location(new_location)

    @handle_exceptions
    def read_location(self, location: Location):
        loc = self.session.scalars(select(self.Location)
                            .where(self.Location.country == location.country)).first()
        return loc

    @handle_exceptions
    def update_location(self, location: Location, modified_location: Location):
        exist = self.read_location(location)
        modified_exist = self.read_location(modified_location)
        if exist is None:
            logger.info(f"No such location: {location}")
        else:
            if modified_exist is not None:
                logger.info(f"Location already exists in database: {modified_exist}")
            else:
                stmt = (
                    update(self.Location)
                    .where(self.Location.country.is_(location.country))
                    .values(country = modified_location.country, wbs = modified_location.wbs))
                self.session.execute(stmt)
                self.session.commit()
                logger.info(f"Location modified from : {location}  to {modified_location}")

    @handle_exceptions
    def delete_location(self, location: Location):
        exist = self.read_location(location)
        if exist is None:
            logger.info(f"No such location: {location}")
        else:
            stmt = (
                delete(self.Location)
                .where(self.Location.country.is_(location.country)))
            self.session.execute(stmt)
            self.session.commit()
            logger.info(f"Location deleted from : {exist}")

    @handle_exceptions
    def clean_location_data(self):
        stmt = delete(self.Location)
        self.session.execute(stmt)
        self.session.commit()
        logger.info("All location data deleted")

    @handle_exceptions
    def read_all_location_names(self):
        names = self.session.scalars(select(self.Location.country)).all()
        return names

    #BookingItem CRUD, +readall, +clean

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
                            .where(self.BookingItem.name == bookingitem.name)).first()
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
                .where(self.BookingItem.name.is_(bookingitem.name)))
            self.session.execute(stmt)
            self.session.commit()
            logger.info(f"Item deleted from : {exist}")

    @handle_exceptions
    def clean_booking_data(self):
        stmt = delete(self.BookingItem)
        self.session.execute(stmt)
        self.session.commit()
        logger.info("All booking data deleted")


    #Topic CRUD, +readall, +clean

    @handle_exceptions
    def create_topic(self, new_topic: Topic):
        exist = self.read_topic(new_topic)
        if exist is None:
            self.session.add(new_topic)
            self.session.commit()
            logger.info(f"Created topic: {new_topic}")
        else:
            logger.warning(f"Topic already exists in database: {exist}")
        return self.read_topic(new_topic)

    @handle_exceptions
    def read_topic(self, topic: Topic):
        booking_item_exist = self.read_booking_item(topic.booking_item)
        item = self.session.scalars(select(self.Topic)
                            .where(self.Topic.name == topic.name)
                            .where(self.Topic.booking_item_id == booking_item_exist.id)).first()
        return item

    @handle_exceptions
    def read_all_topic_names(self, booking_item: BookingItem):
        booking_item_exist = self.read_booking_item(booking_item)
        names = self.session.scalars(select(self.Topic.name)
                            .where(self.Topic.booking_item_id == booking_item_exist.id)
                            .where(self.Topic.active==True)).all()
        return names

    def archive_topic(self, topic: Topic):
        exist = self.read_topic(topic)
        if exist is None:
            logger.info(f"No such topic: {topic}")
        else:
            stmt = (
                update(self.Topic)
                .where(self.Topic.id == exist.id)
                .values(active = False))
            self.session.execute(stmt)
            self.session.commit()
            logger.info(f"Topic archived: {exist}")

    @handle_exceptions
    def update_topic(self, topic: Topic, modified_topic: Topic):
        exist = self.read_topic(topic)
        bi_exist = self.read_booking_item(topic.booking_item)
        modified_exist = self.read_topic(modified_topic)
        bi_modified_exist = self.read_booking_item(modified_topic.booking_item)
        if exist is None:
            logger.info(f"No such item: {topic}")
        else:
            if modified_exist is not None:
                logger.info(f"Item already exists in database: {modified_exist}")
            else:
                stmt = (
                    update(self.Topic)
                    .where(self.Topic.name.is_(topic.name))
                    .where(self.Topic.booking_item_id == bi_exist.id)
                    .values(name = modified_topic.name, booking_item_id = bi_modified_exist.id, active = modified_topic.active))
                self.session.execute(stmt)
                self.session.commit()
                logger.info(f"Item modified from : {topic}  to {exist}")

    #TimeTable CRUD, +readall, +clean

    @handle_exceptions
    def create_time_table_item(self, new_timetable_item: TimeTable):
        exist_topic = self.read_topic(new_timetable_item.topic)
        exist_location = self.read_location(new_timetable_item.location)
        new_timetable_item.topic = exist_topic
        new_timetable_item.location = exist_location

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
        topic_exist = self.read_topic(timetable.topic) if timetable.topic is not None else None
        loc_exist = self.read_location(timetable.location) if timetable.location is not None else None
        item = self.session.scalars(select(self.TimeTable)
                                .where(self.TimeTable.topic == topic_exist) #itt miért nem primary key alapján keresünk?
                                .where(self.TimeTable.location == loc_exist)
                                .where(func.DATE(self.TimeTable.date) == timetable.date)).first()
        return item

    @handle_exceptions
    def update_time_table_item(self, before: TimeTable, timetable: TimeTable): #itt a booking_itemnél volt modified meg prev is, de igazából elég csak a modified, mert az id fix
        before_exist = self.read_time_table_item(before)
        exist = self.read_time_table_item(timetable)
        if before_exist is None:
            logger.info(f"No such item: {before}")
        else:
            # check unique constraint
            if exist is not None:
                logger.info(f"Item already exists in database: {exist}")
                #add hours to existing item
                stmt = (
                    update(self.TimeTable)
                    .where(self.TimeTable.id == exist.id)
                    .values(hours = exist.hours + timetable.hours))
                self.session.execute(stmt)
                stmt2 = (
                    delete(self.TimeTable)
                    .where(self.TimeTable.id == before_exist.id))
                self.session.execute(stmt2)
                self.session.commit()
                logger.info(f"Item {before} merged into {exist}")
            else:
                bi_exist = self.read_booking_item(timetable.booking_item)
                stmt = (
                    update(self.TimeTable)
                    .where(self.TimeTable.id == before_exist.id)
                    .values(booking_item_id=bi_exist.id, date = timetable.date, hours = timetable.hours))
                self.session.execute(stmt)
                self.session.commit()
                logger.info(f"Item modified from : {before}  to {timetable}")

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

    @handle_exceptions
    def read_all_time_table_items(self):
        items = self.session.scalars(select(self.TimeTable)).all()
        return items

    @handle_exceptions
    def clean_time_table_data(self):
        stmt = delete(self.TimeTable)
        self.session.execute(stmt)
        self.session.commit()
        logger.info("All time table data deleted")


def mock_data():
    db=DatabaseHandler()
    db.clean_location_data()
    db.clean_booking_data()
    db.clean_time_table_data()
    l1 = db.Location(
        country="HUN",
        wbs="wbs123"
    )
    l2 = db.Location(
        country="GER",
        wbs="GER"
    )
    l3 = db.Location(
        country="MOR",
        wbs="wbs256"
    )
    db.create_location(l1)
    db.create_location(l2)
    db.create_location(l3)

    b1 = db.BookingItem(
        name = "Project 1",
    )
    b2 = db.BookingItem(
        name = "Project 2",
    )
    b3 = db.BookingItem(
        name = "Project 3",
    )
    db.create_booking_item(b1)
    db.create_booking_item(b2)
    db.create_booking_item(b3)

    t1 = db.TimeTable(
        hours = 6,
        date=date(2024, 11, 24),
        booking_item = b1,
        location=l1
    )
    t2 = db.TimeTable(
        hours = 6,
        date=date(2024, 11, 25),
        booking_item = b2,
        location=l2
    )
    db.create_time_table_item(t1)
    db.create_time_table_item(t2)


if __name__ == "__main__":
    db = DatabaseHandler()
    db.clean_location_data()
    db.clean_booking_data()
    db.clean_time_table_data()
    b1 = db.BookingItem(
        name = "New1111"
    )

    b2 = db.BookingItem(
        name = "Test1"
    )

    b3 = db.BookingItem(
        name = "Test1"
    )
    l1 = db.Location(
        country="TUR",
        wbs="wbs364"
    )
    db.create_location(l1)
    db.create_booking_item(b1)

    db.update_booking_item(b1, b2)

    #db.delete_booking_item(b3)

    t1 = db.TimeTable(
        hours = 6,
        booking_item = b1,
        location=l1
    )

    db.create_time_table_item(t1)

    logger.info(db.read_all_booking_names())