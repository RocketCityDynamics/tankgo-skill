from mycroft import MycroftSkill, intent_file_handler


class Tankgo(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('tankgo.intent')
    def handle_tankgo(self, message):
        self.speak_dialog('tankgo')


def create_skill():
    return Tankgo()

