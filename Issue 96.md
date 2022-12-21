# Issue 96: time command doesn't work in .sage files !?

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-09-29 03:18:33

Assignee: was


```
> computed is for m=1001.  In testing the function I found something  
> strange and maybe you can explain this.  The following code works fine  
> when I type it into the terminal.
>
> m=201
> time chi.bernoulli(m)
> time bernq(m, chi)
>
> But when I try to load this code from a .SAGE file, I get an error.  Any  
> suggestions?

Here's a temporary work-around.  Get rid of the "time" commands.  
Use something like this instead:

t = cputime()
print chi.bernoulli(m)

etc.

That said, I consider this a bug, and will post it to the tracker. 

William
```


Example code:


```
sha:~/tmp was$ more a.sage
time 2*3
sha:~/tmp was$ sage a.sage
  File "a.py", line 3
    time Integer(2)*Integer(3)
               ^
SyntaxError: invalid syntax
```



---

Comment by was created at 2007-01-19 11:29:27

Fixed.


```

# HG changeset patch
# User William Stein <wstein`@`gmail.com>
# Date 1169206024 28800
# Node ID 8833f0a4a8e04425abe51cd6bb2f74530cbc81e1
# Parent  854831432a611d7c3591506c59037c5c22b08897
Fix trac #96 -- time works for scripts.

diff -r 854831432a61 -r 8833f0a4a8e0 sage/misc/interpreter.py
--- a/sage/misc/interpreter.py  Fri Jan 19 03:20:10 2007 -0800
+++ b/sage/misc/interpreter.py  Fri Jan 19 03:27:04 2007 -0800
`@``@` -363,7 +363,7 `@``@` def process_file(name):
     name2 = "%s/%s.py"%(dir,name[:name.find('.')])
     os.chdir(dir)
     contents = open(name).read()
-    parsed = preparse_file(contents, attached) 
+    parsed = preparse_file(contents, attached, do_time=True) 
     os.chdir(cur)
     W = open(name2,'w')
     W.write('#'*70+'\n')
diff -r 854831432a61 -r 8833f0a4a8e0 sage/server/notebook/worksheet.py
--- a/sage/server/notebook/worksheet.py Fri Jan 19 03:20:10 2007 -0800
+++ b/sage/server/notebook/worksheet.py Fri Jan 19 03:27:04 2007 -0800
`@``@` -849,7 +849,7 `@``@` class Worksheet:
         return t
 
     def preparse(self, s):
-        s = preparse_file(s, magic=False, do_time=False,
+        s = preparse_file(s, magic=False, do_time=True,
                           ignore_prompts=False)
         return s

```



---

Comment by was created at 2007-01-19 11:29:27

Resolution: fixed
