# *****************************************************************************
# *                     c s v 2 p q _ g l o b a l s . p y                     *
# *****************************************************************************

# Developed for the LSST Data Management System.
# This product includes software developed by the LSST Project
# (http://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""This module contains variables describing the command line invocation.

This module contains all the variables used to communicate the requirements
csv2pq or pq2csv command invocation across all related modules.
"""

from collections import defaultdict

# *****************************************************************************
# *                               G l o b a l s                               *
# *****************************************************************************

# Column information
#
cNameMax = 0
colNames = []
colNVChk = []
colSpecs = []
colTypes = {}

# File information
#
FIN = []
FOUT = []

# Options
#
OPT = defaultdict(lambda: '')

BLAB = False
DBG = False
