chess_statistics = {
    "Caro Kann": 13,
    "Kings Gambit": 22,
    "Dutch Defence": 5
}
def show_stats(dictionary):
    total_games = sum(chess_statistics.values())
    print(f"the number of games you ever played: {total_games}")
    print("here you can see details:")
    for key, value in dictionary.items():
        print(f"{key}: {value}")
show_stats(chess_statistics)