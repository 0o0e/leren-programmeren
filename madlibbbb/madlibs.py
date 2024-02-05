from payload import payload_COMMANDS
from check import Check_New_Story
import random
import json
import os
def Main():
    class Stories:
        def get_stories(self):
            if os.path.isfile("stories.json"):
                with open("stories.json", "r") as json_file:
                    stories = json.load(json_file)
                    return stories

        def pick_stories(self, stories):
            picked_story = random.choice(stories)
            return picked_story

    class CreateStory:
        def __init__(self, new_story):
            self.new_story = new_story
            
        def create(self, action):
            if action in ["create story", "make story", "add story", "create_story"]:
                new_story = input("Enter new story: ").strip()
                Check_New_Story(new_story).check_story
                if Check_New_Story(self):
                    with open("stories.json", "r") as json_file:
                        existing_stories = json.load(json_file)
                        existing_stories.append(new_story)
                
                with open("stories.json", "w") as json_file:
                        json.dump(existing_stories, json_file)


    def replace_placeholders(story, user_inputs):
        formatted_story = story
        for key, value in user_inputs.items():
            formatted_story = formatted_story.replace("{" + key + "}", value)
        return formatted_story

    def Main():
        while True:
            action = input("What would you like to do? ")
            if action in ["create story", "crt", "new story", "add story"]:
                create_story = CreateStory(action)
                create_story.create(action)
                
            if action in ["play", "pl", "start", "game"]:
                stories = Stories().get_stories()
                picked_story = Stories().pick_stories(stories)
                print("Please do the following:\n")
                payload_COMMANDS.check_payload(picked_story)
                parts_of_speech = payload_COMMANDS.parts_of_speech
                
                user_inputs = {}
                for key, value in parts_of_speech.items():
                    if value:
                        user_input = input(f"Please write {key}: ")
                        user_inputs[key] = user_input
                
                formatted_story = replace_placeholders(picked_story, user_inputs)
                print("\nHere's your story:\n")
                print(formatted_story)

Main()