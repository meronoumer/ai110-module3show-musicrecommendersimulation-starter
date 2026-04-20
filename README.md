# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

This project simulates a simple content-based music recommender. Instead of using millions of users like Spotify or YouTube, my version compares a single user's taste profile to song attributes in a small catalog and gives each song a weighted score. It prioritizes genre, mood, energy similarity, valence similarity, and whether the user prefers more acoustic or less acoustic songs. The final recommendations are the top-scoring songs along with short explanations for why they matched.

---

## How The System Works

Explain your design in plain language.


Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.
Real recommendation systems often combine many signals, including what users skip, like, replay, save, and add to playlists. They may also use collaborative filtering, which looks at patterns across many users, and content-based filtering, which looks at the attributes of each item itself. My version is a much simpler content-based system. It does not compare users to other users. Instead, it compares one user's preferences directly to each song in the CSV file.

Each song in my system uses these features:

- genre
- mood
- energy
- valence
- acousticness
- tempo_bpm, danceability, and artist are stored too, even though the main scoring focuses most on the first five

My `UserProfile` or user preference dictionary stores:

- preferred genre
- preferred mood
- target energy
- target valence
- whether the user likes more acoustic songs

For each song, the recommender computes a weighted score:

- `+2.5` points if the genre matches
- `+1.5` points if the mood matches
- up to `+1.5` points based on how close the song's energy is to the user's target energy
- up to `+1.0` points based on how close the song's valence is to the user's target valence
- extra points based on acousticness depending on whether the user likes acoustic music or not

Then the system sorts all songs from highest score to lowest score and returns the top 5.


Workflow:
User Preferences → Compare to Every Song → Score Each Song → Sort by Score → Return Top Recommendations

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users


I tested the recommender with three very different profiles:

1. High-Energy Pop
genre: pop
mood: happy
energy: 0.85
valence: 0.85
likes_acoustic: False

This profile produced very intuitive results. Songs like Golden Hour Run and Sunrise City ranked at the top because they matched both genre and mood and had very close energy and valence values.

2. Chill Lofi
genre: lofi
mood: chill
energy: 0.35
valence: 0.60
likes_acoustic: True

This profile strongly favored Library Rain and Midnight Coding, which made sense because both are lofi, chill, lower-energy, and fairly acoustic. This was one of the best-performing profiles because the dataset has several songs that fit this vibe closely.

3. Deep Intense Rock
genre: rock
mood: intense
energy: 0.92
valence: 0.50
likes_acoustic: False

This profile correctly ranked Storm Runner first. But after that, the recommender often suggested energetic intense songs from other genres like pop or EDM. That showed me the system can drift away from genre once other numeric features line up well.




---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.


his recommender has several limitations:

It only works on a tiny catalog of songs
It does not understand lyrics, language, artist style, or cultural context
It may over-favor songs from genres that appear more often in the dataset
It assumes that music taste can be summarized by a few simple numeric and category features
It can create a small “filter bubble” by always rewarding songs that are very close to the user's existing taste

In a real product, this could make recommendations repetitive or narrow.


---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

