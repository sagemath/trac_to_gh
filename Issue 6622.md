# Issue 6622: substitution of a dict into a symbolic expression modifies the dict

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-07-25 20:05:50

Assignee: burcin


```
sage: var('v t')
sage: f = v*t
sage: D = {v: 2}
sage: f(D, t=3)
6
sage: D
{v: 2, t: 3}
```


After the call above, D should *not* be changed.


---

Comment by was created at 2009-07-25 20:07:02

Here's how to workaround it (namely, put "dict(constants)" instead of "constants").  In the code for __call__ or subs, something similar should be done. 


```
sage: var('v t')
sage: f = v*t
sage: s = {v: 2}
sage: f(dict(s), t=3)
6
sage: s
{v: 2}
```



---

Attachment

based on sage 4.1.1.alpha1


---

Comment by wcauchois created at 2009-07-29 00:44:36

This was a simple fix.


---

Comment by mvngu created at 2009-08-03 06:34:40

Resolution: fixed
