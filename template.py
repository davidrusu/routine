# -*- mode: python -*-

from api import web, run, rund

'''
Tasks are run in the order they are placed in the list

EXAMPLE:
tasks = [ web('example.com')              # opens the website www.example.com in firefox
        , run('pacman', '-Syu')           # runs and waits for the command 'pacman -Syu' to finish
        , rund('evince', 'path/to/pdf')   # runs and doesn't wait for command to finish
        ]
'''

tasks = [
        ]