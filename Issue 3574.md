# Issue 3574: [with patch; needs review] optimize startup time by not importing mwrank library until needed

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-07-06 22:00:40

Assignee: cwitty

BEFORE, with caching, on OS X:

```
teragon-2:mwrank was$ sage -startuptime|grep mwrank
           mwrank: 0.000 (sage.interfaces.all)
     sage.libs.mwrank.all: 0.013 (sage.libs.all)
      interface: 0.001 (sage.libs.mwrank.all)
teragon-2:mwrank was$ 
```


AFTER:

```
teragon-2:mwrank was$ sage -startuptime|grep mwrank
           mwrank: 0.000 (sage.interfaces.all)
     sage.libs.mwrank.all: 0.001 (sage.libs.all)
      interface: 0.001 (sage.libs.mwrank.all)
```



---

Attachment

This applies and passes tests in sage/libs/mwrank/ for me.


---

Comment by mabshoff created at 2008-07-07 02:35:13

Merged in Sage 3.0.4.alpha2


---

Comment by mabshoff created at 2008-07-07 02:35:13

Resolution: fixed
