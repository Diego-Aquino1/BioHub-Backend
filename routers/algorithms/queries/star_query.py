from routers.algorithms.queries.needleman_query import NeedlemanWunshQuery

MATCH_SCORE = 1
MISMATCH_SCORE = -1
GAP_PENALTY = -2


class StarAlignment:
    def __init__(self, sequences, match=1, mismatch=-1, gap=-2) -> None:
        self.sequences: list = sequences
        self.n = len(self.sequences)
        self.match_score: int = match
        self.mismatch_score: int = mismatch
        self.gap_penalty: int = gap
        self.distance_matrix = [[0] * (self.n) for _ in range(self.n)]
        self.star = 0
        self.best_score = 0
        self.history = {}
        self.msa = []

    def align(self):
        self.fill_distance_matrix()
        self.find_star_sequence()
        self.merge_sequences()
        response = self.generate_results()
        return response

    def find_score(self, sequence1_index, sequence2_index):
        sequence1 = self.sequences[sequence1_index]
        sequence2 = self.sequences[sequence2_index]
        nw = NeedlemanWunshQuery(
            sequence1, sequence2, self.match_score, self.mismatch_score, self.gap_penalty)
        nw.align()
        self.history[sequence1_index, sequence2_index] = nw.alignments[-1]
        return nw.score_matrix[nw.m][nw.n]

    def fill_distance_matrix(self):
        for i in range(self.n):
            for j in range(self.n):
                if i < j:
                    self.distance_matrix[i][j] = self.find_score(i, j)
                    self.distance_matrix[j][i] = self.distance_matrix[i][j]
                elif i == j:
                    self.distance_matrix[i][j] = "-"

    def find_star_sequence(self):
        size = len(self.distance_matrix)
        max_sum = float('-inf')
        central_sequence = None
        central_index = 0
        for i in range(0, size):
            sum_distance = 0
            for j in range(0, size):
                if i != j and self.distance_matrix[i][j] != '-':
                    sum_distance += int(self.distance_matrix[i][j])

            if sum_distance > max_sum:
                max_sum = sum_distance
                central_sequence = self.distance_matrix[i][0]
                central_index = i

        self.star = central_index
        self.best_score = max_sum
        for key in list(self.history.keys()):
            if self.star not in key:
                del self.history[key]

    def merge_sequences(self):
        center_seq = self.sequences[self.star].ljust(
            max(len(seq) for seq in self.sequences), '-')
        self.msa.append(center_seq)
        for center_aligned, seq_aligned in self.history.values():
            if len(center_aligned) > len(self.msa[0]):
                self.msa = [s.ljust(len(center_aligned), '-')
                            for s in self.msa]
            elif len(center_aligned) < len(self.msa[0]):
                center_aligned = center_aligned.ljust(len(self.msa[0]), '-')
                seq_aligned = seq_aligned.ljust(len(self.msa[0]), '-')
            self.msa.append(seq_aligned)

    def generate_results(self):
        results = {
            "sequences": self.sequences,
            "match_score": self.match_score,
            "mismatch_score": self.mismatch_score,
            "gap_penalty": self.gap_penalty,
            "star_index": self.star,
            "star_sequence": f"S{self.star + 1}",
            "best_score": self.best_score,
            "multiple_alignment": self.msa,
            "alignments": list(self.history.values()),
            "score_matrix": self.distance_matrix
        }
        return results
