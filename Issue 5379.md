# Issue 5379: html conversion problems with live version of tutorial (ReST version)

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-02-26 03:09:20

Assignee: tba

In the live version of the tutorial, I'm seeing some problems. The static version seems to be fine.

1.  In tour_assignment.rst, in the lines

```
    sage: a = 5   # a is an integer
    sage: type(a)
    <type 'sage.rings.integer.Integer'>
    sage: a = 5/3  # now a is a rational number
    sage: type(a)
    <type 'sage.rings.rational.Rational'>
    sage: a = 'hello'  # now a is a string
    sage: type(a)
    <type 'str'>
```

the `<` and `>` signs turn into literal "&lt;" and "&gt;"

2. In tour_assignment.rst, in the lines 

```
    sage: n.str(8)   # string representation of n in base 8
    '11'
```

the quotes come out wrong.

3. In introduction.rst, the whitespace in the following lines comes out wrong:

```
    sage: k = 1/(sqrt(3)*I + 3/4 + sqrt(73)*5/9); print k
                                           1
                              ---------------------------
                                           5 sqrt(73)   3
                              sqrt(3)  I + ---------- + -
                                               9        4
```


4. In tour_algebra.rst, the math part of the lines

```
is modeled by the system of 2nd order differential equations

.. math::
    m_1 x_1'' + (k_1+k_2) x_1 - k_2 x_2 = 0
    m_2 x_2''+ k_2 (x_2-x_1) = 0,
```

is completely missing.  Same thing seems to happen for any text marked as ".. math::"

5. In tour_algebra.rst, in the lines

```
REFERENCES: Nagle, Saff, Snider, Fundamentals of Differential
Equations, 6th ed, Addison-Wesley, 2004. (see § 5.5).
```

an extra symbol appears before the section `§` symbol.

6. in tour_polynomial.rst, in the lines

```
.. [Si] G.-M. Greuel, G. Pfister, and H. Schönemann. 
        ``Singular`` 3.0. A Computer Algebra System for Polynomial
        Computations. Center for Computer Algebra, University of
        Kaiserslautern (2005). http://www.singular.uni-kl.de .
```

the o with an umlaut `ö` doesn't come out well.

7. in tour_groups.rst,

```
    sage: G._gap_init_()
    'Sp(4, 7)'
```

the quotes are mistreated.

I haven't done a careful reading; those are just the things I've spotted.




---

Comment by jhpalmieri created at 2009-04-07 21:09:25

Changing assignee from tba to jhpalmieri.


---

Comment by jhpalmieri created at 2009-04-07 21:09:25

Changing status from new to assigned.


---

Comment by jhpalmieri created at 2009-04-07 21:09:25

In the most recent version of Sage (3.4.1.rc1), I don't see problems 4, 5, 6 anymore.  The attached patch fixes the others for me.


---

Attachment


---

Comment by jhpalmieri created at 2009-04-12 19:40:33

This causes some doctest failures, some of which are listed at #5764 (where I think they were erroneously attributed to that patch -- they really come from this patch).  I'll get to work on fixing them soon.


---

Comment by jhpalmieri created at 2009-04-12 19:55:22

Here's a patch for the failed doctests; apply on top of the other one.  This passes all doctests on sage.math (for me, anyway) and also on my Mac.


---

Comment by jhpalmieri created at 2009-04-12 19:55:42

apply this on top of the other patch


---

Attachment

It works now.


---

Comment by mabshoff created at 2009-04-13 23:36:47

Merged both patches in Sage 3.4.1.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-13 23:36:47

Resolution: fixed
