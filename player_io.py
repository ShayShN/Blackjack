def ask_player_action() -> str:
    while True:
        user_ask = input("enter a H/S: ").strip().upper()
        if user_ask in ("H", "S"):
            return user_ask
        continue
    


