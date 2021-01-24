from os import listdir
from html import escape


html_file = open("index.html", "w")

html_file.write(
    """<html>
<head>
<title>Python_misc</title>
<link rel="stylesheet" href="prism.css">
</head>
<body bgcolor="#F5F2F0" link="#1F00FF" vlink="#1F00FF">\n"""
)


def contents(f):
    with open(f, "r") as file:
        return file.read()


"""
 Note that in the above function I have used "with open" instead of the normal
 file=open(...)

 I could have used the following code:

      def contents(f):
          file=open(f,'r')
          return file.readlines()
          file.close()

 It seems exactly same as the one I've used, right?
 But hold on.... do you remember?
 A function exits as soon as it recieves the "return" statement
 Can you see the problem?

 Yeah... As soon as the function reaches "return file.readlines()"
 It just simply ignores the rest of the statements
 And so, the file remains open!

 So what?
 So, if another section of code tries to open that file, it can result to data corruption!
 And nobody in their right mind would want something like that to happen, right?

 And that is why i recommend using "with open"
 It ensures that the file being opened is gracefully closed
"""


file_list = [x for x in listdir(".") if x[-3:] == ".py"]

html_file.write("<br>\n")

html_file.write("<ul>\n")
# I am using numbers as link-id because filenames may have spaces, which are
# not allowed
for a in range(len(file_list)):
    html_file.write("<li>")
    html_file.write('<a href="#' + str(a) + '">' + file_list[a][:-3] + "</a>")
    html_file.write("</li>\n")
html_file.write("</ul>\n")

html_file.write("<br><br>\n")

id = -1

for file in file_list:
    id += 1
    html_file.write('<a id="' + str(id) + '"></a>\n')
    html_file.write("<br><br>\n")
    html_file.write(file[:-3] + "<br>\n")
    html_file.write(
        """<pre>
<code class=" language-python">"""
    )
    html_file.write(escape(contents(file)))
    html_file.write(
        """<br>
</code>
</pre>\n"""
    )

html_file.write(
    """<script src="prism.js"></script>
</body>
</html>"""
)
html_file.close()
