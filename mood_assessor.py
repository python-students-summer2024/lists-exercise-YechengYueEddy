import os
import datetime

def get_mood_input():
    acceptable_moods = ["happy", "relaxed", "apathetic", "sad", "angry"]
    int_moods = [2, 1, 0, -1, -2]
    valid = False
    while not valid:
        user_mood = input("Please enter your mood (happy, relaxed, apathetic, sad, angry): ").strip().lower()
        if user_mood in acceptable_moods:
            valid = True
    return int_moods[acceptable_moods.index(user_mood)]

def mood_already_entered_today():
    date_today = str(datetime.date.today())
    if not os.path.exists('data'):
        os.makedirs('data')
    if os.path.exists('data/mood_diary.txt'):
        with open('data/mood_diary.txt', 'r') as file:
            for line in file:
                if line.startswith(date_today):
                    return True
    return False

def save_mood_in_entry(mood):
    date_today = str(datetime.date.today())
    with open('data/mood_diary.txt', 'a') as file:
        file.write(f"{date_today},{mood}\n")

def diagnose_mood():
    moods = []
    with open('data/mood_diary.txt', 'r') as file:
        for line in file:
            cur_line = line.split(',')
            moods.append(int(cur_line[1]))
    if len(moods) < 7:
        return False
    last_weeks_moods = moods[-7:]
    if last_weeks_moods.count(2) >= 5:
        return "manic"
    elif last_weeks_moods.count(-1) >= 4:
        return "depressive"
    elif last_weeks_moods.count(0) >= 6:
        return "schizoid"
    else:
        average_mood = round(sum(last_weeks_moods) / 7)
        acceptable_moods = ["happy", "relaxed", "apathetic", "sad", "angry"]
        int_moods = [2, 1, 0, -1, -2]
        return acceptable_moods[int_moods.index(average_mood)]

def assess_mood():
    if mood_already_entered_today():
        print("Sorry, you have already entered your mood today.")
        return
    
    mood = get_mood_input()
    save_mood_in_entry(mood)
    
    diagnosis = diagnose_mood()
    if diagnosis:
        print(f"Your diagnosis: {diagnosis}!")