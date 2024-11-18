def determine_mood(audio_features):
    """
    Determine the mood of the song based on the audio features.
    """
    # Define the 13 moods and their corresponding values
    moods = {
        "amusing": 0,
        "annoying": 0,
        "beautiful": 0,
        "calm": 0,
        "dreamy": 0,
        "energizing": 0,
        "desirous": 0,
        "indignant": 0,
        "joyful": 0,
        "sad": 0,
        "scary": 0,
        "tense": 0,
        "triumphant": 0,
    }

    # Iterate through the audio features and tally the moods based on each feature's value
    for feature, value in audio_features.items():
        if feature == "danceability":
            tally_danceability(value, moods)
        if feature == "energy":
            tally_energy(value, moods)
        if feature == "key":
            tally_key(value, moods)
        if feature == "mode":
            tally_mode(value, moods)
        if feature == "loudness":
            tally_loudness(value, moods)
        if feature == "valence":
            tally_valence(value, moods)
        if feature == "tempo":
            tally_tempo(value, moods)

    # Return the mood with the highest tally
    print(moods)
    return max(moods, key=moods.get)


def tally_danceability(value, moods):
    if value > 0.7:
        moods["amusing"] += 1
        moods["energizing"] += 1
    if value >= 0.6:
        moods["joyful"] += 1
        moods["amusing"] += 1
    if value >= 0.4 and value < 0.6:
        moods["calm"] += 1
    if value >= 0.2:
        moods["tense"] += 1
    else:
        moods["sad"] += 1


def tally_energy(value, moods):
    if value > 0.8:
        moods["energizing"] += 1
        moods["triumphant"] += 1
    if value > 0.6:
        moods["joyful"] += 1
        moods["amusing"] += 1
    if value > 0.4:
        moods["beautiful"] += 1
        moods["dreamy"] += 1
    if value > 0.2:
        moods["tense"] += 1
    else:
        moods["sad"] += 1


def tally_key(value, moods):
    major_keys = {
        0: ["joyful"],  # C Major
        2: ["triumphant"],  # D Major
        4: ["energizing"],  # E Major
        5: ["joyful"],  # F Major
        7: ["joyful", "amusing"],  # G Major
        9: ["beautiful"],  # A Major
        11: ["triumphant", "indignant"],  # B Major
    }
    minor_keys = {
        1: ["tense", "dreamy"],  # C Minor
        3: ["tense", "scary", "indignant", "annoying"],  # D Minor
        6: ["sad"],  # F Minor
        8: ["scary", "tense"],  # G Minor
        10: ["sad"],  # A Minor
    }

    # Major keys
    if value in major_keys:
        for mood in major_keys[value]:
            moods[mood] += 1
    # Minor keys
    elif value in minor_keys:
        for mood in minor_keys[value]:
            moods[mood] += 1
    # For unrecognized keys, fallback to general behavior
    else:
        if value in [0, 2, 4, 5, 7, 9, 11]:  # Major keys
            moods["joyful"] += 1
            moods["triumphant"] += 1
        else:  # Minor keys
            moods["sad"] += 1
            moods["scary"] += 1


def tally_loudness(value, moods):
    if value > -5:
        moods["energizing"] += 1
        moods["triumphant"] += 1
    if value > -10:
        moods["joyful"] += 1
    if value > -15:
        moods["calm"] += 1
        moods["dreamy"] += 1
    else:
        moods["sad"] += 1
        moods["scary"] += 1


def tally_mode(value, moods):
    if value == 1:  # Major mode
        moods["joyful"] += 1
        moods["triumphant"] += 1
    else:  # Minor mode
        moods["sad"] += 1
        moods["scary"] += 1


def tally_valence(value, moods):
    """
    From the Spotify API documentation:
    A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).
    """
    if value > 0.8:
        moods["joyful"] += 1
        moods["triumphant"] += 1
        moods["beautiful"] += 1
        moods["energizing"] += 1
    if value >= 0.6:
        moods["amusing"] += 1
        moods["dreamy"] += 1
    if value >= 0.4 and value < 0.6:
        moods["desirous"] += 1
        moods["calm"] += 1
    if value >= 0.2 and value < 0.4:
        moods["indignant"] += 1
        moods["tense"] += 1
    elif value < 0.2:
        moods["sad"] += 1
        moods["scary"] += 1


def tally_tempo(value, moods):
    if value >= 120:
        moods["energizing"] += 1
        moods["triumphant"] += 1
        moods["joyful"] += 1
    if value >= 100 and value < 120:
        moods["indignant"] += 1
    if value >= 100:
        moods["amusing"] += 1
        moods["beautiful"] += 1
    if value >= 80 and value < 100:
        moods["calm"] += 1
        moods["dreamy"] += 1
    if value < 80:
        moods["sad"] += 1
        moods["scary"] += 1
