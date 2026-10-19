def moderate_chat(nickname, msg):
    clean_chat = msg.lower()
    if clean_chat == "skam":
        return f"ALERT: User {nickname} is banned for scamming!"
    else:
        return f"CHAT: {nickname} says: {msg}"

while True:
    name = input("nickname: ")
    name1 = input("msg: ")
    if name.lower() == "stop" or name1.lower() == "stop":
        break
    else:
        report = moderate_chat(name, name1)
        print(report)
