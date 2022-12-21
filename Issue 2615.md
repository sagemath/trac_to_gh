# Issue 2615: wish: compute the jordan basis together with the jordan canonical form

Issue created by migration from Trac.

Original creator: pdenapo

Original creation time: 2008-03-20 14:51:21

Assignee: was

Sage has now an implementation of the Jordan canonical form (see #874)

However for most applications (like computing the exponential of a matrix,
see #2273) we would need to be able to compute not only the Jordan form, but
the Jordan basis as well (or what is equivalent the coordinate-change matrix P
such that P^(-1) A P = J, where A is the matrix, and J is its Jordan normal form)

(As far as I know, Maple can do that)


---

Comment by mhansen created at 2008-04-15 04:10:40

Changing status from new to assigned.


---

Comment by mhansen created at 2008-04-15 04:10:40

Changing assignee from was to mhansen.


---

Attachment


---

Comment by AlexGhitza created at 2008-04-15 23:40:34

Looks good to me.


---

Comment by mabshoff created at 2008-04-16 01:43:44

Merged in Sagr 3.0.alpha6


---

Comment by mabshoff created at 2008-04-16 01:43:44

Resolution: fixed
