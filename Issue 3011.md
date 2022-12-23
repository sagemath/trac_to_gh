# Issue 3011: Set R_HOMES properly so rpy works with an existing R installed

Issue created by migration from https://trac.sagemath.org/ticket/3011

Original creator: mabshoff

Original creation time: 2008-04-23 21:25:50

Assignee: mabshoff

Steve reported:

```
On my Gentoo box I unpacked the subject tarball, changed to the sage
directory and did a make with the results:

gcc version 4.1.2 (Gentoo 4.1.2 p1.0.2)
****************************************************
****************************************************
RHOMES= []
DEBUG= True
Setting RHOMES to  ['/usr/lib64/R']
RHOMES= []
DEBUG= True
Setting RHOMES to  ['/usr/lib64/R']
Traceback (most recent call last):
Traceback (most recent call last):
  File "setup.py", line 106, in <module>
  File "setup.py", line 106, in <module>
        RVERSION = rpy_tools.get_R_VERSION(RHOME, force_exec=True)
RVERSION = rpy_tools.get_R_VERSION(RHOME, force_exec=True)
  File "/local/sage-3.0/spkg/build/rpy-1.0.1.p1/src/rpy_tools.py",
line 99, in get_R_VERSION
  File "/local/sage-3.0/spkg/build/rpy-1.0.1.p1/src/rpy_tools.py",
line 99, in get_R_VERSION
        " `%s'.\n" % rexec )
" `%s'.\n" % rexec )
RuntimeErrorRuntimeError: : Couldn't execute the R interpreter `/usr/
lib64/R/bin/R'.
Couldn't execute the R interpreter `/usr/lib64/R/bin/R'.

Error building RPY -- Python interface to R.
Error building RPY -- Python interface to R.

I tried several corrective measures and the only one that allowed sage
to build was to issue:

RHOMES="`pwd`/local/lib/R" make

However, the following test failed:

sage -t  devel/sage/sage/stats/test.py 
```

Follow up:

```
Michael,

Yes I do have R installed on my system. No, RHOMES is not set;
however, R_HOMES is set to /usr/lib64/R. Apparently, the R
installation does this. And yes I do have the install.log. The
specific test fails as:

sage -t  devel/sage/sage/stats/test.py
**********************************************************************
File "/local/sage-3.0/tmp/test.py", line 5:
    sage: import rpy
Exception raised:
    Traceback (most recent call last):
      File "/local/sage-3.0/local/lib/python2.5/doctest.py", line
1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[1]>", line 1, in <module>
        import rpy###line 5:
    sage: import rpy
      File "/local/sage-3.0/local/lib/python2.5/site-packages/rpy.py",
line 58, in <m
odule>
        RVERSION = rpy_tools.get_R_VERSION(RHOME)
      File "/local/sage-3.0/local/lib/python2.5/site-packages/
rpy_tools.py", line 99,
 in get_R_VERSION
        " `%s'.\n" % rexec )
    RuntimeError: Couldn't execute the R interpreter `/usr/lib64/R/bin/
R'.

**********************************************************************
1 items had failures:
   1 of   2 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /local/sage-3.0/
tmp/.doctest_test.py
         [1.5 s]
exit code: 1024

----------------------------------------------------------------------
The following tests failed:

        sage -t  devel/sage/sage/stats/test.py
Total time for all tests: 1.5 seconds

I've built sage previously, but without R installed. I suspect the
installed (Portage) R is conflicting with what sage does. Let me know
if you wish to see the install.log. I'm presently re-building sage in
a shell where I've disabled the R_HOME variable.

Steve 
```



---

Comment by mabshoff created at 2008-04-23 21:29:08

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-05-05 03:31:54

See also #3086 about the update to R 2.7.0.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-29 11:53:31

Francois opened another ticket about the same issues at #3328. Since he also posted a patch that fixes the issue there I am closing this as a duplicate.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-29 11:53:31

Resolution: duplicate
