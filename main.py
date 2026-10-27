
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window


class BusinessApp(App):
    def build(self):
        Window.clearcolor = (0.95, 0.97, 1, 1)

        root = BoxLayout(
            orientation="vertical",
            padding=15,
            spacing=10
        )

        title = Label(
            text="আমার ব্যবসা",
            font_size="28sp",
            bold=True,
            color=(0.1, 0.25, 0.5, 1),
            size_hint_y=None,
            height=65
        )
        root.add_widget(title)

        subtitle = Label(
            text="ব্যবসার হিসাব সহজেই রাখুন",
            font_size="16sp",
            color=(0.25, 0.3, 0.4, 1),
            size_hint_y=None,
            height=40
        )
        root.add_widget(subtitle)

        scroll = ScrollView()
        menu = BoxLayout(
            orientation="vertical",
            spacing=12,
            size_hint_y=None
        )
        menu.bind(minimum_height=menu.setter("height"))

        options = [
            "📦 পণ্য ও স্টক",
            "🛒 বিক্রয়ের হিসাব",
            "🧾 ক্রয়ের হিসাব",
            "💰 আয় ও খরচ",
            "👥 গ্রাহক ও বকেয়া",
            "📊 লাভ-ক্ষতির রিপোর্ট",
            "💾 ডেটা ব্যাকআপ"
        ]

        for option in options:
            button = Button(
                text=option,
                font_size="19sp",
                size_hint_y=None,
                height=58,
                background_normal="",
                background_color=(0.12, 0.38, 0.72, 1)
            )
            menu.add_widget(button)

        scroll.add_widget(menu)
        root.add_widget(scroll)

        return root


if __name__ == "__main__":
    BusinessApp().run()

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
