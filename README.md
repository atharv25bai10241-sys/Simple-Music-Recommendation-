# MOODIFY: Mood-Based Music Recommender

## Project Overview

MOODIFY is an interactive web-based music recommendation system designed to suggest songs based on a user’s mood, energy level, and activity. Inspired by modern music streaming platforms, the system dynamically adapts recommendations using user input, listening behavior, and simulated trending data.

The platform provides a personalized music discovery experience through a simple and intuitive interface, combining recommendation logic with real-time interaction and dynamic content updates.

---

## Problem Statement

With millions of songs available on music platforms, users often struggle to find music that matches their current mood or situation. Traditional recommendation systems mainly rely on past listening history and lack:

- Real-time mood-based recommendations  
- Context-aware suggestions (activity, energy level)  
- Dynamic adaptation to changing trends  
- Personalized feedback-based learning  
- Lightweight and accessible recommendation systems for learning purposes  

MOODIFY addresses these limitations by providing a system that combines mood-based filtering, user interaction, and simulated trends to generate meaningful and engaging music recommendations.

---

## Target Users

- Students exploring recommendation systems  
- Music listeners seeking mood-based playlists  
- Beginners learning AI/ML concepts  
- Developers interested in building intelligent systems  
- Educational institutions demonstrating applied AI concepts  

---

## Features

### Core Features

1. **Mood-Based Recommendation Engine**
   - Accepts user mood (happy, sad, calm, stressed, etc.)
   - Maps moods to relevant music genres
   - Generates context-aware song suggestions  

2. **Energy & Activity Filtering**
   - Adjusts recommendations based on energy level  
   - Supports activities like study, workout, relaxation  
   - Improves personalization accuracy  

3. **Dynamic Scoring System**
   - Songs ranked using multiple parameters:
     - Trend score (popularity)
     - Mood compatibility
     - User listening frequency
     - Energy alignment  

4. **User Preference Learning**
   - Tracks songs selected by the user  
   - Prioritizes frequently listened artists  
   - Adapts recommendations over time  

5. **Trend Simulation**
   - Randomly updates song popularity  
   - Adds new songs dynamically  
   - Mimics real-world platforms like Spotify  

6. **Web-Based Interface**
   - Built using Flask  
   - Interactive HTML frontend  
   - Runs locally in browser  

7. **Scalable Design**
   - Easily extendable dataset  
   - Modular recommendation logic  
   - Supports future ML integration  

---

## Technologies & Tools Used

- **Programming Language**: Python 3.x  
- **Framework**: Flask  
- **Libraries**:
  - `pandas` – Data handling  
  - `numpy` – Numerical operations  
  - `random` – Trend simulation  
- **Frontend**: HTML, CSS  
- **Platform**: Web-based (Localhost)  

---

## Installation & Setup

### Requirements

- Python 3.8 or higher  
- pip  

### Installation Steps

1. **Download or Clone the Project**
   ```bash
   git clone <repository-url>
   cd music-recommender
   ```

2. **Install Dependencies**
   ```bash
   pip install flask pandas numpy
   ```

3. **Project Files**
   Ensure the following files are present:
   - app.py  
   - recommender.py  
   - songs.csv  
   - templates/index.html  

---

### Running the Project

```bash
python app.py
```

Then open your browser and go to:
```
http://127.0.0.1:5000/
```

---

## Instructions for Testing

### Manual Testing Procedure

1. Run the application  
2. Open browser at localhost  
3. Select:
   - Mood  
   - Energy level  
   - Activity  

4. Click **Get Recommendations**  
5. Observe recommended songs  
6. Select songs you like (if implemented)  
7. Run multiple times to observe:
   - Changing trends  
   - Updated recommendations  

---

### Test Cases

**Test Case 1: Mood Matching**  
- Input: Happy  
- Expected: Upbeat/Pop/EDM songs  

**Test Case 2: Energy Filtering**  
- Input: Low energy  
- Expected: Calm/Lo-fi songs  

**Test Case 3: Trend Update**  
- Run system multiple times  
- Expected: Changing recommendations  

**Test Case 4: Personalization**  
- Select same artist multiple times  
- Expected: More songs from that artist  

---

## Screenshots / Sample Output

### Input Selection
```
Mood: Happy
Energy: High
Activity: Workout
```

### Output Recommendations
```
Top Recommendations:
1. Energy Rush - Artist A (EDM)
2. Power Beats - Artist B (Hip-Hop)
3. Feel Good Vibes - Artist C (Pop)
```

---

## Recommendation Logic

### Scoring Formula

| Factor | Description |
|--------|------------|
| Trend Score | Popularity of song |
| Mood Match | Compatibility with user mood |
| User Preference | Based on listening frequency |
| Energy Match | Matches energy level |

### Final Score

```
final_score = trend_score + mood_weight + user_preference + energy_score
```

---

## Code Architecture

### File Structure

```
music-recommender/
├── app.py
├── recommender.py
├── songs.csv
├── templates/
│   └── index.html
└── README.md
```

### Key Components

- **app.py**: Handles Flask server and routing  
- **recommender.py**: Core recommendation logic  
- **songs.csv**: Dataset  
- **index.html**: User interface  

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

## References & Resources

1. Python Documentation: https://docs.python.org/3/  
2. Flask Documentation: https://flask.palletsprojects.com/  
3. Pandas Documentation: https://pandas.pydata.org/  
4. Recommendation Systems Concepts (online resources)  

---

## Author & Contact

**Project**: BRAINSTORM - MAT Skill Test 
**Version**: 1.0 
**Created**: 27/03/2026 
For questions, suggestions, or contributions, please contact the developer(Atharv Kala) or submit issues through the GitHub repository. 
---

## License

This project is for educational purposes as part of academic coursework in VITyarthi.
---

**Last Updated**: 27 March,2026  
**Status**: Active
