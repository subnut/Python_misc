h=open('index.html','w')
h.write('''<html>
<head>
<title>Python_misc</title>
<link rel="stylesheet" href="prism.css">
</head>
<body bgcolor="#F5F2F0">''')

def contents(f):
    with open(f,'r') as file:
        return file.readlines()

from os import listdir
l=[x for x in listdir() if (x[-3:]=='.py' and x!='index_html_creator.py')]

h.write('<br>')

h.write('<ul>')
for a in range(len(l)):
    h.write('<li>')
    h.write('<a href="#'+str(a)+'">'+l[a][:-3]+'</a>')
    h.write('</li>')
h.write('</ul>')

h.write('<br><br>')

id=-1

for z in l:
    id+=1
    h.write('<a id="'+str(id)+'"></a>')
    h.write('<br><br>')
    h.write(z[:-3]+'<br>')
    h.write('''<pre>
<code class=" language-python">''')
    h.writelines(contents(z))
    h.write('''<br>
</code>
</pre>''')

h.write('''<script src="prism.js"></script>
</body>
</html>''')
h.close()