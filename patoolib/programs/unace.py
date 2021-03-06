# -*- coding: utf-8 -*-
# Copyright (C) 2010-2014 Bastian Kleineidam
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
"""Archive commands for the unace program."""

def extract_ace (archive, compression, cmd, verbosity, outdir):
    """Extract an ACE archive."""
    cmdlist = [cmd, 'x']
    if not outdir.endswith('/'):
        outdir += '/'
    cmdlist.extend([archive, outdir])
    return cmdlist

def list_ace (archive, compression, cmd, verbosity):
    """List an ACE archive."""
    cmdlist = [cmd]
    if verbosity > 1:
        cmdlist.append('v')
    else:
        cmdlist.append('l')
    cmdlist.append(archive)
    return cmdlist

def test_ace (archive, compression, cmd, verbosity):
    """Test an ACE archive."""
    return [cmd, 't', archive]
