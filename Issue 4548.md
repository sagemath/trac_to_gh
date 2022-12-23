# Issue 4548: bug in latexing a certain symbolic expression

Issue created by migration from https://trac.sagemath.org/ticket/4548

Original creator: was

Original creation time: 2008-11-19 15:35:07

Assignee: cwitty

Reported by Anders in sage-devel:


```
There's a problem with powers of negative numbers the latex method for
symbolic arithmetic.
In version 3.1.4 I get this:
{{{
sage: var('n')
n
sage: latex((-1)^n)
{-1}^{n}

It should, of course, be {(-1)}^{n}.
 -- Anders
}}}





---

Comment by was created at 2009-01-18 00:03:38

#5004 dup'd this, but has a patch.


---

Comment by was created at 2009-01-18 00:03:38

Resolution: duplicate
