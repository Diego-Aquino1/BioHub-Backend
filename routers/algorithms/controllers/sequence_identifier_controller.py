from routers.algorithms.queries.waterman_query import SmithWatermanQuery
from routers.algorithms.schemas.algorithms_schema import AlignmentBody, SequenceIdentifyResponse

class SequenceIdentifierController:
    def __init__(self) -> None:
        self.adn_chars = set("ATGC")
        self.arn_chars = set("AUGC")
        self.protein_chars = set("ACDEFGHIKLMNPQRSTVWY")

    def run(self, seq: str):
        
        seq = seq.upper()

        seq_chars = set(seq)

        result = None

        # Comprobar si la secuencia es de ADN
        if seq_chars.issubset(self.adn_chars):
            result = "ADN"
        # Comprobar si la secuencia es de ARN
        elif seq_chars.issubset(self.arn_chars):
            result = "ARN"
        # Comprobar si la secuencia es de Proteína
        elif seq_chars.issubset(self.protein_chars):
            result = "Proteína"
        else:
            result = "Secuencia no reconocida"

        response = SequenceIdentifyResponse(
            type = result
        )

        return response