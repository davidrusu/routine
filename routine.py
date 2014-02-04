#! /usr/bin/python3


import sys
import os
from os.path import join, expanduser, isfile, exists
from subprocess import call


HOME = expanduser("~")
ROUTINE_HOME = join(HOME, ".routine")


def new_routine(args):
    ensure_routine_home()

    if len(args) != 1:
        exit("Need exactly one argument after new")
        
    routine = args[0].lower()
    routine_path = join(ROUTINE_HOME, routine)
    
    if exists(routine_path):
        exit("routine '{}' already exists".format(routine))
        
    call(['emacs', '-nw', routine_path])


def list_routines(args):
    ensure_routine_home()

    dir_list = os.listdir(ROUTINE_HOME)
    files = [f for f in dir_list if isfile(join(ROUTINE_HOME, f))]

    for f in sorted(files):
        print(f)


def remove_routine(args):
    ensure_routine_home()
    
    if len(args) != 1:
        exit("Need exactly one argument after remove")
        
    routine = args[0].lower()
    routine_path = join(ROUTINE_HOME, routine)

    if not exists(routine_path):
        exit("Routine '{}' doesn't exist".format(routine))

    os.remove(routine_path)

def run_routine(args):
    ensure_routine_home()
    
    if len(args) != 1:
        exit("Need exactly one argument after 'run'")
        
    routine =  args[0].lower()
    routine_path = join(ROUTINE_HOME, routine)
    
    if not exists(routine_path):
        exit("Routine '{}' doesn't exist".format(routine))

    call(["/bin/bash", routine_path])


def edit_routine(args):
    ensure_routine_home()
    
    if len(args) != 1:
       exit("Need exactly one argument after 'edit'")

    routine =  args[0].lower()
    routine_path = join(ROUTINE_HOME, routine)
    
    if not exists(routine_path):
        exit("Routine '{}' doesn't exist".format(routine))

    call(['emacs', '-nw', routine_path])

    
def ensure_routine_home():
    if not exists(ROUTINE_HOME):
        os.mkdir(ROUTINE_HOME)


def show_help():
    help = """
routine manager and runner

OPTIONS
    new [ROUTINE]
        Creates a new routine named [ROUTINE]

    remove [ROUTINE]
        removes the routine named [ROUTINE]

    list
        Lists all managed routines

    run [ROUTINE]
        Runs the routine [ROUTINE]

    help
        Displays this help message

EXAMPLES
    routine new wakeup

    routine run wakeup"""
    
    print(help)

if __name__ == "__main__":
    
    command = sys.argv[1].lower()
    commands = {"new": new_routine,
                "remove": remove_routine,
                "list": list_routines,
                "run": run_routine,
                "edit": edit_routine}

    if command in commands:
        args = sys.argv[2:]
        commands[command](args)
    else:
        show_help()

