# Issue 4028: doctest and improve sage/interfaces/axiom.py

Issue created by migration from https://trac.sagemath.org/ticket/4028

Original creator: mhansen

Original creation time: 2008-09-01 02:40:26

Assignee: was




---

Attachment

One spelling error: "requires Axoim" (which Mike corrected) - other than that is passes doctests with and without Axiom installed. Mike went with me over the patch and answered questions. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-01 03:42:51

Oops, with the original axiom running the doctest with -optional results in a fork bomb :(

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-01 03:53:33

Looks like somehow the following ends up getting called:

```
sage -axiom -nox -noclef
```

If I run that from the command line it also starts a fork bomb.

Thoughts?

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-01 03:57:15

It is all William's fault:

```
mabshoff@sage:/usr/local/bin$ pwd
/usr/local/bin
mabshoff@sage:/usr/local/bin$ cat axiom 
#!/bin/sh
sage -axiom $*
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-09-01 04:13:41

Merged in Sage 3.1.2.alpha4


---

Comment by mabshoff created at 2008-09-01 04:13:41

Resolution: fixed
