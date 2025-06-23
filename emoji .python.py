# Step 1: Dictionary mapping moods to emojis and messages
mood_dict = {
    "happy": ("😊", "That's wonderful! Keep smiling and enjoy your day!"),
    "sad": ("😢", "It's okay to feel sad sometimes. You're not alone 💙"),
    "angry": ("😠", "Take a deep breath. Things will get better."),
    "excited": ("🤩", "Awesome! Keep the energy going!"),
    "bored": ("😐", "Maybe try something new or creative today?"),
    "tired": ("😴", "Make sure to get some rest. You deserve it!"),
    "anxious": ("😰", "You're doing your best. Breathe and take it one step at a time.")
}

# Step 2: Ask user for their mood
user_mood = input("How are you feeling today? (e.g., Happy, Sad, Angry): ").lower()

# Step 3 & 4: Match mood and print response
if user_mood in mood_dict:
    emoji, message = mood_dict[user_mood]
    print(f"\n{emoji} {message}")
else:
    # Step 5: Default response
    print("\n🤔 Hmm... I didn't recognize that mood, but I hope you have a good day anyway!")
