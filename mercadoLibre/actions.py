from requests import request
import json


class Actions:

    def get(self, url, hds, prs={}, dt={}):

        response = request("GET",
                           url,
                           headers=hds,
                           params=prs,
                           data=dt)

        if response.status_code == 404:
            return False

        return json.loads(response.text)

    def post(self, url, hds, prs={}, dt={}, fl={}):

        response = request("POST",
                           url,
                           headers=hds,
                           params=prs,
                           data=dt,
                           files=fl)

        if response.status_code == 404:
            response = json.loads(response.text)
            return print("[ERROR] ", response)

        elif response.status_code == 204:
            response = json.loads(response.text)
            return print(response)
