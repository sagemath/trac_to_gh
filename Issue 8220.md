# Issue 8220: Improve consistency and docs for finite fields creation

Issue created by migration from https://trac.sagemath.org/ticket/8220

Original creator: ylchapuy

Original creation time: 2010-02-09 15:30:48

Assignee: AlexGhitza

For the Givaro and the NTL implementations, one can use modulus='random' but not for the Pari implementation.
Moreover, according to the documentation in finite_field.py, modulus must be a polynomial, but in fact it can also be a string.


---

Comment by ylchapuy created at 2010-02-09 15:44:03

Changing status from new to needs_review.


---

Comment by ylchapuy created at 2010-02-09 15:44:03

The provided patch:

   * cleans the code and the documentation for finite field creation;
   * make modulus = 'conway' and modulus = 'random' available for all implementations;
   * make modulus = 'minimal_weight' is available for all binary fields;
   * adds modulus = 'first_lexicographic' for all binary fields.

Yann


---

Comment by ylchapuy created at 2010-02-09 15:54:43

Changing status from needs_review to needs_work.


---

Comment by ylchapuy created at 2010-02-09 16:23:27

needs #8212


---

Attachment


---

Comment by ylchapuy created at 2010-02-09 16:23:39

Changing status from needs_work to needs_review.


---

Comment by fwclarke created at 2010-02-11 08:08:51

There's one doctest that needs modifying after this patch is applied:

```
sage -t  "devel/sage/sage/structure/factory.pyx"            
**********************************************************************
File "/Users/mafwc/sage-4.3.2/devel/sage/sage/structure/factory.pyx", line 234:
    sage: key, _ = GF.create_key_and_extra_args(27, 'k'); key
Expected:
    (27, ('k',), None, None, '{}')
Got:
    (27, ('k',), 'conway', None, '{}')
**********************************************************************
```

Otherwise it seems fine.


---

Comment by fwclarke created at 2010-02-11 08:08:51

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by ylchapuy created at 2010-02-11 08:41:51

Changing status from needs_work to needs_review.


---

Comment by ylchapuy created at 2010-02-11 08:41:51

Replying to [comment:4 fwclarke]:
> There's one doctest that needs modifying after this patch is applied

Oups, sorry, I don't knw how I missed that one...
I made a tiny patch to correct this.


---

Comment by fwclarke created at 2010-02-11 20:39:33

Changing status from needs_review to positive_review.


---

Comment by fwclarke created at 2010-02-11 20:39:33

It's okay now.


---

Comment by mvngu created at 2010-02-14 14:29:29

Resolution: fixed


---

Comment by mvngu created at 2010-02-14 14:29:29

Merged in this order:

 1. [trac_8220-finite_field_creation.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8220/trac_8220-finite_field_creation.patch) --- I put in the ticket number for this patch.
 1. [trac_8220-review.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8220/trac_8220-review.patch) --- I put in a sensible commit message with the ticket number for this patch.
