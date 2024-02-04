from discord import Interaction
from discord.ui import View, RoleSelect
from ui.buttons.time_bot_button import AddRolesButton, AddScenariosButton, CreateButton, SaveButton


class TimeBotView(View):
    def __init__(self):
        super().__init__()
        self.add_item(CreateButton())


class CreateView(View):
    def __init__(self, start_time, end_time, event_name):
        super().__init__()
        self.add_item(SaveButton(start_time, end_time, event_name))
        self.add_item(AddRolesButton())
        self.add_item(AddScenariosButton())


class RoleSelectView(View):
    def __init__(self):
        super().__init__()
        role_select = RolesSel()
        self.add_item(role_select)

    async def interaction_check(self, interaction: Interaction, /):
        print(self.children[0].values)


class RolesSel(RoleSelect):
    def __init__(self):
        super().__init__(placeholder="Выбери роли", min_values=1, max_values=25)
