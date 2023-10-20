from kivymd.uix.screen import MDScreen

class HomeScreen(MDScreen):
    
    name = 'home'

    def open_menu(self, _):
        self.ids.nav_drawer.set_state('toggle')

    def switch_screen(self, screen_name):
        self.manager.current = screen_name
        self.manager.transition.direction = 'left'
