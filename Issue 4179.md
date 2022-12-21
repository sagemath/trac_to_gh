# Issue 4179: [with patch, needs review] ell_finite_field.py "long" doctest fails

Issue created by migration from Trac.

Original creator: GeorgSWeber

Original creation time: 2008-09-23 22:07:17

Assignee: GeorgSWeber

In the file "ell_finite_field.py" change the line 1013 from

            sage: for p in prime_range(10000):           #long time (~20s)

to

            sage: for p in prime_range(32768, 42768):           #long time (~20s)

to achieve the same intended amount of testing for the elliptic cirves code as such.
(But do not run into an --- as of this writing --- outstanding bug related to 16-Bit signed integers on Mac OS X 10.4.)


---

Comment by GeorgSWeber created at 2008-09-23 22:07:26

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-09-23 22:09:18

Georg,

are you planning to post an actual hg patch?

Cheers,

Michael


---

Comment by cremona created at 2008-09-24 08:23:43

I'm not so keen on making this change, since this test was put in originally to show that a previous bug was fixed.  It is natural to use a sequence of primes starting at 2, but not so natural to use a sequence like prime_range(32768, 42768).

Given that we are tracking the root problem anyway, can we not live with this one doctest failure which only occurs on one type of machine with the long option anyway?


---

Comment by cremona created at 2008-09-24 08:25:07

PS this ticket also duplicates #3760.


---

Comment by mabshoff created at 2008-09-24 08:30:57

Resolution: duplicate


---

Comment by mabshoff created at 2008-09-24 08:30:57

Replying to [comment:4 cremona]:
> PS this ticket also duplicates #3760.

Ok, I agree with John here and am closing this as a duplicate of #3760. I did comment on that ticket and mentioned this ticket, so the info should not get lost.

Cheers,

Michael
