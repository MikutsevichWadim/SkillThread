from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivymd.uix.card import MDCard

class ChannelCard(MDCard):

    channel_id = NumericProperty()
    last_update = StringProperty()
    name = StringProperty()
    teacher_name = StringProperty()
    image_source = StringProperty()

    def __init__(
            self, channel_id, last_update, name,
            teacher_name, is_teacher,
            image_source=None,
            *args, **kwargs
        ):
        
        super().__init__(*args, **kwargs)
        
        self.channel_id = channel_id
        self.last_update = last_update
        self.name = name
        self.teacher_name = teacher_name
        if not image_source:
            self.image_source = 'data/channels/default-icon.png'
        else:
            self.image_source = image_source
        
        self.md_bg_color = ((.9,.9,.9), (.7,1,.7))[is_teacher]
    