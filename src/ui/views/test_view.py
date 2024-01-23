from discord.ui import View
from discord import ButtonStyle
from ui.buttons.test_button import TestButton


class TestView(View):
    def __init__(self):
        super().__init__()
        self.add_item(TestButton(label="Click for text input",
                      style=ButtonStyle.primary))
