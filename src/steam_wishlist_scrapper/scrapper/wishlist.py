from pprint import pprint
from string import Template
from typing import Any

import httpx as httpx
from httpx import Response

from steam_wishlist_scrapper.models.game import Game

_WISHLIST_URL_TEMPLATE: Template = Template(
	"https://store.steampowered.com/wishlist/id/${vanity_url}/wishlistdata/?p=${page}"
)


def _get_wishlist_games_for_page(vanity_url: str, page: int) -> list[Game] | None:
	url: str = _WISHLIST_URL_TEMPLATE.substitute(vanity_url=vanity_url, page=page)
	response: Response = httpx.get(url)
	response.raise_for_status()

	response_data: list | dict[dict[str, Any]] = response.json()

	match response_data:
		case []:
			return None
		case {}:
			return list(map(Game.parse_obj, response_data.values()))


def get_all_wishlist_games(vanity_url: str) -> list[Game]:
	page: int = 0
	results: list[Game] = []

	page_results: list[Game] | None

	while (page_results := _get_wishlist_games_for_page(vanity_url, page)) is not None:
		results.extend(page_results)
		page += 1

	return list(filter(Game.is_game, results))


def _main() -> None:
	vanity_url: str = input("Vanity URL: ")
	games: list[Game] = get_all_wishlist_games(vanity_url)
	pprint(games)


if __name__ == '__main__':
	_main()
