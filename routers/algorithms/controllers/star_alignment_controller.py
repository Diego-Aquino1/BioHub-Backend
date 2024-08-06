from datetime import datetime

from routers.algorithms.queries.star_query import generate_file, star_alignment
from routers.algorithms.schemas.algorithms_schema import StarAlignmentBody, StarAlignmentResponse


class StarAlignmentController:
    def __init__(self, body: StarAlignmentBody) -> None:
        self.sequences = [seq.replace(" ", "") for seq in body.sequences]
        self.filename = body.filename

    def run(self):
        start_time = datetime.now()
        multiple_alignment, alignments, star, all_scores, max_score = star_alignment(len(self.sequences), self.sequences)
        end_time = datetime.now()

        execution_time = (end_time - start_time).total_seconds()
        generate_file(all_scores, alignments, multiple_alignment, (star, max_score), self.filename, execution_time)

        response = StarAlignmentResponse(
            execution_time=execution_time,
            best_score=max_score,
            multiple_alignment=multiple_alignment,
            alignments=alignments,
            star_index=star,
            score_matrix=all_scores.tolist()
        )
        return response