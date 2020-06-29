## Used to run commands input as a single string

def run(command):
    command=command.split()
    from subprocess import PIPE,Popen
    process=Popen(command,stdout=PIPE,stderr=PIPE,text=True)
    stdout,stderr=process.communicate()
    exitcode=process.returncode
    return {'stdout':stdout,'stderr':stderr,'exitcode':exitcode}

