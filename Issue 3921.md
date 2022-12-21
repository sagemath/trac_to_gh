# Issue 3921: calculus -- solve(..., constant) should complain by default

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-08-21 15:18:05

Assignee: gfurnish


```
> One thing I came across is, that symbolic expressions with predefined
> variables (i.e. they are not variables) confuse someone when used in
> functions.
> for example
> x = 5
> solve([x^2==3], x)
> then solve does nothing. I think, because there is an explicit x, it
> would be nice to have at least a warning message telling the user that
> x is not a symbolic variable, but already assigned.
>

This is an extremely good idea and trivial to implement.  

William
```





---

Attachment


---

Comment by jwmerrill created at 2008-08-31 21:26:59

This patch makes sage raise a TypeError in the case mentioned above, and adds relevant doctests.


---

Comment by AlexGhitza created at 2008-09-01 10:43:24

Looks good to me.


---

Comment by mabshoff created at 2008-09-01 13:02:23

Merged in Sage 3.1.2.alpha4


---

Comment by mabshoff created at 2008-09-01 13:02:23

Resolution: fixed
