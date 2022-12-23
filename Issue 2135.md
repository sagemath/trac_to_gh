# Issue 2135: [with patch, needs easy review] allow for specifying initial position in spring layout

Issue created by migration from https://trac.sagemath.org/ticket/2135

Original creator: rlm

Original creation time: 2008-02-10 01:06:42

Assignee: rlm

suggested by Peter Jipsen (does he have a track account yet?)


---

Attachment

Apply.  There are no doctests, but how would one doctest this?  There is a small typo in the docstring, I think -- a missing apostrophe.


---

Comment by rlm created at 2008-02-19 22:45:37

Actually, maybe one could test it by giving it a stable initial configuration, and then "..."-ing out most of the output.


---

Comment by mabshoff created at 2008-02-25 01:38:18

Resolution: fixed


---

Attachment

Merged both patches in Sage 2.10.3.alpha0. I fixed the missing apostrophe in plot_positions_with_spring-graphs.patch.

Cheeers,

Michael
