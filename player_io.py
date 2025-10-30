def ask_player_action() -> str:
    while True:
        user_ask = input("enter a H/S: ").upper()
        if user_ask== "H":
            return user_ask.upper()
        elif user_ask == "S":
            return user_ask
        continue
    


