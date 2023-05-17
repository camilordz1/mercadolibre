from calendar import monthrange
from datetime import datetime
from .actions import Actions


class Order(Actions):

    def __init__(self, session) -> None:

        self.session = session

    def date(self, year=None, month=None):

        dt = datetime.now()

        if year is not None and month is not None:
            dt = datetime(2023, 2, 1)

        days = monthrange(int(dt.strftime("%Y")), int(dt.strftime("%m")))[1]

        date: dict = {"start": dt.strftime("%Y-%m-01T00:00:00.000-00:00"),
                      "end": dt.strftime(f"%Y-%m-{days}T23:59:59.000-00:00"),
                      "year": int(dt.strftime("%Y")),
                      "month": str(dt.strftime("%b"))}

        return date

    def list(self, offset=0, year=None, month=None):

        '''read orders from mercado libre api, max 50 orders, and starts with \
            a order offset to read new orders'''

        # set date range
        date = self.date(year, month)

        # endpoint
        url = "https://api.mercadolibre.com/orders/search"

        params = {
            "seller": self.session.user["id"],
            "order.date_created.from": date["start"],
            "order.date_created.to": date["end"],
            "limit": 50,
            "sort": "date_asc",
            "offset": offset
        }

        response = self.get(url, self.session.headers, params)

        return response

    def info(self, id):

        url = f"https://api.mercadolibre.com/orders/{id}"

        response = self.get(url, self.session.headers)

        return response

    def pack(self, order):

        url = f"https://api.mercadolibre.com/packs/{order}"

        response = self.get(url, self.session.headers)

        return response
