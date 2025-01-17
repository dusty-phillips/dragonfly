#
# This file is part of Dragonfly.
# (c) Copyright 2007, 2008 by Christo Butcher
# Licensed under the LGPL.
#
#   Dragonfly is free software: you can redistribute it and/or modify it
#   under the terms of the GNU Lesser General Public License as published
#   by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Dragonfly is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#   Lesser General Public License for more details.
#
#   You should have received a copy of the GNU Lesser General Public
#   License along with Dragonfly.  If not, see
#   <http://www.gnu.org/licenses/>.
#

import win32api

from .base_monitor import BaseMonitor
from .rectangle import Rectangle


#===========================================================================
# Monitor class for storing info about a single display monitor.

class Win32Monitor(BaseMonitor):
    """
    The monitor class used on Win32.
    """

    #-----------------------------------------------------------------------
    # Class methods to create new Monitor objects.

    @classmethod
    def get_all_monitors(cls):
        # Get an updated list of monitors.
        monitors = []
        for py_handle, _, rectangle in win32api.EnumDisplayMonitors():
            # Get the monitor handle.
            handle = py_handle.handle

            # Create a rectangle object representing the monitor's
            # dimensions and relative position.
            top_left_x, top_left_y, bottom_right_x, bottom_right_y = rectangle
            dx = bottom_right_x - top_left_x
            dy = bottom_right_y - top_left_y
            rectangle = Rectangle(top_left_x, top_left_y, dx, dy)

            # Get a new or updated monitor object and add it to the list.
            monitors.append(cls.get_monitor(handle, rectangle))

        return monitors
