from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window


class CanvasWidget(Widget):
    pass

class PaintApp(App):
    def build(self):
        return CanvasWidget()

if __name__ == '__main__':
    Window.clearcolor = (1,1,0,1)
    PaintApp().run()
