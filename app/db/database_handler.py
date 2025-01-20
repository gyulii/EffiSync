
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
        country = Column(Text, nullable=False)
        wbs = Column(Text, nullable=False)
        active = Column(Boolean, default=False)

        def __repr__(self):
            return f"<id={self.id}, country={self.country}, wbs={self.wbs}, active={self.active}>"

        def to_dict(self):
            return {
                "id": self.id,
                "country": self.country,
                "wbs": self.wbs,
                "active": self.active
            }

    class BookingItem(Base):
        __tablename__ = "bookingitem"

        id = Column(Integer, primary_key=True, autoincrement="auto")
        name = Column(Text, unique=True, nullable=False)  #are num
        active = Column(Boolean, default=False)

        def __repr__(self):
            return f"<id={self.id}, name={self.name}, active={self.active}>"

        def to_dict(self):
            return {
                "id": self.id,
                "name": self.name,
                "active": self.active
            }

    class TimeTable(Base):
        __tablename__ = "timetable"

        id = Column(Integer, primary_key=True, autoincrement="auto")
        booking_item_id = Column(Integer, ForeignKey("bookingitem.id"))
        location_id = Column(Integer, ForeignKey("location.id"))
        date = Column(Date)
        hours = Column(Float)
        sent = Column(Boolean, default=False)

        booking_item = relationship("BookingItem")
        location = relationship("Location")

        def __repr__(self):
            return f"<id={self.id}, project_id={self.booking_item_id}, location_id={self.location_id}, date={self.date}, hours={self.hours}>"

        def to_dict(self):
            return {
                "id": self.id,
                "booking_item_id": self.booking_item_id,
                "location_id": self.location_id,
                "date": self.date.strftime("%Y-%m-%d"),
                "hours": self.hours,
                "sent": self.sent
            }


    def __init__(self):
        base_dir = pathlib.Path().cwd()
        engine = sa.create_engine(fr"sqlite:///{base_dir}\app\db\test.db")
        Session = sessionmaker(bind=engine)
        self.session = Session()

        self.Base.metadata.create_all(engine)

    #Location CRUD, +readall, +clean, +activate, +archive

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
    def archive_location(self, location: Location):
        exist = self.read_location(location)
        if exist is None:
            logger.info(f"No such location: {location}")
        else:
            stmt = (
                update(self.Location)
                .where(self.Location.country.is_(location.country))
                .values(active = False))
            self.session.execute(stmt)
            self.session.commit()
            logger.info(f"Location archived : {exist}")


    @handle_exceptions
    def activate_location(self, location: Location):
        exist = self.read_location(location)
        if exist is None:
            logger.info(f"No such location: {location}")
        else:
            stmt = (
                update(self.Location)
                .where(self.Location.country.is_(location.country))
                .values(active = True))
            self.session.execute(stmt)
            self.session.commit()
            logger.info(f"Location activated : {exist}")


    @handle_exceptions
    def clean_location_data(self):
        stmt = delete(self.Location)
        self.session.execute(stmt)
        self.session.commit()
        logger.info("All location data deleted")

    @handle_exceptions
    def read_active_location_names(self):
        names = self.session.scalars(select(self.Location.country).where(self.Location.active==True)).all()
        return names

    @handle_exceptions
    def read_all_locations(self):
        names = self.session.scalars(select(self.Location)).all()
        return names

    #BookingItem CRUD, +readall, +clean, +activate, +archive

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
    def read_active_booking_names(self):
        names = self.session.scalars(select(self.BookingItem.name).where(self.BookingItem.active==True)).all()
        return names

    @handle_exceptions
    def read_all_projects(self):
        names = self.session.scalars(select(self.BookingItem)).all()
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
    def archive_booking_item(self, bookingitem: BookingItem):
        exist = self.read_booking_item(bookingitem)
        if exist is None:
            logger.info(f"No such item: {bookingitem}")
        else:
            stmt = (
                update(self.BookingItem)
                .where(self.BookingItem.name.is_(bookingitem.name))
                .values(active = False))
            self.session.execute(stmt)
            self.session.commit()
            logger.info(f"Item archived : {exist}")

    @handle_exceptions
    def activate_booking_item(self, bookingitem: BookingItem):
        exist = self.read_booking_item(bookingitem)
        if exist is None:
            logger.info(f"No such item: {bookingitem}")
        else:
            stmt = (
                update(self.BookingItem)
                .where(self.BookingItem.name.is_(bookingitem.name))
                .values(active = True))
            self.session.execute(stmt)
            self.session.commit()
            logger.info(f"Item activated : {exist}")


    @handle_exceptions
    def clean_booking_data(self):
        stmt = delete(self.BookingItem)
        self.session.execute(stmt)
        self.session.commit()
        logger.info("All booking data deleted")

    #TimeTable CRUD, +readall, +clean, +archive

    @handle_exceptions
    def create_time_table_item(self, new_timetable_item: TimeTable):
        exist_booking_item = self.read_booking_item(new_timetable_item.booking_item)
        exist_location = self.read_location(new_timetable_item.location)
        new_timetable_item.booking_item = exist_booking_item
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
        bi_exist = self.read_booking_item(timetable.booking_item) if timetable.booking_item is not None else None
        loc_exist = self.read_location(timetable.location) if timetable.location is not None else None
        item = self.session.scalars(select(self.TimeTable)
                                .where(self.TimeTable.booking_item == bi_exist) #itt miért nem primary key alapján keresünk?
                                .where(self.TimeTable.location == loc_exist)
                                .where(func.DATE(self.TimeTable.date) == timetable.date)).first()
        return item

    @handle_exceptions
    def update_time_table_item(self, before: TimeTable, timetable: TimeTable): #itt a booking_itemnél volt modified meg prev is, de igazából elég csak a modified, mert az id fix
        beforeExist = self.read_time_table_item(before)
        exist = self.read_time_table_item(timetable)
        if beforeExist is None:
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
                    .where(self.TimeTable.id == beforeExist.id))
                self.session.execute(stmt2)
                self.session.commit()
                logger.info(f"Item {before} merged into {exist}")
            else:
                bi_exist = self.read_booking_item(timetable.booking_item)
                stmt = (
                    update(self.TimeTable)
                    .where(self.TimeTable.id == beforeExist.id)
                    .values(booking_item_id=bi_exist.id, date = timetable.date, hours = timetable.hours))
                self.session.execute(stmt)
                self.session.commit()
                logger.info(f"Item modified from : {before}  to {timetable}")

    @handle_exceptions
    def archive_time_table_item(self, timetable: TimeTable):
        exist = self.read_time_table_item(timetable)
        if exist is None:
            logger.info(f"No such item: {timetable}")
        else:
            stmt = (
                update(self.TimeTable)
                .where(self.TimeTable.id == exist.id)
                .values(sent = True))
            self.session.execute(stmt)
            self.session.commit()
            logger.info(f"Item achived : {exist}")

    @handle_exceptions
    def read_active_time_table_items(self):
        items = self.session.scalars(select(self.TimeTable).where(self.TimeTable.sent==False)).all()
        return items

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
            logger.info(f"Item deleted : {exist}")

    @handle_exceptions
    def clean_time_table_data(self):
        stmt = delete(self.TimeTable)
        self.session.execute(stmt)
        self.session.commit()
        logger.info("All time table data deleted")


    @handle_exceptions
    def sync_tables(self, projects, topics):

        for project in projects:
            exist = self.session.scalars(select(self.BookingItem).where(self.BookingItem.id == project['id'])).first()
            if exist is None:
                self.session.add(self.BookingItem(name = project['name'], active = project['active'], id = project['id']))
                self.session.commit()
                logger.info(f"Created project: {project}")
            else:
                if exist.name != project['name'] or exist.active != project['active']:
                    stmt = (
                        update(self.BookingItem)
                        .where(self.BookingItem.id == project['id'])
                        .values(name = project['name'], active = project['active']))
                    self.session.execute(stmt)
                    self.session.commit()
                    logger.info(f"Project modified from : {exist} to {project}")

        for topic in topics:
            exist = self.session.scalars(select(self.Location).where(self.Location.id == topic['id'])).first()
            if exist is None:
                self.session.add(self.Location(country = topic['country'], wbs = topic['wbs'], active = topic['active'], id = topic['id']))
                self.session.commit()
                logger.info(f"Created topic: {topic}")
            else:
                if exist.country != topic['country'] or exist.wbs != topic['wbs'] or exist.active != topic['active']:
                    stmt = (
                        update(self.Location)
                        .where(self.Location.id == topic['id'])
                        .values(country = topic['country'], wbs = topic['wbs'], active = topic['active']))
                    self.session.execute(stmt)
                    self.session.commit()
                    logger.info(f"Topic modified from : {exist} to {topic}")

        for proj in self.read_all_projects():
            if proj.to_dict() not in projects:
                self.archive_booking_item(proj)

        for topic in self.read_all_locations():
            if topic.to_dict() not in topics:
                self.archive_location(topic)


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

    logger.info(db.read_active_booking_names())