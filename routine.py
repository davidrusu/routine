#!/usr/bin/python3

import sys, os, shlex
from os.path import join, expanduser, isfile, exists
from shutil import copyfile
from subprocess import call

HOME = expanduser("~")
ROUTINE_HOME = join(HOME, ".routine")
EDITOR = os.environ.get('EDITOR')
if EDITOR == "":
    exit('EDITOR environment vaiable not set')

def new_routine(args):
    ensure_routine_home()

    # ensure that none of the routines already exist
    for a in args:
        ensure_routine_not_exist(a)

    edit_routine(args)

def rename_routine(args):
    ensure_routine_home()

    if len(args) != 2:
        exit("rename takes exactly 2 argument")

    routine = args[0]
    ensure_routines_exist([routine])

    new_routine_path = join(ROUTINE_HOME, args[1].lower())
    ensure_routine_not_exist(new_routine_path)

    routine_path = join(ROUTINE_HOME, routine)
    os.rename(routine_path, new_routine_path)

def list_routines(args):
    ensure_routine_home()
    non_routine_files = {'api.py'}

    dir_list = os.listdir(ROUTINE_HOME)
    files = [f for f in dir_list if isfile(join(ROUTINE_HOME, f))]

    files = filter(lambda f: f not in non_routine_files, files)

    for f in sorted(files):
        print(f)


def remove_routine(args):
    ensure_routine_home()
    ensure_routines_exist(args)

    for a in args:
        routine = a.lower()
        routine_path = join(ROUTINE_HOME, routine)
        os.remove(routine_path)


def run_routine(args):
    ensure_routine_home()
    ensure_routines_exist(args)

    for a in args:
        routine = args[0].lower()
        routine_path = join(ROUTINE_HOME, routine)
        with open(routine_path) as task_file:
            name_space = {}
            exec(task_file.read(), name_space)
            for task in name_space['tasks']:
                task()


def edit_routine(args):
    ensure_routine_home()
    ensure_routines_exist(args)

    # split for case where EDITOR contains arguments e.g. emacs -nw
    editor = shlex.split(EDITOR)
    for a in args:
        routine =  a.lower()
        routine_path = join(ROUTINE_HOME, routine)
        call(editor + [routine_path])


def ensure_routines_exist(routines):
    for r in routines:
        routine = r.lower()
        routine_path = join(ROUTINE_HOME, routine)
        if not exists(routine_path):
            exit("Routine '{}' doesn't exist, no changes made".format(routine))

def ensure_routine_not_exist(routine):
    routine = routine.lower()
    routine_path = join(ROUTINE_HOME, routine)
    if exists(routine_path):
        exit("routine '{}' already exists, no changes made".format(routine))

def ensure_routine_home():
    if not exists(ROUTINE_HOME):
        os.mkdir(ROUTINE_HOME)
    api = 'api.py'
    home_api = join(ROUTINE_HOME, api)
    if not exists(home_api):
        print("{} missing from .routine folder".format(api))

def show_help():
    help_msg = """
routine manager and runner

OPTIONS
    new routine_name
        Creates a new routine named 'routine_name'

    edit routine_name
        Edit the routine named 'routine_name'

    remove routine_name
        removes the routine named [ROUTINE]

    list
        Lists all managed routines

    run routine_name
        Runs the routine

    rename old_name new_name
        Renames the routine 'old_name' to the routine 'new_name'

    help
        Displays this help message

EXAMPLES
    routine new wakeup
    routine run wakeup"""
    print(help_msg)

if __name__ == "__main__":
    command = sys.argv[1].lower() if len(sys.argv) > 1 else 'help'
    commands = {"new": new_routine,
                "remove": remove_routine,
                "list": list_routines,
                "run": run_routine,
                "edit": edit_routine,
                "rename": rename_routine}

    if command in commands:
        args = sys.argv[2:]
        commands[command](args)
    else:
        show_help()
