from mycroft import MycroftSkill, intent_file_handler
import os

class cloner(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('cloner.intent')
    def handle_ii_want_die_school_for_clock(self, message):
        self.speak_dialog('cloner')
        os.system("for repository in $(cat /home/pi/repositories.txt); do rm -rf /home/pi/mycroft-core/skills/$repository; git clone $repository /home/pi/mycroft-core/skills/$repository; done")


def create_skill():
    return cloner()

