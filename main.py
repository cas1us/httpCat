import sys
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivy.uix.image import AsyncImage
from cat import getImage

sys.path.insert(0, '/cat')


class Window(MDApp):
    def press(self, instance):
        getImage.run()

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.title = "httpCat"
        self.icon = "cat/icon.png"
        screen = MDScreen()

        button = MDRaisedButton(text="Button", pos_hint={"center_x": .5,
                                                         "center_y": .8},
                                md_bg_color=(1, 1, 1, 1),
                                text_color=(0.0001, 0, 0, 1),
                                )
        button.bind(on_press=self.press)

        label = MDLabel(text="Suh", pos_hint={'center_x': 0.5,
                                              'center_y': 0.5},
                        theme_text_color="Custom",
                        text_color=(1, 1, 1, 1),
                        font_style="H1",
                        halign="center")

        imgNumber = AsyncImage(source=f'http.cat/{getImage.getCat()}')
        print(getImage.getCat)
        print(imgNumber)

        screen.add_widget(button)
        screen.add_widget(label)
        screen.add_widget(imgNumber)
        return screen


if __name__ == '__main__':
    getImage.run()
    Window().run()

# TODO: Make DB storing how many times a user landed on specific cat and display it
# TODO: Visualise data from SQL into bargraph/chart
