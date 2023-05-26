from enum import StrEnum

from pydantic import BaseModel, StrictStr, Field


class GameType(StrEnum):
	GAME = "Game"


class Game(BaseModel):
	name: StrictStr
	type_: GameType | str = Field(alias="type")

	def is_game(self) -> bool:
		return self.type_ == GameType.GAME
