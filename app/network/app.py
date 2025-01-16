#
#  Example usage of ServerSentEvents with Flask.
#  Created On 21 November 2022
#

# to start the server, execute the following command 👇
# python -m flask --app examples/routes run


from flask import Flask, request, jsonify
from flask_queue_sse import ServerSentEvents
from dataclasses import dataclass
import datetime

app = Flask(__name__)
sse: ServerSentEvents = None


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

    def to_dict(self):
        return {
            "wbs": self.wbs,
            "project": self.project,
            "day": self.day.strftime("%Y-%m-%d"),
            "hours": self.hours,
            "user": self.user
        }

@dataclass
class Topic:
    country: str
    wbs: str

    def __str__(self):
        return f"{self.country} - {self.wbs}"

    def to_dict(self):
        return {
            "country": self.country,
            "wbs": self.wbs
        }


@dataclass
class Project:
    name: str

    def __str__(self):
        return f"{self.name}"

    def to_dict(self):
        return {
            "name": self.name
        }

records_topics = {}
records = {}
keys_to_vals = {"a":"aaaaaaaa", "b":"bbbbbbbb", "c":"cccccccc"}
vals_to_keys = {"aaaaaaaa":"a", "bbbbbbbb":"b", "cccccccc":"c"}


@app.route("/genkeys", methods=["GET"])
def genkeys():
    pass


@app.route("/sync/manager", methods=["POST"])
def sync_manager():
    key = request.headers.get('key')
    if key not in keys_to_vals:
        return "Unauthorized", 401
    time = datetime.datetime.now()
    projects = request.json.get('projects')
    topics = request.json.get('topics')
    records_topics[key] = {
        'time': time,
        'topics': [Topic(**topic) for topic in topics],
        'projects': [Project(**project) for project in projects]
    }
    return "OK", 200


@app.route("/sync/user", methods=["GET"])
def sync_user():
    val = request.headers.get('val')
    date = request.json.get('date')
    if val not in vals_to_keys:
        return "Unauthorized", 401
    key = vals_to_keys[val]
    latest = records_topics.get(key, None)
    if latest is None:
        return "No data", 204
    if date >= latest['time']:
        return "Latest", 204
    return jsonify(latest), 200


@app.route("/send", methods=["POST"])
def send():
    json_data = request.get_json()
    val = request.headers.get('val')
    record = TimetableRecord(**json_data)
    if val in vals_to_keys:
        key = vals_to_keys[val]
        if key not in records:
            records[key] = []
        records[key].append(record)
        return str(record)
    else:
        return "Unauthorized", 401


@app.route("/get", methods=["GET"])
def get():
    key = request.headers.get('key')
    if key in keys_to_vals:
        r = records.get(key, [])
        records[key] = []
        return jsonify(r)
    else:
        return "Unauthorized", 401



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, ssl_context='adhoc')
