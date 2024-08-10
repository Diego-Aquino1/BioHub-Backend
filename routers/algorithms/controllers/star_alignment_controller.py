from datetime import datetime

from routers.algorithms.queries.star_query import StarAlignment
from routers.algorithms.schemas.algorithms_schema import StarAlignmentBody


class StarAlignmentController:
    def __init__(self, body: StarAlignmentBody) -> None:
        self.sequences = [seq.replace(" ", "") for seq in body.sequences]
        if body.match == None and body.mismatch == None and body.gap == None:
            self.query = StarAlignment(self.sequences)
        else:
            self.query = StarAlignment(
                self.sequences, body.match, body.mismatch, body.gap)

    def run(self):
        response = self.query.align()
        return response
