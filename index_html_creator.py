h=open('index.html','w')
h.write('''<html>
<head>
<title>Python_misc</title>
<link rel="stylesheet" href="prism.css">
</head>
<body bgcolor="#F5F2F0" link="#1F00FF" vlink="#1F00FF">\n''')

def contents(f):
    with open(f,'r') as file:
        return file.readlines()

from os import listdir
l=[x for x in listdir('.') if (x[-3:]=='.py' and x!='index_html_creator.py')]

h.write('<br>\n')

h.write('<ul>\n')
for a in range(len(l)):         # I am using numbers as link-id because filenames may have spaces, which are not allowed
    h.write('<li>')
    h.write('<a href="#'+str(a)+'">'+l[a][:-3]+'</a>')
    h.write('</li>\n')
h.write('</ul>\n')

h.write('<br><br>\n')

id=-1

for z in l:
    id+=1
    h.write('<a id="'+str(id)+'"></a>\n')
    h.write('<br><br>\n')
    h.write(z[:-3]+'<br>\n')
    h.write('''<pre>
<code class=" language-python">''')
    h.writelines(contents(z))
    h.write('''<br>
</code>
</pre>\n''')

h.write('''<script src="prism.js"></script>
</body>
</html>''')
h.close()