# Issue 1067: moin moin wiki in sage -- 2 updates needs

Issue created by migration from https://trac.sagemath.org/ticket/1067

Original creator: was

Original creation time: 2007-11-02 18:22:05

Assignee: was

1. It should say "Moin Moin wiki with math typesetting" (this will be trivial to fix).


```
Tombo:tmp was$ sage -wiki
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.10, Release Date: 2007-10-28                      |
| Type notebook() for the GUI, and license() for information.        |
Please wait while the SAGE Notebook server starts...

```


2. Spam filtering should be on by default and anon access off.
I.e., the wikiconfig file *should* look like the attached one.
This should be easy to fix, once somebody remembers where the
default wikiconfig.py file is in the sage install.

William


---

Comment by was created at 2007-11-03 15:33:52

Maybe also


---

Comment by was created at 2007-11-03 23:47:31

1) is fixed and pushed out.


---

Comment by was created at 2007-11-04 00:02:20

patch pushed out and updated moin spkg posted to
   http://sage.math.washington.edu/tmp/


---

Comment by was created at 2007-11-04 00:02:20

Resolution: fixed
