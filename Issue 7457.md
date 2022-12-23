# Issue 7457: improvements to quotient_ring.py

Issue created by migration from https://trac.sagemath.org/ticket/7457

Original creator: AlexGhitza

Original creation time: 2009-11-14 12:29:00

Assignee: AlexGhitza

The attached patch makes a few improvements in `rings/quotient_ring.py`: implement `is_noetherian`, fix a todo in `cover_ring`, and minor docstring fixes.



---

Comment by AlexGhitza created at 2009-11-14 12:30:26

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2009-11-19 22:47:32

Can `self.cover_ring()` ever be non-Noetherian (with our current code)?

Of course if you take an infinitely generated polynomial ring over a field and mod out by all of the polynomial generators, the quotient is Noetherian but the cover ring is not.  I don't know if that can come up in Sage now, and I also don't know how else we would easily tell whether the quotient ring is Noetherian...

Otherwise, the patch looks good.


---

Comment by jhpalmieri created at 2009-11-19 22:47:32

Changing status from needs_review to needs_info.


---

Comment by AlexGhitza created at 2009-11-22 10:21:16

Changing status from needs_info to needs_work.


---

Comment by AlexGhitza created at 2009-11-22 10:21:16

That's a very good point, I should definitely fix this.  I'll have `is_noetherian` return True if `cover_ring` is Noetherian, and raise a `NotImplementedError` otherwise.

I'm marking this as needs_work, and I'll try to get to it soon.


---

Comment by AlexGhitza created at 2009-11-22 11:20:15

Alright, in the process of fixing this I added a few trivial methods to `InfinitePolynomialRing` and fixed a `NotImplementedError` being returned rather than raised in `ring.pyx`.


---

Comment by AlexGhitza created at 2009-11-22 11:20:15

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by jhpalmieri created at 2009-11-23 05:43:22

Two comments: this is not your fault, but can you fix lines 39-40 of quotient_ring.py?  Right now it says

```
    Creates a quotient ring of the ring `R` by the ideal `I`. Variables are 
    labeled by ``names``. (If the quotient ring is a quotient of a 
    polynomial ring.). If ``names`` isn't given, 'bar' will be appended to 
    the variable names in `R`. 
```

and the parentheses and surrounding punctuation really bother me.  Should this say

```
    Creates a quotient ring of the ring `R` by the ideal `I`. Variables are 
    labeled by ``names`` (if the quotient ring is a quotient of a 
    polynomial ring). If ``names`` isn't given, 'bar' will be appended to 
    the variable names in `R`. 
```

?  Or even remove the parentheses altogether?

Second and more importantly, I'm getting doctest failures in schemes/elliptic_curves:

```
The following tests failed:

	sage -t -long devel/sage/sage/schemes/elliptic_curves/sha_tate.py # 8 doctests failed
	sage -t -long devel/sage/sage/schemes/elliptic_curves/padics.py # 46 doctests failed
	sage -t -long devel/sage/sage/schemes/elliptic_curves/formal_group.py # 1 doctests failed
	sage -t -long devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py # 3 doctests failed
```

The problem seems to be the change to rings.pyx.  I don't know why you would ever want to `return` a `NotImplementedError` instead of raising it, but that change seems to be causing the problems.  So my suggestion is to get rid of that change, make sure doctests pass, and then perhaps open up a new ticket in which that issue is addressed.


---

Comment by jhpalmieri created at 2009-11-23 05:43:22

Changing status from needs_review to needs_work.


---

Comment by jhpalmieri created at 2009-11-26 15:35:35

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2009-11-26 15:35:35

Here's a referee's patch to fix these two issues.  See #7532 for a follow-up.


---

Attachment

apply on top of the other patch


---

Comment by jhpalmieri created at 2009-11-26 15:36:27

Changing status from needs_review to positive_review.


---

Comment by AlexGhitza created at 2009-11-26 22:02:35

Wow, I look away for a couple of days and this is all done and fixed.  Thanks, John!


---

Comment by mhansen created at 2009-11-29 05:33:53

Resolution: fixed
