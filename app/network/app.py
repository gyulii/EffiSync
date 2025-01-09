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


records = {}


@app.route("/send", methods=["POST"])
def send():
    json_data = request.get_json()
    record = TimetableRecord(**json_data)
    if record.project not in records:
        records[record.project] = []
    records[record.project].append(record)
    return str(record)


@app.route("/get/<project>", methods=["GET"])
def get(project):
    authorized = request.authorization
    # TODO Check if the request is authorized

    r = records.get(project, [])
    records[project] = []
    return jsonify(r)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, ssl_context='adhoc')
