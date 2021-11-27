import sys
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivy.uix.image import AsyncImage
from kivy.config import Config
from cat import getImage

sys.path.insert(0, '/cat')


class Window(MDApp):

    def callback(self, instance):
        self.newImage.source = f'https://http.cat/{getImage.getCat()}.jpg'

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.title = "httpCat"
        self.icon = "cat/icon.png"
        self.newImage = AsyncImage(source=f'https://http.cat/{getImage.getCat()}.jpg')
        screen = MDScreen()

        button = MDRaisedButton(text="Get new cat", pos_hint={"center_x": .5,
                                                              "center_y": .055},
                                md_bg_color=(1, 1, 1, 1),
                                text_color=(0.0001, 0, 0, 1),
                                on_release=self.callback)

        label = MDLabel(text="Cat generator", pos_hint={'center_x': 0.5,
                                                        'center_y': 0.95},
                        theme_text_color="Custom",
                        text_color=(1, 1, 1, 1),
                        font_style="H4",
                        halign="center")

        screen.add_widget(self.newImage)
        screen.add_widget(label)
        screen.add_widget(button)
        return screen


if __name__ == '__main__':
    Config.set('graphics', 'width', '855')
    Config.set('graphics', 'height', '795')
    Config.write()
    Window().run()

# TODO: Make DB storing how many times a user landed on specific cat and display it
# TODO: Visualise data from SQL into bargraph/chart
