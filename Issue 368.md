# Issue 368: {{{ }}} for worksheet text mode won't cut it.

Issue created by migration from https://trac.sagemath.org/ticket/368

Original creator: was

Original creation time: 2007-05-18 16:12:13

Assignee: boothby

Try this


```
var('x a b')
show(solve(x^3 + c*x + b ==0, x)[0])
```


Then eval, click edit and save.
It doesn't work since the output of show
has }}} in it -- it's part of valid latex.

What are we to do?


---

Comment by was created at 2007-05-31 14:55:32

Fixed by requiring }}} to have a newline before it.  That's hackish, but better than
nothing.


---

Comment by was created at 2007-05-31 14:55:32

Resolution: fixed
