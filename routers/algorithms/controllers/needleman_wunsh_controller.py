from datetime import datetime
from routers.algorithms.queries.needleman_query import NeedlemanWunshQuery
from routers.algorithms.schemas.algorithms_schema import AlignmentBody
# from utilities.auth import ApiAuth

class NeedlemanWunshController:
    def __init__(self, body:AlignmentBody) -> None:

        self.query = NeedlemanWunshQuery(body.seq1, body.seq2, body.match, body.mismatch, body.gap)

    # def run(self, auth: ApiAuth):
    def run(self):

        response = self.query.align()
        
        return response