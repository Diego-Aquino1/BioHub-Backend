from datetime import datetime
from database import get_session
from routers.algorithms.queries.user_queries import UserQuery
# from utilities.auth import ApiAuth

class ProductsAllController:
    def __init__(self) -> None:
        session = get_session()
        self.query = UserQuery(session)

    # def run(self, auth: ApiAuth):
    def run(self):

        products = self.query.find_all()

        return products