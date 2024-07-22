
#This module will handle all database related logic. It will be mostly used in the server side program A.K.A. in the boss machine. @Doni @Szabi
import pathlib
import datetime

import sqlalchemy as sa
from sqlalchemy.exc import IntegrityError
from sqlalchemy import Integer, String, Float, DateTime, ForeignKey, select
from sqlalchemy.orm import (
    declarative_base,
    mapped_column,
    relationship,
    sessionmaker,
    Mapped,
)


base_dir = pathlib.Path().cwd()

db = sa.create_engine(fr"sqlite:///{base_dir}\app\db\test.db")
Session = sessionmaker(bind=db)
Base = declarative_base()
Base.metadata.create_all(db)

class db_BookingItemTable(Base):
    __tablename__ = "BookingItemTable"
    id = mapped_column(Integer, primary_key=True)
    text = mapped_column(String)
    wbs_id = mapped_column(Integer, ForeignKey("BookingWbsTable.id"))

    booked_elements= relationship("db_BookingDateTable", back_populates="booked_item")
    wbs= relationship("db_BookingWbsTable")

    def __repr__(self) -> str:
        return f"<db_BookingItemTable(wbs={self.wbs}, text={self.text})>"

    
    
class db_BookingDateTable(Base):
    __tablename__ = "BookingDateTable"
    id = mapped_column(Integer, primary_key=True)
    date= mapped_column(DateTime) 
    booked_time  = mapped_column(Float)
    booked_item_id = mapped_column(Integer, ForeignKey("BookingItemTable.id"))

    booked_item = relationship("db_BookingItemTable", back_populates="booked_elements")


class db_BookingWbsTable(Base):
    __tablename__ = "BookingWbsTable"
    id = mapped_column(Integer, primary_key=True)
    wbs = mapped_column(String, unique=True)

    def __repr__(self) -> str:
        return f"<wbs={self.wbs}>"
    




def initialize_db() -> None:
    pass

def add_new_booking_item(wbs = 'Empty Wbs' , text = 'Default Booking item'):
    with Session() as session:
        try:
            wbs_new = db_BookingWbsTable(wbs=wbs)
            session.add(wbs_new)
            session.commit()
        except IntegrityError:
            print("wbs already exists")
            session.rollback()
            wbs_new = session.scalars(select(db_BookingWbsTable).where(db_BookingWbsTable.wbs == wbs)).all()[0]

        booking_item = db_BookingItemTable(wbs=wbs_new, text=text)
        session.add(booking_item)
        session.commit()

def edit_booking_item():
    pass
    
def delete_booking_item():
    pass





def main() -> None:



    with Session() as session:
        try:
            wbs = db_BookingWbsTable(wbs="wbs-123232")
            session.add(wbs)
            session.commit()
        except IntegrityError:
            print("wbs already exists")

    with Session() as session:
            #wbs =  session.execute(select(db_BookingWbsTable).where(db_BookingWbsTable.id == 2)).all()[0][0]
            wbs = session.execute(select(db_BookingWbsTable).where(db_BookingWbsTable.wbs == '')).all()[0][0]
            wbs2 = session.scalars(select(db_BookingWbsTable)).all()[0]

            
            booking_item = db_BookingItemTable(wbs=wbs, text="Bookking_text-Example123")
            booking_item2 = db_BookingItemTable(wbs=wbs, text="Bookking_text-Example456")
            booking_log1 = db_BookingDateTable(date = datetime.datetime(year = 1980, month = 3, day = 4), 
                                               booked_time=8,
                                               booked_item = booking_item)
            #session.add(booking_item)
            #session.add(booking_item2)
            
            #session.commit()
            res = session.scalars(select(db_BookingDateTable)).all()[0]
            print(res.booked_time)









if __name__ == "__main__":
    main()


    add_new_booking_item()


class UserAuth(Base):
    __tablename__ = "user_auth"

    id: int = sa.Column(
        sa.Integer, sa.ForeignKey("users.id"), primary_key=True, index=True, unique=True
    )
    username: str = sa.Column(sa.String)
    email: str = sa.Column(sa.String, unique=True)
    password_hash: str = sa.Column(sa.String)
    user: Mapped["User"] = relationship("User", back_populates="auth")

    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

    def set_password(self, password: str) -> None:
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password: str) -> bool:
        return self.password_hash == hashlib.sha256(password.encode()).hexdigest()

    def __repr__(self) -> str:
        return f"<UserAuth(username={self.username}, email={self.email})>"