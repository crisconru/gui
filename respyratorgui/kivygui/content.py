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
from kivy.uix.screenmanager import ScreenManager
# Coded -----------------------------------------------------------------------
from . import logapp, load_kv
# Program ---------------------------------------------------------------------
LOG = 'CONTENT:'
load_kv(__file__)


class GuiContent(ScreenManager):
    def _set_screen(self, screen: str = ''):
        screens = {
            'modes': 'modes_screen',
            'params': 'params_screen',
            'alarms': 'alarms_screen',
            'monitoring': 'monitoring_screen'
        }
        self.current = screens.get(screen, 'loading_screen')

    def loading(self):
        self._set_screen()

    def modes(self):
        self._set_screen('modes')

    def params(self):
        self._set_screen('params')

    def alarms(self):
        self._set_screen('alarms')

    def monitoring(self):
        self._set_screen('monitoring')