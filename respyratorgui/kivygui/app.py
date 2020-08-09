# Copyright (C) 2020 Respyrator
# This file is part of Respyrator <https://respyrator.github.io>.
#
# Respyrator is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Respyrator is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Respyrator.  If not, see <http://www.gnu.org/licenses/>.

# Built-in --------------------------------------------------------------------
# Installed -------------------------------------------------------------------
from kivy.app import App
from kivy.properties import StringProperty
# Coded -----------------------------------------------------------------------
from . import logapp
from .container import GuiContainer
# Program ---------------------------------------------------------------------
LOG = 'APP:'


class GuiApp(App):
    mode = StringProperty()

    def build(self):
        logapp.debug(f'{LOG} build()')
        #Clock.schedule_once(lambda dt: self.setup(), 1.0)
        return GuiContainer()

    def on_start(self):
        self.ui_selected('params')

    def on_mode(self, instance: StringProperty, value: str):
        print(f'{LOG} mode = {self.mode} and value = {value}')

    def ui_selected(self, screen: str):
        ui = {
            'modes': self.root.ui_modes,
            'params': self.root.ui_params,
            'alarms': self.root.ui_alarms,
        }
        ui[screen]()

    def mode_selected(self, mode: str):
        self.mode = mode
        self.root.unblock_tabs()
        self.ui_selected('params')

    def param_selected(self, param: str, value: float):
        print(f'Has changed {param} to {value}')


if __name__ == "__main__":
    GuiApp().run()
