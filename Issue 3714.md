# Issue 3714: add quotes to paramteres passed in lisp and clisp scripts

Issue created by migration from https://trac.sagemath.org/ticket/3714

Original creator: mabshoff

Original creation time: 2008-07-23 18:03:22

Assignee: mabshoff

FriCAS calls clisp with multiple parameters, i.e. there are spaces involved. Wrapping $`@` in quotes solves the problem. This is required to fix the optional FriCAS 1.0.3.spkg.

The patch was provided by Waldek Hebisch.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-23 18:44:12

William opened #3715, so I am closing this as a dupe because of the better description at his ticket.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-23 18:44:12

Resolution: duplicate
