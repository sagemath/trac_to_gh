# Issue 189: bug in text output for notebook

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-01-12 22:15:34

Assignee: boothby

This input to a notebook cell:


```
if gap('1+1 = 3'): 
    print "it is true"
else:
    print "it is false"
///
it is false
```


Click on "text" and get this out, which is wrong:


```
sage: if gap('1+1 = 3'): 
...    print "it is true"
...
sage: else:
...    print "it is false"
it is false
```


It should be:

```
            sage: if gap('1+1 = 3'): 
            ...    print "it is true"
            ... else:
            ...    print "it is false"
            it is false
```



---

Comment by was created at 2007-01-19 11:22:38

Resolution: fixed


---

Comment by was created at 2007-01-19 11:22:38

Fixed

```
# HG changeset patch
# User William Stein <wstein`@`gmail.com>
# Date 1169205610 28800
# Node ID 854831432a611d7c3591506c59037c5c22b08897
# Parent  21687c50ad918c8af09e6338ea5835c19a43f819
Fix trac #189 -- bug in text formatting for notebook for if / else block.

diff -r 21687c50ad91 -r 854831432a61 sage/server/notebook/cell.py
--- a/sage/server/notebook/cell.py      Fri Jan 19 03:11:10 2007 -0800
+++ b/sage/server/notebook/cell.py      Fri Jan 19 03:20:10 2007 -0800
`@``@` -150,7 +150,7 `@``@` class Cell(Cell_generic):
         pr = 'sage: '
             
         if prompts:
-            input_lines = input_lines.split('\n')
+            input_lines = input_lines.splitlines()
             has_prompt = False
             if pr == 'sage: ':
                 for v in input_lines:
`@``@` -170,9 +170,12 `@``@` class Cell(Cell_generic):
                     if len(v) == 0:
                         pass
                     #    s += '<BLANKLINE>\n'
-                    elif v[0] == ' ':
+                    elif len(v.lstrip()) != len(v):  # starts with white space
                         in_loop = True
                         s += '...' + v + '\n'
+                    elif v[:5] == 'else:':
+                        in_loop = True
+                        s += '... ' + v + '\n'
                     else:
                         if in_loop:
                             s += '...\n'
`@``@` -184,7 +187,7 `@``@` class Cell(Cell_generic):
         if prompts:
             msg = 'Traceback (most recent call last):'
             if self.__out.strip()[:len(msg)] == msg:
-                v = self.__out.strip().split('\n')
+                v = self.__out.strip().splitlines()
                 w = [msg, '...']
                 for i in range(1,len(v)):
                     if not (len(v[i]) > 0 and v[i][0] == ' '):
`@``@` -469,7 +472,7 `@``@` class Cell(Cell_generic):
                  </div>
               """%(id, id)
 
-        r = len(t.split('\n'))
+        r = len(t.splitlines())
             
         s += """
            <textarea class="%s" rows=%s cols=100000 columns=100000
`@``@` -569,7 +572,7 `@``@` def format_exception(s0, ncols):
     if ncols > 0:
         s = s.strip()
         s = s.replace('Traceback (most recent call last)','Exception (click to the left for traceback)')
-        w = s.split('\n')
+        w = s.splitlines()
         s = w[0] + '\n...\n' + w[-1]
     else:
         s = s.replace("exec compile(ur'","")
diff -r 21687c50ad91 -r 854831432a61 sage/server/notebook/server.py
--- a/sage/server/notebook/server.py    Fri Jan 19 03:11:10 2007 -0800
+++ b/sage/server/notebook/server.py    Fri Jan 19 03:20:10 2007 -0800
`@``@` -594,7 +594,6 `@``@` class WebServer(BaseHTTPServer.BaseHTTPR
             path = '%s/%s'%(os.path.abspath(notebook.object_directory()), path)
         else:
             path = path[1:]
-        print "path = '%s'"%path
         if path[-5:] == '.html' and not '/' in path and not '/jsmath' in path:
             worksheet_filename = path[:-5]
             if worksheet_filename == '__history__':
```

