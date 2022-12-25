# Issue 4282: [with patch, needs review] symbolic minpoly

archive/issues_004282.json:
```json
{
    "body": "Assignee: @burcin\n\nThe current minpoly algorithm on symbolic objects is slow and often fails. This patch makes it work in many more cases, as well as implementing better conversion into QQbar. \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4282\n\n",
    "created_at": "2008-10-14T14:18:11Z",
    "labels": [
        "component: calculus"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "[with patch, needs review] symbolic minpoly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4282",
    "user": "https://github.com/robertwb"
}
```
Assignee: @burcin

The current minpoly algorithm on symbolic objects is slow and often fails. This patch makes it work in many more cases, as well as implementing better conversion into QQbar. 



Issue created by migration from https://trac.sagemath.org/ticket/4282





---

archive/issue_comments_031265.json:
```json
{
    "body": "Attachment [4282-symbolic-minpoly.patch](tarball://root/attachments/some-uuid/ticket4282/4282-symbolic-minpoly.patch) by @robertwb created at 2008-10-14 14:21:04\n\nIt's still not super fast, but it's a lot better. Perhaps working with resultants directly could be faster (or improving QQbar's implementation, though I'm not sure how much is overhead vs. being a hard computational problem).",
    "created_at": "2008-10-14T14:21:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4282#issuecomment-31265",
    "user": "https://github.com/robertwb"
}
```

