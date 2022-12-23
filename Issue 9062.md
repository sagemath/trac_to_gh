# Issue 9062: Add support for toric lattices

Issue created by migration from https://trac.sagemath.org/ticket/9062

Original creator: novoselt

Original creation time: 2010-05-27 04:45:06

Assignee: mhampton

CC:  vbraun

Toric lattices are ZZ<sup>n</sup>'s with distinction of their roles (in the simplest case - standard dual lattices M and N).

Once this patch is finished, it will be the first part of the toric varieties framework #8986-#8989, but so far I made it actually on top of those modules. Creation of cones and fans seems to work as expected. More work is needed on matrix multiplication. Working on it!


---

Comment by novoselt created at 2010-05-27 04:50:02

Changing status from new to needs_work.


---

Comment by vbraun created at 2010-05-27 09:55:20

Looks good, I'll be happy to review the final version!


---

Attachment

Fixed version.


---

Attachment

Apply this patch only.


---

Comment by novoselt created at 2010-05-28 02:40:04

It will probably work without other "prerequisites," but I tested it with them applied since all got positive review already and hopefully will be merged soon...


---

Comment by novoselt created at 2010-05-28 02:40:04

Changing status from needs_work to needs_review.


---

Comment by novoselt created at 2010-05-28 17:25:28

Functions `is_ToricLattice` and `__hash__` for elements will be added to these new modules in the coming patch for cones at #8986.


---

Comment by vbraun created at 2010-06-03 19:27:54

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2010-06-03 19:27:54

Very nice. I like it how the M/N lattice elements derive from Vector_integer_dense. Positive review. Applies to Sage 4.4.2.


---

Comment by novoselt created at 2010-06-03 20:20:06

Thank you! (I think authors and reviewers should be listed with their full names rather than trac accounts, this simplifies the job of release managers.)


---

Comment by davidloeffler created at 2010-07-01 09:49:12

While testing I found a heisenbug caused by this patch. If you run "make ptestlong", there is a failure in toric_lattice_element.pyx; but it works fine if you doctest just that file.

The problem is this comparison function:

```
    def __cmp__(self, right):
        r"""
[...]
            sage: cmp(n, 1)
            -1
        """
        c = cmp(type(self), type(right))
        if c:
            return c
```


The doctest is sensitively dependent on the exact memory locations of different classes, because `cmp(type(self), type(right))` compares on memory addresses. I suggest changing the doctest to 

```
sage: n == 1
False
```

which is much more robust.

David


---

Comment by davidloeffler created at 2010-07-01 09:49:12

Changing status from positive_review to needs_work.


---

Comment by davidloeffler created at 2010-07-01 10:09:02

Apply this patch over trac_9062_add_support_for_toric_lattices.patch


---

Attachment

Here's a tiny patch which makes the fix I suggested.


---

Comment by davidloeffler created at 2010-07-01 10:09:46

Changing status from needs_work to needs_review.


---

Comment by vbraun created at 2010-07-01 10:25:43

The same potential issue is in `toric_lattice.py`. Here is an updated patch that fixes this one, too. I think this is fine now, if you agree please set to "positive review".


---

Comment by vbraun created at 2010-07-01 10:26:25

Updated patch


---

Attachment

Looks good to me. Apply `trac_9062_add_support_for_toric_lattices.patch` and `trac_9062-cmp_fix.2.patch`.


---

Comment by davidloeffler created at 2010-07-01 10:30:55

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-20 08:46:22

Resolution: fixed


---

Comment by mpatel created at 2010-07-24 02:59:11

One or more of #8986, #8987, and #9062 _may_ cause the doctest failures listed at #9590.
