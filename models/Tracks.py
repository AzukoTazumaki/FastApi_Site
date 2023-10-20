from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship
from .AlbumsTracks import AlbumsTracks
from .ArtistsTracks import ArtistsTracks
from datetime import time, date


class Tracks(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(nullable=False)
    duration: time
    date_release: date
    track_position_in_album: Optional[int] = Field(nullable=True)
    artists: List['Artists'] = Relationship(back_populates='tracks', link_model=ArtistsTracks)
    albums: List['Albums'] = Relationship(back_populates='tracks', link_model=AlbumsTracks)
    single: Optional['Singles'] = Relationship(back_populates='track')
    featuring: Optional['Featurings'] = Relationship(back_populates='track')
    text: Optional['Lyrics'] = Relationship(back_populates='track')