Attachment [4282-symbolic-minpoly.patch](tarball://root/attachments/some-uuid/ticket4282/4282-symbolic-minpoly.patch) by @robertwb created at 2008-10-14 14:21:04

It's still not super fast, but it's a lot better. Perhaps working with resultants directly could be faster (or improving QQbar's implementation, though I'm not sure how much is overhead vs. being a hard computational problem).



---

archive/issue_comments_031266.json:
```json
{
    "body": "There's a problem that comes up testing this, which may be something the improved doctests are exposing rather than causing:\n\n\n```\nsage: sin(pi/7).minpoly()\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/Users/mh/sagestuff/sage-3.1.4/<ipython console> in <module>()\n\n/Users/mh/sagestuff/sage-3.1.4/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in minpoly(self, *args, **kwds)\n   1343         from sage.rings.all import QQbar\n   1344         try:\n-> 1345             return QQbar(self).minpoly()\n   1346         except TypeError, ValueError:\n   1347             return self.minpoly_numeric(*args, **kwds)\n\n/Users/mh/sagestuff/sage-3.1.4/local/lib/python2.5/site-packages/sage/rings/qqbar.pyc in __call__(self, x)\n    661             return AlgebraicNumber(x._descr)\n    662         elif hasattr(x, '_algebraic_'):\n--> 663             return x._algebraic_(QQbar)\n    664         return AlgebraicNumber(x)\n    665 \n\n/Users/mh/sagestuff/sage-3.1.4/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in _algebraic_(self, field)\n   6432                 res = mag * QQbar.zeta(rat_arg.denom())**rat_arg.numer()\n   6433             elif func_name in ['sin', 'cos', 'tan']:\n-> 6434                 exp_ia = exp(SR(-1).sqrt()*operand)._algebraic_(QQbar)\n   6435                 if func_name == 'sin':\n   6436                     res = (exp_ia - ~exp_ia)/(2*QQbar.zeta(4))\n\nAttributeError: 'SymbolicConstant' object has no attribute 'sqrt'\n\n```\n",
    "created_at": "2008-10-24T03:23:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4282#issuecomment-31266",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

There's a problem that comes up testing this, which may be something the improved doctests are exposing rather than causing:


```
sage: sin(pi/7).minpoly()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/Users/mh/sagestuff/sage-3.1.4/<ipython console> in <module>()

/Users/mh/sagestuff/sage-3.1.4/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in minpoly(self, *args, **kwds)
   1343         from sage.rings.all import QQbar
   1344         try:
-> 1345             return QQbar(self).minpoly()
   1346         except TypeError, ValueError:
   1347             return self.minpoly_numeric(*args, **kwds)

/Users/mh/sagestuff/sage-3.1.4/local/lib/python2.5/site-packages/sage/rings/qqbar.pyc in __call__(self, x)
    661             return AlgebraicNumber(x._descr)
    662         elif hasattr(x, '_algebraic_'):
--> 663             return x._algebraic_(QQbar)
    664         return AlgebraicNumber(x)
    665 

/Users/mh/sagestuff/sage-3.1.4/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in _algebraic_(self, field)
   6432                 res = mag * QQbar.zeta(rat_arg.denom())**rat_arg.numer()
   6433             elif func_name in ['sin', 'cos', 'tan']:
-> 6434                 exp_ia = exp(SR(-1).sqrt()*operand)._algebraic_(QQbar)
   6435                 if func_name == 'sin':
   6436                     res = (exp_ia - ~exp_ia)/(2*QQbar.zeta(4))

AttributeError: 'SymbolicConstant' object has no attribute 'sqrt'

```




---

archive/issue_comments_031267.json:
```json
{
    "body": "Ah. That should be an easy fix... (must have fixed it in my branch elsewhere, perhaps in the process of #4276)",
    "created_at": "2008-11-03T21:47:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4282#issuecomment-31267",
    "user": "https://github.com/robertwb"
}
```

Ah. That should be an easy fix... (must have fixed it in my branch elsewhere, perhaps in the process of #4276)



---

archive/issue_comments_031268.json:
```json
{
    "body": "Attachment [4282-sqrt-fix.patch](tarball://root/attachments/some-uuid/ticket4282/4282-sqrt-fix.patch) by @robertwb created at 2008-11-13 23:12:22",
    "created_at": "2008-11-13T23:12:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4282#issuecomment-31268",
    "user": "https://github.com/robertwb"
}
```

Attachment [4282-sqrt-fix.patch](tarball://root/attachments/some-uuid/ticket4282/4282-sqrt-fix.patch) by @robertwb created at 2008-11-13 23:12:22



---

archive/issue_comments_031269.json:
```json
{
    "body": "I fixed the above bug.",
    "created_at": "2008-11-13T23:12:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4282#issuecomment-31269",
    "user": "https://github.com/robertwb"
}
```

I fixed the above bug.



---

archive/issue_comments_031270.json:
```json
{
    "body": "Referee report:\n\nI applied the patch to sage-3.2.1.alpha2. \n\n1. A doctest fails in calculus.py:\n\n```\nsage -t  devel/sage/sage/calculus/calculus.py\n**********************************************************************\nFile \"/home/was/build/sage-3.2.1.alpha1/devel/sage-main/sage/calculus/calculus.py\", line 1337:\n    sage: sin(pi/7).minpoly()\nException raised:\n    Traceback (most recent call last):\n      File \"/home/was/build/sage-3.2.1.alpha1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/was/build/sage-3.2.1.alpha1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/was/build/sage-3.2.1.alpha1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_43[5]>\", line 1, in <module>\n        sin(pi/Integer(7)).minpoly()###line 1337:\n    sage: sin(pi/7).minpoly()\n      File \"/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 1345, in minpoly\n        return QQbar(self).minpoly()\n      File \"/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/qqbar.py\", line 663, in __call__\n        return x._algebraic_(QQbar)\n      File \"/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 6471, in _algebraic_\n        exp_ia = exp(SR(-1).sqrt()*operand)._algebraic_(QQbar)\n      File \"/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 6460, in _algebraic_\n        rat_arg = (operand.imag()/(2*self.parent().pi()))._rational_()\n    AttributeError: 'SymbolicExpressionRing_class' object has no attribute 'pi'\n**********************************************************************\n1 items had failures:\n   1 of   6 in __main__.example_43\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/was/build/sage-3.2.1.alpha1/tmp/.doctest_calculus.py\n\n         [114.8 s]\n\nThe following tests failed:\n\n        sage -t  devel/sage/sage/calculus/calculus.py # 1 doctests failed\n```\n\n\n2. This sentence sounds like nonsense:\n\n```\n \t1335\t        NOTE: Failure of this function does not prove self is \n \t1336\t              not algebraic.  \n```\n\n\n3. There are now only three boring tests of symbolic minpoly. All the old interesting tests are now tests of minpoly_numeric.  I think all the minpoly_numeric tests should *also* be copied to the docstring for minpoly and tested using the new non-numerical algorithm.",
    "created_at": "2008-11-27T16:56:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4282#issuecomment-31270",
    "user": "https://github.com/williamstein"
}
```

Referee report:

I applied the patch to sage-3.2.1.alpha2. 

1. A doctest fails in calculus.py:

```
sage -t  devel/sage/sage/calculus/calculus.py
**********************************************************************
File "/home/was/build/sage-3.2.1.alpha1/devel/sage-main/sage/calculus/calculus.py", line 1337:
    sage: sin(pi/7).minpoly()
Exception raised:
    Traceback (most recent call last):
      File "/home/was/build/sage-3.2.1.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/was/build/sage-3.2.1.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/was/build/sage-3.2.1.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_43[5]>", line 1, in <module>
        sin(pi/Integer(7)).minpoly()###line 1337:
    sage: sin(pi/7).minpoly()
      File "/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 1345, in minpoly
        return QQbar(self).minpoly()
      File "/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/qqbar.py", line 663, in __call__
        return x._algebraic_(QQbar)
      File "/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 6471, in _algebraic_
        exp_ia = exp(SR(-1).sqrt()*operand)._algebraic_(QQbar)
      File "/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 6460, in _algebraic_
        rat_arg = (operand.imag()/(2*self.parent().pi()))._rational_()
    AttributeError: 'SymbolicExpressionRing_class' object has no attribute 'pi'
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_43
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/was/build/sage-3.2.1.alpha1/tmp/.doctest_calculus.py

         [114.8 s]

The following tests failed:

        sage -t  devel/sage/sage/calculus/calculus.py # 1 doctests failed
```


2. This sentence sounds like nonsense:

```
 	1335	        NOTE: Failure of this function does not prove self is 
 	1336	              not algebraic.  
```


3. There are now only three boring tests of symbolic minpoly. All the old interesting tests are now tests of minpoly_numeric.  I think all the minpoly_numeric tests should *also* be copied to the docstring for minpoly and tested using the new non-numerical algorithm.



---

archive/issue_comments_031271.json:
```json
{
    "body": "On point (3), should I simply consolidate minpoly_numeric into minpoly, or is it better to keep these two functions separate?",
    "created_at": "2008-12-03T01:21:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4282#issuecomment-31271",
    "user": "https://github.com/robertwb"
}
```

On point (3), should I simply consolidate minpoly_numeric into minpoly, or is it better to keep these two functions separate?



---

archive/issue_comments_031272.json:
```json
{
    "body": "> On point (3), should I simply consolidate minpoly_numeric into minpoly, or is \n> it better to keep these two functions separate? \n\nI think there should be one function the users sees called \"minpoly\" and it has an algorithm flag.  \n\n sage: foo.minpoly(algorithm='numerical')\n sage: foo.minpoly()\n sage: foo.minpoly(algorithm='something else clever...')\n\nWilliam",
    "created_at": "2008-12-04T22:15:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4282#issuecomment-31272",
    "user": "https://github.com/williamstein"
}
```

> On point (3), should I simply consolidate minpoly_numeric into minpoly, or is 
> it better to keep these two functions separate? 

I think there should be one function the users sees called "minpoly" and it has an algorithm flag.  

 sage: foo.minpoly(algorithm='numerical')
 sage: foo.minpoly()
 sage: foo.minpoly(algorithm='something else clever...')

William



---

archive/issue_comments_031273.json:
```json
{
    "body": "Changing assignee from @burcin to @robertwb.",
    "created_at": "2008-12-07T09:11:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4282#issuecomment-31273",
    "user": "https://github.com/robertwb"
}
```

Changing assignee from @burcin to @robertwb.



---

archive/issue_comments_031274.json:
```json
{
    "body": "OK, I believe I've addressed all the points above, and I expanded the documentation a bit more too.",
    "created_at": "2008-12-07T09:11:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4282#issuecomment-31274",
    "user": "https://github.com/robertwb"
}
```

OK, I believe I've addressed all the points above, and I expanded the documentation a bit more too.



---

archive/issue_comments_031275.json:
```json
{
    "body": "There are several mistakes in English in the new documentation that you added:\n\n* \"Note that simplification may be necessary to see the minimal polynomial is correct.\"  -- missing word \"if\"\n\n* \" If these are known, the numerical algorithm will be faster when these are give them explicitly.\" -- HUH?\n\n* \"use PARI's algdep to get a to get a candidate minpoly $f$.\" -- delete doubled \"to get a\".\n\n* \"Otherwise raise an error.\" -- say which exception is raised\n\n* \"Note that simplification may be necessary to see the minimal polynomial is correct.\" -- missing word \"if\".",
    "created_at": "2008-12-07T19:09:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4282#issuecomment-31275",
    "user": "https://github.com/williamstein"
}
```

There are several mistakes in English in the new documentation that you added:

* "Note that simplification may be necessary to see the minimal polynomial is correct."  -- missing word "if"

* " If these are known, the numerical algorithm will be faster when these are give them explicitly." -- HUH?

* "use PARI's algdep to get a to get a candidate minpoly $f$." -- delete doubled "to get a".

* "Otherwise raise an error." -- say which exception is raised

* "Note that simplification may be necessary to see the minimal polynomial is correct." -- missing word "if".



---

archive/issue_comments_031276.json:
```json
{
    "body": "Attachment [4282-symbolic-minpoly-referee-fixes.patch](tarball://root/attachments/some-uuid/ticket4282/4282-symbolic-minpoly-referee-fixes.patch) by @robertwb created at 2008-12-08 19:21:20\n\nI made these changes and refreshed the patch. On your first (= last) point, I prefer the word \"that\" as there is no question of whether or not the result is correct, it just may not be obvious without the right simplification.",
    "created_at": "2008-12-08T19:21:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4282#issuecomment-31276",
    "user": "https://github.com/robertwb"
}
```

Attachment [4282-symbolic-minpoly-referee-fixes.patch](tarball://root/attachments/some-uuid/ticket4282/4282-symbolic-minpoly-referee-fixes.patch) by @robertwb created at 2008-12-08 19:21:20

I made these changes and refreshed the patch. On your first (= last) point, I prefer the word "that" as there is no question of whether or not the result is correct, it just may not be obvious without the right simplification.



---

archive/issue_comments_031277.json:
```json
{
    "body": "I do not like that 'algebraic' and 'numerical' are not parallel constructions -- the parallel construction *WHICH APPEARS IN SOME OF THE DOCTESTS!* is 'algebraic' and 'numeric'.  I have attached a patch which fixes the doctests but doesn't change it to 'numeric'.  The patch does try to help the user -- instead of testing algorithm='numerical' it tests if algorithm starts with 'numeric'.\n\nI like the results and the performance:\n\nWith patch:\n\n```\nsage: cos(pi/22).minpoly()\nx^10 - 11/4*x^8 + 11/4*x^6 - 77/64*x^4 + 55/256*x^2 - 11/1024\nsage: cos(pi/56).minpoly()\nx^24 - 6*x^22 + 63/4*x^20 - 95/4*x^18 + 5813/256*x^16 - 917/64*x^14 + 3081/512*x^12 - 847/512*x^10 + 9323/32768*x^8 - 459/16384*x^6 + 175/131072*x^4 - 3/131072*x^2 + 1/16777216\n```\n\n\nWithout patch:\n\n\n```\nsage: cos(pi/22).minpoly()\nTraceback (most recent call last):\n...\nNotImplementedError: Could not prove minimal polynomial x^10 - 11/4*x^8 + 11/4*x^6 - 77/64*x^4 + 55/256*x^2 - 11/1024 (epsilon 3.14321532602626e-100)\nsage: cos(pi/56).minpoly()\nTraceback (most recent call last):\n...\nNotImplementedError: Could not prove minimal polynomial x^24 - 6*x^22 + 63/4*x^20 - 95/4*x^18 + 5813/256*x^16 - 917/64*x^14 + 3081/512*x^12 - 847/512*x^10 + 9323/32768*x^8 - 459/16384*x^6 + 175/131072*x^4 - 3/131072*x^2 + 1/16777216 (epsilon 2.29367823690213e-400)\n```\n\n\nWith patch:\n\n```\nsage: %timeit sqrt(5).minpoly()\n100 loops, best of 3: 14.3 ms per loop\nsage: %timeit sqrt(sqrt(5)).minpoly()\n10 loops, best of 3: 54 ms per loop\nsage: %timeit sqrt(sqrt(5) + sqrt(2)).minpoly()\n10 loops, best of 3: 115 ms per loop\n```\n\n\nWithout patch:\n\n\n```\nsage: %timeit sqrt(5).minpoly()\n10 loops, best of 3: 150 ms per loop\nsage: %timeit sqrt(sqrt(5)).minpoly()\n10 loops, best of 3: 174 ms per loop\nsage: %timeit sqrt(sqrt(5) + sqrt(2)).minpoly()\n10 loops, best of 3: 218 ms per loop\n```\n",
    "created_at": "2008-12-09T19:46:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4282#issuecomment-31277",
    "user": "https://github.com/ncalexan"
}
```

I do not like that 'algebraic' and 'numerical' are not parallel constructions -- the parallel construction *WHICH APPEARS IN SOME OF THE DOCTESTS!* is 'algebraic' and 'numeric'.  I have attached a patch which fixes the doctests but doesn't change it to 'numeric'.  The patch does try to help the user -- instead of testing algorithm='numerical' it tests if algorithm starts with 'numeric'.

I like the results and the performance:

With patch:

```
sage: cos(pi/22).minpoly()
x^10 - 11/4*x^8 + 11/4*x^6 - 77/64*x^4 + 55/256*x^2 - 11/1024
sage: cos(pi/56).minpoly()
x^24 - 6*x^22 + 63/4*x^20 - 95/4*x^18 + 5813/256*x^16 - 917/64*x^14 + 3081/512*x^12 - 847/512*x^10 + 9323/32768*x^8 - 459/16384*x^6 + 175/131072*x^4 - 3/131072*x^2 + 1/16777216
```


Without patch:


```
sage: cos(pi/22).minpoly()
Traceback (most recent call last):
...
NotImplementedError: Could not prove minimal polynomial x^10 - 11/4*x^8 + 11/4*x^6 - 77/64*x^4 + 55/256*x^2 - 11/1024 (epsilon 3.14321532602626e-100)
sage: cos(pi/56).minpoly()
Traceback (most recent call last):
...
NotImplementedError: Could not prove minimal polynomial x^24 - 6*x^22 + 63/4*x^20 - 95/4*x^18 + 5813/256*x^16 - 917/64*x^14 + 3081/512*x^12 - 847/512*x^10 + 9323/32768*x^8 - 459/16384*x^6 + 175/131072*x^4 - 3/131072*x^2 + 1/16777216 (epsilon 2.29367823690213e-400)
```


With patch:

```
sage: %timeit sqrt(5).minpoly()
100 loops, best of 3: 14.3 ms per loop
sage: %timeit sqrt(sqrt(5)).minpoly()
10 loops, best of 3: 54 ms per loop
sage: %timeit sqrt(sqrt(5) + sqrt(2)).minpoly()
10 loops, best of 3: 115 ms per loop
```


Without patch:


```
sage: %timeit sqrt(5).minpoly()
10 loops, best of 3: 150 ms per loop
sage: %timeit sqrt(sqrt(5)).minpoly()
10 loops, best of 3: 174 ms per loop
sage: %timeit sqrt(sqrt(5) + sqrt(2)).minpoly()
10 loops, best of 3: 218 ms per loop
```




---

archive/issue_comments_031278.json:
```json
{
    "body": "Attachment [4282-symbolic-minpoly-referee-fixes-2.patch](tarball://root/attachments/some-uuid/ticket4282/4282-symbolic-minpoly-referee-fixes-2.patch) by @ncalexan created at 2008-12-09 19:48:18",
    "created_at": "2008-12-09T19:48:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4282#issuecomment-31278",
    "user": "https://github.com/ncalexan"
}
```

Attachment [4282-symbolic-minpoly-referee-fixes-2.patch](tarball://root/attachments/some-uuid/ticket4282/4282-symbolic-minpoly-referee-fixes-2.patch) by @ncalexan created at 2008-12-09 19:48:18



---

archive/issue_comments_031279.json:
```json
{
    "body": "Thanks. \n\nI heartily agree with your change of \"numerical\" -> \"numeric\" (that's what I had originally, can't remember what the reason was for changing it).",
    "created_at": "2008-12-09T20:00:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4282#issuecomment-31279",
    "user": "https://github.com/robertwb"
}
```

Thanks. 

I heartily agree with your change of "numerical" -> "numeric" (that's what I had originally, can't remember what the reason was for changing it).



---

archive/issue_comments_031280.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-10T07:56:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4282#issuecomment-31280",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004527.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-12-10T07:56:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4282",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4282#event-4527"
}
```



---

archive/issue_comments_031281.json:
```json
{
    "body": "Merged all four patches in Sage 3.2.2.alpha1",
    "created_at": "2008-12-10T07:56:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4282#issuecomment-31281",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged all four patches in Sage 3.2.2.alpha1



---

archive/issue_comments_031282.json:
```json
{
    "body": "Note that trac_4282_part2_sqrt-fix.patch went in with quite a bit of offset, so hopefully this is cause by other changes to calculus.py and not a merge snafu:\n\n```\nsage-3.2.2.alpha1/devel/sage$ hg import trac_4282_part2_sqrt-fix.patch\napplying trac_4282_part2_sqrt-fix.patch\npatching file sage/calculus/calculus.py\nHunk #2 succeeded at 8359 with fuzz 1 (offset 386 lines).\n```\n\nIt builds and doctests pass, so I am confident hg did the right thing.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-10T08:13:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4282",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4282#issuecomment-31282",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Note that trac_4282_part2_sqrt-fix.patch went in with quite a bit of offset, so hopefully this is cause by other changes to calculus.py and not a merge snafu:

```
sage-3.2.2.alpha1/devel/sage$ hg import trac_4282_part2_sqrt-fix.patch
applying trac_4282_part2_sqrt-fix.patch
patching file sage/calculus/calculus.py
Hunk #2 succeeded at 8359 with fuzz 1 (offset 386 lines).
```

It builds and doctests pass, so I am confident hg did the right thing.

Cheers,

Michael
