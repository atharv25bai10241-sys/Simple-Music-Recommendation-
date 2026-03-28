import json
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import pickle
import os

# ── Music Database ──
MUSIC_DB = {
    "lo_fi_study":        {"title": "Lo-Fi Study Beats",          "genre": "Lo-Fi",                "desc": "Mellow beats for deep focus.",                    "yt": "lofi hip hop study beats"},
    "lo_fi_chill":        {"title": "Lo-Fi Chill Vibes",          "genre": "Lo-Fi",                "desc": "Soft jazzy lo-fi to unwind.",                     "yt": "lofi chill vibes playlist"},
    "bollywood_happy":    {"title": "Bollywood Party Hits",       "genre": "Bollywood",            "desc": "High-energy Bollywood bangers.",                   "yt": "bollywood party songs 2024"},
    "bollywood_sad":      {"title": "Bollywood Heartbreak",       "genre": "Bollywood",            "desc": "Emotional melodies for hard feelings.",            "yt": "bollywood sad songs playlist"},
    "bollywood_romantic": {"title": "Bollywood Romance",          "genre": "Bollywood",            "desc": "Dreamy love songs for tender moments.",            "yt": "bollywood romantic songs playlist"},
    "bollywood_motivate": {"title": "Bollywood Pump Up",          "genre": "Bollywood",            "desc": "Motivational tracks to push through anything.",    "yt": "bollywood motivational songs"},
    "english_happy":      {"title": "Feel-Good Pop",              "genre": "English / Pop",        "desc": "Upbeat pop anthems to lift your spirits.",         "yt": "feel good pop songs playlist 2024"},
    "english_sad":        {"title": "Sad Indie / Acoustic",       "genre": "English / Indie",      "desc": "Raw acoustic songs to sit with your emotions.",    "yt": "sad indie acoustic songs playlist"},
    "english_hype":       {"title": "Hype Anthems",               "genre": "English / Pop-Rock",   "desc": "Loud energetic tracks for high-octane energy.",    "yt": "hype songs pump up playlist"},
    "english_night":      {"title": "Late Night Vibes",           "genre": "English / Alternative","desc": "Atmospheric tracks for late nights.",              "yt": "late night vibes playlist"},
    "hiphop_hype":        {"title": "Hip-Hop Bangers",            "genre": "Hip-Hop / Rap",        "desc": "Hard-hitting rap for maximum confidence.",         "yt": "hip hop bangers playlist 2024"},
    "hiphop_chill":       {"title": "Chill Rap / R&B",            "genre": "Hip-Hop / R&B",        "desc": "Smooth laid-back rap and R&B.",                    "yt": "chill rap rnb playlist"},
    "hiphop_motivate":    {"title": "Workout Rap",                "genre": "Hip-Hop / Rap",        "desc": "High-BPM rap to push your limits.",               "yt": "workout rap hip hop playlist"},
    "classical_focus":    {"title": "Classical Focus",            "genre": "Classical",            "desc": "Bach, Mozart for deep concentration.",             "yt": "classical music for focus and concentration"},
    "classical_calm":     {"title": "Ambient Classical",          "genre": "Classical / Ambient",  "desc": "Soft piano and strings for relaxation.",           "yt": "relaxing classical piano music"},
    "instrumental_work":  {"title": "Cinematic Instrumental",     "genre": "Instrumental",         "desc": "Epic orchestral scores for feeling unstoppable.",  "yt": "cinematic instrumental music focus"},
    "edm_party":          {"title": "EDM / Dance",                "genre": "EDM",                  "desc": "Pulsing electronic beats for max energy.",         "yt": "edm dance party playlist 2024"},
    "jazz_morning":       {"title": "Morning Jazz",               "genre": "Jazz",                 "desc": "Warm breezy jazz to ease into the day.",           "yt": "morning jazz playlist cafe"},
    "acoustic_morning":   {"title": "Acoustic Morning",           "genre": "Acoustic / Folk",      "desc": "Light guitars for a fresh start.",                 "yt": "acoustic morning playlist folk"},
    "sleep_ambient":      {"title": "Sleep Sounds / Ambient",     "genre": "Ambient",              "desc": "Soft textures to ease you to sleep.",              "yt": "sleep music ambient sounds relaxing"},
    "workout_edm":        {"title": "Workout EDM / Rock",         "genre": "EDM / Rock",           "desc": "Driving beats for destroying your workout.",       "yt": "workout music edm rock playlist"},
    "nostalgic_hindi":    {"title": "90s Hindi Classics",         "genre": "Bollywood / Retro",    "desc": "Golden era Bollywood straight from the past.",     "yt": "90s hindi songs golden era"},
    "nostalgic_english":  {"title": "2000s Throwbacks",           "genre": "English / Retro",      "desc": "Pop and rock hits dripping with nostalgia.",       "yt": "2000s throwback songs playlist"},
}

