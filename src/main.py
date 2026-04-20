"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""
from recommender import load_songs, recommend_songs


def print_profile_results(name: str, prefs: dict, songs: list, k: int = 5) -> None:
    print(f"\n=== {name} ===")
    print(f"Preferences: {prefs}\n")

    recommendations = recommend_songs(prefs, songs, k=k)

    for i, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        print(f"{i}. {song['title']} by {song['artist']}")
        print(f"   Score: {score:.2f}")
        print(f"   Because: {explanation}")
        print()


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    profiles = {
        "High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.85,
            "valence": 0.85,
            "likes_acoustic": False,
        },
        "Chill Lofi": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.35,
            "valence": 0.60,
            "likes_acoustic": True,
        },
        "Deep Intense Rock": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.92,
            "valence": 0.50,
            "likes_acoustic": False,
        },
    }

    for name, prefs in profiles.items():
        print_profile_results(name, prefs, songs)


if __name__ == "__main__":
    main()