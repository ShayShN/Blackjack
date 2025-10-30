from deck import build_standard_deck
from logic_game import deal_two_each, run_full_game
from deck import temp, arr

player = {"hand": [ ] }
dealer = {"hand": [ ] }

if __name__ == "__main__":
    package = build_standard_deck()
    deal_two_each(package, player, dealer)
    start_game = run_full_game(package, player, dealer)
    print(start_game)