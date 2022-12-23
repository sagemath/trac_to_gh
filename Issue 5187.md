# Issue 5187: fix optional magma doctests that changed in magma-2.15

Issue created by migration from https://trac.sagemath.org/ticket/5187

Original creator: was

Original creation time: 2009-02-05 21:30:50

Assignee: was

The latest version of Magma is Magma-2.15, and there are doctests all over that now slightly fail because the output format of certain things in Magma has changed.  

The file at http://sage.math.washington.edu/home/was/patches/magma-2.15.txt lists all the doctest failures.  It was got by running this script:

```
        sage -t -only_optional=magma "devel/sage/sage/rings/polynomial/multi_polynomial_ring_generic.pyx"
        sage -t -only_optional=magma "devel/sage/sage/rings/polynomial/term_order.py"
        sage -t -only_optional=magma "devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py"
        sage -t -only_optional=magma "devel/sage/sage/crypto/mq/mpolynomialsystem.py"
        sage -t -only_optional=magma "devel/sage/sage/interfaces/magma.py"

```

on eno, which has Magma-2.15.

I think all the changes are purely cosmetic, so this should be very straightforward (but tedious).


---

Comment by mabshoff created at 2009-02-05 21:39:23

It all seems to be 

```
Graded Reverse Lexicographical Order
```

vs

```
Order: Graded Reverse Lexicographical
```

and 

```
Lexicographical Order
```

vs

```
Order: Lexicographical
```


The question is: Do we make 2.15 the only officially blessed release or do we add a sufficient amount of dots to make the tests also pass with 2.13 to 2.14?

Cheers,

Michael


---

Comment by mariah created at 2011-05-24 20:13:59

Changing status from new to needs_review.


---

Comment by mariah created at 2011-05-24 20:13:59

I believe this ticket can be closed as it is superceded by #7870.


---

Comment by was created at 2011-08-23 05:19:54

Resolution: duplicate


---

Comment by was created at 2011-08-24 23:45:51

Changing keywords from "" to "sd32".
