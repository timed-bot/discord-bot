from discord.ui import Modal, TextInput
from discord import Interaction


class TestModal(Modal):
    def __init__(self):
        super().__init__(title="Your Input")

        self.add_item(TextInput(label="Enter your text here"))

    async def on_submit(self, interaction: Interaction, /) -> None:
        # Handle the user's input
        print(self.children)
        response = self.children[0].value  # Gets the value from the TextInput
        await interaction.response.send_message(f"You entered: {response}", ephemeral=True)
