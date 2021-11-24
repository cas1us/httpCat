from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen


class Window(MDApp):
    def build(self):
        screen = Screen()

        label = MDLabel(text="Suh", pos_hint={'center_x': 0.5,
                                              'center_y': 0.5},
                        theme_text_color="Custom",
                        text_color=(0, 0, 0, 1),
                        font_style="H1",
                        halign="center")

        screen.add_widget(label)
        return screen


if __name__ == '__main__':
    Window().run()
