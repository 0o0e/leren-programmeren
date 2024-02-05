from payload import payload_COMMANDS

class Check_New_Story(payload_COMMANDS):
	def __init__(self, story):
		self.story = story
		
	def check_story(self, story):
		parts_of_speech = payload_COMMANDS.parts_of_speech
		if any(part in self.story for part in parts_of_speech):
			print(f"This can be used as a valid story format!")
			return True
			
		else:
			print("Please use atleast one variable separated by + on both sides. Here's the list of variables available:", "\n".join(key for key in parts_of_speech.keys()))