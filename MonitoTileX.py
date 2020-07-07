## MonitoTileX
## Yes, the X stands for X

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
        exit(1)

def get_session_type():
    return run("loginctl show-session "+get_loginid()+" -p Type")['stdout'].split('=')[1].split('\n')[0]

def check_xrandr():
    xrandr_code = run("xrandr")['exitcode']
    if xrandr_code == 0: return True
    elif xrandr_code == 127: print("command 'xrandr' not found \nPlease install the package which includes this command")
    elif xrandr_code == 1: print("xrandr exited with exit code 1\nAre you on a X session? This program only runs inside an X session")
    else: print("Unknown error while running 'xrandr'")
    exit(1)

def check_readline():
    try: import readline
    except ModuleNotFoundError:
        exitcode = run("python -m pip install readline")['exitcode']
        if exitcode != 0: print("Module 'readline' was not found. Please install."); exit(1); return False
    return True

def check():
   if (tuple(version_info)[0]==3) & (platform=='linux') & (get_session_type()=='x11') & check_xrandr() & check_readline():
        return True
   else:
        if tuple(version_info)[0]!=3: print("Python v3 needed")
        elif platform != 'linux': print("Only linux is supported")
        elif get_session_type()=='wayland': print("Wayland is not supported")
        elif get_session_type()!="x11": print("Needs X11 session")
        elif not check_xrandr(): pass
        else: print("Unknown error")
        return False 


def my_completer_helper(inputText,commands,loopState):
    matchList = [x for x in commands if x.startswith(inputText)]
    
    if len(matchList)==0:
        if loopState > 0: return None
        for l in range(1,len(inputText)):
            matches = [x for x in commands if x.startswith(inputText[:-l])]
            if len(matches) > 0:
                return matches[0]+' '

    if len(matchList)==1:
        if loopState==0: return matchList[0]+' '
        else: return None
    
    else:
        try: return matchList[loopState]
        except IndexError: return None




def my_completer_function(inputText, loopState):
    firstCommands = ['do','orient','status','quit']
    monitors = [ x for x in run("xrandr -q | grep ' connected' | cut -d' ' -f1")['stdout'].split('\n') if len(x) > 0 ]
    directionOf = [ 'left', 'right', 'top', 'bottom' ]
    alignTo = { 
                'left':('top', 'bottom'),
                'right':('top', 'bottom'),
                'top':('left', 'right'),
                'bottom':('left', 'right')
              }
    if inputText.count(' ') == 0:
        return my_completer_helper(inputText,firstCommands,loopState)
    if inputText.count(' ') == 1:
        firstCommand = inputText.split()[0]
        availableCommands = 
        return my_completer_helper(,monitors,loopState)
    

def currentlyConnected(monitors):
    return "Currently connected monitors are: "+monitorListToString(monitors)

def monitorListToString(monitors):
    monitorString = ""
    for x in monitors:
        monitorString += x + " "
    return monitorString





def main_loop():
    userInput = input('\n> ')
    monitors = [ x for x in run("xrandr -q | grep ' connected' | cut -d' ' -f1")['stdout'].split('\n') if len(x) > 0 ]
    

    
    if userInput == "status":
        print(currentlyConnected(monitors))
    if userInput in ("quit","q"):
        return False
    return True

def main():
    if not check(): print("Unknown Error"); exit(1); return False
    import readline
    readline.set_completer(my_completer_function)
    readline.parse_and_bind("tab: complete")
    monitors = [ x for x in run("xrandr -q | grep ' connected' | cut -d' ' -f1")['stdout'].split('\n') if len(x) > 0 ]
    print("""Welcome to Monitotilex!
Enter 'q' or 'quit' to exit
{}
To get this list of connected monitors, run 'status' anytime

Valid commands are of the syntax:   
    do <monitor-name-1> <left|right|top|bottom> <monitor-name-2> <aligned-to-side>
    orient <monitor-name> <normal|left-side-down|right-side-down|upside-down>
And are interpreted as:
    <monitor-name-1> is <left|right|top|bottom> of <monitor-name-2> and aligned to the <aligned-to-side> side of <monitor-name-2>
    <monitor-name> has been kept in the position <normal|left-side-down|right-side-down|upside-down>. So adjust the display accordingly.

P.S.: Tab-completion is available at every step""".format(currentlyConnected(monitors)))
    loop = True
    while loop:
        loop = main_loop()
    exit(0)




try: from sys import version_info,platform; from os import getlogin
except ModuleNotFoundError: print("Please insure that the following modules are available:\nsys, os"); exit(1)
else: pass

if (__name__=="__main__") & check(): main()


# To-do
""" wrong command -> suggest
command interpreter -> input().split()
main logic
mirror command (mirror <mon1> <mon2>)
"""
