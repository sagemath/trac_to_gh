# Issue 9946: output bug in GiNaC

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2010-09-19 08:26:08

Assignee: burcin


```
sage: a.imag()
sin(1/2*arctan2(0, -88* + 1))*sqrt(abs(4*(sqrt(3) - 5)*(sqrt(3) + 5) + 1))
```

See the output of the second argument of `arctan2`.
See also #9913.


---

Comment by burcin created at 2010-09-24 11:04:16

add doctest


---

Comment by burcin created at 2010-09-24 11:10:54

Changing status from new to needs_work.


---

Comment by burcin created at 2010-09-24 11:10:54

Changing keywords from "" to "pynac".


---

Comment by burcin created at 2010-09-24 11:10:54

Changing component from calculus to symbolics.


---

Attachment

This was fixed in GiNaC by Richard Kreckel. Here is the relevant patch:

http://www.ginac.de/ginac.git?p=ginac.git;a=commitdiff;h=e08cda1854bdb82f6706ec269233577690ae00e4

I applied the patch to pynac, so this will be fixed in the next release.


---

Comment by burcin created at 2011-05-09 15:09:45

Changing status from needs_work to needs_review.


---

Comment by burcin created at 2011-05-09 15:09:45

New pynac package with the fix is at #11317.


---

Comment by kcrisman created at 2011-05-09 18:37:31

Looks ok.  Same comment as at #9891.

For instance, one could then allow an spkg maintainer to review the upstream fix.  But that's not exactly what we want.


---

Comment by kcrisman created at 2011-05-09 18:37:31

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-05-27 12:01:28

Resolution: fixed
