# Issue 1975: elliptic curve method -- one should trivially be able to implement a toy version, but can't anymore, which sucks

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-30 03:38:42

Assignee: was


```

They definitely very useful sometimes.  E.g., there is something
called the elliptic curve factorization method that is a brilliant trick
to factor integers.  You want to factor an integer N so you pretend
that it is prime, do a bunch of arithmetic with N, and if something goes
wrong, the error message gives just the information you need to factor N.
But it's important that the error message be an exception that you can
catch and that can contain some interesting Python data in it.  Custom
exceptions work very nicely for that. 

(This used to be trivial to implement in Sage, but for some reason
Sage changed and now it is isn't... :-(

sage: E = EllipticCurve(Integers(15),[1,-1])
sage: P = E.point([1,0,1], check=False)
goes boom but didn't used to...

William
```



---

Comment by AlexGhitza created at 2009-01-23 07:06:47

Changing type from defect to enhancement.


---

Comment by davidloeffler created at 2009-07-20 19:47:41

Changing assignee from was to davidloeffler.


---

Comment by davidloeffler created at 2009-07-20 19:47:41

Changing component from number theory to elliptic curves.


---

Comment by davidloeffler created at 2009-10-09 09:11:34

Remove assignee davidloeffler.


---

Comment by wuthrich created at 2010-04-12 18:01:48

See also this [sage-support discussion](http://groups.google.com/group/sage-support/browse_thread/thread/e2a5a329c0699379)


---

Comment by cremona created at 2010-05-04 17:49:07

The simplest workaround, I think, is to set 

```
E._point_class = sage.schemes.elliptic_curves.ell_field.EllipticCurve_field
```

after creating E and before attempting to create points.


---

Attachment

Applies to 4.4.1


---

Comment by cremona created at 2010-05-05 19:32:08

The patch makes possible what is wanted here.  It does two things:
    1. in creating an instance of `EllipticCurve_generic`, if the base ring is an `IntegerModRing` it sets the point_class to be `EllipticCurvePoint_finite_field`.  The is a class with a lot of functionality, eheras the code previous set this to the class `EllipticCurvePoint` (the default for generic elliptic curves) which has no functionality at all (not even an initialiser!).
    2. When a `ZeroDivisionError` is raised on trying to invert a non-invertible element of the base ring during point arithmetic, the error message is expanded when the base ring is an `IntegerModRing` so that it shows a factorization of the modulus.


---

Comment by cremona created at 2010-05-05 19:32:08

Changing status from new to needs_review.


---

Comment by robertwb created at 2010-05-05 21:19:23

I'd really like to see this behavior, but I'm not sure this is the right fix--probably what should happen is that most of the generic, missing code should be moved up to a higher level. That would probably be a bit more invasive though.


---

Comment by cremona created at 2010-05-05 21:30:45

Replying to [comment:7 robertwb]:
> I'd really like to see this behavior, but I'm not sure this is the right fix--probably what should happen is that most of the generic, missing code should be moved up to a higher level. That would probably be a bit more invasive though. 

I rather expected this reaction -- but look, the *only* cases where this makes any difference is precisely the case of an "elliptic curve over Z/NZ".  Since ECM is something many people want to teach, why not allow this in now, pending a more rigorous implementation?  There is absolutely no effect from this patch on any elliptic curve defined over a field;  and I think this is much less dangerous than William's fix of telling a non-field to pretend that it is a field, surely?

We could ask for a vote...


---

Comment by robertwb created at 2010-05-05 21:39:45

That's why I didn't mark this as needs work, because half of me wants to fix this the (pedantically) correct way, and the other half just wants to get this in. 

The code looks good, I haven't run tests as I don't have a clean install handy, but I can't see anything going wrong.


---

Comment by was created at 2010-05-06 00:43:01

Here is an idea (which should not be a show stopper for this patch, but could be for later): Can you change the exceptions so that they include the information about the prime factor found?  I.e., make a class that derives from ZeroDivisionError, and set an attribute that contains extra info.  You can raise class instances in exceptions.


---

Comment by cremona created at 2010-05-06 08:13:41

The exception error messages do include this info, but not in such a sophisticated way -- they give a nontrivial factorisation of the modulus.

If what you're suggesting would be better, I am open to the idea but not sure how to implement it (didn't know that ZeroDivisionError was a class at all!)


---

Comment by wuthrich created at 2010-05-23 23:02:44

I had a look at this patch and it seems ok to me. All tests passed and it does what it promises.

I agree with the fact that this may not be the best way to do it, but I propose to accept this as a temporary solution. I leave it to someone else to open a new ticket requesting for a better solution.


---

Comment by wuthrich created at 2010-05-23 23:02:44

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-06-05 21:35:04

Resolution: fixed
