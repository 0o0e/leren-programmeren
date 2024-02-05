class payload_COMMANDS: 
    parts_of_speech = {
        "sent_makers": {
            "adjective1": False,
            "adjective2": False,
            "adjective3": False,
            "food": False,
            "foods": False,
            "thing": False,
            "things": False,
            "place1": False,
            "place2": False,
            "place3": False,
            "verb1": False,
            "verb2": False,
            "verb3": False,
            "adverb1": False,
            "adverb2": False,
            "adverb3": False,
            "insect": False,
            "animal1": False,
            "animal2": False,
            "animal3": False,
        },
        "characteristics": {
            "color": False,
            "name1": False,
            "name2": False,
            "name3": False,
            "cloth": False,
            "clothes": False,
        }
    }

    def __init__(self, story):
        self.story = story

    def check_payload(self, story):
        for key in self.parts_of_speech["sent_makers"].keys():
            if key in self.story:
                self.parts_of_speech["sent_makers"][key] = True

        for characteristic in self.parts_of_speech["characteristics"].keys():
            if characteristic in self.story:
                self.parts_of_speech["characteristics"][characteristic] = True

        for element in self.parts_of_speech["sent_makers"].keys():
            if element in self.story:
                self.parts_of_speech["sent_makers"][element] = True