# Issue 7595: Chinese Remainder Theorem for polynomials over a field

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2009-12-03 17:27:53

Assignee: AlexGhitza

This wasn't hard to implement, since all the hard work was already done.


---

Comment by rlm created at 2009-12-03 19:03:11

Changing status from new to needs_review.


---

Comment by ncohen created at 2009-12-04 06:03:20

Changing status from needs_review to needs_info.


---

Comment by ncohen created at 2009-12-04 06:03:20

Hello !! This is clearly not my field but I dare intrude : I see you are using functions "crt" and "CRT_list", and I wondered if you would find it sensible to rename them to chinese_remainer_theorem and chinese_remainder_theorem_list ? If this is too long, it may be possible to drop the "theorem" from the name, but the fact remains that if I had to use this function sometime ( which is not excluded, as it is a very famous result ), there is no way on earth I would have thought of trying the "crt" function if I had not seen it related to this ticket :-)

I am under the impression the english speakers would end this message with :

"Well, just my two cents" :-)

Nathann


---

Comment by rlm created at 2009-12-04 17:06:34

Changing status from needs_info to needs_review.


---

Comment by rlm created at 2009-12-04 17:06:34

Replying to [comment:2 ncohen]:
> ... I wondered if you would find it sensible to rename them to chinese_remainer_theorem ...

This is irrelevant to this ticket. You should bring it up on sage-devel instead.


---

Comment by robertwb created at 2009-12-08 07:42:01

Changing status from needs_review to positive_review.


---

Comment by robertwb created at 2009-12-08 07:42:01

Nice.


---

Comment by rlm created at 2009-12-15 22:30:04

This patch wasn't applying, so I've rebased it. No real changes though.


---

Comment by rlm created at 2009-12-15 23:16:07

rebased on 4.3.rc0


---

Attachment

Just caught a doctest failure in sage/rings/arith.py. Oops!


---

Comment by mhansen created at 2009-12-16 02:31:15

Changing status from positive_review to needs_work.


---

Comment by rlm created at 2009-12-16 02:32:28

Which ticket is the patch conflicting with?


---

Comment by rlm created at 2009-12-18 22:38:03

I've checked, and this merges with the current rc1.


---

Comment by rlm created at 2009-12-18 22:38:03

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2009-12-22 15:58:21

The patch is fine, applies to 4.3.rc0 and all tests pass in sage/rings.

I have some problems with the CRT* functions though.

   1. CRT_list does not check that the two lists have the same length;  if the moduli list is shorter you get an IndexError, but it would be better to catch that and raise a more informative error.

   2. CRT_basis is rather silly.   It calls CRT_list n times with the same moduli, which must be wasteful.  It would be better to call plain CRT n times with suitable moduli (exercise for the reader).

Of course, I don't think that these issues should delay the current patch, but deserve a ticket of their own to make sure they are tided up.


---

Comment by cremona created at 2009-12-22 15:58:21

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-01-03 21:38:39

I've made #7836 for this.


---

Comment by mhansen created at 2010-01-03 21:38:39

Resolution: fixed


---

Comment by mhansen created at 2010-01-04 01:17:30

Changing status from closed to needs_work.


---

Comment by mhansen created at 2010-01-04 01:17:30

This causes failures in the following file `sage/quadratic_forms/quadratic_form__ternary_Tornaria.py`:


