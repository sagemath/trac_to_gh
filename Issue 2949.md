# Issue 2949: change slightly the docstring for assume (utterly trivial)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-18 00:24:13

Assignee: was

Change the output of assume? to:


```
sage: from sage.calculus.calculus import maxima as calcmaxima
sage: calcmaxima.eval('declare(n,integer)')
```


to


```
sage: sage.calculus.calculus.maxima.eval('declare(n,integer)')
```



---

Comment by mhansen created at 2008-04-18 06:10:12

Changing assignee from was to mhansen.


---

Attachment


---

Comment by mhansen created at 2008-04-18 06:10:12

Changing status from new to assigned.


---

Comment by dfdeshom created at 2008-04-18 19:04:56

Looks good to me.


---

Comment by mabshoff created at 2008-04-18 20:19:06

Resolution: fixed


---

Comment by mabshoff created at 2008-04-18 20:19:06

Merged in Sage 3.0.alpha6
