from player_io import ask_player_action
from deck import temp, arr

def calculate_hand_value(hand: list[dict]) -> int:
    result = 0
    for i in hand:
        result += int(i["rank"])  
    return result  
        
def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    player["hand"].append(deck.pop(0))
    player["hand"].append(deck.pop(0))
    dealer["hand"].append(deck.pop(0))
    dealer["hand"].append(deck.pop(0))
    print(calculate_hand_value(player["hand"]))
    print(calculate_hand_value(dealer["hand"]))
   
    
    
def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while calculate_hand_value(dealer["hand"]) <= 17:
        dealer["hand"].append(deck.pop())
        if calculate_hand_value(dealer["hand"]) > 21:
            return f'oops the dealer busterd! {False}'
        if calculate_hand_value(dealer["hand"]) > 17 or calculate_hand_value(dealer["hand"]) <= 21:
            return True
        

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    print(deal_two_each(deck, player, dealer))
    
    while True:
        print("player" ,player["hand"], "dealer", dealer["hand"])
        user_choice = ask_player_action()
        if user_choice == "H":
            user_sum = calculate_hand_value(player["hand"])
            if user_sum > 21:
                return f"your sum: {user_sum}\n you are lost!!!"
            else:
                player["hand"].append(deck.pop())
                print(user_sum)
        if user_choice == "S":
            dealer_turn = dealer_play(deck, dealer)
            if dealer_turn == True:
                user_result = calculate_hand_value(player["hand"])
                dealer_result = calculate_hand_value(dealer["hand"])
                if user_result > dealer_result:
                    return f'the user is the winner the sum: {user_result}'
                if user_result < dealer_result:
                    return f'the dealer is the winner the sum: {dealer_result}'
                if user_result == dealer_result:
                    return f'equal\n user: {user_result}\n dealer: {dealer_result}'
            else:
                return dealer_turn
       
       
        
    
    
    
        