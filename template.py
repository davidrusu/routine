# -*- mode: python -*-
# Tasks are run in the order they are placed in the list
# 
# EXAMPLE:
# tasks = [ rund('evince', 'file.pdf')    # doesn't wait for 'evince' to finish
#         , web('example.com')            # opens www.example.com in firefox
#         , run('pacman', '-Syu')         # waits 'pacman -Syu' to finish
#         ]

from api import web, run, rund

tasks = [
        ]