# Issue 8502: evaluating multivariate polynomials yields non-constant

Issue created by migration from https://trac.sagemath.org/ticket/8502

Original creator: cremona

Original creation time: 2010-03-11 22:08:11

Assignee: AlexGhitza

CC:  wuthrich malb

Keywords: polynomial evaluation

The following behaviour does not agree with the documentation for the {{{__call__}} function on multivariable polynomials, which states that (as one would expect and hope) the result should lie in the constant field:

```
sage: K.<t> = NumberField(x^2+47)
sage: R.<X,Y,Z> = K[]
sage: f = X+Y+Z
sage: a = f(t,t,t)
sage: a.parent()
Multivariate Polynomial Ring in X, Y, Z over Number Field in t with defining polynomial x^2 + 47
```

It is also inconsistent:

```
sage: R.<X,Y,Z> = QQ[]
sage: f = X+Y+Z
sage: a = f(2,3,4)
sage: a.parent()
Rational Field
```

This causes strange bugs -- see #8498 for an example.


---

Comment by cremona created at 2010-04-02 11:22:27

Bug fixed:  I added tests for when the resulting value is either 0, or a nonzero constant, in which case an element of the base ring is returned.  Otherwise an element of the parent is returned (so you can still evaluate f(x+y,y) and similar.)

Patch up as soon as testing is finished.

malb: I'm CC-ing you as the past person to work on this file.


---

Comment by cremona created at 2010-04-02 11:43:59

Applies to 4.3.5


---

Comment by cremona created at 2010-04-02 11:44:20

Changing status from new to needs_review.


---

Attachment


---

Comment by AlexGhitza created at 2010-04-03 08:12:32

Changing status from needs_review to positive_review.


---

Comment by AlexGhitza created at 2010-04-03 08:12:32

Looks good.


---

Comment by jhpalmieri created at 2010-04-16 18:44:22

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-16 18:44:22

Merged "trac_8502-mpoly.patch" in 4.4.alpha0.
