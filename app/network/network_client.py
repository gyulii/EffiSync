import requests

class RelayClient:
    val = None
    datas = []

    def __init__(self, url: str="https://152.66.182.112:5002", verify: bool=False):
        self.url = url
        self.verify = verify

    def add_to_queue(self, data: dict):
        self.datas.append(data)

    def send_queue(self):
        if self.val is None:
            return False, "No val set"
        for data in self.datas:
            if not self.send_data(data)[0]:
                #return False, "Error sending data"
                #self.log(f"Error sending data to relay: {data}", "ERROR")
                pass
            else:
                self.datas.remove(data)
        return True, "All data sent"

    def send_data(self, data: dict):
        if self.val is None:
            return False, "No val set"
        response = requests.post(f"{self.url}/send", json=data, headers={'val': self.val}, verify=self.verify)
        if response.status_code == 200:
            return True, response.text
        else:
            return False, response.text

    def sync_projects_topics(self, date: str):
        if self.val is None:
            return False, "No val set"
        response = requests.get(f"{self.url}/sync/user", json={'date': date}, headers={'val': self.val}, verify=self.verify)
        if response.status_code == 200:
            return response.json()
        else:
            return False, response.text


if __name__ == "__main__":
    # The URL where the SSE stream is accessible
    url = "https://152.66.182.112:5002/send"
    data = {"wbs": "GER",
            "day": "2021-10-01",
            "hours": 4.5,
            "project": "Python"}
    for line in requests.post(url, json=data, headers={'val':"aaaaaaaa"}, verify=False).iter_lines():
        print(line)
