from player_io import ask_player_action
from deck import temp, arr

def calculate_hand_value(hand: list[dict]) -> int:
    result = 0
    for i in hand:
        result += int(i["rank"])  
    return result  
        
def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    player["hand"].append(deck.pop())
    player["hand"].append(deck.pop())
    dealer["hand"].append(deck.pop())
    dealer["hand"].append(deck.pop())
    print(calculate_hand_value(player))
    print(calculate_hand_value(dealer))
   
    
    
def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while calculate_hand_value(dealer) <= 17:
        dealer["hand"].append(deck.pop())
        if calculate_hand_value(dealer) > 21:
            return f'oops! {False}'
        if 17 < calculate_hand_value(dealer) <= 21:
            return True
        

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck, player, dealer)
    
    while True:
        user_choice = ask_player_action()
        if user_choice == "H":
            user_sum = calculate_hand_value(player["hand"])
            if user_sum > 21:
                return "you are lost!!!"
            player["hand"].append(deck.pop())
        if user_choice == "S":
            dealer_turn = dealer_play(deck, dealer)
            if dealer_turn == True:
                user_result = calculate_hand_value(player["hand"])
                dealer_result = calculate_hand_value(dealer["hand"])
                if user_result > dealer_result:
                    return f'the user is the winner the sum: {user_result}'
                elif dealer_result < dealer_result:
                    return f'the dealer is the winner the sum: {dealer_result}'
                else:
                    return f'equal\n user: {user_result}\n dealer: {dealer_result}'
            return dealer_turn
        continue
        
        
    
    
    
        