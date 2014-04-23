from subprocess import Popen, call, DEVNULL

def _run_daemon(confirm_msg, cmd, args=""):
    if _confirm(confirm_msg):
        Popen([cmd, args], stdout=DEVNULL, stderr=DEVNULL)

def _confirm(prompt):
    choice = input(prompt + " (Y/N): ")
    return choice == "" or choice.lower()[0] == "y"

def web(site):
    '''Opens the webpage in firefox'''
    def task():
        confirm_msg = "open website " + site
        _run_daemon(confirm_msg, "firefox", site)
    return task

def run(cmd, args=""):
    '''Runs and waits for the cmd to finish'''
    def task():
        if _confirm("run " + cmd + " " + args):
            call([cmd, args])
    return task

def rund(cmd, args=""):
    '''Runs the command but doesn't wait for it to finish'''
    def task():
        confirm_msg = "rund " + cmd + " " + args
        _run_daemon(confirm_msg, cmd, args)
    return task
