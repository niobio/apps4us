import kivy
kivy.require('1.8.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.widget import Widget


class MyW(Widget):
	def my_callback(self):
		self.ids.label1.text = 'Click ! '

class e1App(App):
	def build(self):
		return MyW()

if __name__ == '__main__':
	e1App().run()
