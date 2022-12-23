# Issue 7879: Remove unnecessary signal handling for low prec mpfr operations.

Issue created by migration from https://trac.sagemath.org/ticket/7879

Original creator: robertwb

Original creation time: 2010-01-09 19:31:01

Assignee: AlexGhitza

`_sig_on` and {{{_sig_off}} are more expensive than computing the result itself.


---

Comment by robertwb created at 2010-01-09 19:38:47

Changing status from new to needs_review.


---

Comment by robertwb created at 2010-01-09 19:38:47

Signal handling is omitted for functions/precisions that were clearly and uniformly in the millisecond range or less.


---

Attachment


---

Comment by AlexGhitza created at 2010-01-20 10:24:37

Changing status from needs_review to needs_info.


---

Comment by AlexGhitza created at 2010-01-20 10:24:37

This looks good.  I have one question: you are hardcoding threshold precisions after which the signals should be used, mostly 1000, but also 10000 in a couple of places.  Would it be better to have a global variable PREC_THRESHOLD set to 1000 at the top of the file, and then use it or 10*PREC_THRESHOLD where needed?  It would make it easier to change this in the future, since a search for it would be all that's needed.

I'm marking this as needs_info.  If you think it's not worth the trouble, I'll put a positive review.


---

Comment by jdemeyer created at 2011-01-19 16:10:19

Changing status from needs_info to needs_review.


---

Comment by jdemeyer created at 2011-01-19 16:10:19

I am proposing to close this ticket as invalid since #9678 makes `sig_on()` and `sig_off()` a lot faster.  In any case, if you want to keep the patch, it needs rebasing (`_sig_on` and `_sig_off` must be replaced by `sig_on()` and `sig_off()` but there are more patch conflicts).


---

Comment by mariah created at 2011-05-17 13:19:43

Changing status from needs_review to positive_review.


---

Comment by mariah created at 2011-05-17 13:19:43

Since this ticket is marked sage-duplicate/invalid/wontfix plus has
not been active for 4 months, I believe this ticket can be closed.


---

Comment by jdemeyer created at 2011-05-17 15:56:22

Robert, what is your opinion?  `sig_on()` and `sig_off()` became a lot faster since #9678, but they still take up some cycles.


---

Comment by robertwb created at 2011-05-17 18:26:12

Thanks for taking a look at this. I've been waiting for 4.7 to be released to re-base this, and think it'd still worth having. Perhaps I'll put PREC_THRESHOLD in there while I'm at it, and maybe do some benchmarking.


---

Comment by mariah created at 2011-05-17 18:32:31

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2011-05-17 20:33:12

Replying to [comment:7 robertwb]:
> and maybe do some benchmarking.

If you find useful ways to do benchmarks, please let me know. I might re-use those benchmarks to optimize `sig_on()` and `sig_off()`.


---

Comment by jdemeyer created at 2011-05-17 20:34:06

The patch adds one unrelated doctest.  This doctest has been moved to #11344.


---

Comment by robertwb created at 2011-05-31 08:01:09


```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: bitrot
| Sage Version 4.7, Release Date: 2011-05-23                         |
| Type notebook() for the GUI, and license() for information.        |
sage: L = [RR(k) for k in range(1000)]

sage: %timeit [a.sqrt() for a in L]
 625 loops, best of 3: 569 µs per loop

sage: %timeit [a.sqrt() for a in L]
 625 loops, best of 3: 509 µs per loop

sage: %timeit [a.sqrt() for a in L]
 625 loops, best of 3: 513 µs per loop

sage: timeit("[a.sqrt() for a in L]", number=10000)
10000 loops, best of 3: 519 µs per loop

sage: 
Exiting Sage (CPU time 0m19.94s, Wall time 1m9.75s).
robertwb@sage:/scratch/robertwb/sage-4.7/devel/sage-bitrot$ hg qpush
applying 7879-RR-signal.patch
now at: 7879-RR-signal.patch
robertwb@sage:/scratch/robertwb/sage-4.7/devel/sage-bitrot$ ../../sage -br
[...]
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: bitrot
| Sage Version 4.7, Release Date: 2011-05-23                         |
| Type notebook() for the GUI, and license() for information.        |
sage: L = [RR(k) for k in range(1000)]

sage: %timeit [a.sqrt() for a in L]
 625 loops, best of 3: 498 µs per loop

sage: %timeit [a.sqrt() for a in L]
 625 loops, best of 3: 498 µs per loop

sage: %timeit [a.sqrt() for a in L]
 625 loops, best of 3: 496 µs per loop

sage: timeit("[a.sqrt() for a in L]", number=10000)
10000 loops, best of 3: 499 µs per loop
```


Looks like about a 5% win (much smaller than I remember it being before).


---

Comment by robertwb created at 2011-05-31 08:01:09

Changing status from needs_work to needs_review.


---

Attachment

Rebased on 4.7


---

Comment by mariah created at 2011-06-01 15:19:06

patch [attachment:7879-RR-signal.2.patch] applied to sage-4.7.1.alpha1.  Then did 'sage -b' followed by 'make testlong'.
The following test failed:


```
eno% ./sage -t  -long -force_lib "devel/sage/sage/rings/residue_field.pyx"
sage -t -long -force_lib "devel/sage/sage/rings/residue_field.pyx"
**********************************************************************
File "/home/mariah/sage/sage-4.7.1.alpha1-x86_64-Linux-core2-fc-review-7879/devel/sage/sage/rings/residue_field.pyx", line 670:
    sage: I = QQ[3^(1/3)].factor(5)[1][0]; I
Exception raised:
    Traceback (most recent call last):
      File "/home/mariah/sage/sage-4.7.1.alpha1-x86_64-Linux-core2-fc-review-7879/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mariah/sage/sage-4.7.1.alpha1-x86_64-Linux-core2-fc-review-7879/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mariah/sage/sage-4.7.1.alpha1-x86_64-Linux-core2-fc-review-7879/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[2]>", line 1, in <module>
        I = QQ[Integer(3)**(Integer(1)/Integer(3))].factor(Integer(5))[Integer(1)][Integer(0)]; I###line 670:
    sage: I = QQ[3^(1/3)].factor(5)[1][0]; I
      File "ring.pyx", line 167, in sage.rings.ring.Ring.__getitem__ (sage/rings/ring.c:2007)
      File "expression.pyx", line 8287, in sage.symbolic.expression.Expression.minpoly (sage/symbolic/expression.cpp:31950)
      File "/home/mariah/sage/sage-4.7.1.alpha1-x86_64-Linux-core2-fc-review-7879/local/lib/python/site-packages/sage/calculus/calculus.py", line 925, in minpoly
        if g(ex).simplify_trig().simplify_radical() == 0:
      File "expression.pyx", line 6546, in sage.symbolic.expression.Expression.simplify_trig (sage/symbolic/expression.cpp:24657)
      File "expression.pyx", line 460, in sage.symbolic.expression.Expression._maxima_ (sage/symbolic/expression.cpp:3674)
      File "sage_object.pyx", line 429, in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:3451)
      File "lazy_import.pyx", line 167, in sage.misc.lazy_import.LazyImport.__getattr__ (sage/misc/lazy_import.c:1353)
      File "lazy_import.pyx", line 110, in sage.misc.lazy_import.LazyImport._get_object (sage/misc/lazy_import.c:1023)
      File "/home/mariah/sage/sage-4.7.1.alpha1-x86_64-Linux-core2-fc-review-7879/local/lib/python/site-packages/sage/interfaces/maxima_lib.py", line 152, in <module>
        ecl_eval("#$%s$"%l)
      File "ecl.pyx", line 1224, in sage.libs.ecl.ecl_eval (sage/libs/ecl.c:6301)
      File "ecl.pyx", line 1239, in sage.libs.ecl.ecl_eval (sage/libs/ecl.c:6252)
      File "ecl.pyx", line 252, in sage.libs.ecl.ecl_safe_eval (sage/libs/ecl.c:2544)
    RuntimeError: ECL says: THROW: The catch MACSYMA-QUIT is undefined.
**********************************************************************
File "/home/mariah/sage/sage-4.7.1.alpha1-x86_64-Linux-core2-fc-review-7879/devel/sage/sage/rings/residue_field.pyx", line 672:
    sage: k = I.residue_field(); k
Exception raised:
    Traceback (most recent call last):
      File "/home/mariah/sage/sage-4.7.1.alpha1-x86_64-Linux-core2-fc-review-7879/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mariah/sage/sage-4.7.1.alpha1-x86_64-Linux-core2-fc-review-7879/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mariah/sage/sage-4.7.1.alpha1-x86_64-Linux-core2-fc-review-7879/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[3]>", line 1, in <module>
        k = I.residue_field(); k###line 672:
    sage: k = I.residue_field(); k
      File "element.pyx", line 328, in sage.structure.element.Element.__getattr__ (sage/structure/element.c:2792)
      File "parent.pyx", line 277, in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:2940)
      File "parent.pyx", line 175, in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2709)
    AttributeError: 'sage.symbolic.expression.Expression' object has no attribute 'residue_field'
**********************************************************************
```


etc.


---

Comment by mariah created at 2011-06-01 15:19:06

Changing status from needs_review to needs_work.


---

Comment by was created at 2011-08-23 07:16:55

Replying to [comment:12 mariah]:
> patch [attachment:7879-RR-signal.2.patch] applied to sage-4.7.1.alpha1.  Then did 'sage -b' followed by 'make testlong'.
> The following test failed:
> 
> {{{
> eno% ./sage -t  -long -force_lib "devel/sage/sage/rings/residue_field.pyx"
> sage -t -long -force_lib "devel/sage/sage/rings/residue_field.pyx"
> **********************************************************************
> File "/home/mariah/sage/sage-4.7.1.alpha1-x86_64-Linux-core2-fc-review-7879/devel/sage/sage/rings/residue_field.pyx", line 670:
>     sage: I = QQ[3^(1/3)].factor(5)[1][0]; I
> Exception raised:

These errors don't occur for me with sage-4.7.2.alpha2.


---

Comment by was created at 2011-08-23 07:24:14

Changing status from needs_work to positive_review.


---

Comment by was created at 2011-08-23 07:24:14

I did a full test of Sage on another machine too with 4.7.2.alpha2, and everything works.  Code looks good and addresses other people's issues...


---

Comment by was created at 2011-08-24 23:43:12

Changing keywords from "" to "sd32".


---

Comment by leif created at 2011-09-12 15:51:10

Sage library patch. Robert's patch rebased to Sage 4.7.2.alpha2, because of fuzz 2.


---

Attachment

Do not apply. Fuzz against Sage 4.7.2.alpha2. For reference only.


---

Comment by leif created at 2011-09-12 15:58:22

Attached a rebased patch because of fuzz.


---

Comment by leif created at 2011-09-13 12:16:11

Resolution: fixed
