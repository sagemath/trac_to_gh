# Issue 3243: [with patch; needs review] cygwin -- get it to work on cygwin

Issue created by migration from https://trac.sagemath.org/ticket/3243

Original creator: was

Original creation time: 2008-05-17 20:44:59

Assignee: mabshoff

Wrap log2 in a function so it will work in cygwin.  In cygwin log2 is a macro:

```
sh-3.2$ grep log2 *.h
math.h:#define log2(x) (log (x) / M_LOG2_E)
math.h:#define log2f(x) (logf (x) / (float) M_LOG2_E)
```




---

Attachment

The same issue pops up on Solaris 9. Solaris 10 is fine.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-18 12:30:38

Patch is good, positive review. With the patch applied doctests pass.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-18 12:30:52

Merged in Sage 3.0.2.alpha1


---

Comment by mabshoff created at 2008-05-18 12:30:52

Resolution: fixed
