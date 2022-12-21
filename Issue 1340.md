# Issue 1340: %cython seriously broken

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2007-11-29 13:27:45

Assignee: robertwb

Try this from the notebook:


```
%cython

def foo(e,f):
  return e*f
```


and you'll get:


```
Traceback (most recent call last):    
  File "/home/malb/SAGE/local/lib/python2.5/site-packages/sage/server/support.py", line 303, in cython_import_all
    create_local_c_file=create_local_c_file)
  File "/home/malb/SAGE/local/lib/python2.5/site-packages/sage/server/support.py", line 284, in cython_import
    create_local_c_file=create_local_c_file)
  File "/home/malb/SAGE/local/lib/python2.5/site-packages/sage/misc/cython.py", line 220, in cython
    raise RuntimeError, "Error converting %s to C:\n%s\n%s"%(filename, log, err)
RuntimeError: Error converting /home/malb/Texte/Talks/20071129 - SAGE - Paris/sage_notebook/worksheets/admin/2/code/sage47.spyx to C:

Cython (http://cython.org) is a compiler for code written in the
Cython language.  Cython is based on Pyrex by Greg Ewing.

Usage: cython [options] sourcefile.pyx ...

Options:
  -v, --version                  Display version number of cython compiler
  -l, --create-listing           Write error messages to a listing file
  -I, --include-dir <directory>  Search for include files in named directory
                                 (multiply include directories are allowed).
  -o, --output-file <filename>   Specify name of generated C file
  -p, --embed-positions          If specified, the positions in Cython files of each
                                 function definition is embedded in its docstring.
  -z, --pre-import <module>      If specified, assume undeclared names in this 
                                 module. Emulates the behavior of putting 
                                 "from <module> import *" at the top of the file. 
  --incref-local-binop           Force local an extra incref on local variables before
                                 performing any binary operations.
  -D, --no-docstrings            Remove docstrings.
  -a, --annotate                 Produce an colorized version of the source.
```



---

Comment by was created at 2007-11-29 14:21:05

I cannot replicate this at all.   %cython works fine for me in sage-2.8.14, at least on osx.  and definitely works fine in 2.8.13 in linux.  And there has been no change to related code that I can think of.


```
 raise RuntimeError, "Error converting %s to C:\n%s\n%s"%(filename, log, err)
```


What's with the C: -- looks suspicious.


---

Comment by malb created at 2007-11-29 14:35:02

Resolution: invalid


---

Comment by malb created at 2007-11-29 14:35:02

> What's with the C: -- looks suspicious.

It's not the driver letter C but, "convert to C" ... and then colon to show what when wrong.

Anyway, I'll invalidate it for now.


---

Comment by malb created at 2007-11-29 14:40:33

The problem actually is, that %cython doesn't work well with directory names containing spaces.


---

Comment by malb created at 2007-11-29 14:40:33

Changing status from closed to reopened.


---

Comment by malb created at 2007-11-29 14:40:33

Resolution changed from invalid to 


---

Attachment


---

Comment by mabshoff created at 2007-12-14 04:15:39

Looks good to me.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-14 05:14:38

Resolution: fixed


---

Comment by mabshoff created at 2007-12-14 05:14:38

Merged in 2.9.alpha7.
