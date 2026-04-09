class WiFiDevice:
    def connect_wifi(self):
        print("Wifi Connected")
        
class VoiceAssistant:
    def activate_VoiceAsst(self):
        print("Voice Assistant Activated")
    def give_command(self,command):
        print(f"Executing Command:{command}")
        
class SmartSpeaker(WiFiDevice,VoiceAssistant):
    def Music(self):
        print("What is th weather condition in vizag today...")
        
sp=SmartSpeaker()
sp.connect_wifi()
sp.activate_VoiceAsst()
sp.give_command("What is th weather condition in vizag today")
sp.Music()
