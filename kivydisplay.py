
import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label


def app_display():
    class MyApp(App):

        def build(self):
            return Label(text='Hello world')


