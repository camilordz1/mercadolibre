from .actions import Actions


class Bill(Actions):

    def __init__(self, session) -> None:
        self.session = session

    def info(self, id):

        '''Return billing information from a order by id'''

        url = f"https://api.mercadolibre.com/orders/{id}/billing_info"

        response = self.get(url, self.session.headers)

        return response

    def documents(self, pack_id):

        '''check if order has a invoice return True of False'''

        url = f"https://api.mercadolibre.com/packs/{pack_id}/fiscal_documents"

        response = self.get(url, self.session.headers)

        if response is False:
            return response

        return True

    def upload(self, id, url_file):

        url = f"https://api.mercadolibre.com/packs/{id}/fiscal_documents"

        files = {
            'fiscal_document': open(url_file, 'rb')
        }

        response = self.post(url, self.session.headers, fl=files)

        return response
