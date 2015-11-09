# File: main.py
from kivy.app import App
from kivy.clock import Clock

from time import strftime

class ClockApp(App):
    cron_time = 0
    
    def update(self, intervalo):
        self.cron_time += intervalo
    
        self.root.ids.time.text = strftime('%H:%M:%S')
    
        minutes, seconds = divmod(self.cron_time, 60)
    
        self.root.ids.crono.text = (
            '%02d:%02d.%02d' %
            (int(minutes), int(seconds),
            int(seconds * 100 % 100)))

    
    def on_start(self):
        Clock.schedule_interval(self.update, 0.01)

    
if __name__ == '__main__':
    ClockApp().run()
