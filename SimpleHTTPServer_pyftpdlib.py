#  This is not actually a Python program
#  But it is, undeniably, an amazing piece of code
#
#  At the terminal, cd into the folder you want
#  run the following command
#
#  python -m http.server 8080
#
#  then, it will set up a simple HTTP server on port 8080
#  sharing the contents of the folder
#
#  Explanation of the code -
#
#  This command executes Python
#  and imports the embedded Python2 module SimpleHTTPServer
#  which runs an HTTP server on port 8080 of the machine
#  on the directory this code is executed in
#
#  Simple way to quickly send some files :D
#
#  P.S. For sending larger files,
#  it is better to use a server having 'range' support
#  So, do this -
#       pip install rangehttpserver
#  Then, run - python -m RangeHTTPServer
#  Note: It will ONLY serve on the port 8000
#
#  also, for ftp server
#
#  pip install pyftpdlib
#  python -m pyftpdlib --help
#
#  see the help and configure as required :D
