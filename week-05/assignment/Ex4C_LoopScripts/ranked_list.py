video_games = ["God Of War", "Gears of War", "Halo", "Spider-Man", "Hell Divers 2", "Mortal Kombat"]
top_game = "God Of War"

for i, games in enumerate(video_games, start=1):
    if video_games == top_game:
        print(f"{i}. {games} - This is my Top Game")
    else:
        print(f"{i}. {games}")
    