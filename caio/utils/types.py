from __future__ import annotations
from enum import Enum
from pydantic import BaseModel

RowType = dict[str, str | list[bool]]


class Winner(Enum):
    BLACK = "black"
    WHITE = "white"
    DRAW = "draw"


class Row(BaseModel):
    jogadas_all: list[bool]
    jogadas_white: list[bool]
    jogadas_black: list[bool]
    white_id: str
    black_id: str
    winner: Winner
    white_rating: int
    black_rating: int
    opening_fly: int
    max_sequence_white: int
    max_sequence_black: int

    @property
    def winner_id(self) -> str:
        match self.winner:
            case Winner.WHITE:
                return self.white_id
            case Winner.BLACK:
                return self.black_id
        return "draw"

    @property
    def winner_jogadas(self) -> list[bool]:
        match self.winner:
            case Winner.WHITE:
                return self.jogadas_white
            case Winner.BLACK:
                return self.jogadas_black
        return []

    @property
    def loser_jogadas(self) -> list[bool]:
        match self.winner:
            case Winner.BLACK:
                return self.jogadas_white
            case Winner.WHITE:
                return self.jogadas_black
        return []

    @property
    def white_ratio(self) -> float:
        return self.jogadas_white.count(True) / len(self.jogadas_white)

    @property
    def black_ratio(self) -> float:
        return self.jogadas_black.count(True) / len(self.jogadas_black)

    def deveria_ter_ganhado(self, elo_diff: int = 0) -> bool:
        match self.winner:
            case Winner.BLACK:
                return (
                    self.white_ratio < self.black_ratio
                    and self.black_rating > self.white_rating
                )
            case Winner.WHITE:
                return (
                    self.black_ratio < self.white_ratio
                    and self.white_rating > self.black_rating
                )
        return False

    @classmethod
    def create(cls, values: dict[str, str]) -> Row:
        formatted: dict[str, str | int | list[bool]] = {}

        for k, v in values.items():
            formatted[k] = v.strip()
            if k.startswith("jogadas_"):
                formatted[k] = [bool(int(m)) for m in v.split("|") if m]

        return Row(**formatted)

    def to_csv(self) -> str:
        line = ""
        for attr in self.model_fields:
            value = self.__getattribute__(attr)

            if isinstance(value, list):
                line += "|".join([str(int(f)) for f in value]) + ";"
            elif isinstance(value, str):
                line += value + ";"
            elif isinstance(value, int):
                line += str(value) + ";"
            elif isinstance(value, Winner):
                line += value.value + ";"

        return line
