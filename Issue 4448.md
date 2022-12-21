# Issue 4448: easy-to-fix (?) bug in interact with matrices

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-11-05 20:06:02

Assignee: itolkov

Try this interact in the notebook:

```
`@`interact
def f(n=matrix([This is the Trac macro *pi^2* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#pi^2-macro))):
    print n
```


Notice that the matrix input appears empty.  What is happening, I think, is that
str(...) is being called on each entry instead of repr(...) which causes uses of ASCII art.   It seems this is a problem only for matrices.


---

Attachment

Indeed, that was the problem.


---

Comment by mhansen created at 2008-11-08 05:19:56

Looks good.


---

Comment by mabshoff created at 2008-11-08 07:10:15

Merged in Sage 3.2.rc0


---

Comment by mabshoff created at 2008-11-08 07:10:15

Resolution: fixed
