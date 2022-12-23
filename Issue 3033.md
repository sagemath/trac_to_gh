# Issue 3033: equations.py segfaults without --incref-local-binop cython flag

Issue created by migration from https://trac.sagemath.org/ticket/3033

Original creator: gfurnish

Original creation time: 2008-04-26 22:15:19

Assignee: was

If sage is compiled without the --incref-local-binop for Cython, calculus/equations.py segfaults.


---

Comment by gfurnish created at 2008-04-26 22:21:20

This uses a) Pbuild B) Upstream, patched, Cython.  Furthermore it is a heisenbug (although one that happens most of the time)


---

Comment by mabshoff created at 2008-04-26 22:24:23

No dice. Invalid for now since:

```
[23:37] <mabshoff> I am not sure if #3033 is valid.
[23:37] <mabshoff> At least not in its current form.
[23:37] <gfurnish> Yeah lets invalid that
[23:37] <mabshoff> Wait.
[23:37] <mabshoff> You need to add the fact that 
[23:37] <mabshoff> a) you use pbuild
[23:37] <mabshoff> b) you use an *upstream* *patched* Cython
[23:37] <mabshoff> So it isn't something that we can debug
[23:38] <mabshoff> It might still be valid, so let's keep it open.
[23:38] <mabshoff> I.e. once the updated cython is in-tree is in it might  come up again.
[23:38] <mabshoff> But then we use --incref-local-binop per default anyway?
[23:39] <gfurnish> yeah..
[23:39] <mabshoff> So, in the end?
[23:39] <mabshoff> Let's go with invalid for now. I am closing it with this conversation pasted in the comment.
[23:39] <mabshoff> Alright?
[23:40] <mabshoff> And you never know what happens if you do a complete rebuild of Sage.
[23:40] <mabshoff> That tends to cause fixes for Heisenbugs.
[23:40] <gfurnish> ok
[23:40] <gfurnish> this is with multiple full rebuilds
[23:40] <mabshoff> ok
[23:41] <mabshoff> Well, if we hit it again we can reopen.
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-04-26 22:24:23

Resolution: invalid
