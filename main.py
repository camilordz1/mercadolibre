from mercadoLibre import Session
from mercadoLibre import Order


def run():

    session = Session("ml.pkl", 'user_ml.pkl', "ml_api.pkl")
    orders = Order(session)
    orders.list()


if __name__ == "__main__":
    run()
