from datetime import datetime
from routers.algorithms.queries.needleman_query import NeedlemanWunshQuery
from routers.algorithms.schemas.algorithms_schema import NeedlemanWunshBody
# from utilities.auth import ApiAuth

class NeedlemanWunshController:
    def __init__(self, body:NeedlemanWunshBody) -> None:

        self.query = NeedlemanWunshQuery(body.seq1, body.seq2)

    # def run(self, auth: ApiAuth):
    def run(self):

        response = self.query.align()
        
        return response