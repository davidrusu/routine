from subprocess import call, DEVNULL

def open(cmd, args):
    def task():
        call([cmd, args, '&'], stdout=DEVNULL, stderr=DEVNULL)
    return task

def web(site):
    def task():
        call(['firefox', site], stdout=DEVNULL, stderr=DEVNULL)
    return task

def run(cmd, args):
    def task():
        call([cmd, args])
    return task
