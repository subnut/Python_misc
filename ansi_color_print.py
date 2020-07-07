def colorPrint(string,colorArgs,end='\n'):
    import sys
    fore=back=None
    try: fore=colorArgs[0]
    except: pass
    try: back=colorArgs[1]
    sys.stdout.write('\033[38;5;'+str(foreColor)+'m'+string+'')
