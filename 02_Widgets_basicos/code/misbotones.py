# File name: misbotones.py
import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.widget import Widget

class MiWidget(Widget):
    pass

class MisBotonesApp(App):
    def build(self):
        return MiWidget()

if __name__=="__main__":
    MisBotonesApp().run()
