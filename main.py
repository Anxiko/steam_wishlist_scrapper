import sys
from pprint import pprint

from models.game import Game
from scrapper.wishlist import get_all_wishlist_games


def main() -> None:
	match sys.argv:
		case [_, vanity_url]:
			games: list[Game] = get_all_wishlist_games(vanity_url)
			pprint(games)
		case _:
			print("Usage: python main.py vanity_url")


if __name__ == '__main__':
	main()
