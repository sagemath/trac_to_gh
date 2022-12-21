# Issue 1453: [with patch, positive review] fix cython dependency computation for new files

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-12-10 21:35:48

Assignee: was


```
Building sage/structure/coerce.c because it depends on sage/structure/
coerce.pyx.
cython --embed-positions --incref-local-binop -I/tmp/Work-mabshoff/
release-cycles-2.9/sage-2.9.alpha4/devel/sage-main -o sage/structure/
coerce.c sage/structure/coerce.pyx
Traceback (most recent call last):
  File "setup.py", line 1124, in <module>
    cython(ext_modules)
  File "setup.py", line 1111, in cython
    new_sources += process_cython_file(f, m, deps_of)
  File "setup.py", line 1061, in process_cython_file
    if need_to_cython(f, outfile, deps_of):
  File "setup.py", line 1035, in need_to_cython
    if os.path.exists(pxd) and check_dependencies(pxd, outfile, deps):
  File "setup.py", line 1011, in check_dependencies
    deps = deps_of[filename]
KeyError: 'sage/rings/polynomial/pbori.pxd'
sage: There was an error installing modified sage library code. 
```


Cheers,

Michael


---

Attachment

Merged in 2.9.alpha5.


---

Comment by mabshoff created at 2007-12-10 21:39:42

Resolution: fixed


---

Comment by mabshoff created at 2007-12-10 23:46:17

Since this was a fix for #1366 which I reverted also reverted this patch. It fixes some of the issues of #1366, but since `sage -ba` was completely broken I had little choice  but to revert them for now.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-10 23:46:17

Changing status from closed to reopened.


---

Comment by mabshoff created at 2007-12-10 23:46:17

Resolution changed from fixed to 


---

Comment by moretti created at 2008-02-07 05:19:33

I sent the correct patch for this now. Cython deps checking still has poor asymptotic behavior, but now is very quick.


---

Comment by mabshoff created at 2008-02-12 17:56:18

Resolution: fixed


---

Comment by mabshoff created at 2008-02-12 17:56:18

The issue was fixed by Bobby Moretti via a patch at #1366.

Cheers,

Michael
