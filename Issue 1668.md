# Issue 1668: fix polybori's variable names: _P->PB_P

Issue created by migration from https://trac.sagemath.org/ticket/1668

Original creator: mabshoff

Original creation time: 2008-01-03 15:35:10

Assignee: burcin

Variable names like `_[A-Z]` cause trouble on Cygwin and Solaris. The polybori wrapper uses a couple of those. The renamed variables could be in some other for, but `_PP` also won't work. I have a patch, but since there are a bunch of other patches that touch the code and would need to be fixed wait for those to be merged before redoing this. burcin has volunteered to do this.

Cheers,

Michael


---

Attachment

rename polybori variables


---

Comment by burcin created at 2008-01-08 14:19:13

Changing status from new to assigned.


---

Comment by burcin created at 2008-01-08 14:19:13

attachment:trac_1668.patch renames the problem variables used by the `PolyBoRi` wrapper.


---

Comment by mabshoff created at 2008-01-13 17:55:40

Looks good to me.


---

Comment by mabshoff created at 2008-01-13 18:03:54

Merged in Sage 2.10.alpha3


---

Comment by mabshoff created at 2008-01-13 18:03:54

Resolution: fixed
