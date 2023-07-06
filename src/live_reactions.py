```python
from src.models.reaction import LiveReaction
from src.utils import get_user_input, get_user_media

def record_live_reactions(user, content):
    print("Viewing content...")
    print(content)

    print("Recording live reactions...")
    user_media = get_user_media(user)

    live_reaction = LiveReaction(user=user, content=content, reaction_media=user_media)
    live_reaction.save()

    print("Live reaction recorded and saved.")

def switch_viewing_recording(user, content):
    user_input = get_user_input("Switch to (1) Viewing content (2) Recording reaction: ")

    if user_input == "1":
        print("Switched to viewing content.")
        print(content)
    elif user_input == "2":
        print("Switched to recording reaction.")
        record_live_reactions(user, content)
    else:
        print("Invalid input. Please try again.")
        switch_viewing_recording(user, content)

def send_live_reaction(user, content):
    print("Sending live reaction...")
    live_reaction = LiveReaction.objects.get(user=user, content=content)
    live_reaction.send()

    print("Live reaction sent.")
```