from kivy.core.window import Window
from kivy.lang import Builder
import asyncio

from kivymd.app import MDApp

import screens
import widgets
from widgets.ChannelCard import ChannelCard

class STApp(MDApp):
    title = 'SkillThread'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.loop = asyncio.get_event_loop()

    def build(self):
        self.theme_cls.primary_palette = 'Green'

        manager = Builder.load_file('main.kv')

        home_screen = manager.get_screen('home')
        from channels_list import channels
        for i, channel in enumerate(channels):
            image_source=None
            if i not in (0, 1, 2, 3, 7):
                image_source=f'data/channels/{i}.png'
            home_screen.ids.channel_list.add_widget(ChannelCard(
                channel_id=i,
                last_update=f'{29-i}.10.2023',
                teacher_name=channel[2],
                is_teacher=channel[1],
                name=channel[0],
                image_source=image_source))

        return manager

if __name__ == '__main__':
    STApp().run()

