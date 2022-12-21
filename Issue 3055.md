# Issue 3055: creating subgraph does not delete _pos entries

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-04-29 20:42:56

Assignee: rlm

This means that later, a call to relabel fails.  This affects, for example, the graph isomorphism code (which was how the error was originally found).



---

Attachment

With #3054 and #3055 applied, doctests pass in the graphs/ directory.


---

Comment by rlm created at 2008-04-29 21:43:29

Have not run doctests, but I support this fix.


---

Comment by mabshoff created at 2008-04-30 02:16:50

#3054 and #3055 applied to my current merge tree doctest clean. So I am considering this a positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-30 02:17:29

Resolution: fixed


---

Comment by mabshoff created at 2008-04-30 02:17:29

Merged in Sage 3.0.1.alpha1


---

Comment by jason created at 2008-05-02 22:02:02

Tracy McKay and Laura DeLoss should also get credit for exposing this bug.


---

Comment by mabshoff created at 2008-05-03 03:17:08

Replying to [comment:5 jason]:
> Tracy McKay and Laura DeLoss should also get credit for exposing this bug.

Well, did they fix the bug? So far we only give credit for doing that. People who find bugs are not credited and while we could add a "reported by FOO" byline I am not sure those people will get added to the credit list.

Cheers,

Michael
