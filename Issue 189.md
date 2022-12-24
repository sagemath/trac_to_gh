# Issue 189: bug in text output for notebook

archive/issues_000189.json:
```json
{
    "body": "Assignee: boothby\n\nThis input to a notebook cell:\n\n\n```\nif gap('1+1 = 3'): \n    print \"it is true\"\nelse:\n    print \"it is false\"\n///\nit is false\n```\n\n\nClick on \"text\" and get this out, which is wrong:\n\n\n```\nsage: if gap('1+1 = 3'): \n...    print \"it is true\"\n...\nsage: else:\n...    print \"it is false\"\nit is false\n```\n\n\nIt should be:\n\n```\n            sage: if gap('1+1 = 3'): \n            ...    print \"it is true\"\n            ... else:\n            ...    print \"it is false\"\n            it is false\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/189\n\n",
    "created_at": "2007-01-12T22:15:34Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-1.8",
    "title": "bug in text output for notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/189",
    "user": "was"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/189





---

archive/issue_comments_000856.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-01-19T11:22:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/189#issuecomment-856",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_000857.json:
```json
{
    "body": "Fixed\n\n```\n# HG changeset patch\n# User William Stein <wstein@gmail.com>\n# Date 1169205610 28800\n# Node ID 854831432a611d7c3591506c59037c5c22b08897\n# Parent  21687c50ad918c8af09e6338ea5835c19a43f819\nFix trac #189 -- bug in text formatting for notebook for if / else block.\n\ndiff -r 21687c50ad91 -r 854831432a61 sage/server/notebook/cell.py\n--- a/sage/server/notebook/cell.py      Fri Jan 19 03:11:10 2007 -0800\n+++ b/sage/server/notebook/cell.py      Fri Jan 19 03:20:10 2007 -0800\n@@ -150,7 +150,7 @@ class Cell(Cell_generic):\n         pr = 'sage: '\n             \n         if prompts:\n-            input_lines = input_lines.split('\\n')\n+            input_lines = input_lines.splitlines()\n             has_prompt = False\n             if pr == 'sage: ':\n                 for v in input_lines:\n@@ -170,9 +170,12 @@ class Cell(Cell_generic):\n                     if len(v) == 0:\n                         pass\n                     #    s += '<BLANKLINE>\\n'\n-                    elif v[0] == ' ':\n+                    elif len(v.lstrip()) != len(v):  # starts with white space\n                         in_loop = True\n                         s += '...' + v + '\\n'\n+                    elif v[:5] == 'else:':\n+                        in_loop = True\n+                        s += '... ' + v + '\\n'\n                     else:\n                         if in_loop:\n                             s += '...\\n'\n@@ -184,7 +187,7 @@ class Cell(Cell_generic):\n         if prompts:\n             msg = 'Traceback (most recent call last):'\n             if self.__out.strip()[:len(msg)] == msg:\n-                v = self.__out.strip().split('\\n')\n+                v = self.__out.strip().splitlines()\n                 w = [msg, '...']\n                 for i in range(1,len(v)):\n                     if not (len(v[i]) > 0 and v[i][0] == ' '):\n@@ -469,7 +472,7 @@ class Cell(Cell_generic):\n                  </div>\n               \"\"\"%(id, id)\n \n-        r = len(t.split('\\n'))\n+        r = len(t.splitlines())\n             \n         s += \"\"\"\n            <textarea class=\"%s\" rows=%s cols=100000 columns=100000\n@@ -569,7 +572,7 @@ def format_exception(s0, ncols):\n     if ncols > 0:\n         s = s.strip()\n         s = s.replace('Traceback (most recent call last)','Exception (click to the left for traceback)')\n-        w = s.split('\\n')\n+        w = s.splitlines()\n         s = w[0] + '\\n...\\n' + w[-1]\n     else:\n         s = s.replace(\"exec compile(ur'\",\"\")\ndiff -r 21687c50ad91 -r 854831432a61 sage/server/notebook/server.py\n--- a/sage/server/notebook/server.py    Fri Jan 19 03:11:10 2007 -0800\n+++ b/sage/server/notebook/server.py    Fri Jan 19 03:20:10 2007 -0800\n@@ -594,7 +594,6 @@ class WebServer(BaseHTTPServer.BaseHTTPR\n             path = '%s/%s'%(os.path.abspath(notebook.object_directory()), path)\n         else:\n             path = path[1:]\n-        print \"path = '%s'\"%path\n         if path[-5:] == '.html' and not '/' in path and not '/jsmath' in path:\n             worksheet_filename = path[:-5]\n             if worksheet_filename == '__history__':\n```\n",
    "created_at": "2007-01-19T11:22:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/189#issuecomment-857",
    "user": "was"
}
```

Fixed

```
# HG changeset patch
# User William Stein <wstein@gmail.com>
# Date 1169205610 28800
# Node ID 854831432a611d7c3591506c59037c5c22b08897
# Parent  21687c50ad918c8af09e6338ea5835c19a43f819
Fix trac #189 -- bug in text formatting for notebook for if / else block.

diff -r 21687c50ad91 -r 854831432a61 sage/server/notebook/cell.py
--- a/sage/server/notebook/cell.py      Fri Jan 19 03:11:10 2007 -0800
+++ b/sage/server/notebook/cell.py      Fri Jan 19 03:20:10 2007 -0800
@@ -150,7 +150,7 @@ class Cell(Cell_generic):
         pr = 'sage: '
             
         if prompts:
-            input_lines = input_lines.split('\n')
+            input_lines = input_lines.splitlines()
             has_prompt = False
             if pr == 'sage: ':
                 for v in input_lines:
@@ -170,9 +170,12 @@ class Cell(Cell_generic):
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
@@ -184,7 +187,7 @@ class Cell(Cell_generic):
         if prompts:
             msg = 'Traceback (most recent call last):'
             if self.__out.strip()[:len(msg)] == msg:
-                v = self.__out.strip().split('\n')
+                v = self.__out.strip().splitlines()
                 w = [msg, '...']
                 for i in range(1,len(v)):
                     if not (len(v[i]) > 0 and v[i][0] == ' '):
@@ -469,7 +472,7 @@ class Cell(Cell_generic):
                  </div>
               """%(id, id)
 
-        r = len(t.split('\n'))
+        r = len(t.splitlines())
             
         s += """
            <textarea class="%s" rows=%s cols=100000 columns=100000
@@ -569,7 +572,7 @@ def format_exception(s0, ncols):
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
@@ -594,7 +594,6 @@ class WebServer(BaseHTTPServer.BaseHTTPR
             path = '%s/%s'%(os.path.abspath(notebook.object_directory()), path)
         else:
             path = path[1:]
-        print "path = '%s'"%path
         if path[-5:] == '.html' and not '/' in path and not '/jsmath' in path:
             worksheet_filename = path[:-5]
             if worksheet_filename == '__history__':
```

