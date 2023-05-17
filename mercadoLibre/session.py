from datetime import datetime, timedelta
from requests import request
import pickle
import json


class Session:

    def __init__(self, access, user, meli) -> None:

        self.headers: dict = {
            'Authorization': "",
            "format-new": 'true'
        }

        self.ml_access = read(access)
        self.user = read(user)
        self.meli = read(meli)

        self.access()

    def access(self):

        time_flag = timedelta(hours=5, minutes=59, seconds=0.0)
        token_time = datetime.now()-self.ml_access['date']

        if time_flag > token_time:
            self.headers['Authorization'] = \
                f'Bearer {self.ml_access["access_token"]}'
            return self.ml_access

        self.refresh()
        self.headers['Authorization'] = \
            f'Bearer {self.ml_access["access_token"]}'

        return self.ml_access

    def refresh(self):

        url = "https://api.mercadolibre.com/oauth/token"

        payload: dict = {
            "grant_type": "refresh_token",
            "client_id": self.meli['client_id'],
            "client_secret": self.meli['client_secret'],
            "refresh_token": self.ml_access['refresh_token']
        }

        headers: dict = {
            'accept': 'application/json',
            'content-type': 'application/x-www-form-urlencoded'
        }

        response = request("POST", url, headers=headers, data=payload)

        ml_response: dict = json.loads(response.text)
        ml_response["date"] = datetime.now()

        print(ml_response)

        write("ml.pkl", ml_response)


def read(file_name: str) -> dict:
    with open(file_name, "rb") as tf:
        return pickle.load(tf)


def write(file_name: str, ml_response: dict) -> None:
    with open(file_name, "wb") as tf:
        pickle.dump(ml_response, tf)


if __name__ == "__main__":
    session = Session()
    print(session.user["id"])
