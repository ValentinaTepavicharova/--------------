def read_scoreboard():
    try:
        with open("scoreboard.txt", "r") as sd:
            lines = sd.readlines()
            scoreboard = {}
            for line in lines:
                name, user_wins, comp_wins = line.strip().split(",")
                scoreboard[name] = (int(user_wins), int(comp_wins))
            return scoreboard
    except FileNotFoundError:
        return {}


def write_scoreboard(scoreboard):
    with open("scoreboard.txt", "w") as wsd:
        for name, (user_wins, comp_wins) in scoreboard.items():
            wsd.write(f"{name},{user_wins},{comp_wins}\n")