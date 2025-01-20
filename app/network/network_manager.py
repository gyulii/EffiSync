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

    def __str__(self):
        return f"{self.wbs} - {self.project} - {self.day} - {self.hours}"


class RelayManager:
    key = "a"
    datas = []

    def __init__(self, url: str = "https://152.66.182.112:5002", verify: bool = False):
        self.url = url
        self.verify = verify

    def get_data(self):
        """Get the timetable records for the manager."""
        response = requests.get(f"{self.url}/get", headers={'key': self.key}, verify=self.verify)
        if response.status_code == 200:
            records = response.json()
            return [TimetableRecord(**record) for record in records]
        else:
            return []

    def sync_manager(self, projects: list, topics: list):
        """Sync the projects with the manager."""
        response = requests.post(f"{self.url}/sync/manager", json={'projects':projects, 'topics':topics}, headers={'key': self.key}, verify=self.verify)
        if response.status_code == 200:
            return True, response.text
        else:
            return False, response.text

if __name__ == "__main__":
    manager = RelayManager()
    records = manager.get_data()
    for record in records:
        print(record)