import kivy
kivy.require('2.0.0rc3s')

from kivy.app import App
from .view import MainWindow

class Poppy(App):
    def build(self):
        return MainWindow()