# File: main.py
from kivy.app import App
from kivy.clock import Clock
#from kivy.core.text import LabelBase
#from kivy.core.window import Window

from time import strftime

class ClockApp(App):
    cron_time = 0
    cron_started = False
    
    def update(self, intervalo):
        if self.cron_started == True:
            self.cron_time = self.cron_time + intervalo
    
        self.root.ids.time.text = strftime('%H:%M:%S')
    
        minutes, seconds = divmod(self.cron_time, 60)
    
        self.root.ids.crono.text = (
            '%02d:%02d.%02d' %
            (int(minutes), int(seconds),
            int(seconds * 100 % 100)))

    
    def on_start(self):
        Clock.schedule_interval(self.update, 0.01)

    def start_stop(self):
        self.root.ids.start_stop.text = ('Start' if self.cron_started else 'Stop')
        self.cron_started = not self.cron_started

    def reset(self):
        if self.cron_started:
            self.root.ids.start_stop.text = 'Start'
            self.cron_started = False
        self.cron_time = 0
    
if __name__ == '__main__':
    ClockApp().run()
