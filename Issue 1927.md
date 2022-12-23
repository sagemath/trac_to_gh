# Issue 1927: dots in symbolic variable names should not be allowed, etc. (probably easy to fix)

Issue created by migration from https://trac.sagemath.org/ticket/1927

Original creator: was

Original creation time: 2008-01-25 17:21:18

Assignee: was

Variable names made with the var command should be valid identifiers, but

```
sage: var('.foo')
.foo
sage: var('.foo/x')
.foo/x
```


Thanks to janwil for pointing this out. 


---

Comment by mhansen created at 2008-02-01 03:34:42

Changing assignee from was to mhansen.


---

Attachment


---

Comment by mhansen created at 2008-02-01 03:34:42

Changing status from new to assigned.


---

Comment by ncalexan created at 2008-02-15 04:42:21

Doctests are good.  Apply.


---

Comment by mabshoff created at 2008-02-15 04:48:43

Merged in Sage 2.10.2.alpha0


---

Comment by mabshoff created at 2008-02-15 04:48:43

Resolution: fixed
