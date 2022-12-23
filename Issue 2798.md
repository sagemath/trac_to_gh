# Issue 2798: probably easy-to-fix ptest issue

Issue created by migration from https://trac.sagemath.org/ticket/2798

Original creator: was

Original creation time: 2008-04-04 16:57:05

Assignee: gfurnish


```
09:56 < wstein> I just got this from ptest:
09:56 -!- Irssi: Pasting 5 lines to #sage-devel. Press Ctrl-K if you wish to do this or Ctrl-C to cancel.
09:56 < wstein>   File "/Users/was/build/sage-2.10.4/local/bin/sage-ptest", line 74, in run
09:56 < wstein>     if e==-2:
09:56 < wstein> UnboundLocalError: local variable 'e' referenced before assignment
09:56 < wstein>  
09:56 < wstein> but then it worked...
```



---

Attachment


---

Comment by gfurnish created at 2008-04-04 18:47:37

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-04-04 19:54:06

Patch looks good to me. It doesn't really address the issue wstein encountered, but it will print a proper error message the next time somebody hits the bug that caused the problem in the first place. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-04 19:54:59

Resolution: fixed


---

Comment by mabshoff created at 2008-04-04 19:54:59

Merged in Sage 3.0.alpha1
