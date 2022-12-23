# Issue 2884: notebook -- bug; @interact cell eval doesn't clear out the old html output (easy to fix?)

Issue created by migration from https://trac.sagemath.org/ticket/2884

Original creator: was

Original creation time: 2008-04-11 23:50:22

Assignee: boothby




---

Attachment


---

Comment by boothby created at 2008-05-12 05:48:52

The following is now broken:


```
plot(sin,0,1).show()
@interact
def foo(a="1"):
    a
```



---

Comment by was created at 2008-05-15 05:21:33

Hi,

Your only reason for giving a negative review was a claim that

```
plot(sin,0,1).show()
@interact
def foo(a="1"):
    a
```

is now "broken".  However, this never did what you thought it
did.  The behavior in fact hasn't changed at all from how it was
before, except to remove the bug where old graphics from
the previous version of the cell remained. 

`@`interact *by design* is only supposed to work when it is
the only thing in a cell. 

Having multiple interacts in a cell, having additional graphics in
a cell, having nested interacts -- none of that should work at present,
since none of it has been implemented. 
They're all things that would possibly be very nice to implement,
but they were not part of the design goals for the first version
of interact.


---

Attachment


---

Comment by boothby created at 2008-05-15 06:04:30

It was not clear to me, even upon rereading the documentation, that `@`interact had to be alone in a cell.  The attached "fixes" the issue.  :)


---

Comment by mabshoff created at 2008-05-17 18:45:22

Merged both patches in Sage 3.0.2.alpha1


---

Comment by mabshoff created at 2008-05-17 18:45:22

Resolution: fixed
