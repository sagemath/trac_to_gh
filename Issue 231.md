# Issue 231: inconsistent working directory

Issue created by migration from Trac.

Original creator: nbruin

Original creation time: 2007-01-29 19:26:02

Assignee: boothby

Between executing a cell for the first time and then reexecuting that cell, the "current directory" changes:

```
%sh
pwd
```

the first time gives the "home directory"

```
/usr/local/sage/nobody
```

upon reexecution I get

```
/usr/local/sage/nobody/sage_notebook/worksheets/loaderror/cells/2
```

i.e., the cell directory.


---

Comment by was created at 2007-08-29 02:37:17

this fixes the bug (and more)


---

Attachment


---

Comment by was created at 2007-08-29 02:37:55

Resolution: fixed
