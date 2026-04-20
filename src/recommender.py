from __future__ import annotations

import csv
from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass
class Song:
    """Represents a song and its attributes."""

    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """Represents a user's taste preferences."""

    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """OOP implementation of the recommendation logic."""

    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        scored = []
        for song in self.songs:
            score = 0.0

            if song.genre == user.favorite_genre:
                score += 2.5

            if song.mood == user.favorite_mood:
                score += 1.5

            score += max(0.0, 1.5 - abs(song.energy - user.target_energy) * 3)

            if user.likes_acoustic:
                score += song.acousticness
            else:
                score += (1 - song.acousticness) * 0.5

            scored.append((score, song))

        scored.sort(key=lambda item: item[0], reverse=True)
        return [song for _, song in scored[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        reasons = []

        if song.genre == user.favorite_genre:
            reasons.append("genre match")
        if song.mood == user.favorite_mood:
            reasons.append("mood match")
        if abs(song.energy - user.target_energy) <= 0.15:
            reasons.append("energy is close to target")
        if user.likes_acoustic and song.acousticness >= 0.7:
            reasons.append("high acousticness fits this listener")
        elif not user.likes_acoustic and song.acousticness <= 0.3:
            reasons.append("lower acousticness fits this listener")

        if not reasons:
            return "This song is a weaker match, but it is still relatively close on at least one preference."

        return "Recommended because of " + ", ".join(reasons) + "."


def load_songs(csv_path: str) -> List[Dict]:
    """Loads songs from a CSV file and converts numeric columns."""

    songs: List[Dict] = []

    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            songs.append(
                {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                }
            )

    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Scores a single song against user preferences and returns reasons."""

    score = 0.0
    reasons: List[str] = []

    if song["genre"] == user_prefs["genre"]:
        score += 2.5
        reasons.append("genre match (+2.5)")

    if song["mood"] == user_prefs["mood"]:
        score += 1.5
        reasons.append("mood match (+1.5)")

    energy_gap = abs(song["energy"] - user_prefs["energy"])
    energy_points = max(0.0, 1.5 - energy_gap * 3)
    score += energy_points
    reasons.append(f"energy closeness (+{energy_points:.2f})")

    target_valence = user_prefs.get("valence")
    if target_valence is not None:
        valence_gap = abs(song["valence"] - target_valence)
        valence_points = max(0.0, 1.0 - valence_gap * 2)
        score += valence_points
        reasons.append(f"valence closeness (+{valence_points:.2f})")

    likes_acoustic = user_prefs.get("likes_acoustic")
    if likes_acoustic is True:
        acoustic_points = song["acousticness"]
        score += acoustic_points
        reasons.append(f"acoustic preference (+{acoustic_points:.2f})")
    elif likes_acoustic is False:
        acoustic_points = (1 - song["acousticness"]) * 0.5
        score += acoustic_points
        reasons.append(f"non-acoustic preference (+{acoustic_points:.2f})")

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Ranks songs by score and returns top-k recommendations."""

    scored_songs: List[Tuple[Dict, float, str]] = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons)
        scored_songs.append((song, score, explanation))

    ranked = sorted(scored_songs, key=lambda item: item[1], reverse=True)
    return ranked[:k]