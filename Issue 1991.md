# Issue 1991: PSage -- (parallel sage): every time you create a new psage object, the first view shows it as not finished, but it is!

Issue created by migration from https://trac.sagemath.org/ticket/1991

Original creator: was

Original creation time: 2008-01-31 04:19:51

Assignee: was


```
sage: s = PSage()
sage: a = s('2+2')
sage: a   # wait 10 seconds and press return
<<currently executing code>>
sage: a
4
sage: s = PSage()
sage: a = s('2+2'); s = str(a); a
4
```


Notice above that the first output of a says current executing, but that is wrong.
In the second, we query a, and display it and it is already done very quickly. 
