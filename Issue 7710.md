# Issue 7710: documentation of rational_reconstruction incoherent with code

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2009-12-16 11:59:05

Assignee: AlexGhitza

The documentation of rational_reconstruction says that an error
*ZeroDivisionError* is raised when no solution exists with the given
bounds, but the code returns an error *ValueError*.


---

Comment by zimmerma created at 2010-02-05 20:42:35

Still there in 4.3.1:

```
sage: rational_reconstruction?
...

        exists, that pair is unique and this function returns it. If no
        such pair exists, this function raises ZeroDivisionError.
```

and:

```
sage: rational_reconstruction(29,105)
...
ValueError: Rational reconstruction of 29 (mod 105) does not exist.
```


Note also that in 4.3.1 a.rational_reconstruction? gives a different documentation, which does
not mention what happens in case of error. Why are the documentations different?


---

Comment by jdemeyer created at 2014-10-20 19:00:45

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2014-10-20 19:00:45

Fixed by #17180.


---

Comment by jdemeyer created at 2014-10-20 19:00:51

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-10-27 16:27:09

Resolution: duplicate
