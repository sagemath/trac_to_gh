# Issue 662: Start Browser with clean environment

Issue created by migration from https://trac.sagemath.org/ticket/662

Original creator: malb

Original creation time: 2007-09-15 19:08:50

Assignee: was

If I call `sage -notebook` and Firefox/Iceweasel comes up automatically, it crashes on me with 


```
/usr/lib/iceweasel/firefox-bin: symbol lookup error: /usr/lib/libxml2.so.2: undefined symbol: gzopen64
```


when logging in.

If I start Iceweasel again afterwards, I can log in and everything works. I suspect that this behaviour is caused by the SAGE environment variables (e.g. `LD_PATH`). A fix would be to start the browser with a clean (as in pre-SAGE) environment.


---

Comment by was created at 2007-09-21 00:14:34

Post a patch to fix this, since it will be too hard for me to debug and test myself.


---

Comment by mabshoff created at 2007-10-02 21:59:51

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2007-10-02 21:59:51

Changing status from new to assigned.


---

Comment by malb created at 2007-10-05 10:09:16

a fix is attached.


---

Comment by malb created at 2007-10-05 10:09:16

Changing assignee from mabshoff to malb.


---

Comment by malb created at 2007-10-05 10:09:16

Changing status from assigned to new.


---

Attachment


---

Comment by was created at 2007-10-13 07:39:29

Resolution: fixed
