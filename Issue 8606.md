# Issue 8606: floats in exponent do not propagate

Issue created by migration from https://trac.sagemath.org/ticket/8606

Original creator: zimmerma

Original creation time: 2010-03-25 15:11:24

Assignee: AlexGhitza

CC:  jason alexghitza was

Keywords: float, RR

Consider the following (sage 4.3.3, since 4.3.4 does not compile
on my machine):

```
sage: 2.0^53
9.00719925474099e15
```

This is what we expect: the float `2.0` propagates to the whole
expression.

However:

```
sage: 2^53.0
9007199254740992
```

Note the result is an integer, not a float! Thus the information
about the inexact value has been lost. Same thing with
`2^float(53)` and `2^RR(53)`.


---

Comment by was created at 2010-03-29 05:03:13

The problem is in the function __pow__ in sage/rings/integer.pyx.  There we find:

```
        try:
            nn = PyNumber_Index(n)
        except TypeError:
            try:
```

I think PyNumber_Index(53.0) is the long "53".    Thus to change this as you wish, that code must be changed.


---

Comment by zimmerma created at 2010-03-29 11:03:17

William, in fact `nn = PyNumber_Index(n)` raises an error, thus we go to

```
            try:
                nn = Integer(n)
            except TypeError:
                try:
                    s = parent_c(n)(self)
                    return s**n
```

where `nn = Integer(n)` succeeds for n=53.0, but fails for n=53.1:

```
sage: Integer(53.0)
53
sage: Integer(53.1)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/users/caramel/zimmerma/detached/<ipython console> in <module>()

/usr/local/sage-core2/local/lib/python2.6/site-packages/sage/rings/integer.so in sage.rings.integer.Integer.__init__ (sage/rings/integer.c:6449)()

/usr/local/sage-core2/local/lib/python2.6/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealNumber._integer_ (sage/rings/real_mpfr.c:11846)()

TypeError: Attempt to coerce non-integral RealNumber to Integer
```

If `Integer(53.0)` would return an error too, this would fix the problem. However we would
then need a specific method to coerce an integral real number to integer...

On a side note, `int` seems to behave differently:

```
sage: int(53.0)
53
sage: int(53.1)
53
```



---

Comment by jason created at 2010-03-29 12:14:21

It seems like we should fix pow, rather than change Integer(53.0).  In pow, it seems like we shouldn't just try to blindly coerce to an integer, because that is where we are losing information that we don't want to lose.  Why do we have `nn = Integer(n)`?  The previous PyNumber_Index would take care of cases where we really had an integer power, right?  It seems like just deleting the Integer(n) try clause might be the right thing to do.


---

Attachment

Jason,
> It seems like just deleting the Integer(n) try clause might be the right thing to do.

thanks, that did the trick! I am attaching a patch to review.


---

Comment by zimmerma created at 2010-03-29 13:12:29

Changing assignee from AlexGhitza to zimmerma.


---

Comment by zimmerma created at 2010-03-29 13:13:25

Changing status from new to needs_review.


---

Comment by zimmerma created at 2010-05-24 07:57:13

Jason, Alex, William, please can anyone of you review this patch? This should be easy. Thanks.

Paul


---

Comment by burcin created at 2010-05-24 14:25:08

Changing status from needs_review to needs_info.


---

Comment by burcin created at 2010-05-24 14:25:08

The changes in attachment:trac_8606.patch look good to me and all the doctests pass. I'm ready to give this a positive review, but I have a minor comment first:

Shouldn't we also drop the try/except clause around `parent_c(n)(self)`? The error message returned by the `except` is not very helpful and I can't think of any test case to actually fall in that clause. Note that if the conversion `parent_c(n)(self)` fails, we get a `TypeError` not an `AttributeError`:


```
sage: 5^('a')
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'str'
```



---

Comment by zimmerma created at 2010-05-24 18:44:41

apply only this patch (against 4.4.2)


---

Comment by zimmerma created at 2010-05-24 18:47:17

Changing status from needs_info to needs_review.


---

Attachment

thank you Burcin for your review. I have attached a new patch following your proposal.
However we still get the same (unhelpful) error message for `5^('a')`.
All doctests still pass.


---

Comment by burcin created at 2010-05-26 10:54:15

Changing status from needs_review to positive_review.


---

Comment by burcin created at 2010-05-26 10:54:15

Replying to [comment:10 zimmerma]:
> thank you Burcin for your review. I have attached a new patch following your proposal.
> However we still get the same (unhelpful) error message for `5^('a')`.
> All doctests still pass.

I was referring to the message `"exponent (=%s) must be an integer.\nCoerce your numbers to real or complex numbers first."` as unhelpful. You're right that the message `unsupported operand type(s) for ** or pow(): 'str' and 'str'` can be confusing as well. It just didn't occur to me since I was staring at the code and expected exactly that.

We could catch the `TypeError` and change the message to "Cannot find a common domain to perform the operation. Please convert your arguments to the desired types explicitly." or something similar.

I'm still changing this to positive review since the patch fixes a bug and a more meaningful error message is just an enhancement.


---

Comment by mhansen created at 2010-06-06 08:28:15

Resolution: fixed
