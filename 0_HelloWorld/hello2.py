from kivy.app import App
from kivy.uix.label import Label

class Hello2App(App):
    def build(self):
        return Label()

if __name__ == '__main__':
    Hello2App().run()
