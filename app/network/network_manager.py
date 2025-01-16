from dataclasses import dataclass
import datetime

import requests


@dataclass
class TimetableRecord:
    """A class to represent a timetable record."""
    wbs: str
    project: str
    day: datetime.date
    hours: float
    user: str = "Test User"

    def __str__(self):
        return f"{self.user} - {self.wbs} - {self.project} - {self.day} - {self.hours}"


def get_project_data():
    """Get the timetable records for a specific project."""
    url = f"https://152.66.182.112:5002/get"
    response = requests.get(url, headers={'key': 'a'}, verify=False)
    if response.status_code == 200:
        records = response.json()
        return [TimetableRecord(**record) for record in records]
    else:
        return []

if __name__ == "__main__":
    records = get_project_data()
    for record in records:
        print(record)