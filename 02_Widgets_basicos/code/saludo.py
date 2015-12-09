# coding: utf-8
from kivy.app import App
from kivy.uix.widget import Widget

class MiWidget(Widget):
    def saludar(self):
        if self.ids.label.text == 'Hola':
            self.ids.label.text = u'Hasta luego'
        else:
            self.ids.label.text = 'Hola'
        
class SaludoApp(App):
    def build(self):
        return MiWidget()
        

if __name__=="__main__":
    SaludoApp().run()

