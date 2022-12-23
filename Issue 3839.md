# Issue 3839: Element access for RElement

Issue created by migration from https://trac.sagemath.org/ticket/3839

Original creator: SimonKing

Original creation time: 2008-08-13 17:29:17

Assignee: SimonKing

Keywords: r interface, element access

On [http://groups.google.com/group/sage-support/browse_thread/thread/4868d601510e9642?hl=en](http://groups.google.com/group/sage-support/browse_thread/thread/4868d601510e9642?hl=en), Alexandr Batalshikov pointed out that

```
> v = c(3,5,9,1)
> v[c(2,3)]
[1] 5 9 
```

works in R, but the corresponding statement in Sage does not:

```
sage: v = r.c(3,5,9,1)
sage: n = r.c(2,3)
sage: v[n]
[1] 3
```


I believe this is a defect. With the attached patch, the following works:

```
sage: v = r.c(3,5,9,1)
sage: n = r.c(2,3)
sage: v[n]
[1] 5 9
sage: v[-2]
[1] 3 9 1
sage: v['c(2,3)']
[1] 5 9
sage: v[2,4,3]
[1] 5 1 9
sage: v[2]
[1] 5
```




---

Attachment

Patch relative to 3.1.alpha0


---

Comment by mabshoff created at 2008-08-13 17:30:55

Resolution: duplicate


---

Comment by mabshoff created at 2008-08-13 17:30:55

This is a dupe of #3838.

Cheers,

Michael
