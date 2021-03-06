'''
  This file is part of the PyPhantomJS project.

  Copyright (C) 2011 James Roe <roejames12@hotmail.com>
  Copyright (C) 2011 Ariya Hidayat <ariya.hidayat@gmail.com>

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import argparse, sys

from PyQt4.QtCore import QDateTime, Qt, QtDebugMsg, QtWarningMsg, QtCriticalMsg, QtFatalMsg

version_major = 1
version_minor = 1
version_patch = 0
version = '%d.%d.%d' % (version_major, version_minor, version_patch)

license = '''
  PyPhantomJS Version %s

  Copyright (C) 2011 James Roe <roejames12@hotmail.com>

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
''' % version

def argParser():
    parser = argparse.ArgumentParser(
        description='Minimalistic headless WebKit-based JavaScript-driven tool',
        usage='%(prog)s [options] script.[js|coffee] [script argument [script argument ...]]',
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument('--load-images', default='yes',
        choices=['yes', 'no'],
        help='Load all inlined images (default: %(default)s)'
    )
    parser.add_argument('--load-plugins', default='no',
        choices=['yes', 'no'],
        help='Load all plugins (i.e. Flash, Silverlight, ...)\n(default: %(default)s)'
    )
    parser.add_argument('--proxy', metavar='address:port',
        help='Set the network proxy'
    )
    parser.add_argument('--upload-file', nargs='*',
        metavar='tag=file', help='Upload 1 or more files'
    )
    parser.add_argument('script', metavar='script.[js|coffee]', nargs='*',
        help='The script to execute, and any args to pass to it'
    )
    parser.add_argument('-v', '--verbose', action='store_true',
        help='Show verbose debug messages'
    )
    parser.add_argument('--version',
        action='version', version=license,
        help='show this program\'s version and license'
    )
    return parser

class MessageHandler:
    def __init__(self, verbose):
        self.verbose = verbose

    def process(self, msgType, msg):
        now = QDateTime.currentDateTime().toString(Qt.ISODate)

        if msgType == QtDebugMsg:
            if self.verbose:
                print '%s [DEBUG] %s' % (now, msg)
        elif msgType == QtWarningMsg:
            print >> sys.stderr, '%s [WARNING] %s' % (now, msg)
        elif msgType == QtCriticalMsg:
            print >> sys.stderr, '%s [CRITICAL] %s' % (now, msg)
        elif msgType == QtFatalMsg:
            print >> sys.stderr, '%s [FATAL] %s' % (now, msg)
