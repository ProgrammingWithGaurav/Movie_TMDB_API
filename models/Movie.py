from pydantic import BaseModel
from typing import List, Optional

class Movie(BaseModel):
    id: int
    title: str
    overview: Optional[str] = None
    release_date: Optional[str] = None
    vote_average: Optional[float] = None
    vote_count: Optional[int] = None
    popularity: Optional[float] = None
    poster_path: Optional[str] = None
    originalLanguage: Optional[str] = None
    original_title: Optional[str] = None
    genre_ids: Optional[List[int]] = None
    backdrop_path: Optional[str] = None
    