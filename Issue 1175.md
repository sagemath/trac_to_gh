# Issue 1175: circular link in sage/local/lib/python2.5

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2007-11-15 08:27:09

Assignee: mabshoff

When building sage-2.8.12, there are two circular links in sage/local/lib/python2.5:

```
achille% pwd
/net/achille/localdisk/zimmerma/sage-2.8.12/local/lib/python2.5
achille% ls -l pyt*
lrwxrwxrwx 1 zimmerma spaces 6 2007-11-14 09:53 python -> python
lrwxrwxrwx 1 zimmerma spaces 9 2007-11-14 09:53 python2.5 -> python2.5
```



---

Comment by mabshoff created at 2007-11-21 22:20:49

I thought we did fix that a while ago. Kate did report at least a similar issue. I will look into this in this release cycle.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-19 07:40:53

Ok, while we fixed the issue in the python.spkg itself the same problem pops up when we install the mercurial.spkg. The spkg at

http://sage.math.washington.edu/home/mabshoff/mercurial-0.9.5.p0.spkg

fixes that issue and actually creates an hg repo inside the spkk as well as does some general cleanup. Another python based spkg might still recreate those links, so this might not be over yet.

Cheers,

Michael


---

Comment by rlm created at 2007-12-19 19:08:01

Resolution: fixed


---

Comment by rlm created at 2007-12-19 19:08:01

Merged in Sage 2.9.1 alpha2
