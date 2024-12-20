# Implementation through websocket or SSE 

import requests

def access_sse_stream(url):
    """Access and process events from a Server-Sent Events (SSE) stream."""
    try:
        with requests.get(url, stream=True, verify=False) as response:
            # Ensure the response was successful
            response.raise_for_status()

            # Loop indefinitely to process all events as they come in
            for line in response.iter_lines():
                # Filter out keep-alive new lines
                if line:
                    decoded_line = line.decode('utf-8')
                    print(f"Received event: {decoded_line}")
                    # Here you can add logic to process the event
                    # For example, you could parse the event data and act accordingly

    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # The URL where the SSE stream is accessible
    url = "https://152.66.182.112:5002/send"
    data = {"wbs": "GER",
            "day": "2021-10-01",
            "hours": 4.5,
            "project": "Python"}
    for line in requests.post(url, json=data, verify=False).iter_lines():
        print(line)
    #sse_url = "https://152.66.182.112:5002/subscribe"
    #access_sse_stream(sse_url)
