from typing import Optional
from pydantic import BaseModel

class NeedlemanWunshBody(BaseModel):
    seq1: str
    seq2: str