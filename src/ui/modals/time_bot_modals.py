import datetime
import re
from discord import Interaction, TextInput
from discord.ui.modal import Modal
from ui.views.time_bot_views import CreateView


pattern = re.compile(r'\d{2}\.\d{2}\.\d{4}')


class TestModal(Modal):
    def __init__(self):
        super().__init__(title="Создание События")
        self.add_item(TextInput(label="Введите имя события:"))
        self.add_item(
            TextInput(label="Дата начала события в дд.мм.гггг"))
        self.add_item(
            TextInput(label="Дата конца события в дд.мм.гггг"))

    async def on_submit(self, interaction: Interaction, /) -> None:
        event_name = self.children[0].value
        start_time = self.children[1].value
        end_time = self.children[2].value
        try:
            if re.match(pattern, str(start_time)) and re.match(pattern, str(end_time)):
                start_time = datetime.strptime(
                    start_time, '%d.%m.%Y')
                end_time = datetime.strptime(end_time, '%d.%m.%Y')
                if end_time >= start_time and end_time >= datetime.today():
                    views = CreateView(start_time, end_time, event_name)
                    await interaction.response.send_message(f"Вы ввели: {event_name}, {start_time}, {end_time}", view=views, ephemeral=True)
                else:
                    await interaction.response.send_message(f"Не правильный формат даты", ephemeral=True)
        except ValueError as e:
            await interaction.response.send_message(f"Не правильный формат даты", ephemeral=True)
