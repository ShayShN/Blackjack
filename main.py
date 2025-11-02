from deck import build_standard_deck,shuffle_by_suit, temp, arr
from logic_game import  run_full_game
 

player = {"hand": [ ] }
dealer = {"hand": [ ] }

if __name__ == "__main__":
    player = {"hand": [ ] }
    dealer = {"hand": [ ] }
    
    package = build_standard_deck()
    package = shuffle_by_suit(package)
    start_game = run_full_game(package, player, dealer)
    print(start_game)  