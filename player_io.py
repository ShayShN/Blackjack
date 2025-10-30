def ask_player_action() -> str:
    while True:
        user_ask = input("enter a H/S")
        if user_ask.upper() != "H" or user_ask.upper() != "S":
            continue
        return user_ask.upper()
    

    