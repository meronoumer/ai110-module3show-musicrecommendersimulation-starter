# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  


This recommender suggests songs from a small catalog based on a user’s preferred genre, mood, energy, valence, and acoustic preference. It is designed for classroom exploration and for understanding how a simple recommendation pipeline works. It is not designed for real users, large-scale deployment, or professional music discovery.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.


The model uses a content-based scoring approach. That means it looks at the attributes of each song instead of comparing one user to many other users.

For each song, the system checks whether the genre matches the user’s favorite genre and whether the mood matches the user’s favorite mood. It also measures how close the song’s energy is to the user’s target energy and how close the song’s valence is to the user’s target valence. After that, it adds a small bonus depending on whether the user prefers more acoustic or less acoustic songs.

Every song gets a final score. The system then sorts the songs from highest to lowest and returns the top matches along with short explanations.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The catalog contains 18 songs total. The starter file had 10 songs, and I added 8 more songs to make the dataset more diverse.

The dataset includes genres such as:
- pop
- lofi
- rock
- ambient
- jazz
- synthwave
- indie pop
- acoustic
- edm
- folk

The moods include:
- happy
- chill
- intense
- relaxed
- moody
- focused
- calm

The dataset is still very small and incomplete. It mostly reflects simplified “vibe” categories rather than real musical taste. It also does not include lyrics, language, context, artist popularity, or listening history.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  


This recommender works best when the user has a clear vibe and the catalog contains songs that closely match it. For example, the “High-Energy Pop” profile and the “Chill Lofi” profile both produced results that felt reasonable and easy to explain.

Another strength is transparency. Because the scoring is simple, I can clearly explain why a song was recommended. That makes the system easier to debug and easier to trust in a classroom setting.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  


This system has several weaknesses. First, it only uses a few features, so it reduces music taste to a small set of labels and numbers. That means it misses many important things, like lyrics, nostalgia, culture, language, and artist identity.

Second, the model can over-prioritize whichever features are weighted most heavily. In my case, genre and mood are strong signals, but energy and valence can still push songs from the “wrong” genre into the top results if they are numerically close enough.

Third, the dataset itself is biased because some styles have more representation than others. If a genre or mood appears more often, users who like that style may get better recommendations than users whose taste is underrepresented. In a real product, this could unfairly narrow what users see and reinforce filter bubbles.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.


I evaluated the recommender using three user profiles:

1. **High-Energy Pop**
2. **Chill Lofi**
3. **Deep Intense Rock**

For each one, I looked at the top 5 recommendations and checked whether they matched my intuition. I also compared how the outputs changed when the profile changed. The strongest results came from profiles with clear matches in the dataset, like Chill Lofi.

One thing that surprised me was that after the top result, some intense profiles started recommending songs from other genres just because their energy and valence were close. That showed me how small changes in feature weights can change the system’s behavior a lot, even when the code is simple.

I also ran the starter tests, and the recommendation logic passed them.

---

## 8. Future Work

If I continued this project, I would improve it in several ways:

- Add more songs and a much more diverse catalog
- Use more features, such as lyric themes, language, or artist similarity
- Add a diversity rule so the top results are not all extremely similar
- Let users have multiple favorite genres or moods instead of only one
- Improve the explanations so they sound more natural and helpful


---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  


This project taught me that recommendation systems do not need to be very complicated to feel convincing. Even a simple weighted score can produce outputs that look personalized. That made me realize how much power comes from choosing features and weights carefully.

What surprised me most was how quickly bias can appear. A small dataset and a few design decisions were enough to make the system better for some listeners than others. Building this changed how I think about real music apps, because now I see that what feels like “taste” is often a mix of data representation, ranking rules, and product choices. Human judgment still matters a lot when deciding what should count as a good recommendation and when deciding whether a system is being fair.