from pydantic import BaseModel
from typing import Optional, List

# --- Schémas secondaires ---

class RatingBase(BaseModel):
    userId: int
    movieId: int
    rating: float
    timestamp: int

    model_config = {"from_attributes": True}


class TagBase(BaseModel):
    userId: int
    movieId: int
    tag: str
    timestamp: int

    model_config = {"from_attributes": True}


class LinkBase(BaseModel):
    imdbId: Optional[str]
    tmdbId: Optional[int]

    model_config = {"from_attributes": True}


# --- Schéma principal pour Movie ---
class MovieBase(BaseModel):
    movieId: int
    title: str
    genres: Optional[str] = None

    model_config = {"from_attributes": True}


class MovieDetailed(MovieBase):
    ratings: List[RatingBase] = []
    tags: List[TagBase] = []
    link: Optional[LinkBase] = None


# --- Liste de films simplifiée ---
class MovieSimple(BaseModel):
    movieId: int
    title: str
    genres: Optional[str]

    model_config = {"from_attributes": True}


# --- Schémas pour endpoints isolés ---
class RatingSimple(BaseModel):
    userId: int
    movieId: int
    rating: float
    timestamp: int

    model_config = {"from_attributes": True}


class TagSimple(BaseModel):
    userId: int
    movieId: int
    tag: str
    timestamp: int

    model_config = {"from_attributes": True}


class LinkSimple(BaseModel):
    movieId: int
    imdbId: Optional[str]
    tmdbId: Optional[int]

    model_config = {"from_attributes": True}


class AnalyticsResponse(BaseModel):
    movie_count: int
    rating_count: int
    tag_count: int
    link_count: int

    model_config = {"from_attributes": True}
