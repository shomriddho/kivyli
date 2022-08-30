import kivy
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text="Hello world!",font_size=50) and Label(text="Hello world!",font_size=50)and Label(text="Hello world!",font_size=50)
        

if __name__ == "__main__":
    MyApp().run()        
print(__name__)