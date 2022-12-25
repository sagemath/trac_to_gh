# Issue 7879: Remove unnecessary signal handling for low prec mpfr operations.

archive/issues_007879.json:
```json
{
    "body": "Assignee: @aghitza\n\n`_sig_on` and {{{_sig_off}} are more expensive than computing the result itself.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7879\n\n",
    "created_at": "2010-01-09T19:31:01Z",
    "labels": [
        "component: basic arithmetic",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.2",
    "title": "Remove unnecessary signal handling for low prec mpfr operations.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7879",
    "user": "https://github.com/robertwb"
}
```
Assignee: @aghitza

`_sig_on` and {{{_sig_off}} are more expensive than computing the result itself.

Issue created by migration from https://trac.sagemath.org/ticket/7879





---

archive/issue_comments_068338.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-09T19:38:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7879#issuecomment-68338",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068339.json:
```json
{
    "body": "Signal handling is omitted for functions/precisions that were clearly and uniformly in the millisecond range or less.",
    "created_at": "2010-01-09T19:38:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7879#issuecomment-68339",
    "user": "https://github.com/robertwb"
}
```

Signal handling is omitted for functions/precisions that were clearly and uniformly in the millisecond range or less.



---

archive/issue_comments_068340.json:
```json
{
    "body": "Attachment [7879-RR-signal.patch](tarball://root/attachments/some-uuid/ticket7879/7879-RR-signal.patch) by @robertwb created at 2010-01-09 19:42:17",
    "created_at": "2010-01-09T19:42:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7879#issuecomment-68340",
    "user": "https://github.com/robertwb"
}
```

Attachment [7879-RR-signal.patch](tarball://root/attachments/some-uuid/ticket7879/7879-RR-signal.patch) by @robertwb created at 2010-01-09 19:42:17



---

archive/issue_comments_068341.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-01-20T10:24:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7879#issuecomment-68341",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_068342.json:
```json
{
    "body": "This looks good.  I have one question: you are hardcoding threshold precisions after which the signals should be used, mostly 1000, but also 10000 in a couple of places.  Would it be better to have a global variable PREC_THRESHOLD set to 1000 at the top of the file, and then use it or 10*PREC_THRESHOLD where needed?  It would make it easier to change this in the future, since a search for it would be all that's needed.\n\nI'm marking this as needs_info.  If you think it's not worth the trouble, I'll put a positive review.",
    "created_at": "2010-01-20T10:24:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7879#issuecomment-68342",
    "user": "https://github.com/aghitza"
}
```

This looks good.  I have one question: you are hardcoding threshold precisions after which the signals should be used, mostly 1000, but also 10000 in a couple of places.  Would it be better to have a global variable PREC_THRESHOLD set to 1000 at the top of the file, and then use it or 10*PREC_THRESHOLD where needed?  It would make it easier to change this in the future, since a search for it would be all that's needed.

I'm marking this as needs_info.  If you think it's not worth the trouble, I'll put a positive review.



---

archive/issue_comments_068343.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-01-19T16:10:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7879#issuecomment-68343",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_068344.json:
```json
{
    "body": "I am proposing to close this ticket as invalid since #9678 makes `sig_on()` and `sig_off()` a lot faster.  In any case, if you want to keep the patch, it needs rebasing (`_sig_on` and `_sig_off` must be replaced by `sig_on()` and `sig_off()` but there are more patch conflicts).",
    "created_at": "2011-01-19T16:10:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7879#issuecomment-68344",
    "user": "https://github.com/jdemeyer"
}
```

I am proposing to close this ticket as invalid since #9678 makes `sig_on()` and `sig_off()` a lot faster.  In any case, if you want to keep the patch, it needs rebasing (`_sig_on` and `_sig_off` must be replaced by `sig_on()` and `sig_off()` but there are more patch conflicts).



---

archive/issue_comments_068345.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-05-17T13:19:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7879#issuecomment-68345",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068346.json:
```json
{
    "body": "Since this ticket is marked sage-duplicate/invalid/wontfix plus has\nnot been active for 4 months, I believe this ticket can be closed.",
    "created_at": "2011-05-17T13:19:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7879#issuecomment-68346",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

Since this ticket is marked sage-duplicate/invalid/wontfix plus has
not been active for 4 months, I believe this ticket can be closed.



---

archive/issue_comments_068347.json:
```json
{
    "body": "Robert, what is your opinion?  `sig_on()` and `sig_off()` became a lot faster since #9678, but they still take up some cycles.",
    "created_at": "2011-05-17T15:56:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7879#issuecomment-68347",
    "user": "https://github.com/jdemeyer"
}
```

Robert, what is your opinion?  `sig_on()` and `sig_off()` became a lot faster since #9678, but they still take up some cycles.



---

archive/issue_comments_068348.json:
```json
{
    "body": "Thanks for taking a look at this. I've been waiting for 4.7 to be released to re-base this, and think it'd still worth having. Perhaps I'll put PREC_THRESHOLD in there while I'm at it, and maybe do some benchmarking.",
    "created_at": "2011-05-17T18:26:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7879#issuecomment-68348",
    "user": "https://github.com/robertwb"
}
```

Thanks for taking a look at this. I've been waiting for 4.7 to be released to re-base this, and think it'd still worth having. Perhaps I'll put PREC_THRESHOLD in there while I'm at it, and maybe do some benchmarking.



---

archive/issue_comments_068349.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-05-17T18:32:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7879#issuecomment-68349",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_068350.json:
```json
{
    "body": "Replying to [comment:7 robertwb]:\n> and maybe do some benchmarking.\n\nIf you find useful ways to do benchmarks, please let me know. I might re-use those benchmarks to optimize `sig_on()` and `sig_off()`.",
    "created_at": "2011-05-17T20:33:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7879#issuecomment-68350",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:7 robertwb]:
> and maybe do some benchmarking.

If you find useful ways to do benchmarks, please let me know. I might re-use those benchmarks to optimize `sig_on()` and `sig_off()`.



---

archive/issue_comments_068351.json:
```json
{
    "body": "The patch adds one unrelated doctest.  This doctest has been moved to #11344.",
    "created_at": "2011-05-17T20:34:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7879#issuecomment-68351",
    "user": "https://github.com/jdemeyer"
}
```

The patch adds one unrelated doctest.  This doctest has been moved to #11344.



---

archive/issue_comments_068352.json:
```json
{
    "body": "\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading Sage library. Current Mercurial branch is: bitrot\n| Sage Version 4.7, Release Date: 2011-05-23                         |\n| Type notebook() for the GUI, and license() for information.        |\nsage: L = [RR(k) for k in range(1000)]\n\nsage: %timeit [a.sqrt() for a in L]\n 625 loops, best of 3: 569 \u00b5s per loop\n\nsage: %timeit [a.sqrt() for a in L]\n 625 loops, best of 3: 509 \u00b5s per loop\n\nsage: %timeit [a.sqrt() for a in L]\n 625 loops, best of 3: 513 \u00b5s per loop\n\nsage: timeit(\"[a.sqrt() for a in L]\", number=10000)\n10000 loops, best of 3: 519 \u00b5s per loop\n\nsage: \nExiting Sage (CPU time 0m19.94s, Wall time 1m9.75s).\nrobertwb@sage:/scratch/robertwb/sage-4.7/devel/sage-bitrot$ hg qpush\napplying 7879-RR-signal.patch\nnow at: 7879-RR-signal.patch\nrobertwb@sage:/scratch/robertwb/sage-4.7/devel/sage-bitrot$ ../../sage -br\n[...]\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading Sage library. Current Mercurial branch is: bitrot\n| Sage Version 4.7, Release Date: 2011-05-23                         |\n| Type notebook() for the GUI, and license() for information.        |\nsage: L = [RR(k) for k in range(1000)]\n\nsage: %timeit [a.sqrt() for a in L]\n 625 loops, best of 3: 498 \u00b5s per loop\n\nsage: %timeit [a.sqrt() for a in L]\n 625 loops, best of 3: 498 \u00b5s per loop\n\nsage: %timeit [a.sqrt() for a in L]\n 625 loops, best of 3: 496 \u00b5s per loop\n\nsage: timeit(\"[a.sqrt() for a in L]\", number=10000)\n10000 loops, best of 3: 499 \u00b5s per loop\n```\n\n\nLooks like about a 5% win (much smaller than I remember it being before).",
    "created_at": "2011-05-31T08:01:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7879#issuecomment-68352",
    "user": "https://github.com/robertwb"
}
```


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

archive/issue_comments_068353.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-05-31T08:01:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7879#issuecomment-68353",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_068354.json:
```json
{
    "body": "Attachment [7879-RR-signal.2.patch](tarball://root/attachments/some-uuid/ticket7879/7879-RR-signal.2.patch) by @robertwb created at 2011-05-31 08:01:57\n\nRebased on 4.7",
    "created_at": "2011-05-31T08:01:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7879#issuecomment-68354",
    "user": "https://github.com/robertwb"
}
```

Attachment [7879-RR-signal.2.patch](tarball://root/attachments/some-uuid/ticket7879/7879-RR-signal.2.patch) by @robertwb created at 2011-05-31 08:01:57

Rebased on 4.7



---

archive/issue_comments_068355.json:
```json
{
    "body": "patch [attachment:7879-RR-signal.2.patch] applied to sage-4.7.1.alpha1.  Then did 'sage -b' followed by 'make testlong'.\nThe following test failed:\n\n\n```\neno% ./sage -t  -long -force_lib \"devel/sage/sage/rings/residue_field.pyx\"\nsage -t -long -force_lib \"devel/sage/sage/rings/residue_field.pyx\"\n**********************************************************************\nFile \"/home/mariah/sage/sage-4.7.1.alpha1-x86_64-Linux-core2-fc-review-7879/devel/sage/sage/rings/residue_field.pyx\", line 670:\n    sage: I = QQ[3^(1/3)].factor(5)[1][0]; I\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mariah/sage/sage-4.7.1.alpha1-x86_64-Linux-core2-fc-review-7879/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/mariah/sage/sage-4.7.1.alpha1-x86_64-Linux-core2-fc-review-7879/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/mariah/sage/sage-4.7.1.alpha1-x86_64-Linux-core2-fc-review-7879/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_10[2]>\", line 1, in <module>\n        I = QQ[Integer(3)**(Integer(1)/Integer(3))].factor(Integer(5))[Integer(1)][Integer(0)]; I###line 670:\n    sage: I = QQ[3^(1/3)].factor(5)[1][0]; I\n      File \"ring.pyx\", line 167, in sage.rings.ring.Ring.__getitem__ (sage/rings/ring.c:2007)\n      File \"expression.pyx\", line 8287, in sage.symbolic.expression.Expression.minpoly (sage/symbolic/expression.cpp:31950)\n      File \"/home/mariah/sage/sage-4.7.1.alpha1-x86_64-Linux-core2-fc-review-7879/local/lib/python/site-packages/sage/calculus/calculus.py\", line 925, in minpoly\n        if g(ex).simplify_trig().simplify_radical() == 0:\n      File \"expression.pyx\", line 6546, in sage.symbolic.expression.Expression.simplify_trig (sage/symbolic/expression.cpp:24657)\n      File \"expression.pyx\", line 460, in sage.symbolic.expression.Expression._maxima_ (sage/symbolic/expression.cpp:3674)\n      File \"sage_object.pyx\", line 429, in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:3451)\n      File \"lazy_import.pyx\", line 167, in sage.misc.lazy_import.LazyImport.__getattr__ (sage/misc/lazy_import.c:1353)\n      File \"lazy_import.pyx\", line 110, in sage.misc.lazy_import.LazyImport._get_object (sage/misc/lazy_import.c:1023)\n      File \"/home/mariah/sage/sage-4.7.1.alpha1-x86_64-Linux-core2-fc-review-7879/local/lib/python/site-packages/sage/interfaces/maxima_lib.py\", line 152, in <module>\n        ecl_eval(\"#$%s$\"%l)\n      File \"ecl.pyx\", line 1224, in sage.libs.ecl.ecl_eval (sage/libs/ecl.c:6301)\n      File \"ecl.pyx\", line 1239, in sage.libs.ecl.ecl_eval (sage/libs/ecl.c:6252)\n      File \"ecl.pyx\", line 252, in sage.libs.ecl.ecl_safe_eval (sage/libs/ecl.c:2544)\n    RuntimeError: ECL says: THROW: The catch MACSYMA-QUIT is undefined.\n**********************************************************************\nFile \"/home/mariah/sage/sage-4.7.1.alpha1-x86_64-Linux-core2-fc-review-7879/devel/sage/sage/rings/residue_field.pyx\", line 672:\n    sage: k = I.residue_field(); k\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mariah/sage/sage-4.7.1.alpha1-x86_64-Linux-core2-fc-review-7879/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/mariah/sage/sage-4.7.1.alpha1-x86_64-Linux-core2-fc-review-7879/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/mariah/sage/sage-4.7.1.alpha1-x86_64-Linux-core2-fc-review-7879/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_10[3]>\", line 1, in <module>\n        k = I.residue_field(); k###line 672:\n    sage: k = I.residue_field(); k\n      File \"element.pyx\", line 328, in sage.structure.element.Element.__getattr__ (sage/structure/element.c:2792)\n      File \"parent.pyx\", line 277, in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:2940)\n      File \"parent.pyx\", line 175, in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2709)\n    AttributeError: 'sage.symbolic.expression.Expression' object has no attribute 'residue_field'\n**********************************************************************\n```\n\n\netc.",
    "created_at": "2011-06-01T15:19:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7879#issuecomment-68355",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

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

archive/issue_comments_068356.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-06-01T15:19:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7879#issuecomment-68356",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_068357.json:
```json
{
    "body": "Replying to [comment:12 mariah]:\n> patch [attachment:7879-RR-signal.2.patch] applied to sage-4.7.1.alpha1.  Then did 'sage -b' followed by 'make testlong'.\n> The following test failed:\n> \n> {{{\n> eno% ./sage -t  -long -force_lib \"devel/sage/sage/rings/residue_field.pyx\"\n> sage -t -long -force_lib \"devel/sage/sage/rings/residue_field.pyx\"\n> **********************************************************************\n> File \"/home/mariah/sage/sage-4.7.1.alpha1-x86_64-Linux-core2-fc-review-7879/devel/sage/sage/rings/residue_field.pyx\", line 670:\n>     sage: I = QQ[3^(1/3)].factor(5)[1][0]; I\n> Exception raised:\n\nThese errors don't occur for me with sage-4.7.2.alpha2.",
    "created_at": "2011-08-23T07:16:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7879#issuecomment-68357",
    "user": "https://github.com/williamstein"
}
```

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

archive/issue_comments_068358.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2011-08-23T07:24:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7879#issuecomment-68358",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_068359.json:
```json
{
    "body": "I did a full test of Sage on another machine too with 4.7.2.alpha2, and everything works.  Code looks good and addresses other people's issues...",
    "created_at": "2011-08-23T07:24:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7879#issuecomment-68359",
    "user": "https://github.com/williamstein"
}
```

I did a full test of Sage on another machine too with 4.7.2.alpha2, and everything works.  Code looks good and addresses other people's issues...



---

archive/issue_comments_068360.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd32\".",
    "created_at": "2011-08-24T23:43:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7879#issuecomment-68360",
    "user": "https://github.com/williamstein"
}
```

Changing keywords from "" to "sd32".



---

archive/issue_comments_068361.json:
```json
{
    "body": "Sage library patch. Robert's patch rebased to Sage 4.7.2.alpha2, because of fuzz 2.",
    "created_at": "2011-09-12T15:51:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7879#issuecomment-68361",
    "user": "https://github.com/nexttime"
}
```

Sage library patch. Robert's patch rebased to Sage 4.7.2.alpha2, because of fuzz 2.



---

archive/issue_comments_068362.json:
```json
{
    "body": "Attachment [trac_7879-harmless_fuzz_2.diff](tarball://root/attachments/some-uuid/ticket7879/trac_7879-harmless_fuzz_2.diff) by @nexttime created at 2011-09-12 15:52:24\n\nDo not apply. Fuzz against Sage 4.7.2.alpha2. For reference only.",
    "created_at": "2011-09-12T15:52:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7879#issuecomment-68362",
    "user": "https://github.com/nexttime"
}
```

Attachment [trac_7879-harmless_fuzz_2.diff](tarball://root/attachments/some-uuid/ticket7879/trac_7879-harmless_fuzz_2.diff) by @nexttime created at 2011-09-12 15:52:24

Do not apply. Fuzz against Sage 4.7.2.alpha2. For reference only.



---

archive/issue_comments_068363.json:
```json
{
    "body": "Attached a rebased patch because of fuzz.",
    "created_at": "2011-09-12T15:58:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7879#issuecomment-68363",
    "user": "https://github.com/nexttime"
}
```

Attached a rebased patch because of fuzz.



---

archive/issue_comments_068364.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-09-13T12:16:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7879#issuecomment-68364",
    "user": "https://github.com/nexttime"
}
```

Resolution: fixed
