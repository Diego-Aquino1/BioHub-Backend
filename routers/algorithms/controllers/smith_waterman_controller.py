from routers.algorithms.queries.waterman_query import SmithWatermanQuery
from routers.algorithms.schemas.algorithms_schema import AlignmentBody

class SmithWatermanController:
    def __init__(self, body: AlignmentBody) -> None:
        self.query = SmithWatermanQuery(body.seq1, body.seq2, body.match, body.mismatch, body.gap)

    def run(self):
        response = self.query.align()
        return response