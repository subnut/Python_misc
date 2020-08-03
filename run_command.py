# Used to run commands input as a single string using "sh -c"


def run(command):
    from subprocess import PIPE, Popen

    process = Popen(["sh", "-c", command], stdout=PIPE, stderr=PIPE, text=True)
    stdout, stderr = process.communicate()
    exitcode = process.returncode
    return {"stdout": stdout, "stderr": stderr, "exitcode": exitcode}
