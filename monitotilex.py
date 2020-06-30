def run(command):
    from subprocess import PIPE,Popen
    process=Popen(["sh","-c",command],stdout=PIPE,stderr=PIPE,text=True)
    stdout,stderr=process.communicate()
    exitcode=process.returncode
    return {'stdout':stdout,'stderr':stderr,'exitcode':exitcode}

def get_loginid():
    for string in run("loginctl")['stdout'].lower().split('\n'):
        if string.find(getlogin()) != -1 & string.find("tty") == -1:
            return string.split()[0]
    else:
        print("No non-tty logins of this user has been found. Please login into a X session.")
        exit()

def get_session_type():
    return run("loginctl show-session "+get_loginid()+" -p Type")['stdout'].split('=')[1].split('\n')[0]

def check_xrandr():
    xrandr_code = run("xrandr")['exitcode']
    if xrandr_code == 0: return True
    elif xrandr_code == 127: print("command 'xrandr' not found \nPlease install the package which includes this command")
    elif xrandr_code == 1: print("xrandr exited with exit code 1\nAre you on a X session? This program only runs inside an X session")
    else: print("Unknown error while running 'xrandr'")
    exit()

def check():
   if (tuple(version_info)[0]==3) & (platform=='linux') & (get_session_type()=='x11') & check_xrandr():
        return True
   else:
        if tuple(version_info)[0]!=3: print("Python v3 needed")
        elif platform != 'linux': print("Only linux is supported")
        elif get_session_type()=='wayland': print("Wayland is not supported")
        elif get_session_type()!="x11": print("Needs X11 session")
        elif not check_xrandr(): pass
        else: print("Unknown error")
        return False 

def main():
    print("yay!")


try: from sys import version_info,platform; from os import getlogin
except ModuleNotFoundError: print("Please insure that the following modules are available:\nsys, os"); exit()
else: pass

if (__name__=="__main__") & check(): main()
