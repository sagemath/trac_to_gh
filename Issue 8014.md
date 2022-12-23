# Issue 8014: Make `EllipticCurveIsogeny` objects faster to create via lazy evaluation

Issue created by migration from https://trac.sagemath.org/ticket/8014

Original creator: craigcitro

Original creation time: 2010-01-20 19:20:48

Assignee: cremona

CC:  cremona wuthrich shumow lorenz

Currently, it's quite slow to create an `EllipticCurveIsogeny` object, because it precomputes a huge amount of information about itself. (This blocks the original request at #7262, for instance.) It seems like it would be easy enough (and generally useful!) to speed up creation of isogeny objects, and have them lazily evaluate the appropriate bits as needed. Then one could unify the `multiplication_by_m` and `multiplication_by_m_isogeny` methods, for instance (maybe by deprecating the former?).

That said, I haven't spent much time with the isogeny code -- if there's some obvious reason this is a bad idea, please comment on the ticket.


---

Comment by cremona created at 2010-01-20 20:17:14

See also #7368 for an isogeny wishlist.

Chris W and I have lots of other ideas for redesigning the isogeny code.  At present it consists of a lot of intricately related functions and the code is hard to get into.  And the file ell_curve_isogeny.py is very long (4790 lines):  I plan to move lines 3733 to the end when we add implementations for {2,3,5,7,13}-isogenies in characteristics {2,3} for {j=0, j!=0}, which are currently being worked out by my student Kimi (5*2*2=20 special cases!)


---

Comment by lorenz created at 2021-11-05 06:35:29

The performance issues of `multiplication_by_m_isogeny` would be addressed by #32826.
