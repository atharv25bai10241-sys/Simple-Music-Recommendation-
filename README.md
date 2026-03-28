# 🎵 Moodify — Mood-Based Music Recommender

## Project Overview

Moodify is an AI-powered music recommendation system that suggests the perfect music based on how you're feeling right now. Instead of scrolling endlessly through playlists, simply tell Moodify your mood, energy level, time of day, and current activity — and it instantly recommends the best music categories with direct YouTube links.

The project has two components: a clean web-based interface for everyday use, and a Python ML backend using a Decision Tree classifier for the actual recommendation logic.

---

## Problem Statement

People often don't know what to listen to based on their current mood or situation. Existing music apps recommend based on listening history, not how you actually feel right now. Moodify bridges this gap by taking simple human inputs — mood, energy, time, activity — and mapping them to the most fitting music using machine learning.

---

## Target Users

- Students who need the right music for studying or working out
- Anyone who wants music that actually matches their current vibe
- People who spend too long choosing what to listen to
- Developers and researchers exploring mood-based recommendation systems

---

## Features

### Core Features

1. **Mood-Based Recommendation Engine**
   - 10 mood categories: Happy, Sad, Focused, Romantic, Angry, Nostalgic, Hyped, Chill, Lonely, Motivated
   - Decision Tree classifier trained on mood + energy + time + activity inputs
   - Returns top 4 recommendations ranked by confidence score

2. **Rich Music Database**
   - 23 curated music categories spanning all major genres
   - Covers Bollywood, English/Pop, Lo-Fi, Hip-Hop/Rap, Classical, Instrumental, EDM, Jazz, Acoustic, Ambient
   - Every recommendation links directly to a YouTube search — effectively infinite songs

3. **Smart Input System**
   - Energy level slider (1–10)
   - Time of day selector (Morning / Afternoon / Evening / Night)
   - Activity selector (Studying, Workout, Relaxing, Commuting, Cooking, Partying, Sleeping)
   - Mood chips for one-tap selection

4. **Web Interface**
   - Fully self-contained HTML file — no server needed, just open in a browser
   - Elegant dark-themed UI with smooth animations
   - One-click YouTube links for every recommendation
   - Works offline (except YouTube links)

5. **Python ML Backend**
   - Decision Tree classifier (scikit-learn)
   - Feature encoding for categorical inputs
   - Probability-based ranking of recommendations
   - Session logging to JSON for history tracking
   - Model persistence with pickle

---

## Technologies Used

| Component | Technology |
|---|---|
| ML Model | scikit-learn (Decision Tree Classifier) |
| Numerical Processing | NumPy |
| Model Persistence | Python pickle |
| Web Interface | HTML5 + CSS3 + Vanilla JavaScript |
| Data Storage | JSON |
| Music Links | YouTube Search URLs |

---

## Project Structure

```
moodify/
├── index.html          # Web app — open in browser for full UI
├── musicrecommender.py      # Python ML backend — CLI version
├── requirements.txt    # Python dependencies
├── mood_model.pkl      # Auto-generated trained model
└── recommendation_log.json  # Auto-generated session history
```

---

## Setup & Installation

### Requirements

- Python 3.6 or higher
- pip

### Installation Steps

**1. Clone the repository**
```bash
git clone https://github.com/atharv25bai10241-sys/moodify.git
cd moodify
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the web app**

Simply double-click `index.html` or open it in any browser. No server required.

**4. Run the Python CLI version**
```bash
python musicrecommender.py
```
Or on Windows with multiple Python versions:
```bash
py -3.13 musicrecommender.py
```

---

## How to Use

### Web App (Recommended for Demo)
1. Open `index.html` in your browser
2. Select your current mood using the mood chips
3. Set your energy level using the slider
4. Choose your time of day and current activity
5. Click **Find My Music**
6. Click any recommendation card to open YouTube

### Python CLI(Sample output)
```
=== Moodify — Mood-Based Music Recommender ===

Mood options: happy, sad, focused, romantic, angry, nostalgic, hyped, chill, lonely, motivated
Your mood: happy
Energy level (1-10): 7
Time options: morning, afternoon, evening, night
Time of day: evening
Activity options: studying, workout, relaxing, commuting, cooking, partying, sleeping
Current activity: relaxing

