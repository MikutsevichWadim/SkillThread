import asyncio

from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

from widgets.ChannelCard import ChannelCard

class LoginScreen(MDScreen):
    name = 'login'

    def login(self):
        self.success_login()

    def go_to_signup(self):

        self.manager.current = 'signup'
        self.manager.transition.direction = 'right'

    def success_login(self):
        self.manager.current = 'home'
        self.manager.transition.direction = 'left'