
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class BusinessApp(App):
    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        layout.add_widget(Label(
            text="Amar Business",
            font_size=28
        ))

        layout.add_widget(Label(
            text="Business App Test Successful!",
            font_size=20
        ))

        layout.add_widget(Button(
            text="পরীক্ষা সম্পন্ন",
            font_size=20,
            size_hint=(1, 0.25)
        ))

        return layout

BusinessApp().run()
