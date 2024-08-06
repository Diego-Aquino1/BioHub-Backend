import numpy as np

class SmithWatermanQuery:
    def __init__(self, seq1, seq2, match=1, mismatch=-1, gap=-2):
        self.seq1 = seq1
        self.seq2 = seq2
        self.match = match
        self.mismatch = mismatch
        self.gap = gap

    def align(self):
        seq1 = self.seq1
        seq2 = self.seq2
        match = self.match
        mismatch = self.mismatch
        gap = self.gap

        rows = len(seq1) + 1
        cols = len(seq2) + 1
        score_matrix = np.zeros((rows, cols), dtype=int)
        max_score = 0
        max_positions = []

        for i in range(1, rows):
            for j in range(1, cols):
                if seq1[i - 1] == seq2[j - 1]:
                    score = match
                else:
                    score = mismatch

                score_matrix[i][j] = max(
                    score_matrix[i - 1][j - 1] + score,  # Diagonal
                    score_matrix[i - 1][j] + gap,        # Arriba
                    score_matrix[i][j - 1] + gap,        # Izquierda
                    0                                    # Cero
                )

                if score_matrix[i][j] > max_score:
                    max_score = score_matrix[i][j]
                    max_positions = [(i, j)]
                elif score_matrix[i][j] == max_score:
                    max_positions.append((i, j))

        alignments = []
        for pos in max_positions:
            i, j = pos
            aligned_seq = []
            end_i, end_j = i, j
            while score_matrix[i][j] != 0:
                aligned_seq.append(seq1[i - 1])
                if score_matrix[i][j] == score_matrix[i - 1][j - 1] + (match if seq1[i - 1] == seq2[j - 1] else mismatch):
                    if score_matrix[i][j] > score_matrix[i - 1][j - 1]:
                        i -= 1
                        j -= 1
                    else:
                        aligned_seq.pop()
                        break
                else:
                    break
            aligned_seq.reverse()
            alignments.append({
                'seq1': ''.join(seq1),
                'seq2': ''.join(seq2),
                'subseq': ''.join(aligned_seq),
                'end_pos1': end_i + 1,
                'end_pos2': end_j + 1,
                'start_pos1': i + 1,
                'start_pos2': j + 1
            })

        results = {
            "score_matrix": score_matrix.tolist(),
            "max_score": max_score,
            "alignments": alignments
        }
        
        return results