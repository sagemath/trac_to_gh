# Issue 6406: fixing p_primary_bound on Tate-Shafarevich groups not to allow the reducible case

Issue created by migration from Trac.

Original creator: wuthrich

Original creation time: 2009-06-25 14:37:36

Assignee: was

CC:  rlm

Keywords: elliptic curves, tate shafarevich group,

Currently the p_primary_bound pretends to give back a proven result when the p-torsion is reducible. That is wrong.


---

Attachment


---

Comment by wuthrich created at 2009-06-25 14:59:26

.... and there was a bug. It actually never tested for surjectivity, since {{not E.is_surjective(p)}} is always False.


---

Comment by cremona created at 2009-06-28 15:44:27

Looks good, applies fine to 4.1.alpha2 and tests pass (I tested all schemes/elliptic_curves).

Is it possible to add a doctest illustrating the suggestion to "try an_padic instead"?  That would be useful for the reference manual.  Of course, an_padic has its own tests but it would look good to include one right after one of the new tests which shows the message.


---

Comment by rlm created at 2009-06-29 21:10:12

Resolution: fixed