```
**********************************************************************
File "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/devel/sage-main/sage/quadratic_forms/quadratic_form__ternary_Tornaria.py", line 476:
    sage: map(Q1.xi_rec, [-1,2,3,5])
Exception raised:
    Traceback (most recent call last):
      File "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_18[8]>", line 1, in <module>
        map(Q1.xi_rec, [-Integer(1),Integer(2),Integer(3),Integer(5)])###line 476:
    sage: map(Q1.xi_rec, [-1,2,3,5])
      File "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/lib/python/site-packages/sage/quadratic_forms/quadratic_form__ternary_Tornaria.py", line 481, in xi_rec
        return self.reciprocal().xi(p)
      File "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/lib/python/site-packages/sage/quadratic_forms/quadratic_form__ternary_Tornaria.py", line 456, in xi
        return kronecker_symbol(p, self.basiclemma(2))
      File "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/lib/python/site-packages/sage/quadratic_forms/quadratic_form__ternary_Tornaria.py", line 385, in basiclemma
        a=self(self.basiclemmavec(M))
      File "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/lib/python/site-packages/sage/quadratic_forms/quadratic_form__ternary_Tornaria.py", line 416, in basiclemmavec
        return CRT_list(vec,mod)
      File "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/lib/python/site-packages/sage/rings/arith.py", line 2522, in CRT_list
        return moduli[0].parent()(v[0])
      File "parent.pyx", line 538, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4956)
      File "coerce_maps.pyx", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3142)
      File "coerce_maps.pyx", line 77, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3040)
      File "integer.pyx", line 653, in sage.rings.integer.Integer.__init__ (sage/rings/integer.c:6803)
    TypeError: unable to coerce <type 'sage.modules.vector_integer_dense.Vector_integer_dense'> to an integer
**********************************************************************
File "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/devel/sage-main/sage/quadratic_forms/quadratic_form__ternary_Tornaria.py", line 478:
    sage: map(Q2.xi_rec, [-1,2,3,5])
Exception raised:
    Traceback (most recent call last):
      File "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_18[9]>", line 1, in <module>
        map(Q2.xi_rec, [-Integer(1),Integer(2),Integer(3),Integer(5)])###line 478:
    sage: map(Q2.xi_rec, [-1,2,3,5])
      File "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/lib/python/site-packages/sage/quadratic_forms/quadratic_form__ternary_Tornaria.py", line 481, in xi_rec
        return self.reciprocal().xi(p)
      File "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/lib/python/site-packages/sage/quadratic_forms/quadratic_form__ternary_Tornaria.py", line 456, in xi
        return kronecker_symbol(p, self.basiclemma(2))
      File "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/lib/python/site-packages/sage/quadratic_forms/quadratic_form__ternary_Tornaria.py", line 385, in basiclemma
        a=self(self.basiclemmavec(M))
      File "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/lib/python/site-packages/sage/quadratic_forms/quadratic_form__ternary_Tornaria.py", line 416, in basiclemmavec
        return CRT_list(vec,mod)
      File "/virtual/scratch/mhansen/release/4.3.1/alpha0/sage-4.3.1.alpha0/local/lib/python/site-packages/sage/rings/arith.py", line 2522, in CRT_list
        return moduli[0].parent()(v[0])
      File "parent.pyx", line 538, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4956)
      File "coerce_maps.pyx", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3142)
      File "coerce_maps.pyx", line 77, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3040)
      File "integer.pyx", line 653, in sage.rings.integer.Integer.__init__ (sage/rings/integer.c:6803)
    TypeError: unable to coerce <type 'sage.modules.vector_integer_dense.Vector_integer_dense'> to an integer
```



---

Attachment

Should fix the issues in quadratic_form__ternary_Tornaria.py


---

Comment by rlm created at 2010-01-04 15:38:29

This patch should fix the issues mentioned above. I wasn't sure whether to make a new ticket, or just post it here (never seen a "needs_work" closed ticket...)


---

Comment by cremona created at 2010-01-04 16:21:29

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2010-01-04 16:22:42

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-01-04 16:22:42

I changed the ticket to "needs review" and then gave it a positive review -- it works for me.


---

Comment by mvngu created at 2010-01-07 00:22:32

This ticket is rather messy. The patch `trac_7595.patch` is merged in Sage 4.3.1.alpha0 and it was then closed as being fixed in that version. Later on, the value in the field "Merged in:" was deleted. Now there is another patch `trac_7595-failures.patch` which hasn't been merged yet as of Sage 4.3.1.alpha1. And yet the ticket is declared as "fixed", but without a value for the field "Merged in:". I think the ticket's status should now be "open" not "fixed", until `trac_7595-failures.patch` is merged.


---

Comment by rlm created at 2010-01-07 04:30:47

Replying to [comment:16 mvngu]:
> The patch `trac_7595.patch` is merged in Sage 4.3.1.alpha0 ... Now there is another patch `trac_7595-failures.patch` which hasn't been merged yet as of Sage 4.3.1.alpha1.

The patch was rolled back-- neither is in Sage-4.3.1.alpha1

> And yet the ticket is declared as "fixed"...

Apparently when the ticket was reopened, this did not revert. I don't know how to fix this, but the ticket is definitely open.

> ... until `trac_7595-failures.patch` is merged.

Repeat: as of sage-4.3.1.alpha1, *both* patches need to be merged.
