# Issue 1503: [with patch] calculus -- formal function calls don't coerce correctly to Mathematica

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-12-14 05:50:21

Assignee: was

Before this patch if you make a formal function it will
not coerce into Mathematica.  E.g..


```
sage: f = function('Foo', var('x'), var('y'))
sage: mathematica(f)
Foo[x, y]
```


With this patch it does work. 


---

Attachment


---

Comment by mabshoff created at 2007-12-15 23:41:08


```
[00:32] <mabshoff> about 1503: Shoudln't the mathematica doctests require mathematica?
[00:32] <rlm> was-1464: it was a rewrite or nice, line by line, so actually it's a little cleaner
[00:32] <rlm> the memory management for example
[00:33] <was-1464> yes, put # optional there.
[00:33] <mabshoff> ok, will do.
[00:33] <was-1464> But *only* in the two lines with mathematica(...)
[00:33] <was-1464> Matheamtica is *not* needed for the _mathematica_init_ lines
[00:33] <mabshoff> Yep, I was about to ask for clarification on that.
```



---

Comment by mabshoff created at 2007-12-16 01:12:49

Resolution: fixed


---

Comment by mabshoff created at 2007-12-16 01:12:49

Merged in 2.9.rc2.
