# Issue 8131: Catalan numbers are integers

Issue created by migration from https://trac.sagemath.org/ticket/8131

Original creator: fwclarke

Original creation time: 2010-01-30 09:40:20

Assignee: sage-combinat

Keywords: Catalan numbers

The patch makes Sage aware of this fact.


---

Comment by fwclarke created at 2010-01-30 09:42:37

Changing status from new to needs_review.


---

Attachment


---

Comment by nthiery created at 2010-01-30 21:57:31

Changing status from needs_review to needs_work.


---

Comment by nthiery created at 2010-01-30 21:57:31

Thanks for spotting and fixing this!

Please add an:

```
OUTPUT: integer
```

line in the documentation, as per http://www.sagemath.org/doc/developer/conventions.html#documentation-strings, as well an
example in the doctests showing/testing that property, and I'll set a positive review!

Note: you may want to use the method divide_knowing_divisible_by on ZZ elements.


---

Comment by fwclarke created at 2010-02-06 13:13:56

Replying to [comment:2 nthiery]:

In the replacement patch I've improved the documentation and added a doctest as suggested.

In addition, I've simplified an existing doctest and slightly modified another (because `divide_knowing_divisible_by` gives a different error when trying to divide by zero).  I've made one more adjustment to the documentation so that the mathematics displays properly; at least it does in the notebook now.


---

Comment by fwclarke created at 2010-02-06 13:13:56

Changing status from needs_work to needs_review.


---

Comment by fwclarke created at 2010-02-06 13:15:23

replaces earlier patch, based on 4.3.1


---

Comment by nborie created at 2010-02-23 23:09:08

Changing status from needs_review to positive_review.


---

Attachment

It's look good for code, test and applying. I give this patch a positive review.


---

Comment by mvngu created at 2010-03-02 21:44:14

Merged [trac_8131-replacement.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8131/trac_8131-replacement.patch).



Francis: You should put the ticket number in your commit message.


---

Comment by mvngu created at 2010-03-02 21:44:14

Resolution: fixed


---

Comment by pelegm created at 2016-12-06 13:19:37

Changing keywords from "Catalan numbers" to "catalan".


---

Comment by fwclarke created at 2016-12-07 14:44:16

Replying to [comment:6 pelegm]:

The trouble with using the keyword 'catalan' is that it makes it look as though it concerns the Catalan constant rather than the Catalan numbers:

```
sage: catalan.n()
0.915965594177219
sage: catalan_number(7)
429
```

