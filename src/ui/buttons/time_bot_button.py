from discord import Button, Interaction
from ui.views.time_bot_views import RoleSelectView
from ui.modals.test_modal import TestModal
from interfaces.create_event_dto import CreateEventDTO


class CreateButton(Button):
    def __init__(self):
        super().__init__(label='Создать', custom_id='create_button')

    async def callback(self, interaction: Interaction):
        modal = TestModal()
        await interaction.response.send_modal(modal)


class SaveButton(Button):
    def __init__(self, start_time, end_time, event_name):
        super().__init__(label='Сохранить', custom_id='save_button')
        self.start_time = start_time
        self.end_time = end_time
        self.event_name = event_name

    async def callback(self, interaction):
        dto = CreateEventDTO(self.start_time, self.end_time, self.event_name)
        await interaction.response.send_message(f'Событие {self.event_name} сохранено и активировано.', ephemeral=True)


class AddRolesButton(Button):
    def __init__(self):
        super().__init__(label='Добавить роли', custom_id='add_roles_button')
        ...

    async def callback(self, interaction):
        role = RoleSelectView()
        await interaction.response.send_message(view=role)


class AddScenariosButton(Button):
    def __init__(self):
        super().__init__(label='Добавить сценарии', custom_id='add_scenarios_button')
        ...

    async def callback(self, interaction):
        ...
