from dataclasses import dataclass

@dataclass
class BookingItem:
    text: str = ""
    booked_hours: float = 0
    wbs: str = "O-HU-4-002-08-01"

    def __post_init__(self):
        self.booked_hours = str(self.booked_hours).replace(".", ",")

    def start_time(self, current_time: str):
        pass

    def stop_time(self, current_time:str):
        pass
