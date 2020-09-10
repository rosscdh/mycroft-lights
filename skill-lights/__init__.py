# Copyright 2017, Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from os.path import dirname, join

import requests

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler


class LightsSkill(MycroftSkill):
    def __init__(self):
        super(LightsSkill, self).__init__(name="LightsSkill")

    def send(self, on_off, gpio: int = 25):
        server = self.settings.get('server')
        resp = requests.post(server, json={'event_type': on_off, 'gpio': gpio})
        return resp.ok

    @intent_handler(IntentBuilder("LightsOnIntent").require("LightsOn"))
    def handle_on(self, message):
        self.speak_dialog("turn.lights.on")
        self.send(on_off='on', gpio=self.settings.get('gpio'))

    @intent_handler(IntentBuilder("LightsOffIntent").require("LightsOff"))
    def handle_off(self, message):
        self.speak_dialog("turn.lights.off")
        self.send(on_off='off', gpio=self.settings.get('gpio'))

    def stop(self):
        pass


def create_skill():
    return LightsSkill()
