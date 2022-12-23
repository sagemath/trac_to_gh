# Issue 1366: speed up "sage -br" -- make it cache the dependency diagram instead of computing it every time

Issue created by migration from https://trac.sagemath.org/ticket/1366

Original creator: was

Original creation time: 2007-12-02 06:15:13

Assignee: was

If you do "sage -br" on a very very fast machine, it still takes nearly
10 seconds.  This is in a sense a bug, because it should take < 0.4 seconds.
It takes a long time, since the entire dependency graph for all .pyx files
is being computed every single time.  This information should somehow be cached,
which would vastly speed things up. 

I consider this a bug since the performance is so bad as to make "sage -br"
very painful. 


---

Comment by moretti created at 2007-12-03 05:48:16

I modified setup.py to cache dependency information. It would be nice to get some people who are modifying a lot of cython code right now to test it out and report any bugs; the modifications seem to work for me but they need to be tested a bunch.


---

Comment by moretti created at 2007-12-03 05:50:39

(the information is cached in SAGE_DEVEL/sage/.cython_dependencies)


---

Comment by moretti created at 2007-12-03 06:00:30

the actual patch


---

Attachment

note - there are lots of bugs with the current version. I will work on fixing them on 12/3, but probably not before.
-Bobby


---

Attachment

Ignore the deps* stuff that bobby posted above, and just use this patch (or later ones?)


---

Attachment


---

Comment by mabshoff created at 2007-12-10 05:30:30

Resolution: fixed


---

Comment by mabshoff created at 2007-12-10 05:30:30

Merged trac1366.patch in 2.9.alpha3.


---

Comment by mabshoff created at 2007-12-10 23:43:35

Changing status from closed to reopened.


---

Comment by mabshoff created at 2007-12-10 23:43:35

Resolution changed from fixed to 


---

Comment by mabshoff created at 2007-12-10 23:43:35

This patch has two issues:

 * adding new files breaks it (fixed by #1453)
 * sage -ba is broken, probably because time stamps on files are not considered.

This is out for 2.9, but please resubmit after fixing in the next round.

Cheers,

Michael


---

Comment by moretti created at 2008-02-08 02:41:58

I reimplemented this from the ground up, hopefully correctly this time. There is still room for improvement, but the dependency graph computation happens nearly instantly now (on my laptop).


---

Comment by cwitty created at 2008-02-08 02:55:09

The patch in deps2.hg seems to ignore .pxi files.  (I modified sage/rings/mpfi.pxi, and then did "sage -b", and nothing got recompiled.)


---

Comment by moretti created at 2008-02-08 04:11:29

Changed the status so the bugfix could get a review.


---

Comment by cwitty created at 2008-02-08 04:55:40

The same testcase still fails (but in a different way now).  When I touch sage/rings/mpfi.pxi, and then run "sage -b", it now dumps me into a debugger.  Then, when I press Ctrl-D to exit the debugger, I get a backtrace.

```
cwitty@magnetar:~/sage-2.10.1$ ./sage -b

----------------------------------------------------------
sage: Building and installing modified SAGE library files.


Installing c_lib
scons: `install' is up to date.
> /home/cwitty/sage-2.10.1/devel/sage-review2/setup.py(1040)search_all_includes()
-> C = [x.strip() for x in S if 'cimport' in x]
(Pdb) 
Traceback (most recent call last):
  File "setup.py", line 1155, in <module>
    deps = create_deps(ext_modules)
  File "setup.py", line 1146, in create_deps
    deps_graph(deps, f, visited)
  File "setup.py", line 1113, in deps_graph
    this_deps = search_all_includes(f)
  File "setup.py", line 1040, in search_all_includes
    C = [x.strip() for x in S if 'cimport' in x]
  File "setup.py", line 1040, in search_all_includes
    C = [x.strip() for x in S if 'cimport' in x]
  File "/home/cwitty/sage-2.10.1/local/lib/python2.5/bdb.py", line 48, in trace_dispatch
    return self.dispatch_line(frame)
  File "/home/cwitty/sage-2.10.1/local/lib/python2.5/bdb.py", line 67, in dispatch_line
    if self.quitting: raise BdbQuit
bdb.BdbQuit
sage: There was an error installing modified sage library code.
```



---

Comment by moretti created at 2008-02-08 05:49:33

removed debug statements :)


---

Attachment


---

Comment by cwitty created at 2008-02-09 21:09:35

Looks good.

I tried the following tests: touch a .pxi file, then rebuild; touch a .pxd file, then rebuild; touch a .pyx file, then rebuild; rebuild everything with "sage -ba"; create a new .pyx file, then rebuild.  All of these tests passed.

Apply only deps2.hg


---

Comment by mabshoff created at 2008-02-10 01:26:31

Resolution: fixed


---

Comment by mabshoff created at 2008-02-10 01:26:31

Merged deps2.hg in Sage 2.10.2.alpha0
