# Twisted, the Framework of Your Internet
# Copyright (C) 2001 Matthew W. Lefkowitz
# 
# This library is free software; you can redistribute it and/or
# modify it under the terms of version 2.1 of the GNU Lesser General Public
# License as published by the Free Software Foundation.
# 
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

"""Coil plugin for telnet shell."""

# Twisted Imports
from twisted.coil import app, coil
from twisted.protocols import telnet

# System Imports
import types


class ShellFactoryConfigurator(app.ProtocolFactoryConfigurator):

    configurableClass = telnet.ShellFactory
    
    configTypes = {
        'username': types.StringType,
        'password': types.StringType,
        }

    configName = 'Telnet Python Shell'


def factory(container, name):
    return telnet.ShellFactory()


coil.registerConfigurator(ShellFactoryConfigurator, factory)