🎵 Recommending music...

1. Feel-Good Pop [English / Pop]
   Upbeat pop anthems guaranteed to lift your spirits instantly.
   ▶ https://youtube.com/results?search_query=feel+good+pop+songs+playlist+2024

2. Bollywood Party Hits [Bollywood]
   ...


## How It Works


User inputs (mood, energy, time, activity)
        ↓
Feature encoding (text → numbers)
        ↓
Decision Tree Classifier
        ↓
Probability scores for all 23 music categories
        ↓
Top 4 recommendations ranked by confidence
        ↓
YouTube search links generated
```

### ML Concepts Used

- **Decision Tree Classification** — learns rules from training data to map mood inputs to music categories
- **Feature Encoding** — converts categorical inputs (mood, time, activity) into numerical features
- **Probability-Based Ranking** — uses `predict_proba()` to rank all possible recommendations by confidence
- **Model Persistence** — trained model saved with `pickle` so it doesn't retrain every run
- **Rule-Based Scoring** — web version uses a weighted scoring system to complement the ML model
```
---

## Music Categories
```
| Genre | Examples |
|---|---|
| Lo-Fi | Study Beats, Chill Vibes |
| Bollywood | Party Hits, Heartbreak, Romance, Motivation |
| English | Feel-Good Pop, Sad Indie, Hype Anthems, Late Night |
| Hip-Hop / Rap | Bangers, Chill R&B, Workout Rap |
| Classical | Focus, Ambient/Calm |
| Instrumental | Cinematic / Epic |
| EDM | Party, Workout |
| Jazz | Morning Jazz |
| Acoustic | Morning Folk |
| Ambient | Sleep Sounds |
| Retro | 90s Hindi, 2000s English |

---
```
```
## Sample Output

### Web App
Select: **Mood → Focused | Energy → 6 | Time → Afternoon | Activity → Studying**

Recommendations:
- 🎵 Lo-Fi Study Beats → YouTube
- 🎵 Classical Focus → YouTube
- 🎵 Cinematic Instrumental → YouTube
- 🎵 Chill Rap / R&B → YouTube
---

## Challenges Faced & Solutions

### Challenge 1: Personalization Logic  
**Problem**: Adapting recommendations based on user behavior  
**Solution**: Implemented frequency-based weighting system  

### Challenge 2: Simulating Trends  
**Problem**: No real-time API data  
**Solution**: Random trend score updates  

### Challenge 3: Multi-Factor Scoring  
**Problem**: Combining multiple parameters  
**Solution**: Weighted scoring formula  

---

## Learnings & Key Takeaways

1. Understanding recommendation systems  
2. Applying scoring algorithms  
3. Building web apps with Flask  
4. Data handling using pandas  
5. Importance of personalization in AI systems  

---

## Future Enhancements

1. Spotify API integration  
2. Real-time song database  
3. Machine learning models (collaborative filtering)  
4. User login & profiles  
5. Like/Dislike feedback system  
6. Advanced UI (React or modern frontend)  
7. Playlist generation  
8. Mobile app version  

---

Here are the references you can add to your README:

References & Resources

scikit-learn Documentation — Decision Tree Classifier:-
https://scikit-learn.org/stable/modules/tree.html
scikit-learn — predict_proba() method:-
https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
Python Documentation — pickle module:-
https://docs.python.org/3/library/pickle.html
Python Documentation — json module:-
https://docs.python.org/3/library/json.html
NumPy Documentation:-
https://numpy.org/doc/stable/
GeeksforGeeks — Decision Tree in Python:-
https://www.geeksforgeeks.org/decision-tree-implementation-python/
---

## Author & Contact

**Project**: Moodify — Mood-Based Music Recommender
**Version**: 1.0 
**Created**: 27/03/2026 
For questions, suggestions, or contributions, please contact the developer(Atharv Kala) or submit issues through the GitHub repository. 
---

## License

This project is for educational purposes as part of academic coursework in VITyarthi.
---

**Last Updated**: 28 March,2026  
**Status**: Active
