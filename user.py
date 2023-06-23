from pydantic import BaseModel
from typing import Optional

class pelicula(BaseModel):
    id: Optional[str]
    films: str
    director: str
    year: int
    url: str 