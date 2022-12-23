# Issue 6439: doctests beginning with Sage: are silently ignored

Issue created by migration from https://trac.sagemath.org/ticket/6439

Original creator: broune

Original creation time: 2009-06-28 09:45:32

Assignee: tbd

CC:  mjo

This doctest is silently ignored:


```
Sage: 1+1
45
```


I.e. no warning is displayed, and doctesting the file it is in produces no failures. This is because I wrote Sage: rather than sage:. I don't now if other capitalizations than "sage" should be accepted, but certainly they should not be silently ignored.

I propose to report an error on "Sage:" or any other capitalization of that in any context where "sage:" would be interpreted as a doctest.



---

Comment by mjo created at 2011-12-14 20:03:13

Is this *really* a problem?

 1. You shouldn't be re-typing your doctests by hand; you should copy/paste an actual sage session to avoid errors.
 2. This only affects one-line doctests, unless you make the same mistake more than once. For example any lines referencing `t` should fail if your first line is "Sage: var('t')".
 3. If there are N tests passing before you add yours, there should be N+1 passing afterwards.
 4. All patches are reviewed and this should certainly catch (3).


---

Comment by kini created at 2012-01-03 23:36:37

Yeah, this is developer error, IMO. "Sage: 1+1" is not recognized by the doctester as a test input line, and neither is "Warning: 1+1" or "Hello: World" or any other such examples. We don't (and obviously shouldn't) produce error messages for these other examples, and I see no reason why "Sage:" should get special treatment.


---

Comment by davidloeffler created at 2012-01-04 09:56:18

Changing status from new to needs_review.


---

Comment by davidloeffler created at 2012-01-04 09:56:42

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-01-05 13:37:00

Resolution: wontfix
