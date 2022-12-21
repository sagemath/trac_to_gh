# Issue 3712: clisp+nohup eats ones disc

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-07-23 13:17:01

Assignee: mabshoff


```
ABORT          :R364    Abort debug loop
ABORT          :R365    Abort debug loop
ABORT          :R366    Abort debug loop
ABORT          :R367    Abort debug loop
ABORT          :R368    Abort debug loop
ABORT          :R369    Abort debug loop
ABORT          :R370    Abort debug loop
ABORT          :R371    Abort debug loop
ABORT        tee: write e
```



---

Comment by mabshoff created at 2008-07-25 10:34:51

This is likely fixed by putting William's workaround in back into spkg-install. Nils Bruin hot a likely related issue on OSX 10.4.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-29 16:00:42

The spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.6/final/clisp-2.46.p6.spkg

reintroduces the old fix from the previous spkg. Notice that this spkg also fixes #3715.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-29 16:00:42

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-07-29 16:55:45

Resolution: fixed


---

Comment by mabshoff created at 2008-07-29 16:55:45

Merged in Sage 3.0.6.final
