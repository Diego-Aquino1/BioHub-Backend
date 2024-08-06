from typing import Optional
from pydantic import BaseModel

class SequenceIdentifyResponse(BaseModel):
    type: str

class AlignmentBody(BaseModel):
    seq1: str
    seq2: str
    match: Optional[int]
    mismatch: Optional[int]
    gap: Optional[int]

class IntroductionBody(BaseModel):
    seq1: str
    seq2: str

class StarAlignmentBody(BaseModel):
    sequences: list[str]
    filename: str
    match: Optional[int]
    mismatch: Optional[int]
    gap: Optional[int]

class StarAlignmentResponse(BaseModel):
    execution_time: float
    best_score: int
    multiple_alignment: list[str]
    alignments: list[tuple[str, str]]
    star_index: int
    score_matrix: list[list[int]]

class ClusteringBody(BaseModel):
    distance_matrix: list[list[float]]
    filename: str

class ClusteringResponse(BaseModel):
    execution_time: float
    clusters: list[int]
    history: list[tuple[list[int], list[int], float]]