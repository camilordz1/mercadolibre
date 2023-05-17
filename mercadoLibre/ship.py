from .actions import Actions


class Ship(Actions):

    def __init__(self, session) -> None:

        self.session = session

    def info(self, id) -> dict:

        '''Return shipping information from a order by id'''

        url = f"https://api.mercadolibre.com/shipments/{id}"

        response = self.get(url, self.session.headers)

        return response
