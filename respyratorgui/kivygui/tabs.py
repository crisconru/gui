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
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty
# Coded -----------------------------------------------------------------------
from . import logapp, load_kv
# Program ---------------------------------------------------------------------
LOG = 'TABS:'
load_kv(__file__)


class GuiTabs(BoxLayout):
    tab_selected = ''
    tab_config = ObjectProperty()
    tab_modes = ObjectProperty()
    tab_params = ObjectProperty()
    tab_alarms = ObjectProperty()
    tab_monitoring = ObjectProperty()

    def _tab_clicked(self, tab: str, tab_obj):
        if tab != self.tab_selected:
            self.parent.tab_clicked(tab)
        else:
            tab_obj.state = 'down'

    def _set_tabs(self, tab_down: ToggleButton, *tabs_normal: ToggleButton):
        if tab_down:
            tab_down.state = 'down'
        for tab_normal in tabs_normal:
            tab_normal.state = 'normal'

    def tab_config_selected(self):
        self._set_tabs(self.tab_config, self.tab_modes, self.tab_params,
                       self.tab_alarms, self.tab_monitoring)
        self.tab_selected = 'configuration'

    def tab_modes_selected(self):
        self._set_tabs(self.tab_modes, self.tab_config, self.tab_params,
                       self.tab_alarms, self.tab_monitoring)
        self.tab_selected = 'modes'

    def tab_params_selected(self):
        self._set_tabs(self.tab_params, self.tab_config, self.tab_modes,
                       self.tab_alarms, self.tab_monitoring)
        self.tab_selected = 'params'

    def tab_alarms_selected(self):
        self._set_tabs(self.tab_alarms, self.tab_config, self.tab_modes,
                       self.tab_params, self.tab_monitoring)
        self.tab_selected = 'alarms'

    def tab_monitoring_selected(self):
        self._set_tabs(self.tab_monitoring, self.tab_config, self.tab_modes,
                       self.tab_params, self.tab_alarms)
        self.tab_selected = 'monitoring'

    def tab_nothing_selected(self):
        self._set_tabs(None, self.tab_config, self.tab_modes, self.tab_params,
                       self.tab_alarms, self.tab_monitoring)
        self.tab_selected = ''