# ── Rule function: assigns the correct label for ANY combination of inputs ──
def get_label(mood, energy, time, activity):
    if activity == "sleeping":
        return "sleep_ambient"

    if activity == "workout":
        if mood in ["angry", "hyped"] or energy >= 8:
            return "workout_edm"
        elif mood == "motivated":
            return "hiphop_motivate"
        else:
            return "bollywood_motivate"

    if activity == "partying":
        return "edm_party" if energy >= 7 else "bollywood_happy"

    if activity == "studying":
        if mood in ["focused", "motivated"]:
            if energy >= 7:   return "instrumental_work"
            elif energy >= 4: return "lo_fi_study"
            else:             return "classical_focus"
        elif mood == "happy":  return "lo_fi_study"
        elif mood in ["sad", "lonely"]: return "lo_fi_chill"
        else: return "classical_focus"

    if activity == "commuting":
        if energy >= 7:             return "hiphop_hype"
        elif mood == "motivated":   return "bollywood_motivate"
        elif mood == "nostalgic":   return "nostalgic_hindi"
        elif time == "morning":     return "acoustic_morning"
        else:                       return "hiphop_chill"

    if activity == "cooking":
        if mood == "romantic":      return "bollywood_romantic"
        elif mood == "happy":       return "bollywood_happy"
        elif energy >= 6:           return "english_happy"
        else:                       return "jazz_morning"

    if activity == "relaxing":
        if mood == "happy":
            if time == "morning":   return "jazz_morning"
            elif energy >= 6:       return "english_happy"
            else:                   return "acoustic_morning"
        elif mood == "sad":
            return "english_sad" if energy <= 3 else "bollywood_sad"
        elif mood == "focused":     return "lo_fi_chill"
        elif mood == "romantic":    return "bollywood_romantic"
        elif mood == "angry":       return "hiphop_hype"
        elif mood == "nostalgic":
            return "nostalgic_hindi" if time in ["night", "evening"] else "nostalgic_english"
        elif mood == "hyped":       return "edm_party"
        elif mood == "chill":
            if time == "morning":   return "acoustic_morning"
            elif energy <= 3:       return "classical_calm"
            else:                   return "lo_fi_chill"
        elif mood == "lonely":      return "english_sad"
        elif mood == "motivated":   return "instrumental_work"

    if time == "morning":   return "acoustic_morning"
    elif time == "night":   return "english_night"
    return "lo_fi_chill"


# ── Generate ALL 2800 permutations automatically ──
def generate_training_data():
    moods      = ["happy","sad","focused","romantic","angry","nostalgic","hyped","chill","lonely","motivated"]
    energies   = list(range(1, 11))
    times      = ["morning","afternoon","evening","night"]
    activities = ["studying","workout","relaxing","commuting","cooking","partying","sleeping"]

    data = []
    for mood in moods:
        for energy in energies:
            for time in times:
                for activity in activities:
                    label = get_label(mood, energy, time, activity)
                    data.append((mood, energy, time, activity, label))

    print(f"Generated {len(data)} training samples covering all combinations.")
    return data


# ── Feature encoding ──
def encode_features(mood, energy, time, activity):
    mood_map     = {"happy":0,"sad":1,"focused":2,"romantic":3,"angry":4,"nostalgic":5,"hyped":6,"chill":7,"lonely":8,"motivated":9}
    time_map     = {"morning":0,"afternoon":1,"evening":2,"night":3}
    activity_map = {"studying":0,"workout":1,"relaxing":2,"commuting":3,"cooking":4,"partying":5,"sleeping":6}
    return [mood_map.get(mood,0), int(energy), time_map.get(time,0), activity_map.get(activity,2)]


# ── Train model ──
def train_model():
    data = generate_training_data()
    X, y = [], []
    for mood, energy, time, activity, label in data:
        X.append(encode_features(mood, energy, time, activity))
        y.append(label)

    model = DecisionTreeClassifier(max_depth=15, random_state=42)
    model.fit(X, y)

    with open("mood_model.pkl", "wb") as f:
        pickle.dump(model, f)

    print("Model trained and saved!")
    return model


# ── Recommend ──
def recommend(mood, energy, time_of_day, activity, top_n=4):
    model = train_model()
    features = encode_features(mood, energy, time_of_day, activity)

    proba   = model.predict_proba([features])[0]
    classes = model.classes_

    top_indices = np.argsort(proba)[::-1][:top_n]
    results = []
    for idx in top_indices:
        key = classes[idx]
        if key in MUSIC_DB:
            entry = MUSIC_DB[key].copy()
            entry["key"]          = key
            entry["confidence"]   = round(proba[idx] * 100, 1)
            entry["youtube_url"]  = f"https://www.youtube.com/results?search_query={entry['yt'].replace(' ', '+')}"
            results.append(entry)
    return results


# ── Main CLI ──
def main():
    print("=== Moodify — Mood-Based Music Recommender ===\n")

    moods      = ["happy","sad","focused","romantic","angry","nostalgic","hyped","chill","lonely","motivated"]
    times      = ["morning","afternoon","evening","night"]
    activities = ["studying","workout","relaxing","commuting","cooking","partying","sleeping"]

    print("Mood options:", ", ".join(moods))
    mood = input("Your mood: ").strip().lower()

    energy = int(input("Energy level (1-10): ").strip())

    print("Time options:", ", ".join(times))
    time_of_day = input("Time of day: ").strip().lower()

    print("Activity options:", ", ".join(activities))
    activity = input("Current activity: ").strip().lower()

    print("\n🎵 Recommending music...\n")
    results = recommend(mood, energy, time_of_day, activity)

    for i, r in enumerate(results, 1):
        print(f"{i}. {r['title']} [{r['genre']}]")
        print(f"   {r['desc']}")
        print(f"   ▶ {r['youtube_url']}\n")

    log_entry = {
        "mood": mood, "energy": energy,
        "time": time_of_day, "activity": activity,
        "recommendations": [r["title"] for r in results]
    }

    log = []
    if os.path.exists("recommendation_log.json"):
        with open("recommendation_log.json") as f:
            log = json.load(f)

    log.append(log_entry)
    with open("recommendation_log.json", "w") as f:
        json.dump(log, f, indent=2)

    print("Saved to recommendation_log.json")

if __name__ == "__main__":
    main()
