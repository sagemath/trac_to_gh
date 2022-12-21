# Issue 3947: readline and ipython

Issue created by migration from Trac.

Original creator: dphilp

Original creation time: 2008-08-25 07:04:19

Assignee: tbd

When built with --enable-framework, python doesn't produce a file 
` local/lib/python2.5/lib-dynload/readline.so `
because it doesn't find libreadline.dylib.

The reason for that is that with enable-framework, python doesn't look in the SAGE_LOCAL/include and SAGE_LOCAL/lib directories.  mabshoff reckons this is a generic issue.

spkg-install requires the following:

```
LDFLAGS="-L/Users/dphilp/sage-3.0.3fo/local/lib $LDFLAGS"
export LDFLAGS

CPPFLAGS="-I/Users/dphilp/sage-3.0.3fo/local/include $CPPFLAGS"
export CPPFLAGS
```



---

Comment by dphilp created at 2008-08-25 07:04:37

except probly not that specific to my system.


---

Comment by mabshoff created at 2008-08-25 07:06:45

Changing assignee from tbd to mabshoff.


---

Comment by mabshoff created at 2008-08-25 07:06:45

Changing component from algebra to build.


---

Comment by mabshoff created at 2008-08-25 07:22:29

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-08-25 07:22:29

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/alpha1/python-2.5.2.p4.spkg

fixes the issue.

Cheers,

Michael


---

Comment by mhansen created at 2008-08-25 19:57:57

Looks good to me.


---

Comment by mabshoff created at 2008-08-25 20:05:44

Merged in Sage 3.1.2.alpha1


---

Comment by mabshoff created at 2008-08-25 20:05:44

Resolution: fixed
