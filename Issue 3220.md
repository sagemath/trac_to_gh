# Issue 3220: [with patch; needs review] readline -- fix a couple of issues

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-05-16 14:39:03

Assignee: mabshoff

This is what is fixed by this spkg:

```
  * /usr/bin/env bash;  change == to =; add support for cygwin; improve error messages and checking
```


The spkg is here:

http://sage.math.washington.edu/home/was/cygwin/gmp-4.2.2.spkg


---

Comment by mhansen created at 2008-05-17 09:00:37

This spkg builds fine for me under cygwin.


---

Comment by mabshoff created at 2008-05-18 12:40:11

Positive review. It builds fine for me on several platforms. I did fix up SPKG.txt to conform with the new formatting rules.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-18 12:40:22

Merged in Sage 3.0.2.alpha1


---

Comment by mabshoff created at 2008-05-18 12:40:22

Resolution: fixed
