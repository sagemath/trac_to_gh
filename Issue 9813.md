# Issue 9813: Improve creation time for p-adic elements

Issue created by migration from Trac.

Original creator: roed

Original creation time: 2010-08-27 05:29:00

Assignee: AlexGhitza

Keywords: padic, p-adic

I've implemented coercion morphisms from ZZ and QQ to Zp and Qp.  This drops item creation time from about 20 microseconds to about 1 microsecond on my machine.


---

Attachment

See the thread http://groups.google.com/group/sage-devel/browse_thread/thread/612ea8f2f9d06e37?pli=1


---

Comment by roed created at 2010-08-27 05:32:31

Changing status from new to needs_review.


---

Comment by dmharvey created at 2010-08-28 02:08:00

Changing status from needs_review to needs_work.


---

Comment by dmharvey created at 2010-08-28 02:08:00

seems to work as advertised, but I get lots of doctest failures with -testall, typical example is like this:


```
File "/Users/david/sage-4.5.2/devel/sage/sage/rings/padics/padic_generic_element.pyx", line 1002:
    sage: R3(-1).square_root() == R3.teichmuller(2) or R3(-1).square_root() == R3.teichmuller(3)
Exception raised:
    Traceback (most recent call last):
      File "/Users/david/sage-4.5.2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/david/sage-4.5.2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/david/sage-4.5.2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_24[33]>", line 1, in <module>
        R3(-Integer(1)).square_root() == R3.teichmuller(Integer(2)) or R3(-Integer(1)).square_root() == R3.teichmuller(Integer(3))###line 1002:
    sage: R3(-1).square_root() == R3.teichmuller(2) or R3(-1).square_root() == R3.teichmuller(3)
      File "/Users/david/sage-4.5.2/local/lib/python/site-packages/sage/rings/padics/padic_generic.py", line 377, in teichmuller
        ans = self(x, prec)
      File "parent.pyx", line 861, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6427)
      File "map.pyx", line 478, in sage.categories.map.Map._call_with_args (sage/categories/map.c:3666)
    NotImplementedError: _call_with_args not overridden to accept arguments for <type 'sage.rings.padics.padic_base_coercion.pAdicCoercion_ZZ_CR'>
```



---

Comment by AlexGhitza created at 2010-09-02 11:14:29

Changing component from basic arithmetic to padics.


---

Comment by AlexGhitza created at 2010-09-02 11:14:29

Changing keywords from "padic, p-adic" to "coercion".


---

Comment by roed created at 2010-09-18 21:28:40

Replaces first patch.


---

Comment by roed created at 2010-09-18 21:29:25

Changing status from needs_work to needs_review.


---

Attachment

Well, that was more work than I expected, but it also fixes some problems with non-uniqueness of p-adic parents.


---

Comment by dmharvey created at 2010-09-22 01:12:35

Changing status from needs_review to positive_review.


---

Comment by dmharvey created at 2010-09-22 01:12:35

Excellent. You've restored my faith in Sage :-)


---

Comment by roed created at 2010-09-22 01:17:14

Good.  The series of patches in 7883 -> 8333 -> 8334 plus a bit of other additional work will fix most of your object creation problems with IntegerMods as well.


---

Comment by mpatel created at 2010-09-28 08:12:49

Changing status from positive_review to needs_work.


---

Comment by mpatel created at 2010-09-28 08:12:49

Could someone prepend the ticket number to the commit string's first line and restore the positive review?  The first line should also be < 80 characters long, so that `hg log` messages are compact.


---

Attachment

Commit message fixed. Apply only this patch.


---

Comment by davidloeffler created at 2010-09-28 08:21:52

Done.


---

Comment by davidloeffler created at 2010-09-28 08:21:52

Changing status from needs_work to positive_review.


---

Comment by mpatel created at 2010-09-28 10:54:51

Resolution: fixed
