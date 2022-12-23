# Issue 5015: Horrible bug in old (and new) symbolic calculus: f(x)=1; f*e --> BOOM!

Issue created by migration from https://trac.sagemath.org/ticket/5015

Original creator: was

Original creation time: 2009-01-18 15:18:36

Assignee: burcin


```


On Sun, Jan 18, 2009 at 7:08 AM, YannLC  wrote:
>
> but in fact the same error occurs without ns=1...
>
> ----------------------------------------------------------------------
> | Sage Version 3.2.3, Release Date: 2009-01-05                       |
> | Type notebook() for the GUI, and license() for information.        |
> ----------------------------------------------------------------------
> sage: f(x)=1
> sage: f*e
> [...]
> RuntimeError: maximum recursion depth exceeded

That is weird.  What a horrible bug!   Thanks for reporting this.  It is now trac #
```


It also happens with ns=1.  I've verified this.


---

Attachment

Note that the new code doesn't get run as doing

f(x) = 1

overwrites the old x (which was created with var('x',ns=1)) with just var('x').  The infinite recursion is due the CallableSymbolicExpression ring assuming that all elements of SR were instances of SymbolicExpression.


---

Comment by was created at 2009-01-18 20:38:32

Looks good.  Great work fixing this so quickly!


---

Comment by mabshoff created at 2009-01-19 04:14:59

Resolution: fixed


---

Comment by mabshoff created at 2009-01-19 04:14:59

Merged in Sage 3.3.alpha0
