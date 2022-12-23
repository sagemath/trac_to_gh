# Issue 6468: FiniteField_prime_modn.__call__ should raise an error, rather than return an error

Issue created by migration from https://trac.sagemath.org/ticket/6468

Original creator: SimonKing

Original creation time: 2009-07-06 13:10:08

Assignee: somebody

Keywords: Finite field, call

The `__call__` method of `FiniteField_prime_modn` reads like this:

```
    def __call__(self, x):
        try:
            return integer_mod.IntegerMod(self, x)
        except (NotImplementedError, PariError):
            return TypeError, "error coercing to finite field"
        except TypeError:
            if sage.interfaces.all.is_GapElement(x):
                from sage.interfaces.gap import gfq_gap_to_sage
                try:
                    return gfq_gap_to_sage(x, self)
                except (ValueError, IndexError, TypeError), msg:
                    raise TypeError, "%s\nerror coercing to finite field"%msg
            else:
                raise
```


So, in the fourth line of the function body, an error is not raised but returned.

Actually I met this when calling `GF(2)` with one of my extension types. Unfortunately I did not find anything in Sage that would trigger it as well.

Anyway, I think it should be obvious that 

```
            return TypeError, "error coercing to finite field"
```

should be changed into

```
            raise TypeError, "error coercing to finite field"
```


This is what my patch does.


---

Comment by SimonKing created at 2009-07-06 13:12:17

Changing status from new to assigned.


---

Comment by SimonKing created at 2009-07-06 13:12:17

Changing assignee from somebody to SimonKing.


---

Comment by was created at 2009-07-07 04:07:18

REFEREE REPORT:

* Put in an example in the patch that clearly illustrates that you've fixed the bug.  I.e., write some code that raises that exception, and illustrate that it is raised.  Put this in the TESTS: section of the tests.


---

Comment by SimonKing created at 2009-07-07 06:38:52

Replying to [comment:2 was]:
> REFEREE REPORT:
> 
> * Put in an example in the patch that clearly illustrates that you've fixed the bug.  I.e., write some code that raises that exception, and illustrate that it is raised.  Put this in the TESTS: section of the tests. 

I'd be happy to do so. But it turns out that it is not easy to make `integer_mod.IntegerMod(self, x)` raising a `NotImplementedError` or a `PariError`. By accident, I found that this is the case when using my extension class for describing elements of modular polynomial rings of finite p-groups. But certainly items from a to-be-created-and-at-most-optional package can't be part of a doc test...

I try to cook something else up that triggers the error. But perhaps you now better how to produce a PariError?

Anyway, since currently the call method has no doc test at all, it is certainly wise to create one.

Best regards
   Simon


---

Comment by SimonKing created at 2009-07-07 12:54:40

Gotcha!

The following nasty example triggers the error:

```
sage: class foo_parent(Parent):
....:     pass
....:
sage: class foo(RingElement):
....:     def lift(self):
....:         raise PariError
....:
sage: P = foo_parent()
sage: F = foo(P)
sage: GF(2)(F)
(<type 'exceptions.TypeError'>, 'error coercing to finite field')
```


I will produce a patch, adding doc tests to the call method (it is currently lacking any doc tests!), and also adding the nasty example with reference to this ticket.


---

Comment by SimonKing created at 2009-07-07 13:14:53

OK, done, there is a new patch including doc tests.


---

Comment by SimonKing created at 2009-07-07 13:16:30

FiniteField.__call__ should raise an error rather than return an error


---

Attachment

Replying to [comment:5 SimonKing]:
> OK, done, there is a new patch including doc tests.

PS: I did the doc tests for the patched version of sage/rings/integer_mod_ring.py, and they passed. However, as I have only sage-4.0.2, it'd be better if someone else runs the tests as well.

Cheers,
  Simon


---

Comment by AlexGhitza created at 2009-07-11 09:13:11

Looks good to me.


---

Comment by mvngu created at 2009-07-17 08:09:52

Resolution: fixed
