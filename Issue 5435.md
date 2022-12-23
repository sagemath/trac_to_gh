# Issue 5435: [with patch, needs review] sage-ptest "Using cached timings." message could be better

Issue created by migration from https://trac.sagemath.org/ticket/5435

Original creator: cwitty

Original creation time: 2009-03-04 04:07:39

Assignee: cwitty

The attached patch changes the message from

```
Using cached timings.
```

to

```
Using cached timings to run slower doctests first.
```


Hopefully this is enough to explain the otherwise surprising long pause at the beginning of parallel testing runs.


---

Attachment


---

Comment by mhansen created at 2009-03-04 04:39:09

Looks good to me.  It took me a second to figure out what this meant when I first encountered it.


---

Comment by mabshoff created at 2009-03-04 05:44:35

Mhh, I think this needs fixing, but I think `slower` is the wrong term here. Maybe `longer` is better? Either way I want this patch to go in, but if there is a consensus I would be happy to change the patch.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-10 23:13:45

Merged in Sage 3.4.final.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-10 23:13:45

Resolution: fixed
