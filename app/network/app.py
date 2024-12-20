#
#  Example usage of ServerSentEvents with Flask.
#  Created On 21 November 2022
#

# to start the server, execute the following command 👇
# python -m flask --app examples/routes run


from flask import Flask, request
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

    def __str__(self):
        return f"{self.wbs} - {self.project} - {self.day} - {self.hours}"

records = []

@app.route("/send", methods=["POST"])
def send():
    json_data = request.get_json()
    record = TimetableRecord(**json_data)
    return str(record)

    global sse

    if sse:
        sse.send({"msg": "Python is awesome!"})
    else:
        return "NO CONNECTION"

    return "OK"


@app.route("/end")
def end():
    global sse

    if sse:
        sse.send(event="end")
        sse = None
    else:
        return "NO CONNECTION"

    return "FINISHED"


@app.route("/subscribe")
def subscribe():
    global sse

    # create a new server sent events channel
    sse = ServerSentEvents()

    return sse.response()


if __name__ == "__main__":
    app.run(host='0.0.0.0' , port=5002, ssl_context='adhoc')
