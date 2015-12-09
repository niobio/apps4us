#coding:utf-8
from kivy.app import App
from kivy.uix.widget import Widget

class MiWidget (Widget):
    def suerte (self):
        palabra = "Pisa fuerte y mira adelante"
        import random
        lista = ["La vida son dos dias, disfrutala","El secreto de la vida es vivirla","Pisa fuerte y mira adelante", "No esperes el momento perfecto, cogelo y hazlo único", "este año traera muchas sorpresas"]
        x = random.randint(0,4)
        texto = lista[x]
                 
        if self.ids.label.text == "La vida son dos dias, disfrutala":
            self.ids.label.text = u"El secreto de la vida es vivirla"
        else:
            self.ids.label.text = texto


class SuerteApp (App):
    def build (self):
        return MiWidget()

if __name__== "__main__":
    SuerteApp().run()

