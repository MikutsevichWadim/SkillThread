from kivymd.uix.screen import MDScreen

class SignupScreen(MDScreen):
    name = 'signup'

    def signup(self):
        self.success_signup()

    def success_signup(self):
        self.manager.current = 'home'
        self.manager.transition.direction = 'left'

    def go_to_login(self):
        self.manager.current = 'login'
        self.manager.transition.direction = 'left'
