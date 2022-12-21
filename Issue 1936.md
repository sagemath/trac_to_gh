# Issue 1936: r-2.6.1.p11: sage-check fails on OSX 10.5

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-01-26 10:41:50

Assignee: mabshoff

On bsd the following happens:

```
     missing link(s):  methods methods
  zScript                           text    html    latex   example
  zpackages                         text    html    latex   example
  zutils                            text    html    latex
  Signals                           text    html    latex
make[5]: *** [test-Examples-Base] Error 2
make[4]: *** [test-Examples] Error 2
make[3]: *** [test-all-basics] Error 1
make[2]: *** [check] Error 2
*************************************
Error testing package ** r-2.6.1.p11 **
*************************************
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-01-26 10:42:26

Changing component from packages to sage-check.


---

Comment by mabshoff created at 2008-01-26 15:58:14

The exact same issue happens on sage.math.

Cheers,

Michael


---

Comment by mvngu created at 2010-02-02 07:01:46

Resolution: wontfix


---

Comment by mvngu created at 2010-02-02 07:01:46

As of Sage 4.3.2 (see #6532), the R spkg has been upgraded to version 2.10.1. I'm closing this ticket as wontfix. If the testsuite of R 2.10.1 fails, one needs to open a ticket for that.
