from discord.ui import Button
from discord import Interaction, ButtonStyle
from data.modals.test_modal import TestModal


class TestButton(Button):
    def __init__(self, label: str, style: ButtonStyle):
        super().__init__(label=label, style=style)

    async def callback(self, interaction: Interaction):
        # Define what happens when the button is clicked
        modal = TestModal()
        await interaction.response.send_modal(modal)
