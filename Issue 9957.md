# Issue 9957: Upgrade python to 2.7

archive/issues_009957.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  jhpalmieri leif jason kcrisman kini\n\nFrom the release notes:\n\nPython 2.7 was released on July 3rd, 2010.\n\nPython 2.7 is scheduled to be the last major version in the 2.x series before it moves into an extended maintenance period. This release contains many of the features that were first released in Python 3.1. Improvements in this release include:\n\n* An ordered dictionary type\n* New unittest features including test skipping, new assert methods, and test discovery\n* A much faster io module\n* Automatic numbering of fields in the str.format() method\n* Float repr improvements backported from 3.x\n* Tile support for Tkinter\n* A backport of the memoryview object from 3.x\n* Set literals\n* Set and dictionary comprehensions\n* Dictionary views\n* New syntax for nested with statements\n* The sysconfig module\n\nIssue created by migration from https://trac.sagemath.org/ticket/9958\n\n",
    "created_at": "2010-09-20T20:01:06Z",
    "labels": [
        "PLEASE CHANGE",
        "major",
        "bug"
    ],
    "title": "Upgrade python to 2.7",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9957",
    "user": "mhampton"
}
```
Assignee: tbd

CC:  jhpalmieri leif jason kcrisman kini

From the release notes:

Python 2.7 was released on July 3rd, 2010.

Python 2.7 is scheduled to be the last major version in the 2.x series before it moves into an extended maintenance period. This release contains many of the features that were first released in Python 3.1. Improvements in this release include:

* An ordered dictionary type
* New unittest features including test skipping, new assert methods, and test discovery
* A much faster io module
* Automatic numbering of fields in the str.format() method
* Float repr improvements backported from 3.x
* Tile support for Tkinter
* A backport of the memoryview object from 3.x
* Set literals
* Set and dictionary comprehensions
* Dictionary views
* New syntax for nested with statements
* The sysconfig module

Issue created by migration from https://trac.sagemath.org/ticket/9958





---

archive/issue_comments_099310.json:
```json
{
    "body": "First attempt is at:\n[http://sage.math.washington.edu/home/palmieri/SPKG/python-2.7.p0.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/python-2.7.p0.spkg)\n\nJohn (jhpalmieri) reports that this builds but Sage does not on sage.math, and \"packages for\ntwisted, zodb, pygments, and numpy don't build correctly.\"\n\nApparently the fix for [http://bugs.python.org/issue7491](http://bugs.python.org/issue7491) causes some of these problems.\n\nOn the numpy/scipy lists Ralf Gommers says \"Numpy 1.5 should work with Python 2.7 and 3.1 and not be too far off. In August hopefully\". \n\nSo it looks like [http://trac.sagemath.org/sage_trac/ticket/9808](http://trac.sagemath.org/sage_trac/ticket/9808) should fix the numpy issues.",
    "created_at": "2010-09-20T20:09:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99310",
    "user": "mhampton"
}
```

First attempt is at:
[http://sage.math.washington.edu/home/palmieri/SPKG/python-2.7.p0.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/python-2.7.p0.spkg)

John (jhpalmieri) reports that this builds but Sage does not on sage.math, and "packages for
twisted, zodb, pygments, and numpy don't build correctly."

Apparently the fix for [http://bugs.python.org/issue7491](http://bugs.python.org/issue7491) causes some of these problems.

On the numpy/scipy lists Ralf Gommers says "Numpy 1.5 should work with Python 2.7 and 3.1 and not be too far off. In August hopefully". 

So it looks like [http://trac.sagemath.org/sage_trac/ticket/9808](http://trac.sagemath.org/sage_trac/ticket/9808) should fix the numpy issues.



---

archive/issue_comments_099311.json:
```json
{
    "body": "Changing component from PLEASE CHANGE to packages.",
    "created_at": "2010-09-20T20:17:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99311",
    "user": "jhpalmieri"
}
```

Changing component from PLEASE CHANGE to packages.



---

archive/issue_comments_099312.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-09-24T12:28:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99312",
    "user": "leif"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_099313.json:
```json
{
    "body": "Replying to [comment:1 mhampton]:\n> First attempt is at:\n> [http://sage.math.washington.edu/home/palmieri/SPKG/python-2.7.p0.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/python-2.7.p0.spkg)\n> \n> John (jhpalmieri) reports that this builds but Sage does not on sage.math, and \"packages for\n> twisted, zodb, pygments, and numpy don't build correctly.\"\n> \n> Apparently the fix for [http://bugs.python.org/issue7491](http://bugs.python.org/issue7491) causes some of these problems.\n\nThis fix has been included in python-2.6.5 onwards. We are using 2.6.5 which includes this fix and everything builds (haven't tried 2.7 yet). The only problem we have is with [http://github.com/cschwan/sage-on-gentoo/issues#issue/1](http://github.com/cschwan/sage-on-gentoo/issues#issue/1) so I think it is unfair to single out this issue as the source of problems.",
    "created_at": "2010-10-04T00:03:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99313",
    "user": "fbissey"
}
```

Replying to [comment:1 mhampton]:
> First attempt is at:
> [http://sage.math.washington.edu/home/palmieri/SPKG/python-2.7.p0.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/python-2.7.p0.spkg)
> 
> John (jhpalmieri) reports that this builds but Sage does not on sage.math, and "packages for
> twisted, zodb, pygments, and numpy don't build correctly."
> 
> Apparently the fix for [http://bugs.python.org/issue7491](http://bugs.python.org/issue7491) causes some of these problems.

This fix has been included in python-2.6.5 onwards. We are using 2.6.5 which includes this fix and everything builds (haven't tried 2.7 yet). The only problem we have is with [http://github.com/cschwan/sage-on-gentoo/issues#issue/1](http://github.com/cschwan/sage-on-gentoo/issues#issue/1) so I think it is unfair to single out this issue as the source of problems.



---

archive/issue_comments_099314.json:
```json
{
    "body": "Is there still any interest in this upgrade? I wanted to use ordered dictionaries, which require 2.7. Unfortunately, active participation in this ticket is beyond my current capabilities...",
    "created_at": "2011-02-27T21:19:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99314",
    "user": "novoselt"
}
```

Is there still any interest in this upgrade? I wanted to use ordered dictionaries, which require 2.7. Unfortunately, active participation in this ticket is beyond my current capabilities...



---

archive/issue_comments_099315.json:
```json
{
    "body": "It will happen at least in sage-on-gentoo as we are following the system python.\nI have a couple of things in our tree to fix problems with python-2.6.5 and 2.6.6\nwe are looking into 2.7 now. I should post any patch to have it working here.\n\nWe are not talking about using the new capabilities just porting, I imagine my\ncounterpart in Mandriva does the same.",
    "created_at": "2011-02-27T21:27:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99315",
    "user": "fbissey"
}
```

It will happen at least in sage-on-gentoo as we are following the system python.
I have a couple of things in our tree to fix problems with python-2.6.5 and 2.6.6
we are looking into 2.7 now. I should post any patch to have it working here.

We are not talking about using the new capabilities just porting, I imagine my
counterpart in Mandriva does the same.



---

archive/issue_comments_099316.json:
```json
{
    "body": "I just attached a patch that is needed for python 2.6.5 and later.",
    "created_at": "2011-02-28T09:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99316",
    "user": "fbissey"
}
```

I just attached a patch that is needed for python 2.6.5 and later.



---

archive/issue_comments_099317.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2011-02-28T09:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99317",
    "user": "fbissey"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_099318.json:
```json
{
    "body": "Build sage-4.6.2 (and dependency) against python-2.7.1 on OS X. I get a lot of the following\n\n```\nExpected nothing\nGot:\n    Failure in _test_pickling:\n    Traceback (most recent call last):\n      File \"/Users/frb15/Desktop/Gentoo/usr/lib/python2.7/site-packages/sage/misc/sage_unittest.py\", line 275, in run\n        test_method(tester = tester)\n      File \"/Users/frb15/Desktop/Gentoo/usr/lib/python2.7/site-packages/sage/misc/sage_unittest.py\", line 498, in _test_pickling\n        tester.assertEqual(loads(dumps(self._instance)), self._instance)\n      File \"/Users/frb15/Desktop/Gentoo/usr/lib/python2.7/unittest/case.py\", line 493, in assertEqual\n        assertion_func = self._getAssertEqualityFunc(first, second)\n      File \"/Users/frb15/Desktop/Gentoo/usr/lib/python2.7/unittest/case.py\", line 476, in _getAssertEqualityFunc\n        asserter = self._type_equality_funcs.get(type(first))\n    AttributeError: 'InstanceTester' object has no attribute '_type_equality_funcs'\n    ------------------------------------------------------------\n```\n\nI patched python with the cpickle patch. Any ideas?",
    "created_at": "2011-03-11T03:44:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99318",
    "user": "fbissey"
}
```

Build sage-4.6.2 (and dependency) against python-2.7.1 on OS X. I get a lot of the following

```
Expected nothing
Got:
    Failure in _test_pickling:
    Traceback (most recent call last):
      File "/Users/frb15/Desktop/Gentoo/usr/lib/python2.7/site-packages/sage/misc/sage_unittest.py", line 275, in run
        test_method(tester = tester)
      File "/Users/frb15/Desktop/Gentoo/usr/lib/python2.7/site-packages/sage/misc/sage_unittest.py", line 498, in _test_pickling
        tester.assertEqual(loads(dumps(self._instance)), self._instance)
      File "/Users/frb15/Desktop/Gentoo/usr/lib/python2.7/unittest/case.py", line 493, in assertEqual
        assertion_func = self._getAssertEqualityFunc(first, second)
      File "/Users/frb15/Desktop/Gentoo/usr/lib/python2.7/unittest/case.py", line 476, in _getAssertEqualityFunc
        asserter = self._type_equality_funcs.get(type(first))
    AttributeError: 'InstanceTester' object has no attribute '_type_equality_funcs'
    ------------------------------------------------------------
```

I patched python with the cpickle patch. Any ideas?



---

archive/issue_comments_099319.json:
```json
{
    "body": "A lot of \"doctest... DeprecationWarning: ...\" lines that were expected are just gone. Which fails the test.",
    "created_at": "2011-03-11T03:48:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99319",
    "user": "fbissey"
}
```

A lot of "doctest... DeprecationWarning: ..." lines that were expected are just gone. Which fails the test.



---

archive/issue_comments_099320.json:
```json
{
    "body": "Lots of numerical and a little bit of formatting noise.",
    "created_at": "2011-03-11T03:50:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99320",
    "user": "fbissey"
}
```

Lots of numerical and a little bit of formatting noise.



---

archive/issue_comments_099321.json:
```json
{
    "body": "Ok so now I understand the differences between unittest and unittest2 which is shipped with python-2.7. This will require a massive number of non-backward compatible changes. I am starting to experiment with a few sage components but that promise to be long and boring.",
    "created_at": "2011-03-27T03:47:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99321",
    "user": "fbissey"
}
```

Ok so now I understand the differences between unittest and unittest2 which is shipped with python-2.7. This will require a massive number of non-backward compatible changes. I am starting to experiment with a few sage components but that promise to be long and boring.



---

archive/issue_comments_099322.json:
```json
{
    "body": "I have attached a log of sage -testall. This is a sage-on-gentoo install a few tests are expected to fail [https://github.com/cschwan/sage-on-gentoo/wiki/Known-test-failures](https://github.com/cschwan/sage-on-gentoo/wiki/Known-test-failures) but it should give you an idea of the problems we face.",
    "created_at": "2011-04-08T02:41:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99322",
    "user": "fbissey"
}
```

I have attached a log of sage -testall. This is a sage-on-gentoo install a few tests are expected to fail [https://github.com/cschwan/sage-on-gentoo/wiki/Known-test-failures](https://github.com/cschwan/sage-on-gentoo/wiki/Known-test-failures) but it should give you an idea of the problems we face.



---

archive/issue_comments_099323.json:
```json
{
    "body": "I attached a log of test failures with 4.7.alpha4 (+ #7377). It is mostly number of decimals and messages. I added PYTHONWARNINGS=default to sage-env so I collected extra messages. The most important one being the deprecations of \"sets\".\n\nThere are 3 tests killed reason currently unknown. And a few that may need special attention.",
    "created_at": "2011-04-14T09:21:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99323",
    "user": "fbissey"
}
```

I attached a log of test failures with 4.7.alpha4 (+ #7377). It is mostly number of decimals and messages. I added PYTHONWARNINGS=default to sage-env so I collected extra messages. The most important one being the deprecations of "sets".

There are 3 tests killed reason currently unknown. And a few that may need special attention.



---

archive/issue_comments_099324.json:
```json
{
    "body": "A little bit more details, these are curious:\n\n```\nsage -t -long  -force_lib devel/sage-main/sage/rings/padics/padic_capped_relative_element.pyx\n**********************************************************************\nFile \"/usr/share/sage/devel/sage-main/sage/rings/padics/padic_capped_relative_element.pyx\", line 2297:\n    sage: hash(R(-1)) \nExpected:\n    95367431640624\nGot:\n    1977800240\n```\n\n\n\n```\nsage -t -long  -force_lib devel/sage-main/sage/combinat/words/suffix_trees.py\n**********************************************************************\nFile \"/usr/share/sage/devel/sage-main/sage/combinat/words/suffix_trees.py\", line 1345:\n    sage: t.trie_type_dict() == dict([[(0, W(\"a\")), 4], [(0, W(\"b\")), 3], [(3, W(\"a\")), 2], [(4, W(\"b\")), 5], [(5, W(\"a\")), 1]])\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nsage -t -long  -force_lib devel/sage-main/sage/combinat/words/suffix_trees.py\n**********************************************************************\nFile \"/usr/share/sage/devel/sage-main/sage/combinat/words/suffix_trees.py\", line 1345:\n    sage: t.trie_type_dict() == dict([[(0, W(\"a\")), 4], [(0, W(\"b\")), 3], [(3, W(\"a\")), 2], [(4, W(\"b\")), 5], [(5, W(\"a\")), 1]])\nExpected:\n    True\nGot:\n    False\n**********************************************************************\n```\n\nThis one doesn't worry me as much but should be looked at\n\n```\nsage -t -long  -force_lib devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py\n**********************************************************************\nFile \"/usr/share/sage/devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py\", line 22:\n    sage: it.next()\nExpected:\n    word: 5645\nGot:\n    word: 4564\n**********************************************************************\nFile \"/usr/share/sage/devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py\", line 24:\n    sage: it.next()\nExpected:\n    word: 4564\nGot:\n    word: 5645\n**********************************************************************\n```\n\n\n\n```\nsage -t -long  -force_lib devel/sage-main/sage/structure/parent.pyx\n**********************************************************************\nFile \"/usr/share/sage/devel/sage-main/sage/structure/parent.pyx\", line 634:\n    sage: CCls()._test_eq()\nExpected:\n    Traceback (most recent call last):\n    ...\n    AssertionError: <class '__main__.CCls'> == None\nGot nothing\n```\n\n\nThe following were killed:\n\n```\nsage -t -long  -force_lib devel/sage-main/sage/rings/homset.py # Killed/crashed\nsage -t -long  -force_lib devel/sage-main/sage/schemes/generic/scheme.py # Killed/crashed\n```\n\nIn my original run \n\n```\nsage -t -long -force_lib \"devel/sage-main/sage/rings/morphism.pyx\"\n```\n\nalso got killed but not in a subsequent run after I adopted a small change in sage-doctest to get rid of PYTHONWARNINGS=default in sage-env.\n\nExample of killed test:\n\n```\nsage -t -long -verbose -force_lib \"devel/sage-main/sage/rings/homset.py\"\n...\n\nTrying:\n    phi = S.hom([b,a])###line 141:_sage_    >>> phi = S.hom([b,a])\nExpecting nothing\nok\nTrying:\n    phi == loads(dumps(phi))###line 142:_sage_    >>> phi == loads(dumps(phi))\nExpecting:\n    True\n/usr/lib64/libcsage.so(print_backtrace+0x24)[0x7f83de940534]\n/usr/lib64/libcsage.so(sigdie+0x1d)[0x7f83de9405cd]\n/usr/lib64/libcsage.so(sage_signal_handler+0x131)[0x7f83de940741]\n/lib64/libpthread.so.0(+0xfae0)[0x7f83e2385ae0]\n/usr/lib64/libsingular.so.3(_Z9id_DeletePP10sip_sidealP9sip_sring+0x53)[0x7f83c5c48383]\n/usr/lib64/python2.7/site-packages/sage/libs/singular/groebner_strategy.so(+0x388d)[0x7f83ad27488d]\n/usr/lib64/libpython2.7.so.1.0(PyDict_Clear+0xfc)[0x7f83e261597c]\n/usr/lib64/libpython2.7.so.1.0(+0x82a09)[0x7f83e2615a09]\n/usr/lib64/libpython2.7.so.1.0(+0x112e7e)[0x7f83e26a5e7e]\n/usr/lib64/libpython2.7.so.1.0(_PyObject_GC_Malloc+0x11c)[0x7f83e26a684c]\n/usr/lib64/libpython2.7.so.1.0(_PyObject_GC_New+0xd)[0x7f83e26a685d]\n/usr/lib64/libpython2.7.so.1.0(+0x7fe11)[0x7f83e2612e11]\n/usr/lib64/libpython2.7.so.1.0(PyObject_Call+0x53)[0x7f83e25de453]\n/usr/lib64/python2.7/site-packages/sage/rings/polynomial/polydict.so(+0x168c3)[0x7f83c8f378c3]\n/usr/lib64/libpython2.7.so.1.0(+0xa0468)[0x7f83e2633468]\n/usr/lib64/libpython2.7.so.1.0(PyObject_Call+0x53)[0x7f83e25de453]\n/usr/lib64/python2.7/site-packages/sage/rings/polynomial/polydict.so(+0xa451)[0x7f83c8f2b451]\n/usr/lib64/libpython2.7.so.1.0(PyObject_Call+0x53)[0x7f83e25de453]\n/usr/lib64/libpython2.7.so.1.0(PyEval_CallObjectWithKeywords+0x47)[0x7f83e2670ca7]\n/usr/lib64/python2.7/lib-dynload/cPickle.so(+0x5f06)[0x7f83dcb2df06]\n/usr/lib64/python2.7/lib-dynload/cPickle.so(+0xaf47)[0x7f83dcb32f47]\n/usr/lib64/libpython2.7.so.1.0(PyObject_Call+0x53)[0x7f83e25de453]\n/usr/lib64/python2.7/site-packages/sage/structure/sage_object.so(+0x152fc)[0x7f83dc7012fc]\n/usr/lib64/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x56bc)[0x7f83e267692c]\n/usr/lib64/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x88d)[0x7f83e26781dd]\n/usr/lib64/libpython2.7.so.1.0(PyEval_EvalCode+0x32)[0x7f83e26782f2]\n/usr/lib64/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x5a78)[0x7f83e2676ce8]\n/usr/lib64/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x88d)[0x7f83e26781dd]\n/usr/lib64/libpython2.7.so.1.0(+0x71282)[0x7f83e2604282]\n/usr/lib64/libpython2.7.so.1.0(PyObject_Call+0x53)[0x7f83e25de453]\n/usr/lib64/libpython2.7.so.1.0(+0x5a24f)[0x7f83e25ed24f]\n/usr/lib64/libpython2.7.so.1.0(PyObject_Call+0x53)[0x7f83e25de453]\n/usr/lib64/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x491d)[0x7f83e2675b8d]\n/usr/lib64/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x88d)[0x7f83e26781dd]\n/usr/lib64/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x522e)[0x7f83e267649e]\n/usr/lib64/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x88d)[0x7f83e26781dd]\n/usr/lib64/libpython2.7.so.1.0(+0x71282)[0x7f83e2604282]\n/usr/lib64/libpython2.7.so.1.0(PyObject_Call+0x53)[0x7f83e25de453]\n/usr/lib64/libpython2.7.so.1.0(+0x5a24f)[0x7f83e25ed24f]\n/usr/lib64/libpython2.7.so.1.0(PyObject_Call+0x53)[0x7f83e25de453]\n/usr/lib64/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x491d)[0x7f83e2675b8d]\n/usr/lib64/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x88d)[0x7f83e26781dd]\n/usr/lib64/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x522e)[0x7f83e267649e]\n/usr/lib64/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x88d)[0x7f83e26781dd]\n/usr/lib64/libpython2.7.so.1.0(+0x7138b)[0x7f83e260438b]\n/usr/lib64/libpython2.7.so.1.0(PyObject_Call+0x53)[0x7f83e25de453]\n/usr/lib64/libpython2.7.so.1.0(+0x5a24f)[0x7f83e25ed24f]\n/usr/lib64/libpython2.7.so.1.0(PyObject_Call+0x53)[0x7f83e25de453]\n/usr/lib64/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x491d)[0x7f83e2675b8d]\n/usr/lib64/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x88d)[0x7f83e26781dd]\n/usr/lib64/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x522e)[0x7f83e267649e]\n/usr/lib64/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x88d)[0x7f83e26781dd]\n/usr/lib64/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x522e)[0x7f83e267649e]\n/usr/lib64/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x88d)[0x7f83e26781dd]\n/usr/lib64/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x522e)[0x7f83e267649e]\n/usr/lib64/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x88d)[0x7f83e26781dd]\n/usr/lib64/libpython2.7.so.1.0(PyEval_EvalCode+0x32)[0x7f83e26782f2]\n/usr/lib64/libpython2.7.so.1.0(+0xff25c)[0x7f83e269225c]\n/usr/lib64/libpython2.7.so.1.0(PyRun_FileExFlags+0x90)[0x7f83e2693090]\n/usr/lib64/libpython2.7.so.1.0(PyRun_SimpleFileExFlags+0x1ff)[0x7f83e2693c6f]\n/usr/lib64/libpython2.7.so.1.0(Py_Main+0xb53)[0x7f83e26a4fc3]\n/lib64/libc.so.6(__libc_start_main+0xfd)[0x7f83e201cb6d]\n/usr/bin/python2.7[0x4008a9]\n\n------------------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occurred in Sage.\nThis probably occurred because a *compiled* component of Sage has a bug\nin it and is not properly wrapped with sig_on(), sig_off(). You might\nwant to run Sage under gdb with 'sage -gdb' to debug this.\nSage will now terminate.\n------------------------------------------------------------------------\nThe doctested process was killed by signal 11\n         [2.5 s]\n```\n",
    "created_at": "2011-04-14T23:27:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99324",
    "user": "fbissey"
}
```

A little bit more details, these are curious:

```
sage -t -long  -force_lib devel/sage-main/sage/rings/padics/padic_capped_relative_element.pyx
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/rings/padics/padic_capped_relative_element.pyx", line 2297:
    sage: hash(R(-1)) 
Expected:
    95367431640624
Got:
    1977800240
```



```
sage -t -long  -force_lib devel/sage-main/sage/combinat/words/suffix_trees.py
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/combinat/words/suffix_trees.py", line 1345:
    sage: t.trie_type_dict() == dict([[(0, W("a")), 4], [(0, W("b")), 3], [(3, W("a")), 2], [(4, W("b")), 5], [(5, W("a")), 1]])
Expected:
    True
Got:
    False
**********************************************************************
sage -t -long  -force_lib devel/sage-main/sage/combinat/words/suffix_trees.py
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/combinat/words/suffix_trees.py", line 1345:
    sage: t.trie_type_dict() == dict([[(0, W("a")), 4], [(0, W("b")), 3], [(3, W("a")), 2], [(4, W("b")), 5], [(5, W("a")), 1]])
Expected:
    True
Got:
    False
**********************************************************************
```

This one doesn't worry me as much but should be looked at

```
sage -t -long  -force_lib devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py", line 22:
    sage: it.next()
Expected:
    word: 5645
Got:
    word: 4564
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py", line 24:
    sage: it.next()
Expected:
    word: 4564
Got:
    word: 5645
**********************************************************************
```



```
sage -t -long  -force_lib devel/sage-main/sage/structure/parent.pyx
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/structure/parent.pyx", line 634:
    sage: CCls()._test_eq()
Expected:
    Traceback (most recent call last):
    ...
    AssertionError: <class '__main__.CCls'> == None
Got nothing
```


The following were killed:

```
sage -t -long  -force_lib devel/sage-main/sage/rings/homset.py # Killed/crashed
sage -t -long  -force_lib devel/sage-main/sage/schemes/generic/scheme.py # Killed/crashed
```

In my original run 

```
sage -t -long -force_lib "devel/sage-main/sage/rings/morphism.pyx"
```

also got killed but not in a subsequent run after I adopted a small change in sage-doctest to get rid of PYTHONWARNINGS=default in sage-env.

Example of killed test:

```
sage -t -long -verbose -force_lib "devel/sage-main/sage/rings/homset.py"
...

Trying:
    phi = S.hom([b,a])###line 141:_sage_    >>> phi = S.hom([b,a])
Expecting nothing
ok
Trying:
    phi == loads(dumps(phi))###line 142:_sage_    >>> phi == loads(dumps(phi))
Expecting:
    True
/usr/lib64/libcsage.so(print_backtrace+0x24)[0x7f83de940534]
/usr/lib64/libcsage.so(sigdie+0x1d)[0x7f83de9405cd]
/usr/lib64/libcsage.so(sage_signal_handler+0x131)[0x7f83de940741]
/lib64/libpthread.so.0(+0xfae0)[0x7f83e2385ae0]
/usr/lib64/libsingular.so.3(_Z9id_DeletePP10sip_sidealP9sip_sring+0x53)[0x7f83c5c48383]
/usr/lib64/python2.7/site-packages/sage/libs/singular/groebner_strategy.so(+0x388d)[0x7f83ad27488d]
/usr/lib64/libpython2.7.so.1.0(PyDict_Clear+0xfc)[0x7f83e261597c]
/usr/lib64/libpython2.7.so.1.0(+0x82a09)[0x7f83e2615a09]
/usr/lib64/libpython2.7.so.1.0(+0x112e7e)[0x7f83e26a5e7e]
/usr/lib64/libpython2.7.so.1.0(_PyObject_GC_Malloc+0x11c)[0x7f83e26a684c]
/usr/lib64/libpython2.7.so.1.0(_PyObject_GC_New+0xd)[0x7f83e26a685d]
/usr/lib64/libpython2.7.so.1.0(+0x7fe11)[0x7f83e2612e11]
/usr/lib64/libpython2.7.so.1.0(PyObject_Call+0x53)[0x7f83e25de453]
/usr/lib64/python2.7/site-packages/sage/rings/polynomial/polydict.so(+0x168c3)[0x7f83c8f378c3]
/usr/lib64/libpython2.7.so.1.0(+0xa0468)[0x7f83e2633468]
/usr/lib64/libpython2.7.so.1.0(PyObject_Call+0x53)[0x7f83e25de453]
/usr/lib64/python2.7/site-packages/sage/rings/polynomial/polydict.so(+0xa451)[0x7f83c8f2b451]
/usr/lib64/libpython2.7.so.1.0(PyObject_Call+0x53)[0x7f83e25de453]
/usr/lib64/libpython2.7.so.1.0(PyEval_CallObjectWithKeywords+0x47)[0x7f83e2670ca7]
/usr/lib64/python2.7/lib-dynload/cPickle.so(+0x5f06)[0x7f83dcb2df06]
/usr/lib64/python2.7/lib-dynload/cPickle.so(+0xaf47)[0x7f83dcb32f47]
/usr/lib64/libpython2.7.so.1.0(PyObject_Call+0x53)[0x7f83e25de453]
/usr/lib64/python2.7/site-packages/sage/structure/sage_object.so(+0x152fc)[0x7f83dc7012fc]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x56bc)[0x7f83e267692c]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x88d)[0x7f83e26781dd]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalCode+0x32)[0x7f83e26782f2]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x5a78)[0x7f83e2676ce8]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x88d)[0x7f83e26781dd]
/usr/lib64/libpython2.7.so.1.0(+0x71282)[0x7f83e2604282]
/usr/lib64/libpython2.7.so.1.0(PyObject_Call+0x53)[0x7f83e25de453]
/usr/lib64/libpython2.7.so.1.0(+0x5a24f)[0x7f83e25ed24f]
/usr/lib64/libpython2.7.so.1.0(PyObject_Call+0x53)[0x7f83e25de453]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x491d)[0x7f83e2675b8d]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x88d)[0x7f83e26781dd]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x522e)[0x7f83e267649e]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x88d)[0x7f83e26781dd]
/usr/lib64/libpython2.7.so.1.0(+0x71282)[0x7f83e2604282]
/usr/lib64/libpython2.7.so.1.0(PyObject_Call+0x53)[0x7f83e25de453]
/usr/lib64/libpython2.7.so.1.0(+0x5a24f)[0x7f83e25ed24f]
/usr/lib64/libpython2.7.so.1.0(PyObject_Call+0x53)[0x7f83e25de453]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x491d)[0x7f83e2675b8d]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x88d)[0x7f83e26781dd]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x522e)[0x7f83e267649e]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x88d)[0x7f83e26781dd]
/usr/lib64/libpython2.7.so.1.0(+0x7138b)[0x7f83e260438b]
/usr/lib64/libpython2.7.so.1.0(PyObject_Call+0x53)[0x7f83e25de453]
/usr/lib64/libpython2.7.so.1.0(+0x5a24f)[0x7f83e25ed24f]
/usr/lib64/libpython2.7.so.1.0(PyObject_Call+0x53)[0x7f83e25de453]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x491d)[0x7f83e2675b8d]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x88d)[0x7f83e26781dd]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x522e)[0x7f83e267649e]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x88d)[0x7f83e26781dd]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x522e)[0x7f83e267649e]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x88d)[0x7f83e26781dd]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalFrameEx+0x522e)[0x7f83e267649e]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalCodeEx+0x88d)[0x7f83e26781dd]
/usr/lib64/libpython2.7.so.1.0(PyEval_EvalCode+0x32)[0x7f83e26782f2]
/usr/lib64/libpython2.7.so.1.0(+0xff25c)[0x7f83e269225c]
/usr/lib64/libpython2.7.so.1.0(PyRun_FileExFlags+0x90)[0x7f83e2693090]
/usr/lib64/libpython2.7.so.1.0(PyRun_SimpleFileExFlags+0x1ff)[0x7f83e2693c6f]
/usr/lib64/libpython2.7.so.1.0(Py_Main+0xb53)[0x7f83e26a4fc3]
/lib64/libc.so.6(__libc_start_main+0xfd)[0x7f83e201cb6d]
/usr/bin/python2.7[0x4008a9]

------------------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occurred in Sage.
This probably occurred because a *compiled* component of Sage has a bug
in it and is not properly wrapped with sig_on(), sig_off(). You might
want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate.
------------------------------------------------------------------------
The doctested process was killed by signal 11
         [2.5 s]
```




---

archive/issue_comments_099325.json:
```json
{
    "body": "small patch to sage-doctest in sage_script to reenable sage's deprecation warnings. Idea by my friend Steve Trogdon.",
    "created_at": "2011-04-15T00:10:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99325",
    "user": "fbissey"
}
```

small patch to sage-doctest in sage_script to reenable sage's deprecation warnings. Idea by my friend Steve Trogdon.



---

archive/issue_comments_099326.json:
```json
{
    "body": "Attachment\n\nthis form of comparison is removed in python 2.6.5 and later, refreshed using --git.",
    "created_at": "2011-04-15T00:16:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99326",
    "user": "fbissey"
}
```

Attachment

this form of comparison is removed in python 2.6.5 and later, refreshed using --git.



---

archive/issue_comments_099327.json:
```json
{
    "body": "It looks like the crash problems originates somewhere in libsingular\n\n```\nsage: f = Zmod(6).cover()\nsage: f.kernel()\nPrincipal ideal (6) of Integer Ring\nsage: R.<x,y> = PolynomialRing(QQ, 2)\nsage: S.<a,b> = R.quo(x^2 + y^2)\nsage: phi = S.cover()\nsage: phi == loads(dumps(phi))\nTrue\nsage: phi == R.quo(x^2 + y^3).cover()\n\nProgram received signal SIGSEGV, Segmentation fault.\nid_Delete (h=0x50687d8, r=0x0) at ideals.cc:127\n127     ideals.cc: No such file or directory.\n        in ideals.cc\n(gdb) bt\n#0  id_Delete (h=0x50687d8, r=0x0) at ideals.cc:127\n#1  0x00007fffb9670b49 in __pyx_pf_4sage_4libs_8singular_17groebner_strategy_16GroebnerStrategy_1__dealloc__ (\n    o=<value optimized out>) at sage/libs/singular/groebner_strategy.cpp:2570\n#2  __pyx_tp_dealloc_4sage_4libs_8singular_17groebner_strategy_GroebnerStrategy (o=<value optimized out>)\n    at sage/libs/singular/groebner_strategy.cpp:3190\n#3  0x00007ffff7aa98c7 in PyDict_Clear (op=<value optimized out>) at Objects/dictobject.c:891\n#4  0x00007ffff7aa990f in dict_tp_clear (op=<value optimized out>) at Objects/dictobject.c:2088\n#5  0x00007ffff7b32f27 in delete_garbage (generation=0) at Modules/gcmodule.c:769\n#6  collect (generation=0) at Modules/gcmodule.c:930\n#7  0x00007ffff7b33616 in collect_generations (basicsize=<value optimized out>) at Modules/gcmodule.c:996\n#8  _PyObject_GC_Malloc (basicsize=<value optimized out>) at Modules/gcmodule.c:1457\n#9  0x00007ffff7ac4a96 in PyType_GenericAlloc (type=0x7ffff7d9ad40, nitems=0) at Objects/typeobject.c:744\n#10 0x00007ffff7a8d256 in BaseException_new (type=<value optimized out>, args=<value optimized out>, kwds=<value optimized out>)\n    at Objects/exceptions.c:34\n#11 0x00007ffff7ac57b5 in type_call (type=0x7ffff7d9ad40, args=0x4ae46d0, kwds=0x0) at Objects/typeobject.c:712\n#12 0x00007ffff7a77539 in PyObject_Call (func=0x7ffff7d9ad40, arg=0x4ae46d0, kw=0x0) at Objects/abstract.c:2529\n#13 0x00007ffff7b00b45 in PyEval_CallObjectWithKeywords (func=0x7ffff7d9ad40, arg=0x4ae46d0, kw=0x0) at Python/ceval.c:3881\n#14 0x00007ffff7b10443 in PyErr_NormalizeException (exc=0x7fffffffa778, val=0x7fffffffa770, tb=0x7fffffffa768)\n    at Python/errors.c:190\n#15 0x00007fffe433021c in __Pyx_GetException (type=0x7fffffffa7c0, value=0x7fffffffa7b8, tb=0x7fffffffa7c8)\n    at sage/structure/parent.c:20909\n#16 0x00007fffe433e4d1 in __pyx_pf_4sage_9structure_6parent_6Parent_2element_class (__pyx_v_self=0x4aea500, \n    unused=<value optimized out>) at sage/structure/parent.c:4251\n#17 0x00007ffff7aac1e2 in PyCFunction_Call (func=0x504ebd8, arg=0x7ffff7f81050, kw=<value optimized out>)\n    at Objects/methodobject.c:90\n#18 0x00007ffff7a77539 in PyObject_Call (func=0x504ebd8, arg=0x7ffff7f81050, kw=0x0) at Objects/abstract.c:2529\n#19 0x00007ffff7b00b45 in PyEval_CallObjectWithKeywords (func=0x504ebd8, arg=0x7ffff7f81050, kw=0x0) at Python/ceval.c:3881\n#20 0x00007ffff7a8b51f in methoddescr_call (descr=<value optimized out>, args=0x7ffff7f81050, kwds=0x0)\n    at Objects/descrobject.c:246\n#21 0x00007ffff7a77539 in PyObject_Call (func=0x138e950, arg=0x7ffff7e9c050, kw=0x0) at Objects/abstract.c:2529\n#22 0x00007ffff7b05efe in do_call (f=<value optimized out>, throwflag=<value optimized out>) at Python/ceval.c:4230\n#23 call_function (f=<value optimized out>, throwflag=<value optimized out>) at Python/ceval.c:4035\n#24 PyEval_EvalFrameEx (f=<value optimized out>, throwflag=<value optimized out>) at Python/ceval.c:2665\n#25 0x00007ffff7b07b65 in PyEval_EvalCodeEx (co=0x1159e30, globals=<value optimized out>, locals=<value optimized out>, \n    args=<value optimized out>, argcount=3, kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:3252\n#26 0x00007ffff7a99a97 in function_call (func=0x115d5f0, arg=0xfadeb0, kw=0x0) at Objects/funcobject.c:526\n#27 0x00007ffff7a77539 in PyObject_Call (func=0x115d5f0, arg=0xfadeb0, kw=0x0) at Objects/abstract.c:2529\n#28 0x00007ffff7a77cca in PyObject_CallFunctionObjArgs (callable=0x115d5f0) at Objects/abstract.c:2760\n#29 0x00007ffff7ac8a8e in slot_tp_descr_get (self=0x13179d0, obj=0x4aea500, type=0x19e91f0) at Objects/typeobject.c:5621\n#30 0x00007ffff7aae433 in _PyObject_GenericGetAttrWithDict (obj=0x4aea500, name=0x13c5a78, dict=0x5068fb0) at Objects/object.c:1432\n#31 0x00007ffff7aae4d1 in PyObject_GenericGetAttr (obj=<value optimized out>, name=<value optimized out>) at Objects/object.c:1454\n#32 0x00007fffe434ed62 in __pyx_tp_getattro_4sage_9structure_6parent_Parent (o=0x4aea500, n=0x13c5a78)\n    at sage/structure/parent.c:18702\n#33 0x00007ffff7aad8f4 in PyObject_GetAttr (v=0x4aea500, name=<value optimized out>) at Objects/object.c:1189\n#34 0x00007ffff7afdbab in builtin_hasattr (self=<value optimized out>, args=<value optimized out>) at Python/bltinmodule.c:885\n#35 0x00007ffff7aac1a0 in PyCFunction_Call (func=0x7ffff7fae3b0, arg=0x503d680, kw=<value optimized out>)\n    at Objects/methodobject.c:81\n#36 0x00007ffff7b05ba3 in call_function (f=<value optimized out>, throwflag=<value optimized out>) at Python/ceval.c:4012\n#37 PyEval_EvalFrameEx (f=<value optimized out>, throwflag=<value optimized out>) at Python/ceval.c:2665\n#38 0x00007ffff7b05cfa in fast_function (f=<value optimized out>, throwflag=<value optimized out>) at Python/ceval.c:4098\n#39 call_function (f=<value optimized out>, throwflag=<value optimized out>) at Python/ceval.c:4033\n#40 PyEval_EvalFrameEx (f=<value optimized out>, throwflag=<value optimized out>) at Python/ceval.c:2665\n#41 0x00007ffff7b07b65 in PyEval_EvalCodeEx (co=0x1159e30, globals=<value optimized out>, locals=<value optimized out>, \n    args=<value optimized out>, argcount=3, kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:3252\n#42 0x00007ffff7a99a97 in function_call (func=0x115d5f0, arg=0xfadbe0, kw=0x0) at Objects/funcobject.c:526\n\n```\n",
    "created_at": "2011-04-15T02:42:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99327",
    "user": "fbissey"
}
```

It looks like the crash problems originates somewhere in libsingular

```
sage: f = Zmod(6).cover()
sage: f.kernel()
Principal ideal (6) of Integer Ring
sage: R.<x,y> = PolynomialRing(QQ, 2)
sage: S.<a,b> = R.quo(x^2 + y^2)
sage: phi = S.cover()
sage: phi == loads(dumps(phi))
True
sage: phi == R.quo(x^2 + y^3).cover()

Program received signal SIGSEGV, Segmentation fault.
id_Delete (h=0x50687d8, r=0x0) at ideals.cc:127
127     ideals.cc: No such file or directory.
        in ideals.cc
(gdb) bt
#0  id_Delete (h=0x50687d8, r=0x0) at ideals.cc:127
#1  0x00007fffb9670b49 in __pyx_pf_4sage_4libs_8singular_17groebner_strategy_16GroebnerStrategy_1__dealloc__ (
    o=<value optimized out>) at sage/libs/singular/groebner_strategy.cpp:2570
#2  __pyx_tp_dealloc_4sage_4libs_8singular_17groebner_strategy_GroebnerStrategy (o=<value optimized out>)
    at sage/libs/singular/groebner_strategy.cpp:3190
#3  0x00007ffff7aa98c7 in PyDict_Clear (op=<value optimized out>) at Objects/dictobject.c:891
#4  0x00007ffff7aa990f in dict_tp_clear (op=<value optimized out>) at Objects/dictobject.c:2088
#5  0x00007ffff7b32f27 in delete_garbage (generation=0) at Modules/gcmodule.c:769
#6  collect (generation=0) at Modules/gcmodule.c:930
#7  0x00007ffff7b33616 in collect_generations (basicsize=<value optimized out>) at Modules/gcmodule.c:996
#8  _PyObject_GC_Malloc (basicsize=<value optimized out>) at Modules/gcmodule.c:1457
#9  0x00007ffff7ac4a96 in PyType_GenericAlloc (type=0x7ffff7d9ad40, nitems=0) at Objects/typeobject.c:744
#10 0x00007ffff7a8d256 in BaseException_new (type=<value optimized out>, args=<value optimized out>, kwds=<value optimized out>)
    at Objects/exceptions.c:34
#11 0x00007ffff7ac57b5 in type_call (type=0x7ffff7d9ad40, args=0x4ae46d0, kwds=0x0) at Objects/typeobject.c:712
#12 0x00007ffff7a77539 in PyObject_Call (func=0x7ffff7d9ad40, arg=0x4ae46d0, kw=0x0) at Objects/abstract.c:2529
#13 0x00007ffff7b00b45 in PyEval_CallObjectWithKeywords (func=0x7ffff7d9ad40, arg=0x4ae46d0, kw=0x0) at Python/ceval.c:3881
#14 0x00007ffff7b10443 in PyErr_NormalizeException (exc=0x7fffffffa778, val=0x7fffffffa770, tb=0x7fffffffa768)
    at Python/errors.c:190
#15 0x00007fffe433021c in __Pyx_GetException (type=0x7fffffffa7c0, value=0x7fffffffa7b8, tb=0x7fffffffa7c8)
    at sage/structure/parent.c:20909
#16 0x00007fffe433e4d1 in __pyx_pf_4sage_9structure_6parent_6Parent_2element_class (__pyx_v_self=0x4aea500, 
    unused=<value optimized out>) at sage/structure/parent.c:4251
#17 0x00007ffff7aac1e2 in PyCFunction_Call (func=0x504ebd8, arg=0x7ffff7f81050, kw=<value optimized out>)
    at Objects/methodobject.c:90
#18 0x00007ffff7a77539 in PyObject_Call (func=0x504ebd8, arg=0x7ffff7f81050, kw=0x0) at Objects/abstract.c:2529
#19 0x00007ffff7b00b45 in PyEval_CallObjectWithKeywords (func=0x504ebd8, arg=0x7ffff7f81050, kw=0x0) at Python/ceval.c:3881
#20 0x00007ffff7a8b51f in methoddescr_call (descr=<value optimized out>, args=0x7ffff7f81050, kwds=0x0)
    at Objects/descrobject.c:246
#21 0x00007ffff7a77539 in PyObject_Call (func=0x138e950, arg=0x7ffff7e9c050, kw=0x0) at Objects/abstract.c:2529
#22 0x00007ffff7b05efe in do_call (f=<value optimized out>, throwflag=<value optimized out>) at Python/ceval.c:4230
#23 call_function (f=<value optimized out>, throwflag=<value optimized out>) at Python/ceval.c:4035
#24 PyEval_EvalFrameEx (f=<value optimized out>, throwflag=<value optimized out>) at Python/ceval.c:2665
#25 0x00007ffff7b07b65 in PyEval_EvalCodeEx (co=0x1159e30, globals=<value optimized out>, locals=<value optimized out>, 
    args=<value optimized out>, argcount=3, kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:3252
#26 0x00007ffff7a99a97 in function_call (func=0x115d5f0, arg=0xfadeb0, kw=0x0) at Objects/funcobject.c:526
#27 0x00007ffff7a77539 in PyObject_Call (func=0x115d5f0, arg=0xfadeb0, kw=0x0) at Objects/abstract.c:2529
#28 0x00007ffff7a77cca in PyObject_CallFunctionObjArgs (callable=0x115d5f0) at Objects/abstract.c:2760
#29 0x00007ffff7ac8a8e in slot_tp_descr_get (self=0x13179d0, obj=0x4aea500, type=0x19e91f0) at Objects/typeobject.c:5621
#30 0x00007ffff7aae433 in _PyObject_GenericGetAttrWithDict (obj=0x4aea500, name=0x13c5a78, dict=0x5068fb0) at Objects/object.c:1432
#31 0x00007ffff7aae4d1 in PyObject_GenericGetAttr (obj=<value optimized out>, name=<value optimized out>) at Objects/object.c:1454
#32 0x00007fffe434ed62 in __pyx_tp_getattro_4sage_9structure_6parent_Parent (o=0x4aea500, n=0x13c5a78)
    at sage/structure/parent.c:18702
#33 0x00007ffff7aad8f4 in PyObject_GetAttr (v=0x4aea500, name=<value optimized out>) at Objects/object.c:1189
#34 0x00007ffff7afdbab in builtin_hasattr (self=<value optimized out>, args=<value optimized out>) at Python/bltinmodule.c:885
#35 0x00007ffff7aac1a0 in PyCFunction_Call (func=0x7ffff7fae3b0, arg=0x503d680, kw=<value optimized out>)
    at Objects/methodobject.c:81
#36 0x00007ffff7b05ba3 in call_function (f=<value optimized out>, throwflag=<value optimized out>) at Python/ceval.c:4012
#37 PyEval_EvalFrameEx (f=<value optimized out>, throwflag=<value optimized out>) at Python/ceval.c:2665
#38 0x00007ffff7b05cfa in fast_function (f=<value optimized out>, throwflag=<value optimized out>) at Python/ceval.c:4098
#39 call_function (f=<value optimized out>, throwflag=<value optimized out>) at Python/ceval.c:4033
#40 PyEval_EvalFrameEx (f=<value optimized out>, throwflag=<value optimized out>) at Python/ceval.c:2665
#41 0x00007ffff7b07b65 in PyEval_EvalCodeEx (co=0x1159e30, globals=<value optimized out>, locals=<value optimized out>, 
    args=<value optimized out>, argcount=3, kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:3252
#42 0x00007ffff7a99a97 in function_call (func=0x115d5f0, arg=0xfadbe0, kw=0x0) at Objects/funcobject.c:526

```




---

archive/issue_comments_099328.json:
```json
{
    "body": "Same two doctests killed after upgrade to alpha5.",
    "created_at": "2011-04-20T23:30:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99328",
    "user": "fbissey"
}
```

Same two doctests killed after upgrade to alpha5.



---

archive/issue_comments_099329.json:
```json
{
    "body": "Over-eager garbage collection in python-2.7.1! Preceding the sequence by\n\n```\nsage: import gc\nsage: gc.disable()\n```\n\nMakes everything go smoothly.",
    "created_at": "2011-04-21T00:42:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99329",
    "user": "fbissey"
}
```

Over-eager garbage collection in python-2.7.1! Preceding the sequence by

```
sage: import gc
sage: gc.disable()
```

Makes everything go smoothly.



---

archive/issue_comments_099330.json:
```json
{
    "body": "trac_9958-fix_cmp.patch is perfectly reasonable, since this is the idiom used everywhere else in similar situations. I don't have enough background to judge on the warning patch.",
    "created_at": "2011-04-22T13:43:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99330",
    "user": "nthiery"
}
```

trac_9958-fix_cmp.patch is perfectly reasonable, since this is the idiom used everywhere else in similar situations. I don't have enough background to judge on the warning patch.



---

archive/issue_comments_099331.json:
```json
{
    "body": "Put an updated list of tests failing with 4.7.alpha5 and the latest patches from Nicolas M. Thiery.\nI think the next area do need some work is the problem of garbage collection in polynomial rings that leads to \"random\" failures in libsingular. See:\n[http://groups.google.com/group/sage-devel/browse_thread/thread/8c165c887d6b9e54](http://groups.google.com/group/sage-devel/browse_thread/thread/8c165c887d6b9e54)",
    "created_at": "2011-04-24T02:16:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99331",
    "user": "fbissey"
}
```

Put an updated list of tests failing with 4.7.alpha5 and the latest patches from Nicolas M. Thiery.
I think the next area do need some work is the problem of garbage collection in polynomial rings that leads to "random" failures in libsingular. See:
[http://groups.google.com/group/sage-devel/browse_thread/thread/8c165c887d6b9e54](http://groups.google.com/group/sage-devel/browse_thread/thread/8c165c887d6b9e54)



---

archive/issue_comments_099332.json:
```json
{
    "body": "Split the deprecation issue in its own ticket in #11244 - this is a different patch.",
    "created_at": "2011-04-24T03:48:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99332",
    "user": "fbissey"
}
```

Split the deprecation issue in its own ticket in #11244 - this is a different patch.



---

archive/issue_comments_099333.json:
```json
{
    "body": "Replying to [comment:23 nthiery]:\n> trac_9958-fix_cmp.patch is perfectly reasonable, since this is the idiom used everywhere else in similar situations. I don't have enough background to judge on the warning patch.\n\nI will put the cmp patch in its own ticket would you review it?",
    "created_at": "2011-04-27T01:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99333",
    "user": "fbissey"
}
```

Replying to [comment:23 nthiery]:
> trac_9958-fix_cmp.patch is perfectly reasonable, since this is the idiom used everywhere else in similar situations. I don't have enough background to judge on the warning patch.

I will put the cmp patch in its own ticket would you review it?



---

archive/issue_comments_099334.json:
```json
{
    "body": "Attachment\n\nfix numerical noise part 1",
    "created_at": "2011-04-28T03:19:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99334",
    "user": "fbissey"
}
```

Attachment

fix numerical noise part 1



---

archive/issue_comments_099335.json:
```json
{
    "body": "Attachment\n\nfix numerical noise part 3",
    "created_at": "2011-04-28T03:19:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99335",
    "user": "fbissey"
}
```

Attachment

fix numerical noise part 3



---

archive/issue_comments_099336.json:
```json
{
    "body": "fix numerical noise part 4: the forgotten bits",
    "created_at": "2011-04-28T03:19:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99336",
    "user": "fbissey"
}
```

fix numerical noise part 4: the forgotten bits



---

archive/issue_comments_099337.json:
```json
{
    "body": "Attachment\n\n49 failures in colors.py, numerical noise except one.",
    "created_at": "2011-04-28T03:20:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99337",
    "user": "fbissey"
}
```

Attachment

49 failures in colors.py, numerical noise except one.



---

archive/issue_comments_099338.json:
```json
{
    "body": "Attachment\n\nfix the element reported by list index",
    "created_at": "2011-04-28T03:21:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99338",
    "user": "fbissey"
}
```

Attachment

fix the element reported by list index



---

archive/issue_comments_099339.json:
```json
{
    "body": "odds and ends missed in the other patches",
    "created_at": "2011-04-28T03:22:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99339",
    "user": "fbissey"
}
```

odds and ends missed in the other patches



---

archive/issue_comments_099340.json:
```json
{
    "body": "Attachment\n\nI have attached some patches to fix all the noise for numerics and formatting changes. What's left should be looked at before patching.\n\nThere are several failures because hashes have changed but I cannot say it is allright to just change the doctest:\n\n```\nsage -t -long -force_lib \"devel/sage-main/sage/rings/padics/padic_capped_relative_element.pyx\"\n**********************************************************************\nFile \"/usr/share/sage/devel/sage-main/sage/rings/padics/padic_capped_relative_element.pyx\", line 2339:\n    sage: hash(R(-1)) \nExpected:\n    95367431640624\nGot:\n    1977800240\n**********************************************************************\n```\n\n\n\n```\nsage -t -long -force_lib \"devel/sage-main/sage/rings/integer.pyx\"\n**********************************************************************\nFile \"/usr/share/sage/devel/sage-main/sage/rings/integer.pyx\", line 2995:\n    sage: n = -920390823904823094890238490238484; n.__hash__()                                                                      \nExpected:                                                                                                                           \n    6874330978542788722                                                                                                             \nGot:                                                                                                                                \n    -2623069716                                                                                                                     \n**********************************************************************                                                              \nFile \"/usr/share/sage/devel/sage-main/sage/rings/integer.pyx\", line 3010:                                                           \n    sage: hash(n)                                                                                                                   \nExpected:                                                                                                                           \n    -9223372036854767616                                                                                                            \nGot:                                                                                                                                \n    8192                                                                                                                            \n**********************************************************************                                                              \nFile \"/usr/share/sage/devel/sage-main/sage/rings/integer.pyx\", line 3013:                                                           \n    sage: hash(n) == hash(int(n))                                                                                                   \nExpected:                                                                                                                           \n    True\nGot:\n    False\n**********************************************************************\n```\n\nThat hash(n) == hash(int(n)) is now false should be looked into carefully.\n\n```\nsage -t -long -force_lib \"devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py\"\n**********************************************************************\nFile \"/usr/share/sage/devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py\", line 20:\n    sage: it.next()\nExpected:\n    word: 6456\nGot:\n    word: 5645\n**********************************************************************\nFile \"/usr/share/sage/devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py\", line 22:\n    sage: it.next()\nExpected:\n    word: 5645\nGot:\n    word: 6456\n**********************************************************************\n```\n\nI think that one is OK, just a change of order but a second opinion would be nice.\n\nFinally there are still three tests killed in libsingular's id_delete because a ring has been garbage collected even so there are some precautions in place for it:\n[http://groups.google.com/group/sage-devel/browse_thread/thread/8c165c887d6b9e54](http://groups.google.com/group/sage-devel/browse_thread/thread/8c165c887d6b9e54)\n\nNext we need an updated python spkg so that more people can play and even try the patchbot on it.",
    "created_at": "2011-04-28T03:33:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99340",
    "user": "fbissey"
}
```

Attachment

I have attached some patches to fix all the noise for numerics and formatting changes. What's left should be looked at before patching.

There are several failures because hashes have changed but I cannot say it is allright to just change the doctest:

```
sage -t -long -force_lib "devel/sage-main/sage/rings/padics/padic_capped_relative_element.pyx"
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/rings/padics/padic_capped_relative_element.pyx", line 2339:
    sage: hash(R(-1)) 
Expected:
    95367431640624
Got:
    1977800240
**********************************************************************
```



```
sage -t -long -force_lib "devel/sage-main/sage/rings/integer.pyx"
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/rings/integer.pyx", line 2995:
    sage: n = -920390823904823094890238490238484; n.__hash__()                                                                      
Expected:                                                                                                                           
    6874330978542788722                                                                                                             
Got:                                                                                                                                
    -2623069716                                                                                                                     
**********************************************************************                                                              
File "/usr/share/sage/devel/sage-main/sage/rings/integer.pyx", line 3010:                                                           
    sage: hash(n)                                                                                                                   
Expected:                                                                                                                           
    -9223372036854767616                                                                                                            
Got:                                                                                                                                
    8192                                                                                                                            
**********************************************************************                                                              
File "/usr/share/sage/devel/sage-main/sage/rings/integer.pyx", line 3013:                                                           
    sage: hash(n) == hash(int(n))                                                                                                   
Expected:                                                                                                                           
    True
Got:
    False
**********************************************************************
```

That hash(n) == hash(int(n)) is now false should be looked into carefully.

```
sage -t -long -force_lib "devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py"
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py", line 20:
    sage: it.next()
Expected:
    word: 6456
Got:
    word: 5645
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py", line 22:
    sage: it.next()
Expected:
    word: 5645
Got:
    word: 6456
**********************************************************************
```

I think that one is OK, just a change of order but a second opinion would be nice.

Finally there are still three tests killed in libsingular's id_delete because a ring has been garbage collected even so there are some precautions in place for it:
[http://groups.google.com/group/sage-devel/browse_thread/thread/8c165c887d6b9e54](http://groups.google.com/group/sage-devel/browse_thread/thread/8c165c887d6b9e54)

Next we need an updated python spkg so that more people can play and even try the patchbot on it.



---

archive/issue_comments_099341.json:
```json
{
    "body": "The replacement of type.__cmp__ by cmp in strata.py is now in its own ticket #11264 as it can be applied independently of a python upgrade.",
    "created_at": "2011-04-28T03:48:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99341",
    "user": "fbissey"
}
```

The replacement of type.__cmp__ by cmp in strata.py is now in its own ticket #11264 as it can be applied independently of a python upgrade.



---

archive/issue_comments_099342.json:
```json
{
    "body": "I forgot because I build on sage-on-gentoo but I'll post some patch to build against python-2.7 a little bit later.",
    "created_at": "2011-04-28T09:31:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99342",
    "user": "fbissey"
}
```

I forgot because I build on sage-on-gentoo but I'll post some patch to build against python-2.7 a little bit later.



---

archive/issue_comments_099343.json:
```json
{
    "body": "Unless someone steps in I'll make a new python-2.7.1 spkg by the end of the week. I'll have to figure out if the latest change going in for sage-4.7 will be needed for that one.",
    "created_at": "2011-05-02T23:37:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99343",
    "user": "fbissey"
}
```

Unless someone steps in I'll make a new python-2.7.1 spkg by the end of the week. I'll have to figure out if the latest change going in for sage-4.7 will be needed for that one.



---

archive/issue_comments_099344.json:
```json
{
    "body": "I won't be able to do that this week.",
    "created_at": "2011-05-05T22:32:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99344",
    "user": "fbissey"
}
```

I won't be able to do that this week.



---

archive/issue_comments_099345.json:
```json
{
    "body": "Our lead sage-on-gentoo debugger Martin tracked down the segfault problem to cython, this is now #11339",
    "created_at": "2011-05-16T21:47:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99345",
    "user": "fbissey"
}
```

Our lead sage-on-gentoo debugger Martin tracked down the segfault problem to cython, this is now #11339



---

archive/issue_comments_099346.json:
```json
{
    "body": "I'd like to try this but don't have time to figure out exactly what patches are needed in what order - can someone update the description with this?  Also, is it the same spkg that Marshall originally posted that one should try?",
    "created_at": "2011-05-18T16:01:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99346",
    "user": "kcrisman"
}
```

I'd like to try this but don't have time to figure out exactly what patches are needed in what order - can someone update the description with this?  Also, is it the same spkg that Marshall originally posted that one should try?



---

archive/issue_comments_099347.json:
```json
{
    "body": "Also, is it possible to test this by ./sage -f something, or would one have to take a fresh tarball and replace the Python spkg?",
    "created_at": "2011-05-18T16:24:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99347",
    "user": "kcrisman"
}
```

Also, is it possible to test this by ./sage -f something, or would one have to take a fresh tarball and replace the Python spkg?



---

archive/issue_comments_099348.json:
```json
{
    "body": "Replying to [comment:34 kcrisman]:\n> Also, is it possible to test this by ./sage -f something, or would one have to take a fresh tarball and replace the Python spkg?\n\nHi Karl,\n\nI am mainly developing from sage-on-gentoo at the moment. I need to make a current python-2.7.1 spkg to match. I will update the description and give the patch order when there is a spkg (feel free to make one). The patch have initially been made against 4.7.1.alpha0 and the current version works against 4.7.1.alpha1. You would get failures against a 4.7 because #7377 finally landed.\n\nI think the best course of action will be to start from scratch, it may even be useful to host an alternative tarball somewhere because the change in python version will be extremely messy. I don't know if we can do it without breaking sage -upgrade or being overly complicated.\n\nIn the meantime you could have a look at #11244 (which I need to update for 4.7.1.alpha1 because of #10334). \n\nFrancois",
    "created_at": "2011-05-18T21:41:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99348",
    "user": "fbissey"
}
```

Replying to [comment:34 kcrisman]:
> Also, is it possible to test this by ./sage -f something, or would one have to take a fresh tarball and replace the Python spkg?

Hi Karl,

I am mainly developing from sage-on-gentoo at the moment. I need to make a current python-2.7.1 spkg to match. I will update the description and give the patch order when there is a spkg (feel free to make one). The patch have initially been made against 4.7.1.alpha0 and the current version works against 4.7.1.alpha1. You would get failures against a 4.7 because #7377 finally landed.

I think the best course of action will be to start from scratch, it may even be useful to host an alternative tarball somewhere because the change in python version will be extremely messy. I don't know if we can do it without breaking sage -upgrade or being overly complicated.

In the meantime you could have a look at #11244 (which I need to update for 4.7.1.alpha1 because of #10334). 

Francois



---

archive/issue_comments_099349.json:
```json
{
    "body": "OK if you want to look at #11244 it can be tested against either the latest 4.7 or 4.7.1.alpha1 now.",
    "created_at": "2011-05-18T23:29:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99349",
    "user": "fbissey"
}
```

OK if you want to look at #11244 it can be tested against either the latest 4.7 or 4.7.1.alpha1 now.



---

archive/issue_comments_099350.json:
```json
{
    "body": "I see.  Well, I just want to make sure that it all works fine on older Macs, of course.  I definitely don't have time to make an spkg now, though I do have time to do ./sage -f and slap a few patches on it :)  Just let me know when you get around to it; I don't think there is a huge rush.\n\nI should probably test 4.7.1.alpha1 on my box.  I'm amazed at Jeroen's stamina on this, especially with several different versions simultaneously existing.",
    "created_at": "2011-05-19T00:33:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99350",
    "user": "kcrisman"
}
```

I see.  Well, I just want to make sure that it all works fine on older Macs, of course.  I definitely don't have time to make an spkg now, though I do have time to do ./sage -f and slap a few patches on it :)  Just let me know when you get around to it; I don't think there is a huge rush.

I should probably test 4.7.1.alpha1 on my box.  I'm amazed at Jeroen's stamina on this, especially with several different versions simultaneously existing.



---

archive/issue_comments_099351.json:
```json
{
    "body": "Replying to [comment:37 kcrisman]:\n> I see.  Well, I just want to make sure that it all works fine on older Macs, of course.  I definitely don't have time to make an spkg now, though I do have time to do ./sage -f and slap a few patches on it :)  Just let me know when you get around to it; I don't think there is a huge rush.\n> \n> I should probably test 4.7.1.alpha1 on my box.  I'm amazed at Jeroen's stamina on this, especially with several different versions simultaneously existing.\n\nThat's why I asked about #11244 it is an issue I split from this ticket because it should apply on a sage running python-2.6 without side effects. So it could be in place when we come around to the upgrade. Any ideas on #11339 which was recently split from this ticket is also welcome.",
    "created_at": "2011-05-19T00:49:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99351",
    "user": "fbissey"
}
```

Replying to [comment:37 kcrisman]:
> I see.  Well, I just want to make sure that it all works fine on older Macs, of course.  I definitely don't have time to make an spkg now, though I do have time to do ./sage -f and slap a few patches on it :)  Just let me know when you get around to it; I don't think there is a huge rush.
> 
> I should probably test 4.7.1.alpha1 on my box.  I'm amazed at Jeroen's stamina on this, especially with several different versions simultaneously existing.

That's why I asked about #11244 it is an issue I split from this ticket because it should apply on a sage running python-2.6 without side effects. So it could be in place when we come around to the upgrade. Any ideas on #11339 which was recently split from this ticket is also welcome.



---

archive/issue_comments_099352.json:
```json
{
    "body": "My friend Steven Trogdon made some quick and dirty spkgs. His early tests indicate that setuptools needs to be updated. This is now #11363 it also revealed that I missed something in misc/cython.py watch out for an updated patch sometimes this weekend.\nThere were also a few things that needed to be done in two other patches which I refreshed yesterday.\nI have a python-2.7.1 spkg ready to be uploaded probably sometimes today.\nIf you want fun before that you can always use Steve's spkg (they are not in a reviewable state) at:\n[http://www.d.umn.edu/~strogdon/sage/](http://www.d.umn.edu/~strogdon/sage/)",
    "created_at": "2011-05-20T20:49:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99352",
    "user": "fbissey"
}
```

My friend Steven Trogdon made some quick and dirty spkgs. His early tests indicate that setuptools needs to be updated. This is now #11363 it also revealed that I missed something in misc/cython.py watch out for an updated patch sometimes this weekend.
There were also a few things that needed to be done in two other patches which I refreshed yesterday.
I have a python-2.7.1 spkg ready to be uploaded probably sometimes today.
If you want fun before that you can always use Steve's spkg (they are not in a reviewable state) at:
[http://www.d.umn.edu/~strogdon/sage/](http://www.d.umn.edu/~strogdon/sage/)



---

archive/issue_comments_099353.json:
```json
{
    "body": "Didn't take long. I have been naughty and committed two changes to patches that needed touching after my first commit of python-2.7.1 so the log will show 3 entries for just the one SPKG.txt entry. They were minor changes.\nI dropped a number of patches because they were applied upstream. However in the case of two patches I dropped them because the upstream has changed in a way they don't apply anymore but I don't know if patching is still necessary for the underlying issues. If so new patches will need to be developed. The issues are\n* readline on itanium\n* multiprocessing on solaris\n\nAs promised I will give a patch order. The next to last one needs updating as stated earlier and the last one is really optional. The patches do not have to be taken n that order as they don't overlap.",
    "created_at": "2011-05-20T21:09:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99353",
    "user": "fbissey"
}
```

Didn't take long. I have been naughty and committed two changes to patches that needed touching after my first commit of python-2.7.1 so the log will show 3 entries for just the one SPKG.txt entry. They were minor changes.
I dropped a number of patches because they were applied upstream. However in the case of two patches I dropped them because the upstream has changed in a way they don't apply anymore but I don't know if patching is still necessary for the underlying issues. If so new patches will need to be developed. The issues are
* readline on itanium
* multiprocessing on solaris

As promised I will give a patch order. The next to last one needs updating as stated earlier and the last one is really optional. The patches do not have to be taken n that order as they don't overlap.



---

archive/issue_comments_099354.json:
```json
{
    "body": "I forgot apply the patches on 4.7.1.alpha1, there may be rejection on 4.7.rcX.",
    "created_at": "2011-05-20T21:11:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99354",
    "user": "fbissey"
}
```

I forgot apply the patches on 4.7.1.alpha1, there may be rejection on 4.7.rcX.



---

archive/issue_comments_099355.json:
```json
{
    "body": "misc/cython.py patch updated for people who want to test it.",
    "created_at": "2011-05-21T12:23:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99355",
    "user": "fbissey"
}
```

misc/cython.py patch updated for people who want to test it.



---

archive/issue_comments_099356.json:
```json
{
    "body": "corrected a syntax error in the last patch.",
    "created_at": "2011-05-21T19:45:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99356",
    "user": "fbissey"
}
```

corrected a syntax error in the last patch.



---

archive/issue_comments_099357.json:
```json
{
    "body": "Not strictly necessary but this file needed a scrub. (refreshed for syntax errors)",
    "created_at": "2011-05-22T12:32:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99357",
    "user": "fbissey"
}
```

Not strictly necessary but this file needed a scrub. (refreshed for syntax errors)



---

archive/issue_comments_099358.json:
```json
{
    "body": "Attachment\n\nHad to redo trac_9958-build_module_listpy.patch again as I messed up the syntax of one bit.",
    "created_at": "2011-05-22T12:33:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99358",
    "user": "fbissey"
}
```

Attachment

Had to redo trac_9958-build_module_listpy.patch again as I messed up the syntax of one bit.



---

archive/issue_comments_099359.json:
```json
{
    "body": "My friend Steve Trogdon made a prepatched sage-4.7.1.alpha1 spkg (4.7.1.alpha1.p0 we named it) available to make testing easier, find it with hos own test.log here\n[http://www.d.umn.edu/~strogdon/sage/](http://www.d.umn.edu/~strogdon/sage/)\nIt has all the necessary patches from #11244 and this this ticket.\nWe are a bit puzzled by the cause of failure in sage/misc/cython.py, white spaces?",
    "created_at": "2011-05-22T18:44:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99359",
    "user": "fbissey"
}
```

My friend Steve Trogdon made a prepatched sage-4.7.1.alpha1 spkg (4.7.1.alpha1.p0 we named it) available to make testing easier, find it with hos own test.log here
[http://www.d.umn.edu/~strogdon/sage/](http://www.d.umn.edu/~strogdon/sage/)
It has all the necessary patches from #11244 and this this ticket.
We are a bit puzzled by the cause of failure in sage/misc/cython.py, white spaces?



---

archive/issue_comments_099360.json:
```json
{
    "body": "I am getting the twisted install fail that jhpalmieri refers to.  So my guess is that the Gentoo system has some updated things along those lines that vanilla 4.7.1.alpha1 does not.  Is that possible?",
    "created_at": "2011-05-23T12:54:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99360",
    "user": "kcrisman"
}
```

I am getting the twisted install fail that jhpalmieri refers to.  So my guess is that the Gentoo system has some updated things along those lines that vanilla 4.7.1.alpha1 does not.  Is that possible?



---

archive/issue_comments_099361.json:
```json
{
    "body": "Replying to [comment:46 kcrisman]:\n> I am getting the twisted install fail that jhpalmieri refers to.  So my guess is that the Gentoo system has some updated things along those lines that vanilla 4.7.1.alpha1 does not.  Is that possible?\n\nWell sage-on-gentoo uses a newer twisted. On the other I and Steve have build twisted in vanilla sage with python-2.7.1. Did you get the new setuptools spkg from #11363? It is necessary to build twisted with python-2.7.1.",
    "created_at": "2011-05-23T13:59:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99361",
    "user": "fbissey"
}
```

Replying to [comment:46 kcrisman]:
> I am getting the twisted install fail that jhpalmieri refers to.  So my guess is that the Gentoo system has some updated things along those lines that vanilla 4.7.1.alpha1 does not.  Is that possible?

Well sage-on-gentoo uses a newer twisted. On the other I and Steve have build twisted in vanilla sage with python-2.7.1. Did you get the new setuptools spkg from #11363? It is necessary to build twisted with python-2.7.1.



---

archive/issue_comments_099362.json:
```json
{
    "body": "No, I didn't realize there was an spkg involved with that.  I installed that first, and it seems to be working now.",
    "created_at": "2011-05-23T15:01:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99362",
    "user": "kcrisman"
}
```

No, I didn't realize there was an spkg involved with that.  I installed that first, and it seems to be working now.



---

archive/issue_comments_099363.json:
```json
{
    "body": "Replying to [comment:45 fbissey]:\n> My friend Steve Trogdon made a prepatched sage-4.7.1.alpha1 spkg (4.7.1.alpha1.p0 we named it) available to make testing easier, find it with hos own test.log here\n> [http://www.d.umn.edu/~strogdon/sage/](http://www.d.umn.edu/~strogdon/sage/)\n> It has all the necessary patches from #11244 and this this ticket.\n\nIs one of these patches needed *before* doing the Sage spkg itself? I get an immediate failure\n\n```\ngcc -o src/convert.os -c -fPIC -I/Users/student/Desktop/sage-4.7.1.alpha1/local/include -I/Users/student/Desktop/sage-4.7.1.alpha1/local/include/python2.6 -I/Users/student/Desktop/sage-4.7.1.alpha1/local/include/NTL -Iinclude src/convert.c\nIn file included from include/memory.h:23,\n                 from /Users/student/Desktop/sage-4.7.1.alpha1/local/include/pari/pari.h:42,\n                 from include/convert.h:12,\n                 from src/convert.c:14:\ninclude/interrupt.h:32:20: error: Python.h: No such file or directory\nscons: *** [src/convert.os] Error 1\n*** TOUCHING ALL CYTHON (.pyx) FILES ***\ngcc -o src/convert.os -c -fPIC -I/Users/student/Desktop/sage-4.7.1.alpha1/local/include -I/Users/student/Desktop/sage-4.7.1.alpha1/local/include/python2.6 -I/Users/student/Desktop/sage-4.7.1.alpha1/local/include/NTL -Iinclude src/convert.c\nIn file included from include/memory.h:23,\n                 from /Users/student/Desktop/sage-4.7.1.alpha1/local/include/pari/pari.h:42,\n                 from include/convert.h:12,\n                 from src/convert.c:14:\ninclude/interrupt.h:32:20: error: Python.h: No such file or directory\nscons: *** [src/convert.os] Error 1\n\n----------------------------------------------------------\nsage: Building and installing modified Sage library files.\n\n\nInstalling c_lib\ngcc -o src/convert.os -c -fPIC -I/Users/student/Desktop/sage-4.7.1.alpha1/local/include -I/Users/student/Desktop/sage-4.7.1.alpha1/local/include/python2.6 -I/Users/student/Desktop/sage-4.7.1.alpha1/local/include/NTL -Iinclude src/convert.c\nIn file included from include/memory.h:23,\n                 from /Users/student/Desktop/sage-4.7.1.alpha1/local/include/pari/pari.h:42,\n                 from include/convert.h:12,\n                 from src/convert.c:14:\ninclude/interrupt.h:32:20: error: Python.h: No such file or directory\nscons: *** [src/convert.os] Error 1\nERROR: There was an error building c_lib.\n```\n\nwhich I assume is related to one of the patches involved here, though I couldn't say which one...",
    "created_at": "2011-05-23T19:51:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99363",
    "user": "kcrisman"
}
```

Replying to [comment:45 fbissey]:
> My friend Steve Trogdon made a prepatched sage-4.7.1.alpha1 spkg (4.7.1.alpha1.p0 we named it) available to make testing easier, find it with hos own test.log here
> [http://www.d.umn.edu/~strogdon/sage/](http://www.d.umn.edu/~strogdon/sage/)
> It has all the necessary patches from #11244 and this this ticket.

Is one of these patches needed *before* doing the Sage spkg itself? I get an immediate failure

```
gcc -o src/convert.os -c -fPIC -I/Users/student/Desktop/sage-4.7.1.alpha1/local/include -I/Users/student/Desktop/sage-4.7.1.alpha1/local/include/python2.6 -I/Users/student/Desktop/sage-4.7.1.alpha1/local/include/NTL -Iinclude src/convert.c
In file included from include/memory.h:23,
                 from /Users/student/Desktop/sage-4.7.1.alpha1/local/include/pari/pari.h:42,
                 from include/convert.h:12,
                 from src/convert.c:14:
include/interrupt.h:32:20: error: Python.h: No such file or directory
scons: *** [src/convert.os] Error 1
*** TOUCHING ALL CYTHON (.pyx) FILES ***
gcc -o src/convert.os -c -fPIC -I/Users/student/Desktop/sage-4.7.1.alpha1/local/include -I/Users/student/Desktop/sage-4.7.1.alpha1/local/include/python2.6 -I/Users/student/Desktop/sage-4.7.1.alpha1/local/include/NTL -Iinclude src/convert.c
In file included from include/memory.h:23,
                 from /Users/student/Desktop/sage-4.7.1.alpha1/local/include/pari/pari.h:42,
                 from include/convert.h:12,
                 from src/convert.c:14:
include/interrupt.h:32:20: error: Python.h: No such file or directory
scons: *** [src/convert.os] Error 1

----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
gcc -o src/convert.os -c -fPIC -I/Users/student/Desktop/sage-4.7.1.alpha1/local/include -I/Users/student/Desktop/sage-4.7.1.alpha1/local/include/python2.6 -I/Users/student/Desktop/sage-4.7.1.alpha1/local/include/NTL -Iinclude src/convert.c
In file included from include/memory.h:23,
                 from /Users/student/Desktop/sage-4.7.1.alpha1/local/include/pari/pari.h:42,
                 from include/convert.h:12,
                 from src/convert.c:14:
include/interrupt.h:32:20: error: Python.h: No such file or directory
scons: *** [src/convert.os] Error 1
ERROR: There was an error building c_lib.
```

which I assume is related to one of the patches involved here, though I couldn't say which one...



---

archive/issue_comments_099364.json:
```json
{
    "body": "Did you rebuild cython after the python upgrade? In fact I have now added a list of package that needs to be rebuild after the python upgrade. Not all of them are necessary for building sage (scipy could be done after) but cython, numpy, matplotlib and pynac really need to be rebuilt.\n\nOnce you have done that apply all the patches with build in their names:\n* [attachment:trac_9958-build_setuppy.patch]\n* [attachment:trac_9958-build-sage_clib.patch]\n* [attachment:trac_9958-build_misc_cythonpy.patch]\n* [attachment:trac_9958-build_module_listpy.patch] (actually optional)\n\nThat should help sage build but will not correct many of the doctests. To fix most of the doctests apply the patches in #11244 as well as the one in the description of this bug. I have made a list now, have you seen it?",
    "created_at": "2011-05-23T20:04:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99364",
    "user": "fbissey"
}
```

Did you rebuild cython after the python upgrade? In fact I have now added a list of package that needs to be rebuild after the python upgrade. Not all of them are necessary for building sage (scipy could be done after) but cython, numpy, matplotlib and pynac really need to be rebuilt.

Once you have done that apply all the patches with build in their names:
* [attachment:trac_9958-build_setuppy.patch]
* [attachment:trac_9958-build-sage_clib.patch]
* [attachment:trac_9958-build_misc_cythonpy.patch]
* [attachment:trac_9958-build_module_listpy.patch] (actually optional)

That should help sage build but will not correct many of the doctests. To fix most of the doctests apply the patches in #11244 as well as the one in the description of this bug. I have made a list now, have you seen it?



---

archive/issue_comments_099365.json:
```json
{
    "body": "Well, I'm building from scratch, so that shouldn't affect it from that side.  \n\nAre you saying that before I build the Sage library, I have to apply these patches?  That's a little tricky in a scratch build (for me, at least). \n\nYes, I saw the lists, but I thought they were only relevant for an upgrade/after actually building Sage.  My apologies.  I may not be able to finish testing this properly for a while now.",
    "created_at": "2011-05-23T20:17:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99365",
    "user": "kcrisman"
}
```

Well, I'm building from scratch, so that shouldn't affect it from that side.  

Are you saying that before I build the Sage library, I have to apply these patches?  That's a little tricky in a scratch build (for me, at least). 

Yes, I saw the lists, but I thought they were only relevant for an upgrade/after actually building Sage.  My apologies.  I may not be able to finish testing this properly for a while now.



---

archive/issue_comments_099366.json:
```json
{
    "body": "Replying to [comment:52 kcrisman]:\n> Well, I'm building from scratch, so that shouldn't affect it from that side.  \n> \n> Are you saying that before I build the Sage library, I have to apply these patches?  That's a little tricky in a scratch build (for me, at least). \n> \n> Yes, I saw the lists, but I thought they were only relevant for an upgrade/after actually building Sage.  My apologies.  I may not be able to finish testing this properly for a while now.\n\nThat's all right there are still things to sort out. But you could use the sage spkg prepared by Steve with all patches included rather than patch yourself:\n[http://www.d.umn.edu/~strogdon/sage/sage-4.7.1.alpha1.p0.spkg](http://www.d.umn.edu/~strogdon/sage/sage-4.7.1.alpha1.p0.spkg)\n\nAnd yes it is tricky from scratch unless you have a premade spkg.",
    "created_at": "2011-05-23T20:24:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99366",
    "user": "fbissey"
}
```

Replying to [comment:52 kcrisman]:
> Well, I'm building from scratch, so that shouldn't affect it from that side.  
> 
> Are you saying that before I build the Sage library, I have to apply these patches?  That's a little tricky in a scratch build (for me, at least). 
> 
> Yes, I saw the lists, but I thought they were only relevant for an upgrade/after actually building Sage.  My apologies.  I may not be able to finish testing this properly for a while now.

That's all right there are still things to sort out. But you could use the sage spkg prepared by Steve with all patches included rather than patch yourself:
[http://www.d.umn.edu/~strogdon/sage/sage-4.7.1.alpha1.p0.spkg](http://www.d.umn.edu/~strogdon/sage/sage-4.7.1.alpha1.p0.spkg)

And yes it is tricky from scratch unless you have a premade spkg.



---

archive/issue_comments_099367.json:
```json
{
    "body": "I may have made mistakes, but I tried to do this, starting with sage-4.7.rc4:\n\n- install the new python spkg\n- install the new setuptools spkg (from #11363)\n- apply the patches from #11244 to the main Sage library\n- apply the patches from this ticket with \"build\" in their name -- some of these didn't apply cleanly, so I had to work around that.\n\nI used that to build a new version of Sage (using \"sage -sdist ...\").  The tar file is here:\n\n- [http://sage.math.washington.edu/home/palmieri/misc/python2.7/sage-4.7.rc4-python2.7.tar](http://sage.math.washington.edu/home/palmieri/misc/python2.7/sage-4.7.rc4-python2.7.tar)\n\nOn sage.math, I've been able to untar this and build Sage, although tests haven't run yet.  You can also try upgrading, although I haven't tested this at all: run\n\n\n```\n$ sage -upgrade http://sage.math.washington.edu/home/palmieri/misc/python2.7/sage-4.7.rc4-python2.7/\n```\n",
    "created_at": "2011-05-24T01:01:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99367",
    "user": "jhpalmieri"
}
```

I may have made mistakes, but I tried to do this, starting with sage-4.7.rc4:

- install the new python spkg
- install the new setuptools spkg (from #11363)
- apply the patches from #11244 to the main Sage library
- apply the patches from this ticket with "build" in their name -- some of these didn't apply cleanly, so I had to work around that.

I used that to build a new version of Sage (using "sage -sdist ...").  The tar file is here:

- [http://sage.math.washington.edu/home/palmieri/misc/python2.7/sage-4.7.rc4-python2.7.tar](http://sage.math.washington.edu/home/palmieri/misc/python2.7/sage-4.7.rc4-python2.7.tar)

On sage.math, I've been able to untar this and build Sage, although tests haven't run yet.  You can also try upgrading, although I haven't tested this at all: run


```
$ sage -upgrade http://sage.math.washington.edu/home/palmieri/misc/python2.7/sage-4.7.rc4-python2.7/
```




---

archive/issue_comments_099368.json:
```json
{
    "body": "Replying to [comment:54 jhpalmieri]:\n> I may have made mistakes, but I tried to do this, starting with sage-4.7.rc4:\n> \n>  - install the new python spkg\n>  - install the new setuptools spkg (from #11363)\n>  - apply the patches from #11244 to the main Sage library\n>  - apply the patches from this ticket with \"build\" in their name -- some of these didn't apply cleanly, so I had to work around that.\n> \n> I used that to build a new version of Sage (using \"sage -sdist ...\").  The tar file is here:\n> \n>  - [http://sage.math.washington.edu/home/palmieri/misc/python2.7/sage-4.7.rc4-python2.7.tar](http://sage.math.washington.edu/home/palmieri/misc/python2.7/sage-4.7.rc4-python2.7.tar)\n> \n> On sage.math, I've been able to untar this and build Sage, although tests haven't run yet.  You can also try upgrading, although I haven't tested this at all: run\n> \n> {{{\n> $ sage -upgrade http://sage.math.washington.edu/home/palmieri/misc/python2.7/sage-4.7.rc4-python2.7/\n> }}}\n\nI have tried to keep abreast of everything so the patches are based on 4.7.1.alpha1 there are enough differences that a lot of patches for 4.7 would need rebasing.\n\nSo I decided to go straight for the bleeding edge. I am doing some more work on the \"build\" patches, I am trying to do something smarter with the python version number so some change could be applied independently of this ticket. The module_list,py patch definitely won't apply cleanly on 4.7.rc mainly because of #10334. What's more #11264 and #11236 which are needed here are merged in 4.7.1.alpha0.\n\nThat's all a bit of hassle to start from 4.7.1.alpha, but I would have to start again if I was starting from 4.7.rc.",
    "created_at": "2011-05-24T02:13:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99368",
    "user": "fbissey"
}
```

Replying to [comment:54 jhpalmieri]:
> I may have made mistakes, but I tried to do this, starting with sage-4.7.rc4:
> 
>  - install the new python spkg
>  - install the new setuptools spkg (from #11363)
>  - apply the patches from #11244 to the main Sage library
>  - apply the patches from this ticket with "build" in their name -- some of these didn't apply cleanly, so I had to work around that.
> 
> I used that to build a new version of Sage (using "sage -sdist ...").  The tar file is here:
> 
>  - [http://sage.math.washington.edu/home/palmieri/misc/python2.7/sage-4.7.rc4-python2.7.tar](http://sage.math.washington.edu/home/palmieri/misc/python2.7/sage-4.7.rc4-python2.7.tar)
> 
> On sage.math, I've been able to untar this and build Sage, although tests haven't run yet.  You can also try upgrading, although I haven't tested this at all: run
> 
> {{{
> $ sage -upgrade http://sage.math.washington.edu/home/palmieri/misc/python2.7/sage-4.7.rc4-python2.7/
> }}}

I have tried to keep abreast of everything so the patches are based on 4.7.1.alpha1 there are enough differences that a lot of patches for 4.7 would need rebasing.

So I decided to go straight for the bleeding edge. I am doing some more work on the "build" patches, I am trying to do something smarter with the python version number so some change could be applied independently of this ticket. The module_list,py patch definitely won't apply cleanly on 4.7.rc mainly because of #10334. What's more #11264 and #11236 which are needed here are merged in 4.7.1.alpha0.

That's all a bit of hassle to start from 4.7.1.alpha, but I would have to start again if I was starting from 4.7.rc.



---

archive/issue_comments_099369.json:
```json
{
    "body": "let's not forget the hardcoded version of python in SConstruct for sage_clib",
    "created_at": "2011-05-24T03:31:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99369",
    "user": "fbissey"
}
```

let's not forget the hardcoded version of python in SConstruct for sage_clib



---

archive/issue_comments_099370.json:
```json
{
    "body": "Attachment\n\nI have updated trac_9958-build-sage_clib.patch it could now be splited in its own ticket. It enables sage-clib to be smarter about the python version used. It would figure it on its own. I am looking at doing the same for setup.py, anyone would review that in its own ticket? Once in, we could at least build sage against python2.6 or 2.7 without changes.",
    "created_at": "2011-05-24T03:34:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99370",
    "user": "fbissey"
}
```

Attachment

I have updated trac_9958-build-sage_clib.patch it could now be splited in its own ticket. It enables sage-clib to be smarter about the python version used. It would figure it on its own. I am looking at doing the same for setup.py, anyone would review that in its own ticket? Once in, we could at least build sage against python2.6 or 2.7 without changes.



---

archive/issue_comments_099371.json:
```json
{
    "body": "change needed in setup.py made it python version smart. I also scrubbed the debian stuff",
    "created_at": "2011-05-24T03:44:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99371",
    "user": "fbissey"
}
```

change needed in setup.py made it python version smart. I also scrubbed the debian stuff



---

archive/issue_comments_099372.json:
```json
{
    "body": "Attachment\n\nOK I also made setup.py python version smart any volunteer to review a separate ticket?",
    "created_at": "2011-05-24T03:45:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99372",
    "user": "fbissey"
}
```

Attachment

OK I also made setup.py python version smart any volunteer to review a separate ticket?



---

archive/issue_comments_099373.json:
```json
{
    "body": "\n```\ng++ -o libcsage.dylib -single_module -flat_namespace -undefined dynamic_lookup -dynamiclib src/convert.os src/interrupt.os src/memory.os src/mpn_pylong.os src/mpz_pylong.os src/mpz_longlong.os src/stdsage.os src/gmp_globals.os src/ZZ_pylong.os src/ntl_wrap.os -L/Users/student/Desktop/sage-4.7.1.alpha1/local/lib -L/Users/student/Desktop/sage-4.7.1.alpha1/local/lib/python/config -lntl -lpari -lgmp -lpython2.7\nTraceback (most recent call last):\n  File \"setup.py\", line 18, in <module>\n    from module_list import ext_modules\n  File \"/Users/student/Desktop/sage-4.7.1.alpha1/devel/sage-main/module_list.py\", line 1529, in <module>\n    flint_depends],\nTypeError: cannot concatenate 'str' and 'list' objects\nsage: There was an error installing modified sage library code.\n\n\nreal    0m34.577s\nuser    0m19.519s\nsys     0m6.901s\nError building new version of SAGE.\nYou might try typing 'sage -ba' or write to sage-support with as much information as possible.\n\nreal    2m42.066s\nuser    0m52.903s\nsys     0m25.133s\nsage: An error occurred while installing sage-4.7.1.alpha1.p0\n```\n\nNote this is the p0 package referred to above.",
    "created_at": "2011-05-24T12:50:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99373",
    "user": "kcrisman"
}
```


```
g++ -o libcsage.dylib -single_module -flat_namespace -undefined dynamic_lookup -dynamiclib src/convert.os src/interrupt.os src/memory.os src/mpn_pylong.os src/mpz_pylong.os src/mpz_longlong.os src/stdsage.os src/gmp_globals.os src/ZZ_pylong.os src/ntl_wrap.os -L/Users/student/Desktop/sage-4.7.1.alpha1/local/lib -L/Users/student/Desktop/sage-4.7.1.alpha1/local/lib/python/config -lntl -lpari -lgmp -lpython2.7
Traceback (most recent call last):
  File "setup.py", line 18, in <module>
    from module_list import ext_modules
  File "/Users/student/Desktop/sage-4.7.1.alpha1/devel/sage-main/module_list.py", line 1529, in <module>
    flint_depends],
TypeError: cannot concatenate 'str' and 'list' objects
sage: There was an error installing modified sage library code.


real    0m34.577s
user    0m19.519s
sys     0m6.901s
Error building new version of SAGE.
You might try typing 'sage -ba' or write to sage-support with as much information as possible.

real    2m42.066s
user    0m52.903s
sys     0m25.133s
sage: An error occurred while installing sage-4.7.1.alpha1.p0
```

Note this is the p0 package referred to above.



---

archive/issue_comments_099374.json:
```json
{
    "body": "Well, there was a problem with this but it was corrected. I've checked the present\u00a0sage-4.7.1.alpha.p0 and this problem should not be there. The md5sum (md5sum\u00a0sage-4.7.1.alpha1.p0.spkg) should be\u00a0\n\nb54da7bee966eaf15942964a05a8b6b1 \u00a0sage-4.7.1.alpha1.p0.spkg\n\nIf the spkg you have is not this could you download again and see if that fixed things.",
    "created_at": "2011-05-24T14:15:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99374",
    "user": "strogdon"
}
```

Well, there was a problem with this but it was corrected. I've checked the present sage-4.7.1.alpha.p0 and this problem should not be there. The md5sum (md5sum sage-4.7.1.alpha1.p0.spkg) should be 

b54da7bee966eaf15942964a05a8b6b1  sage-4.7.1.alpha1.p0.spkg

If the spkg you have is not this could you download again and see if that fixed things.



---

archive/issue_comments_099375.json:
```json
{
    "body": "Attachment\n\nSome minor changes. The biggest change is to the doctest which explicitly refereed to python2.6 also we have extra include folders in a doctest apparently. [updated 20110525]",
    "created_at": "2011-05-25T01:01:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99375",
    "user": "fbissey"
}
```

Attachment

Some minor changes. The biggest change is to the doctest which explicitly refereed to python2.6 also we have extra include folders in a doctest apparently. [updated 20110525]



---

archive/issue_comments_099376.json:
```json
{
    "body": "I am splitting the ticket again: in #11376 we make sage building system smart and work out the python version by itself. If we get this in the next alpha that will make testing easier as you won't need a patched sage spkg to build against python-2.7.1. One will still need to patch the doctests afterwards and any other issues but it will build.\n\nIn #11377 I put the clean up of module_list.py this is not necessary for python-2.7.1 per see but it would be a huge favour to me if it was going in (it makes work on sage-on-gentoo and sage-prefix much easier).",
    "created_at": "2011-05-25T01:33:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99376",
    "user": "fbissey"
}
```

I am splitting the ticket again: in #11376 we make sage building system smart and work out the python version by itself. If we get this in the next alpha that will make testing easier as you won't need a patched sage spkg to build against python-2.7.1. One will still need to patch the doctests afterwards and any other issues but it will build.

In #11377 I put the clean up of module_list.py this is not necessary for python-2.7.1 per see but it would be a huge favour to me if it was going in (it makes work on sage-on-gentoo and sage-prefix much easier).



---

archive/issue_comments_099377.json:
```json
{
    "body": "Replying to [comment:59 strogdon]:\n> Well, there was a problem with this but it was corrected. I've checked the present\u00a0sage-4.7.1.alpha.p0 and this problem should not be there. The md5sum (md5sum\u00a0sage-4.7.1.alpha1.p0.spkg) should be\u00a0\n> \n> b54da7bee966eaf15942964a05a8b6b1 \u00a0sage-4.7.1.alpha1.p0.spkg\n> \n> If the spkg you have is not this could you download again and see if that fixed things.\n\nIt didn't seem to fix things (and I did check the md5 sum).  I'm now starting a build from scratch, having replaced the python and sage spkgs.  \n\nBy the way, now that 4.7.1.alpha1 is \"official\", one may have to upgrade the drop-in spkg.",
    "created_at": "2011-06-01T16:02:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99377",
    "user": "kcrisman"
}
```

Replying to [comment:59 strogdon]:
> Well, there was a problem with this but it was corrected. I've checked the present sage-4.7.1.alpha.p0 and this problem should not be there. The md5sum (md5sum sage-4.7.1.alpha1.p0.spkg) should be 
> 
> b54da7bee966eaf15942964a05a8b6b1  sage-4.7.1.alpha1.p0.spkg
> 
> If the spkg you have is not this could you download again and see if that fixed things.

It didn't seem to fix things (and I did check the md5 sum).  I'm now starting a build from scratch, having replaced the python and sage spkgs.  

By the way, now that 4.7.1.alpha1 is "official", one may have to upgrade the drop-in spkg.



---

archive/issue_comments_099378.json:
```json
{
    "body": "Replying to [comment:61 kcrisman]:\n\n> Replying to [comment:59 strogdon]:\n> > Well, there was a problem with this but it was corrected. I've checked the present sage-4.7.1.alpha.p0 and this problem should not be there. The md5sum (md5sum sage-4.7.1.alpha1.p0.spkg) should be  b54da7bee966eaf15942964a05a8b6b1  sage-4.7.1.alpha1.p0.spkg If the spkg you have is not this could you download again and see if that fixed things.\n> It didn't seem to fix things (and I did check the md5 sum).  I'm now starting a build from scratch, having replaced the python and sage spkgs.   By the way, now that 4.7.1.alpha1 is \"official\", one may have to upgrade the drop-in spkg.\n\nOK, for those interested I have a new drop-in spkg based on the released\u00a04.7.1.alpha1. This spkg includes the patches from this ticket as well as the patches from tickets\u00a0#11244,\u00a0#11373,\u00a0#11376\u00a0and\u00a0#11377\u00a0. I'm presently building Sage to make sure everything is as it should be. If successful, I'll post links to the drop-in spkg later today.",
    "created_at": "2011-06-01T17:59:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99378",
    "user": "strogdon"
}
```

Replying to [comment:61 kcrisman]:

> Replying to [comment:59 strogdon]:
> > Well, there was a problem with this but it was corrected. I've checked the present sage-4.7.1.alpha.p0 and this problem should not be there. The md5sum (md5sum sage-4.7.1.alpha1.p0.spkg) should be  b54da7bee966eaf15942964a05a8b6b1  sage-4.7.1.alpha1.p0.spkg If the spkg you have is not this could you download again and see if that fixed things.
> It didn't seem to fix things (and I did check the md5 sum).  I'm now starting a build from scratch, having replaced the python and sage spkgs.   By the way, now that 4.7.1.alpha1 is "official", one may have to upgrade the drop-in spkg.

OK, for those interested I have a new drop-in spkg based on the released 4.7.1.alpha1. This spkg includes the patches from this ticket as well as the patches from tickets #11244, #11373, #11376 and #11377 . I'm presently building Sage to make sure everything is as it should be. If successful, I'll post links to the drop-in spkg later today.



---

archive/issue_comments_099379.json:
```json
{
    "body": "I was hoping that #11376 and #11363 would have made it in alpha2 which would have made things easier. But I think Jeroen has closed alpha2 and is starting on alpha3. We should try to have at least these two in 4.7.1 to make testing easier.",
    "created_at": "2011-06-01T19:18:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99379",
    "user": "fbissey"
}
```

I was hoping that #11376 and #11363 would have made it in alpha2 which would have made things easier. But I think Jeroen has closed alpha2 and is starting on alpha3. We should try to have at least these two in 4.7.1 to make testing easier.



---

archive/issue_comments_099380.json:
```json
{
    "body": "The following have been uploaded:\n\nhttp://www.d.umn.edu/~strogdon/sage/install.log-4.7.1.alpha1\n\nhttp://www.d.umn.edu/~strogdon/sage/test.log-4.7.1.alpha1\n\nhttp://www.d.umn.edu/~strogdon/sage/sage-4.7.1.alpha1.p0.spkg\n\nhttp://www.d.umn.edu/~strogdon/sage/sage-4.7.1.alpha1.p0.spkg.md5\n\nfor comparisons, perhaps just under the wire for alpha2. Note, the drop-in sage spkg has the same revision .p0 extension, so I've provided the md5 sum for the spkg.",
    "created_at": "2011-06-01T20:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99380",
    "user": "strogdon"
}
```

The following have been uploaded:

http://www.d.umn.edu/~strogdon/sage/install.log-4.7.1.alpha1

http://www.d.umn.edu/~strogdon/sage/test.log-4.7.1.alpha1

http://www.d.umn.edu/~strogdon/sage/sage-4.7.1.alpha1.p0.spkg

http://www.d.umn.edu/~strogdon/sage/sage-4.7.1.alpha1.p0.spkg.md5

for comparisons, perhaps just under the wire for alpha2. Note, the drop-in sage spkg has the same revision .p0 extension, so I've provided the md5 sum for the spkg.



---

archive/issue_comments_099381.json:
```json
{
    "body": "Changed the cython.py patch in the list to accommodate new changes made in #11376.",
    "created_at": "2011-06-02T00:41:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99381",
    "user": "fbissey"
}
```

Changed the cython.py patch in the list to accommodate new changes made in #11376.



---

archive/issue_comments_099382.json:
```json
{
    "body": "End of a looong traceback while building from scratch on PPC 10.4 with the spkgs dropped in (though not the absolute most recent alpha1.p0 spkg, but that hasn't even been gotten to yet, so it shouldn't matter).  Just FYI in case that helps.\n\n```\n  File \"/Users/student/Desktop/sage-4.7.1.alpha1-python/local/lib/python/os.py\", line 284, in walk\n    if isdir(join(top, name)):\n  File \"/Users/student/Desktop/sage-4.7.1.alpha1-python/local/lib/python/genericpath.py\", line 44, in isdir\n    return stat.S_ISDIR(st.st_mode)\n  File \"/Users/student/Desktop/sage-4.7.1.alpha1-python/local/lib/python/stat.py\", line 41, in S_ISDIR\n    return S_IFMT(mode) == S_IFDIR\nRuntimeError: maximum recursion depth exceeded\nError installing Zope/Twisted interface.\n\nreal    0m16.055s\nuser    0m3.349s\nsys     0m4.671s\nsage: An error occurred while installing twisted-9.0.p2\n```\n",
    "created_at": "2011-06-06T15:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99382",
    "user": "kcrisman"
}
```

End of a looong traceback while building from scratch on PPC 10.4 with the spkgs dropped in (though not the absolute most recent alpha1.p0 spkg, but that hasn't even been gotten to yet, so it shouldn't matter).  Just FYI in case that helps.

```
  File "/Users/student/Desktop/sage-4.7.1.alpha1-python/local/lib/python/os.py", line 284, in walk
    if isdir(join(top, name)):
  File "/Users/student/Desktop/sage-4.7.1.alpha1-python/local/lib/python/genericpath.py", line 44, in isdir
    return stat.S_ISDIR(st.st_mode)
  File "/Users/student/Desktop/sage-4.7.1.alpha1-python/local/lib/python/stat.py", line 41, in S_ISDIR
    return S_IFMT(mode) == S_IFDIR
RuntimeError: maximum recursion depth exceeded
Error installing Zope/Twisted interface.

real    0m16.055s
user    0m3.349s
sys     0m4.671s
sage: An error occurred while installing twisted-9.0.p2
```




---

archive/issue_comments_099383.json:
```json
{
    "body": "Replying to [comment:66 kcrisman]:\n> End of a looong traceback while building from scratch on PPC 10.4 with the spkgs dropped in (though not the absolute most recent alpha1.p0 spkg, but that hasn't even been gotten to yet, so it shouldn't matter).  Just FYI in case that helps.\n> {{{\n>   File \"/Users/student/Desktop/sage-4.7.1.alpha1-python/local/lib/python/os.py\", line 284, in walk\n>     if isdir(join(top, name)):\n>   File \"/Users/student/Desktop/sage-4.7.1.alpha1-python/local/lib/python/genericpath.py\", line 44, in isdir\n>     return stat.S_ISDIR(st.st_mode)\n>   File \"/Users/student/Desktop/sage-4.7.1.alpha1-python/local/lib/python/stat.py\", line 41, in S_ISDIR\n>     return S_IFMT(mode) == S_IFDIR\n> RuntimeError: maximum recursion depth exceeded\n> Error installing Zope/Twisted interface.\n> \n> real    0m16.055s\n> user    0m3.349s\n> sys     0m4.671s\n> sage: An error occurred while installing twisted-9.0.p2\n> }}}\n\nWere you using the new setuptools from #11363? If so it may be worth trying a newer twisted from #8741.",
    "created_at": "2011-06-06T19:38:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99383",
    "user": "fbissey"
}
```

Replying to [comment:66 kcrisman]:
> End of a looong traceback while building from scratch on PPC 10.4 with the spkgs dropped in (though not the absolute most recent alpha1.p0 spkg, but that hasn't even been gotten to yet, so it shouldn't matter).  Just FYI in case that helps.
> {{{
>   File "/Users/student/Desktop/sage-4.7.1.alpha1-python/local/lib/python/os.py", line 284, in walk
>     if isdir(join(top, name)):
>   File "/Users/student/Desktop/sage-4.7.1.alpha1-python/local/lib/python/genericpath.py", line 44, in isdir
>     return stat.S_ISDIR(st.st_mode)
>   File "/Users/student/Desktop/sage-4.7.1.alpha1-python/local/lib/python/stat.py", line 41, in S_ISDIR
>     return S_IFMT(mode) == S_IFDIR
> RuntimeError: maximum recursion depth exceeded
> Error installing Zope/Twisted interface.
> 
> real    0m16.055s
> user    0m3.349s
> sys     0m4.671s
> sage: An error occurred while installing twisted-9.0.p2
> }}}

Were you using the new setuptools from #11363? If so it may be worth trying a newer twisted from #8741.



---

archive/issue_comments_099384.json:
```json
{
    "body": "fix doctest in sage/misc/cython.py, needs to be applied after #11376.",
    "created_at": "2011-06-14T13:33:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99384",
    "user": "fbissey"
}
```

fix doctest in sage/misc/cython.py, needs to be applied after #11376.



---

archive/issue_comments_099385.json:
```json
{
    "body": "Attachment\n\nUpdated trac_9958-fix-misc_cythonpy.patch to take into account changes in #11376. For some reason the numpy include line appears after the application of the other patches over there. Why it didn't appear before is a mistery.",
    "created_at": "2011-06-14T13:36:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99385",
    "user": "fbissey"
}
```

Attachment

Updated trac_9958-fix-misc_cythonpy.patch to take into account changes in #11376. For some reason the numpy include line appears after the application of the other patches over there. Why it didn't appear before is a mistery.



---

archive/issue_comments_099386.json:
```json
{
    "body": "By the way, I don't know how feasible this is, but it would be very nice if the new python spkg passed self-tests: set SAGE_CHECK to \"yes\" and install the spkg.  Previous versions of Python have failed the self-tests, but it's perhaps the only standard spkg for which this is true.  With the spkg here, on an OS X box:\n\n```\n344 tests OK.\n4 tests failed:\n    test__locale test_ctypes test_distutils test_locale\n38 tests skipped:\n    test_aepack test_al test_applesingle test_bsddb test_bsddb3\n    test_cd test_cl test_codecmaps_cn test_codecmaps_hk\n    test_codecmaps_jp test_codecmaps_kr test_codecmaps_tw test_curses\n    test_dl test_epoll test_gdb test_gdbm test_gl test_imageop\n    test_imgfile test_largefile test_linuxaudiodev test_macos\n    test_macostools test_ossaudiodev test_scriptpackages test_smtpnet\n    test_socketserver test_startfile test_sunaudiodev test_timeout\n    test_tk test_ttk_guionly test_urllib2net test_urllibnet\n    test_winreg test_winsound test_zipfile64\n5 skips unexpected on darwin:\n    test_aepack test_applesingle test_dl test_macos\n    test_scriptpackages\nmake: *** [test] Error 1\nAn error occurred while testing Python\n```\n\nOn sage.math:\n\n```\n346 tests OK.\n1 test failed:\n    test_distutils\n39 tests skipped:\n    test_aepack test_al test_applesingle test_bsddb test_bsddb185\n    test_bsddb3 test_cd test_cl test_codecmaps_cn test_codecmaps_hk\n    test_codecmaps_jp test_codecmaps_kr test_codecmaps_tw test_curses\n    test_dbm test_dl test_gdb test_gdbm test_gl test_imageop\n    test_imgfile test_kqueue test_linuxaudiodev test_macos\n    test_macostools test_ossaudiodev test_scriptpackages test_smtpnet\n    test_socketserver test_startfile test_sunaudiodev test_timeout\n    test_tk test_ttk_guionly test_urllib2net test_urllibnet\n    test_winreg test_winsound test_zipfile64\n7 skips unexpected on linux2:\n    test_bsddb test_bsddb3 test_dbm test_gdb test_gdbm test_tk\n    test_ttk_guionly\nmake: *** [test] Error 1\nAn error occurred while testing Python\n```\n\n(I didn't upgrade the distutils package or anything else, just ran \"sage -f python-2.7.1.spkg\", so some of these may go away.)",
    "created_at": "2011-06-20T18:40:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99386",
    "user": "jhpalmieri"
}
```

By the way, I don't know how feasible this is, but it would be very nice if the new python spkg passed self-tests: set SAGE_CHECK to "yes" and install the spkg.  Previous versions of Python have failed the self-tests, but it's perhaps the only standard spkg for which this is true.  With the spkg here, on an OS X box:

```
344 tests OK.
4 tests failed:
    test__locale test_ctypes test_distutils test_locale
38 tests skipped:
    test_aepack test_al test_applesingle test_bsddb test_bsddb3
    test_cd test_cl test_codecmaps_cn test_codecmaps_hk
    test_codecmaps_jp test_codecmaps_kr test_codecmaps_tw test_curses
    test_dl test_epoll test_gdb test_gdbm test_gl test_imageop
    test_imgfile test_largefile test_linuxaudiodev test_macos
    test_macostools test_ossaudiodev test_scriptpackages test_smtpnet
    test_socketserver test_startfile test_sunaudiodev test_timeout
    test_tk test_ttk_guionly test_urllib2net test_urllibnet
    test_winreg test_winsound test_zipfile64
5 skips unexpected on darwin:
    test_aepack test_applesingle test_dl test_macos
    test_scriptpackages
make: *** [test] Error 1
An error occurred while testing Python
```

On sage.math:

```
346 tests OK.
1 test failed:
    test_distutils
39 tests skipped:
    test_aepack test_al test_applesingle test_bsddb test_bsddb185
    test_bsddb3 test_cd test_cl test_codecmaps_cn test_codecmaps_hk
    test_codecmaps_jp test_codecmaps_kr test_codecmaps_tw test_curses
    test_dbm test_dl test_gdb test_gdbm test_gl test_imageop
    test_imgfile test_kqueue test_linuxaudiodev test_macos
    test_macostools test_ossaudiodev test_scriptpackages test_smtpnet
    test_socketserver test_startfile test_sunaudiodev test_timeout
    test_tk test_ttk_guionly test_urllib2net test_urllibnet
    test_winreg test_winsound test_zipfile64
7 skips unexpected on linux2:
    test_bsddb test_bsddb3 test_dbm test_gdb test_gdbm test_tk
    test_ttk_guionly
make: *** [test] Error 1
An error occurred while testing Python
```

(I didn't upgrade the distutils package or anything else, just ran "sage -f python-2.7.1.spkg", so some of these may go away.)



---

archive/issue_comments_099387.json:
```json
{
    "body": "python testing is difficult. Even in gentoo the procedure is complicated. I'll have a look at it but I cannot make promise. There may be modules that we shouldn't build in the first place (nothing useful to sage, don't worry).\n\nWe have this for example in the ebuild:\n\n```\n\tif use berkdb; then\n\t\tewarn \"\\\"bsddb\\\" module is out-of-date and no longer maintained inside dev-lang/python. It has\"\n\t\tewarn \"been additionally removed in Python 3. You should use external, still maintained \\\"bsddb3\\\"\"\n\t\tewarn \"module provided by dev-python/bsddb3 which supports both Python 2 and Python 3.\"\n\tfi\n```\n\n\ngdb, gdm, dbm and tk require extra things on the host system so they may very well fail without. Actually according to the ebuild distutils and gdm are known to fail.",
    "created_at": "2011-06-20T20:25:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99387",
    "user": "fbissey"
}
```

python testing is difficult. Even in gentoo the procedure is complicated. I'll have a look at it but I cannot make promise. There may be modules that we shouldn't build in the first place (nothing useful to sage, don't worry).

We have this for example in the ebuild:

```
	if use berkdb; then
		ewarn "\"bsddb\" module is out-of-date and no longer maintained inside dev-lang/python. It has"
		ewarn "been additionally removed in Python 3. You should use external, still maintained \"bsddb3\""
		ewarn "module provided by dev-python/bsddb3 which supports both Python 2 and Python 3."
	fi
```


gdb, gdm, dbm and tk require extra things on the host system so they may very well fail without. Actually according to the ebuild distutils and gdm are known to fail.



---

archive/issue_comments_099388.json:
```json
{
    "body": "Just for the record:\n\nhttp://trac.sagemath.org/sage_trac/ticket/8664#comment:33 gives an example on how to automatically rebuild packages that depend on a newly added spkg (here: Python).\n\n(Artificial version bumps aren't necessary, and simply `touch`ing `spkg/installed/<spkg-that-others-depend-on>` alone doesn't work.)\n\nIn general:\n1. Copy the new spkg(s) to `$SAGE_ROOT/spkg/standard/`.\n2. `export SAGE_UPGRADING=yes`\n3. (Optionally set `MAKE` and `SAGE_PARALLEL_SPKG_BUILD`, perhaps `SAGE_CHECK`.)\n4. Run `make` (or better `make build`) rather than doing `./sage -f ...`\n5. Apply patches to the Sage library.\n6. Run `./sage -b` (or `./sage -ba-force` in case not all dependencies are covered by `module_list.py`, which in general I'd consider a bug, but this might be necessary upon a Python upgrade)\n7. Run tests or whatever.\n\nNote that Sage switches to the \"main\" branch whenever the Sage spkg gets reinstalled.\n\nOf course patches to the build system are usually a bit trickier, but as far as I can see Francois already sorted these out.",
    "created_at": "2011-06-24T22:55:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99388",
    "user": "leif"
}
```

Just for the record:

http://trac.sagemath.org/sage_trac/ticket/8664#comment:33 gives an example on how to automatically rebuild packages that depend on a newly added spkg (here: Python).

(Artificial version bumps aren't necessary, and simply `touch`ing `spkg/installed/<spkg-that-others-depend-on>` alone doesn't work.)

In general:
1. Copy the new spkg(s) to `$SAGE_ROOT/spkg/standard/`.
2. `export SAGE_UPGRADING=yes`
3. (Optionally set `MAKE` and `SAGE_PARALLEL_SPKG_BUILD`, perhaps `SAGE_CHECK`.)
4. Run `make` (or better `make build`) rather than doing `./sage -f ...`
5. Apply patches to the Sage library.
6. Run `./sage -b` (or `./sage -ba-force` in case not all dependencies are covered by `module_list.py`, which in general I'd consider a bug, but this might be necessary upon a Python upgrade)
7. Run tests or whatever.

Note that Sage switches to the "main" branch whenever the Sage spkg gets reinstalled.

Of course patches to the build system are usually a bit trickier, but as far as I can see Francois already sorted these out.



---

archive/issue_comments_099389.json:
```json
{
    "body": "Thanks for the pointer, it will make testing easier for everyone. The bad news is that all the bits that makes testing easier won't be in 4.7.1. The good news is that everything is merged in 4.7.2.alpha0 at the moment. So once the next release cycle begins things will get easier. No patch will be needed to the build system. All that will remain will be doctest fix and issues like #11339.\n\nI will update trac_9958-fixing_numericalnoise-part2.patch shortly as #11255 broke it. Which means an extra patch may appear later once I have put all the pieces back together.",
    "created_at": "2011-06-24T23:13:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99389",
    "user": "fbissey"
}
```

Thanks for the pointer, it will make testing easier for everyone. The bad news is that all the bits that makes testing easier won't be in 4.7.1. The good news is that everything is merged in 4.7.2.alpha0 at the moment. So once the next release cycle begins things will get easier. No patch will be needed to the build system. All that will remain will be doctest fix and issues like #11339.

I will update trac_9958-fixing_numericalnoise-part2.patch shortly as #11255 broke it. Which means an extra patch may appear later once I have put all the pieces back together.



---

archive/issue_comments_099390.json:
```json
{
    "body": "fix numerical noise part 2 (refreshed against 4.7.1.alpha3 -20110625)",
    "created_at": "2011-06-24T23:15:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99390",
    "user": "fbissey"
}
```

fix numerical noise part 2 (refreshed against 4.7.1.alpha3 -20110625)



---

archive/issue_comments_099391.json:
```json
{
    "body": "Attachment\n\nOK. There are a few more patches needed for numerical and formatting noise in 4.7.2.alpha1 but now anyone should be able to upgrade python without a premade sage spkg. All fixes to be able to build sage against python-2.7 out of the box are in!",
    "created_at": "2011-08-23T22:04:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99391",
    "user": "fbissey"
}
```

Attachment

OK. There are a few more patches needed for numerical and formatting noise in 4.7.2.alpha1 but now anyone should be able to upgrade python without a premade sage spkg. All fixes to be able to build sage against python-2.7 out of the box are in!



---

archive/issue_comments_099392.json:
```json
{
    "body": "> (Artificial version bumps aren't necessary, and simply `touch`ing `spkg/installed/<spkg-that-others-depend-on>` alone doesn't work.)\n> \n> In general:\n>  1. Copy the new spkg(s) to `$SAGE_ROOT/spkg/standard/`.\n>  1. `export SAGE_UPGRADING=yes`\nHuh, I didn't know about that, and it would be quite useful.  I can't find it in either the installation guide or the developer guide, though - is this documented yet?  Just curious.\n\nFrancois, I'll try to give this a test run on PPC OS X and/or Cygwin if you like.",
    "created_at": "2011-08-23T23:58:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99392",
    "user": "kcrisman"
}
```

> (Artificial version bumps aren't necessary, and simply `touch`ing `spkg/installed/<spkg-that-others-depend-on>` alone doesn't work.)
> 
> In general:
>  1. Copy the new spkg(s) to `$SAGE_ROOT/spkg/standard/`.
>  1. `export SAGE_UPGRADING=yes`
Huh, I didn't know about that, and it would be quite useful.  I can't find it in either the installation guide or the developer guide, though - is this documented yet?  Just curious.

Francois, I'll try to give this a test run on PPC OS X and/or Cygwin if you like.



---

archive/issue_comments_099393.json:
```json
{
    "body": "Replying to [comment:76 kcrisman]:\n> Francois, I'll try to give this a test run on PPC OS X and/or Cygwin if you like.  \n\nBe my guest, I thought that the fact things just became easier warranted an announcement.",
    "created_at": "2011-08-24T00:03:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99393",
    "user": "fbissey"
}
```

Replying to [comment:76 kcrisman]:
> Francois, I'll try to give this a test run on PPC OS X and/or Cygwin if you like.  

Be my guest, I thought that the fact things just became easier warranted an announcement.



---

archive/issue_comments_099394.json:
```json
{
    "body": "Wonderful, this is great news! :) Thanks!",
    "created_at": "2011-08-24T01:33:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99394",
    "user": "kini"
}
```

Wonderful, this is great news! :) Thanks!



---

archive/issue_comments_099395.json:
```json
{
    "body": "So far Mac PPC is doing fine (I just swapped out the spkgs in a source tar).  Numpy, mercurial, various other python-related spkgs apparently built ok, though it isn't at Scipy or Sage yet.  I did NOT check with `SAGE_CHECK=yes` since I didn't want to have to watch the build and turn that off during the Python build...  Anyway, looks good so far.  If it finishes I'll apply all the patches :)",
    "created_at": "2011-08-24T17:43:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99395",
    "user": "kcrisman"
}
```

So far Mac PPC is doing fine (I just swapped out the spkgs in a source tar).  Numpy, mercurial, various other python-related spkgs apparently built ok, though it isn't at Scipy or Sage yet.  I did NOT check with `SAGE_CHECK=yes` since I didn't want to have to watch the build and turn that off during the Python build...  Anyway, looks good so far.  If it finishes I'll apply all the patches :)



---

archive/issue_comments_099396.json:
```json
{
    "body": "I tried this (new python spkg plus all of the patches, then built from scratch) and I'm seeing a bunch of doctest failures.  Are some of these due to #11339?\n\n```\nThe following tests failed:\n\n        sage -t  -long -force_lib devel/sage/sage/categories/finite_crystals.py # 1 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/rings/morphism.pyx # 0 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/rings/integer.pyx # 3 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/rings/homset.py # 0 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/rings/padics/padic_capped_relative_element.pyx #  1 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/combinat/e_one_star.py # 1 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/combinat/words/nfactor_enumerable_word.py # 2 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/geometry/polyhedra.py # 1 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/schemes/generic/scheme.py # 0 doctests failed\n        sage -t  -long -force_lib devel/sage/sage/symbolic/callable.py # 5 doctests failed\n```\n\nI think I did everything right.  I put together a Sage distribution with the python spkg and the patches, based on 4.7.2.alpha1:\n\n- [http://sage.math.washington.edu/home/palmieri/misc/9958/sage-4.7.2.9958.tar](http://sage.math.washington.edu/home/palmieri/misc/9958/sage-4.7.2.9958.tar)\n\nUpgrade path:\n\n- [http://sage.math.washington.edu/home/palmieri/misc/9958/sage-4.7.2.9958/](http://sage.math.washington.edu/home/palmieri/misc/9958/sage-4.7.2.9958/)",
    "created_at": "2011-08-25T02:00:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99396",
    "user": "jhpalmieri"
}
```

I tried this (new python spkg plus all of the patches, then built from scratch) and I'm seeing a bunch of doctest failures.  Are some of these due to #11339?

```
The following tests failed:

        sage -t  -long -force_lib devel/sage/sage/categories/finite_crystals.py # 1 doctests failed
        sage -t  -long -force_lib devel/sage/sage/rings/morphism.pyx # 0 doctests failed
        sage -t  -long -force_lib devel/sage/sage/rings/integer.pyx # 3 doctests failed
        sage -t  -long -force_lib devel/sage/sage/rings/homset.py # 0 doctests failed
        sage -t  -long -force_lib devel/sage/sage/rings/padics/padic_capped_relative_element.pyx #  1 doctests failed
        sage -t  -long -force_lib devel/sage/sage/combinat/e_one_star.py # 1 doctests failed
        sage -t  -long -force_lib devel/sage/sage/combinat/words/nfactor_enumerable_word.py # 2 doctests failed
        sage -t  -long -force_lib devel/sage/sage/geometry/polyhedra.py # 1 doctests failed
        sage -t  -long -force_lib devel/sage/sage/schemes/generic/scheme.py # 0 doctests failed
        sage -t  -long -force_lib devel/sage/sage/symbolic/callable.py # 5 doctests failed
```

I think I did everything right.  I put together a Sage distribution with the python spkg and the patches, based on 4.7.2.alpha1:

- [http://sage.math.washington.edu/home/palmieri/misc/9958/sage-4.7.2.9958.tar](http://sage.math.washington.edu/home/palmieri/misc/9958/sage-4.7.2.9958.tar)

Upgrade path:

- [http://sage.math.washington.edu/home/palmieri/misc/9958/sage-4.7.2.9958/](http://sage.math.washington.edu/home/palmieri/misc/9958/sage-4.7.2.9958/)



---

archive/issue_comments_099397.json:
```json
{
    "body": "Any failures from #11339 gives you a killed doctest, so\n\n```\nsage -t  -long -force_lib devel/sage/sage/rings/morphism.pyx\nsage -t  -long -force_lib devel/sage/sage/rings/homset.py\nsage -t  -long -force_lib devel/sage/sage/schemes/generic/scheme.py\n```\n\ncould all be, a verbose run would help figure it out. By nature #11339 is somewhat random, not everyone see the same failures but all these are familiar.\n\nJust checking the others with my current list.\n\n* sage/categories/finite_crystals.py is a new one introduced in 4.7.2 where the error message has changed slightly when using python-2.7.\n* sage/rings/integer.pyx is definitely python-2.7 related but not patched yet because I am not sure what should be done there.\n* sage/rings/padics/padic_capped_relative_element.pyx same thing\n* sage/combinat/e_one_star.py I had a patch but it became to fuzzy haven't done a new one.\n* sage/combinat/words/nfactor_enumerable_word.py python-2.7 two successive results are inverted, I want someone else to look at that one to make sure we can just do the obvious thing.\n* sage/symbolic/callable.py new in 4.7.2 change in the error message because we are running python-2.7\n* sage/geometry/polyhedra.py never seen that one before, can you re-run it and give more info on the failure?\n\nAs you can see a few more patches are needed and apart from #11339 which is a big show stopper because of the crashes at least two other tests point to some potential problems that should be looked at.",
    "created_at": "2011-08-25T03:44:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99397",
    "user": "fbissey"
}
```

Any failures from #11339 gives you a killed doctest, so

```
sage -t  -long -force_lib devel/sage/sage/rings/morphism.pyx
sage -t  -long -force_lib devel/sage/sage/rings/homset.py
sage -t  -long -force_lib devel/sage/sage/schemes/generic/scheme.py
```

could all be, a verbose run would help figure it out. By nature #11339 is somewhat random, not everyone see the same failures but all these are familiar.

Just checking the others with my current list.

* sage/categories/finite_crystals.py is a new one introduced in 4.7.2 where the error message has changed slightly when using python-2.7.
* sage/rings/integer.pyx is definitely python-2.7 related but not patched yet because I am not sure what should be done there.
* sage/rings/padics/padic_capped_relative_element.pyx same thing
* sage/combinat/e_one_star.py I had a patch but it became to fuzzy haven't done a new one.
* sage/combinat/words/nfactor_enumerable_word.py python-2.7 two successive results are inverted, I want someone else to look at that one to make sure we can just do the obvious thing.
* sage/symbolic/callable.py new in 4.7.2 change in the error message because we are running python-2.7
* sage/geometry/polyhedra.py never seen that one before, can you re-run it and give more info on the failure?

As you can see a few more patches are needed and apart from #11339 which is a big show stopper because of the crashes at least two other tests point to some potential problems that should be looked at.



---

archive/issue_comments_099398.json:
```json
{
    "body": "Here are the failures I get on x86:\n\n\n```\nsage -t -long \u00a0-force_lib devel/sage-main/sage/libs/cremona/newforms.pyx # 1 doctests failed\nsage -t -long \u00a0-force_lib devel/sage-main/sage/misc/sageinspect.py # 1 doctests failed\nsage -t -long \u00a0-force_lib devel/sage-main/sage/misc/randstate.pyx # 1 doctests failed\nsage -t -long \u00a0-force_lib devel/sage-main/sage/rings/real_mpfr.pyx # 1 doctests failed\nsage -t -long \u00a0-force_lib devel/sage-main/sage/stats/intlist.pyx # 1 doctests failed\nsage -t -long \u00a0-force_lib devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py # 1 doctests failed\nsage -t -long \u00a0-force_lib devel/sage-main/sage/combinat/e_one_star.py # 1 doctests failed\nsage -t -long \u00a0-force_lib devel/sage-main/sage/geometry/polyhedra.py # 1 doctests failed\nsage -t -long \u00a0-force_lib devel/sage-main/sage/crypto/mq/mpolynomialsystem.py # Killed/crashed\nsage -t -long \u00a0-force_lib devel/sage-main/sage/symbolic/callable.py # 5 doctests failed\nsage -t -long \u00a0-force_lib devel/sage-main/sage/functions/transcendental.py # 1 doctests failed\nsage -t -long \u00a0-force_lib devel/sage-main/sage/categories/finite_crystals.py # 1 doctests failed\n```\n\n\nThe failures newforms.pyx, real_mpfr.pyx and intlist.pyx are all of the form:\n\n\n```\nFile \"/storage/sage/sage-4.7.2.alpha1/devel/sage-main/sage/libs/cremona/newforms.pyx\", line 53:\n    sage: ECModularSymbol(E)\nExpected:\n    Traceback (most recent call last):\n    ...\n    OverflowError: long int too large to convert to int\nGot:\n    Traceback (most recent call last):\n      File \"/storage/sage/sage-4.7.2.alpha1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/storage/sage/sage-4.7.2.alpha1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/storage/sage/sage-4.7.2.alpha1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[11]>\", line 1, in <module>\n        ECModularSymbol(E)###line 53:\n    sage: ECModularSymbol(E)\n      File \"newforms.pyx\", line 69, in sage.libs.cremona.newforms.ECModularSymbol.__init__ (sage/libs/cremona/newforms.cpp:1820)\n        a6 = new_bigint(int(E.a6()))\n    OverflowError: Python int too large to convert to C long\n```\n\n\nThese tests do not fail on amd64 because \"long int too large to convert to int\" is returned as the OverflowError instead of \"Python int too large to convert to C long\".",
    "created_at": "2011-08-25T04:50:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99398",
    "user": "strogdon"
}
```

Here are the failures I get on x86:


```
sage -t -long  -force_lib devel/sage-main/sage/libs/cremona/newforms.pyx # 1 doctests failed
sage -t -long  -force_lib devel/sage-main/sage/misc/sageinspect.py # 1 doctests failed
sage -t -long  -force_lib devel/sage-main/sage/misc/randstate.pyx # 1 doctests failed
sage -t -long  -force_lib devel/sage-main/sage/rings/real_mpfr.pyx # 1 doctests failed
sage -t -long  -force_lib devel/sage-main/sage/stats/intlist.pyx # 1 doctests failed
sage -t -long  -force_lib devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py # 1 doctests failed
sage -t -long  -force_lib devel/sage-main/sage/combinat/e_one_star.py # 1 doctests failed
sage -t -long  -force_lib devel/sage-main/sage/geometry/polyhedra.py # 1 doctests failed
sage -t -long  -force_lib devel/sage-main/sage/crypto/mq/mpolynomialsystem.py # Killed/crashed
sage -t -long  -force_lib devel/sage-main/sage/symbolic/callable.py # 5 doctests failed
sage -t -long  -force_lib devel/sage-main/sage/functions/transcendental.py # 1 doctests failed
sage -t -long  -force_lib devel/sage-main/sage/categories/finite_crystals.py # 1 doctests failed
```


The failures newforms.pyx, real_mpfr.pyx and intlist.pyx are all of the form:


```
File "/storage/sage/sage-4.7.2.alpha1/devel/sage-main/sage/libs/cremona/newforms.pyx", line 53:
    sage: ECModularSymbol(E)
Expected:
    Traceback (most recent call last):
    ...
    OverflowError: long int too large to convert to int
Got:
    Traceback (most recent call last):
      File "/storage/sage/sage-4.7.2.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/storage/sage/sage-4.7.2.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/storage/sage/sage-4.7.2.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[11]>", line 1, in <module>
        ECModularSymbol(E)###line 53:
    sage: ECModularSymbol(E)
      File "newforms.pyx", line 69, in sage.libs.cremona.newforms.ECModularSymbol.__init__ (sage/libs/cremona/newforms.cpp:1820)
        a6 = new_bigint(int(E.a6()))
    OverflowError: Python int too large to convert to C long
```


These tests do not fail on amd64 because "long int too large to convert to int" is returned as the OverflowError instead of "Python int too large to convert to C long".



---

archive/issue_comments_099399.json:
```json
{
    "body": "I had forgotten about these. We need different test results for 32 and 64 bits for these.",
    "created_at": "2011-08-25T05:00:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99399",
    "user": "fbissey"
}
```

I had forgotten about these. We need different test results for 32 and 64 bits for these.



---

archive/issue_comments_099400.json:
```json
{
    "body": "Here's the failure for `sage/geometry/polyhedra.py`:\n\n```\nsage -t -long -force_lib \"devel/sage/sage/geometry/polyhedra.py\"\n**********************************************************************\nFile \"/mnt/usb1/scratch/palmieri/9958/sage-4.7.2.9958/devel/sage/sage/geometry/polyhedra.py\", line 4948:\n    sage: ppoints[0]\nExpected:\n    (-1.92296268638e-15, -1.92296268638e-15)\nGot:\n    (0.0, 0.0)\n**********************************************************************\n```\n\nIt looks like numerical noise, but is it an acceptable level of accuracy?",
    "created_at": "2011-08-25T17:30:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99400",
    "user": "jhpalmieri"
}
```

Here's the failure for `sage/geometry/polyhedra.py`:

```
sage -t -long -force_lib "devel/sage/sage/geometry/polyhedra.py"
**********************************************************************
File "/mnt/usb1/scratch/palmieri/9958/sage-4.7.2.9958/devel/sage/sage/geometry/polyhedra.py", line 4948:
    sage: ppoints[0]
Expected:
    (-1.92296268638e-15, -1.92296268638e-15)
Got:
    (0.0, 0.0)
**********************************************************************
```

It looks like numerical noise, but is it an acceptable level of accuracy?



---

archive/issue_comments_099401.json:
```json
{
    "body": "Now I remember that test, it is even in the log [attachment:sage-4.7.alpha5-test.log.bz2] I produced a while ago. Strangely enough it doesn't happen anymore on my sage-on-gentoo install. I also have pari-2.5.0 and maxima-5.25.0 on this install, I suspect one of them may be responsible for the disparition of that failure",
    "created_at": "2011-08-26T01:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99401",
    "user": "fbissey"
}
```

Now I remember that test, it is even in the log [attachment:sage-4.7.alpha5-test.log.bz2] I produced a while ago. Strangely enough it doesn't happen anymore on my sage-on-gentoo install. I also have pari-2.5.0 and maxima-5.25.0 on this install, I suspect one of them may be responsible for the disparition of that failure



---

archive/issue_comments_099402.json:
```json
{
    "body": "I am wrong! Not maxima or pari, there is a patch for it in [attachment:trac_9958-fixing_numericalnoise-part1.patch]. So it looks like that bit may not be applied properly.",
    "created_at": "2011-08-26T01:35:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99402",
    "user": "fbissey"
}
```

I am wrong! Not maxima or pari, there is a patch for it in [attachment:trac_9958-fixing_numericalnoise-part1.patch]. So it looks like that bit may not be applied properly.



---

archive/issue_comments_099403.json:
```json
{
    "body": "Attachment\n\nfix numerical noise in e_one_star.py",
    "created_at": "2011-08-26T03:22:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99403",
    "user": "fbissey"
}
```

Attachment

fix numerical noise in e_one_star.py



---

archive/issue_comments_099404.json:
```json
{
    "body": "fix error message in finite_crystals.py",
    "created_at": "2011-08-26T03:22:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99404",
    "user": "fbissey"
}
```

fix error message in finite_crystals.py



---

archive/issue_comments_099405.json:
```json
{
    "body": "Attachment\n\nfix error message in symbolics/callable.py",
    "created_at": "2011-08-26T03:23:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99405",
    "user": "fbissey"
}
```

Attachment

fix error message in symbolics/callable.py



---

archive/issue_comments_099406.json:
```json
{
    "body": "Attachment\n\nAdded three new patches. I will rework the patches that need adjusting between 32 and 64 bits next.",
    "created_at": "2011-08-26T03:25:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99406",
    "user": "fbissey"
}
```

Attachment

Added three new patches. I will rework the patches that need adjusting between 32 and 64 bits next.



---

archive/issue_comments_099407.json:
```json
{
    "body": "Replying to [comment:82 strogdon]:\n> Here are the failures I get on x86:\n> \n> {{{\n> sage -t -long \u00a0-force_lib devel/sage-main/sage/libs/cremona/newforms.pyx # 1 doctests failed\n> sage -t -long \u00a0-force_lib devel/sage-main/sage/misc/sageinspect.py # 1 doctests failed\n> sage -t -long \u00a0-force_lib devel/sage-main/sage/misc/randstate.pyx # 1 doctests failed\n> sage -t -long \u00a0-force_lib devel/sage-main/sage/rings/real_mpfr.pyx # 1 doctests failed\n> sage -t -long \u00a0-force_lib devel/sage-main/sage/stats/intlist.pyx # 1 doctests failed\n> sage -t -long \u00a0-force_lib devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py # 1 doctests failed\n> sage -t -long \u00a0-force_lib devel/sage-main/sage/combinat/e_one_star.py # 1 doctests failed\n> sage -t -long \u00a0-force_lib devel/sage-main/sage/geometry/polyhedra.py # 1 doctests failed\n> sage -t -long \u00a0-force_lib devel/sage-main/sage/crypto/mq/mpolynomialsystem.py # Killed/crashed\n> sage -t -long \u00a0-force_lib devel/sage-main/sage/symbolic/callable.py # 5 doctests failed\n> sage -t -long \u00a0-force_lib devel/sage-main/sage/functions/transcendental.py # 1 doctests failed\n> sage -t -long \u00a0-force_lib devel/sage-main/sage/categories/finite_crystals.py # 1 doctests failed\n> }}}\n> \n> The failures newforms.pyx, real_mpfr.pyx and intlist.pyx are all of the form:\n> \n> {{{\n> File \"/storage/sage/sage-4.7.2.alpha1/devel/sage-main/sage/libs/cremona/newforms.pyx\", line 53:\n>     sage: ECModularSymbol(E)\n> Expected:\n>     Traceback (most recent call last):\n>     ...\n>     OverflowError: long int too large to convert to int\n> Got:\n>     Traceback (most recent call last):\n>       File \"/storage/sage/sage-4.7.2.alpha1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n>         self.run_one_example(test, example, filename, compileflags)\n>       File \"/storage/sage/sage-4.7.2.alpha1/local/bin/sagedoctest.py\", line 38, in run_one_example\n>         OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n>       File \"/storage/sage/sage-4.7.2.alpha1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n>         compileflags, 1) in test.globs\n>       File \"<doctest __main__.example_1[11]>\", line 1, in <module>\n>         ECModularSymbol(E)###line 53:\n>     sage: ECModularSymbol(E)\n>       File \"newforms.pyx\", line 69, in sage.libs.cremona.newforms.ECModularSymbol.__init__ (sage/libs/cremona/newforms.cpp:1820)\n>         a6 = new_bigint(int(E.a6()))\n>     OverflowError: Python int too large to convert to C long\n> }}}\n> \n> These tests do not fail on amd64 because \"long int too large to convert to int\" is returned as the OverflowError instead of \"Python int too large to convert to C long\".\n\n\nSteve, what about\n\n```\nsage -t -long  -force_lib devel/sage-main/sage/rings/polynomial/polynomial_rational_flint.pyx\n```\n",
    "created_at": "2011-08-26T03:37:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99407",
    "user": "fbissey"
}
```

Replying to [comment:82 strogdon]:
> Here are the failures I get on x86:
> 
> {{{
> sage -t -long  -force_lib devel/sage-main/sage/libs/cremona/newforms.pyx # 1 doctests failed
> sage -t -long  -force_lib devel/sage-main/sage/misc/sageinspect.py # 1 doctests failed
> sage -t -long  -force_lib devel/sage-main/sage/misc/randstate.pyx # 1 doctests failed
> sage -t -long  -force_lib devel/sage-main/sage/rings/real_mpfr.pyx # 1 doctests failed
> sage -t -long  -force_lib devel/sage-main/sage/stats/intlist.pyx # 1 doctests failed
> sage -t -long  -force_lib devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py # 1 doctests failed
> sage -t -long  -force_lib devel/sage-main/sage/combinat/e_one_star.py # 1 doctests failed
> sage -t -long  -force_lib devel/sage-main/sage/geometry/polyhedra.py # 1 doctests failed
> sage -t -long  -force_lib devel/sage-main/sage/crypto/mq/mpolynomialsystem.py # Killed/crashed
> sage -t -long  -force_lib devel/sage-main/sage/symbolic/callable.py # 5 doctests failed
> sage -t -long  -force_lib devel/sage-main/sage/functions/transcendental.py # 1 doctests failed
> sage -t -long  -force_lib devel/sage-main/sage/categories/finite_crystals.py # 1 doctests failed
> }}}
> 
> The failures newforms.pyx, real_mpfr.pyx and intlist.pyx are all of the form:
> 
> {{{
> File "/storage/sage/sage-4.7.2.alpha1/devel/sage-main/sage/libs/cremona/newforms.pyx", line 53:
>     sage: ECModularSymbol(E)
> Expected:
>     Traceback (most recent call last):
>     ...
>     OverflowError: long int too large to convert to int
> Got:
>     Traceback (most recent call last):
>       File "/storage/sage/sage-4.7.2.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
>         self.run_one_example(test, example, filename, compileflags)
>       File "/storage/sage/sage-4.7.2.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
>         OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
>       File "/storage/sage/sage-4.7.2.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
>         compileflags, 1) in test.globs
>       File "<doctest __main__.example_1[11]>", line 1, in <module>
>         ECModularSymbol(E)###line 53:
>     sage: ECModularSymbol(E)
>       File "newforms.pyx", line 69, in sage.libs.cremona.newforms.ECModularSymbol.__init__ (sage/libs/cremona/newforms.cpp:1820)
>         a6 = new_bigint(int(E.a6()))
>     OverflowError: Python int too large to convert to C long
> }}}
> 
> These tests do not fail on amd64 because "long int too large to convert to int" is returned as the OverflowError instead of "Python int too large to convert to C long".


Steve, what about

```
sage -t -long  -force_lib devel/sage-main/sage/rings/polynomial/polynomial_rational_flint.pyx
```




---

archive/issue_comments_099408.json:
```json
{
    "body": "Replying to [comment:88 fbissey]:\n> Replying to [comment:82 strogdon]:\n> \n> Steve, what about\n> {{{\n> sage -t -long  -force_lib devel/sage-main/sage/rings/polynomial/polynomial_rational_flint.pyx\n> }}}\n\nHere on x86 and amd64 the test passes. So, there seems to be some sort of inconsistency, doesn't it?",
    "created_at": "2011-08-26T03:53:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99408",
    "user": "strogdon"
}
```

Replying to [comment:88 fbissey]:
> Replying to [comment:82 strogdon]:
> 
> Steve, what about
> {{{
> sage -t -long  -force_lib devel/sage-main/sage/rings/polynomial/polynomial_rational_flint.pyx
> }}}

Here on x86 and amd64 the test passes. So, there seems to be some sort of inconsistency, doesn't it?



---

archive/issue_comments_099409.json:
```json
{
    "body": "Replying to [comment:89 strogdon]:\n> Replying to [comment:88 fbissey]:\n> > Replying to [comment:82 strogdon]:\n> > \n> > Steve, what about\n> > {{{\n> > sage -t -long  -force_lib devel/sage-main/sage/rings/polynomial/polynomial_rational_flint.pyx\n> > }}}\n> \n> Here on x86 and amd64 the test passes. So, there seems to be some sort of inconsistency, doesn't it?\n\nYes! I'll fix it but it should be investigated. Gut feeling is on variation in cython definitions.",
    "created_at": "2011-08-26T03:58:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99409",
    "user": "fbissey"
}
```

Replying to [comment:89 strogdon]:
> Replying to [comment:88 fbissey]:
> > Replying to [comment:82 strogdon]:
> > 
> > Steve, what about
> > {{{
> > sage -t -long  -force_lib devel/sage-main/sage/rings/polynomial/polynomial_rational_flint.pyx
> > }}}
> 
> Here on x86 and amd64 the test passes. So, there seems to be some sort of inconsistency, doesn't it?

Yes! I'll fix it but it should be investigated. Gut feeling is on variation in cython definitions.



---

archive/issue_comments_099410.json:
```json
{
    "body": "I've tried to remove the failures known above here.  Note that I didn't get the last few patches in time, but I removed those failures as well, assuming they were the same.  The timeouts/killed are *probably* unrelated - my computer is < 1 GHz, so I get a lot of timeouts and I forgot to set `SAGE_TIMEOUT_LONG` before I ran the tests - but at any rate I hope this will be useful.  After the hurricane I'll start this up again and run the remaining tests.\n\n```\n        sage -t -long \"devel/sage/sage/crypto/mq/mpolynomialsystem.py\" # Killed/crashed\n        sage -t -long \"devel/sage/sage/functions/transcendental.py\"\n        sage -t -long \"devel/sage/sage/groups/generic.py\" # Killed/crashed\n        sage -t -long \"devel/sage/sage/interfaces/maxima.py\" # Time out\n        sage -t -long \"devel/sage/sage/interfaces/singular.py\" # Killed/crashed\n        sage -t -long \"devel/sage/sage/libs/cremona/newforms.pyx\"\n        sage -t -long \"devel/sage/sage/libs/ppl.pyx\" # Time out\n        sage -t -long \"devel/sage/sage/libs/singular/ring.pyx\" # Killed/crashed\n        sage -t -long \"devel/sage/sage/misc/randstate.pyx\"\n        sage -t -long \"devel/sage/sage/misc/sageinspect.py\"\n        sage -t -long \"devel/sage/sage/rings/multi_power_series_ring_element.py\" # Killed/crashed\n        sage -t -long \"devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py\" # Killed/crashed\n        sage -t -long \"devel/sage/sage/rings/polynomial/multi_polynomial_libsingular.pyx\" # Killed/crashed\n        sage -t -long \"devel/sage/sage/rings/polynomial/polynomial_singular_interface.py\" # Killed/crashed\n        sage -t -long \"devel/sage/sage/rings/real_mpfr.pyx\"\n        sage -t -long \"devel/sage/sage/rings/tests.py\" # Killed/crashed\n        sage -t -long \"devel/sage/sage/schemes/elliptic_curves/BSD.py\" # Killed/crashed\n        sage -t -long \"devel/sage/sage/schemes/elliptic_curves/ell_curve_isogeny.py\" # Killed/crashed\n        sage -t -long \"devel/sage/sage/schemes/elliptic_curves/ell_field.py\" # Killed/crashed\n        sage -t -long \"devel/sage/sage/schemes/elliptic_curves/ell_finite_field.py\" # Killed/crashed\n        sage -t -long \"devel/sage/sage/schemes/elliptic_curves/ell_generic.py\" # Killed/crashed\n        sage -t -long \"devel/sage/sage/schemes/elliptic_curves/ell_local_data.py\" # Killed/crashed\n        sage -t -long \"devel/sage/sage/schemes/elliptic_curves/ell_number_field.py\" # Killed/crashed\n        sage -t -long \"devel/sage/sage/schemes/elliptic_curves/ell_point.py\" # Killed/crashed\n        sage -t -long \"devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py\" # Time out\n        sage -t -long \"devel/sage/sage/schemes/elliptic_curves/gal_reps.py\" # Killed/crashed\n        sage -t -long \"devel/sage/sage/schemes/elliptic_curves/heegner.py\" # Killed/crashed\n        sage -t -long \"devel/sage/sage/schemes/elliptic_curves/period_lattice.py\" # Killed/crashed\n        sage -t -long \"devel/sage/sage/schemes/generic/scheme.py\" # Killed/crashed\n        sage -t -long \"devel/sage/sage/schemes/plane_conics/con_finite_field.py\" # Killed/crashed\n        sage -t -long \"devel/sage/sage/schemes/plane_curves/projective_curve.py\" # Killed/crashed\n        sage -t -long \"devel/sage/sage/stats/intlist.pyx\"\n        sage -t -long \"devel/sage/sage/structure/sage_object.pyx\" # Killed/crashed\n```\n",
    "created_at": "2011-08-26T19:45:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99410",
    "user": "kcrisman"
}
```

I've tried to remove the failures known above here.  Note that I didn't get the last few patches in time, but I removed those failures as well, assuming they were the same.  The timeouts/killed are *probably* unrelated - my computer is < 1 GHz, so I get a lot of timeouts and I forgot to set `SAGE_TIMEOUT_LONG` before I ran the tests - but at any rate I hope this will be useful.  After the hurricane I'll start this up again and run the remaining tests.

```
        sage -t -long "devel/sage/sage/crypto/mq/mpolynomialsystem.py" # Killed/crashed
        sage -t -long "devel/sage/sage/functions/transcendental.py"
        sage -t -long "devel/sage/sage/groups/generic.py" # Killed/crashed
        sage -t -long "devel/sage/sage/interfaces/maxima.py" # Time out
        sage -t -long "devel/sage/sage/interfaces/singular.py" # Killed/crashed
        sage -t -long "devel/sage/sage/libs/cremona/newforms.pyx"
        sage -t -long "devel/sage/sage/libs/ppl.pyx" # Time out
        sage -t -long "devel/sage/sage/libs/singular/ring.pyx" # Killed/crashed
        sage -t -long "devel/sage/sage/misc/randstate.pyx"
        sage -t -long "devel/sage/sage/misc/sageinspect.py"
        sage -t -long "devel/sage/sage/rings/multi_power_series_ring_element.py" # Killed/crashed
        sage -t -long "devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py" # Killed/crashed
        sage -t -long "devel/sage/sage/rings/polynomial/multi_polynomial_libsingular.pyx" # Killed/crashed
        sage -t -long "devel/sage/sage/rings/polynomial/polynomial_singular_interface.py" # Killed/crashed
        sage -t -long "devel/sage/sage/rings/real_mpfr.pyx"
        sage -t -long "devel/sage/sage/rings/tests.py" # Killed/crashed
        sage -t -long "devel/sage/sage/schemes/elliptic_curves/BSD.py" # Killed/crashed
        sage -t -long "devel/sage/sage/schemes/elliptic_curves/ell_curve_isogeny.py" # Killed/crashed
        sage -t -long "devel/sage/sage/schemes/elliptic_curves/ell_field.py" # Killed/crashed
        sage -t -long "devel/sage/sage/schemes/elliptic_curves/ell_finite_field.py" # Killed/crashed
        sage -t -long "devel/sage/sage/schemes/elliptic_curves/ell_generic.py" # Killed/crashed
        sage -t -long "devel/sage/sage/schemes/elliptic_curves/ell_local_data.py" # Killed/crashed
        sage -t -long "devel/sage/sage/schemes/elliptic_curves/ell_number_field.py" # Killed/crashed
        sage -t -long "devel/sage/sage/schemes/elliptic_curves/ell_point.py" # Killed/crashed
        sage -t -long "devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py" # Time out
        sage -t -long "devel/sage/sage/schemes/elliptic_curves/gal_reps.py" # Killed/crashed
        sage -t -long "devel/sage/sage/schemes/elliptic_curves/heegner.py" # Killed/crashed
        sage -t -long "devel/sage/sage/schemes/elliptic_curves/period_lattice.py" # Killed/crashed
        sage -t -long "devel/sage/sage/schemes/generic/scheme.py" # Killed/crashed
        sage -t -long "devel/sage/sage/schemes/plane_conics/con_finite_field.py" # Killed/crashed
        sage -t -long "devel/sage/sage/schemes/plane_curves/projective_curve.py" # Killed/crashed
        sage -t -long "devel/sage/sage/stats/intlist.pyx"
        sage -t -long "devel/sage/sage/structure/sage_object.pyx" # Killed/crashed
```




---

archive/issue_comments_099411.json:
```json
{
    "body": "Here is one example.\n\n```\nsage -t -long \"devel/sage/sage/functions/transcendental.py\" \n**********************************************************************\nFile \"/Users/student/Desktop/sage-4.7.2.alpha1/devel/sage/sage/functions/transcendental.py\", line 83:\n    sage: w = exponential_integral_1(2,4); w\nExpected:\n    [0.04890051070806112, 0.0037793524098489067, 0.00036008245216265873, 3.7665622843924751e-05] \nGot:\n    [0.04890051070806112, 0.0037793524098489067, 0.00036008245216265873, 3.766562284392475e-05]\n**********************************************************************\n```\n\nHere is one of the killed ones (not a timeout, I'm surprised):\n\n```\nsage -t -long \"devel/sage/sage/crypto/mq/mpolynomialsystem.py\"\nThe doctested process was killed by signal 10\n         [352.0 s]\n```\n\nCould this be an unrelated 4.7.2.alpha1 issue on my platform?",
    "created_at": "2011-08-26T20:14:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99411",
    "user": "kcrisman"
}
```

Here is one example.

```
sage -t -long "devel/sage/sage/functions/transcendental.py" 
**********************************************************************
File "/Users/student/Desktop/sage-4.7.2.alpha1/devel/sage/sage/functions/transcendental.py", line 83:
    sage: w = exponential_integral_1(2,4); w
Expected:
    [0.04890051070806112, 0.0037793524098489067, 0.00036008245216265873, 3.7665622843924751e-05] 
Got:
    [0.04890051070806112, 0.0037793524098489067, 0.00036008245216265873, 3.766562284392475e-05]
**********************************************************************
```

Here is one of the killed ones (not a timeout, I'm surprised):

```
sage -t -long "devel/sage/sage/crypto/mq/mpolynomialsystem.py"
The doctested process was killed by signal 10
         [352.0 s]
```

Could this be an unrelated 4.7.2.alpha1 issue on my platform?



---

archive/issue_comments_099412.json:
```json
{
    "body": "I am particularly interested in the killed/crashed tests. And also those for which there is already a patch.\n\n```\nsage -t -long \"devel/sage/sage/libs/cremona/newforms.pyx\"\nsage -t -long \"devel/sage/sage/rings/real_mpfr.pyx\"\nsage -t -long \"devel/sage/sage/stats/intlist.pyx\"\n```\n\nare the 32/64 bits message difference already mentioned by Steve.\n\nThe timeouts are the regular suspect on ppc if I am not mistaken.\n\nThe transcendental.py doctest you are quoting is worrying me. It is patched in [attachment:trac_9958-fixing_numericalnoise-part1.patch] but you have a slightly different result again (one less digit on the last number). We may have to consider \na different patch.\n\nAll killed/crashed doctest are candidates for #11339 but you'll have to run sage -gdb on them to be sure.",
    "created_at": "2011-08-26T21:22:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99412",
    "user": "fbissey"
}
```

I am particularly interested in the killed/crashed tests. And also those for which there is already a patch.

```
sage -t -long "devel/sage/sage/libs/cremona/newforms.pyx"
sage -t -long "devel/sage/sage/rings/real_mpfr.pyx"
sage -t -long "devel/sage/sage/stats/intlist.pyx"
```

are the 32/64 bits message difference already mentioned by Steve.

The timeouts are the regular suspect on ppc if I am not mistaken.

The transcendental.py doctest you are quoting is worrying me. It is patched in [attachment:trac_9958-fixing_numericalnoise-part1.patch] but you have a slightly different result again (one less digit on the last number). We may have to consider 
a different patch.

All killed/crashed doctest are candidates for #11339 but you'll have to run sage -gdb on them to be sure.



---

archive/issue_comments_099413.json:
```json
{
    "body": "Replying to [comment:93 kcrisman]:\n> Here is one of the killed ones (not a timeout, I'm surprised):\n\n```\nsage -t -long \"devel/sage/sage/crypto/mq/mpolynomialsystem.py\"\nThe doctested process was killed by signal 10\n         [352.0 s]\n```\n\n> Could this be an unrelated 4.7.2.alpha1 issue on my platform?\n\nDoes `SIGUSR1` (!#10) have a special meaning on Darwin?",
    "created_at": "2011-08-26T23:32:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99413",
    "user": "leif"
}
```

Replying to [comment:93 kcrisman]:
> Here is one of the killed ones (not a timeout, I'm surprised):

```
sage -t -long "devel/sage/sage/crypto/mq/mpolynomialsystem.py"
The doctested process was killed by signal 10
         [352.0 s]
```

> Could this be an unrelated 4.7.2.alpha1 issue on my platform?

Does `SIGUSR1` (!#10) have a special meaning on Darwin?



---

archive/issue_comments_099414.json:
```json
{
    "body": "Almost anything with \"polynomial\" in its name is likely to use singular (and crypto/mq/mpolynomialsystem.py is no exception), signal 10 is apparently a user defined signal so it could be anything. \n\nWe'll have to wait for the hurricane to move on before Karl can answer us on any of this points.\n\nLooking back at you list Karl I am also very curious about\n\n```\nsage -t -long \"devel/sage/sage/structure/sage_object.pyx\nsage -t -long \"devel/sage/sage/misc/sageinspect.py\"\nsage -t -long \"devel/sage/sage/misc/randstate.pyx\"\n```\n\ntwo of these have already been patched (sage_object and randstate) in this ticket so I am quite curious about what's wrong with them.",
    "created_at": "2011-08-26T23:52:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99414",
    "user": "fbissey"
}
```

Almost anything with "polynomial" in its name is likely to use singular (and crypto/mq/mpolynomialsystem.py is no exception), signal 10 is apparently a user defined signal so it could be anything. 

We'll have to wait for the hurricane to move on before Karl can answer us on any of this points.

Looking back at you list Karl I am also very curious about

```
sage -t -long "devel/sage/sage/structure/sage_object.pyx
sage -t -long "devel/sage/sage/misc/sageinspect.py"
sage -t -long "devel/sage/sage/misc/randstate.pyx"
```

two of these have already been patched (sage_object and randstate) in this ticket so I am quite curious about what's wrong with them.



---

archive/issue_comments_099415.json:
```json
{
    "body": "Yeah, I'm sorry I couldn't provide more information.  The tests only just finished after classes, and I had one hour to copy/paste the above, restart just doing the failed tests, write a lecture, check email, and then turn off and unplug my PPC machine.   I just couldn't do any more.  I certainly wasn't taking an eMac home on the bike/train with me!\n\nBut we are just due for heavy rain and wind, so hopefully Monday I can get back on it and tell you more, save an extended power outage.  Much better than an earthquake, I think fbissey would heartily agree.  I wish I'd had a chance to run tests after #11339, but I just knew it would take eons.  I'd do it on one of my home PPC machines (believe it or not, I have two more) but one I can no longer get !XCode for, and the other is also slow enough it wouldn't be ready by the time we have to unplug *it*... sigh.\n\nAnyway, I'll keep this ticket on the priority list for the machine I did these tests on.",
    "created_at": "2011-08-27T00:47:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99415",
    "user": "kcrisman"
}
```

Yeah, I'm sorry I couldn't provide more information.  The tests only just finished after classes, and I had one hour to copy/paste the above, restart just doing the failed tests, write a lecture, check email, and then turn off and unplug my PPC machine.   I just couldn't do any more.  I certainly wasn't taking an eMac home on the bike/train with me!

But we are just due for heavy rain and wind, so hopefully Monday I can get back on it and tell you more, save an extended power outage.  Much better than an earthquake, I think fbissey would heartily agree.  I wish I'd had a chance to run tests after #11339, but I just knew it would take eons.  I'd do it on one of my home PPC machines (believe it or not, I have two more) but one I can no longer get !XCode for, and the other is also slow enough it wouldn't be ready by the time we have to unplug *it*... sigh.

Anyway, I'll keep this ticket on the priority list for the machine I did these tests on.



---

archive/issue_comments_099416.json:
```json
{
    "body": "So, I did test this with Sage 4.7.2.alpha2 on my \"last\" 32-bit machine, a Pentium4 Prescott (which has SSE3) running Ubuntu 9.04; my other Pentium4 (Northwood, without SSE3 / PNI) recently died, and I won't revive it in the near future.\n\nThe good news are: The patches all still apply to 4.7.2.alpha2, though many hunks with partially large offsets, but no fuzz.\n\nThe bad news: I expected some numerical noise because of 32-bit architecture with (there rather rare) SSE3 (`-mfpmath=sse`), but also experienced at least one segfault (in `sage/rings/homset.py`). I'll have to investigate the rest, for now just:\n\n```\n...\nsage -t  -long -force_lib \"devel/sage/sage/geometry/polyhedra.py\"\n**********************************************************************\nFile \"/media/H-1TB-P6-linux2/Sage/sage-4.7.2.alpha2-gcc-4.5.1/devel/sage/sage/geometry/polyhedra.py\", line 4948:\n    sage: ppoints[0]\nExpected:\n    (-1.92296268638e-15, -1.92296268638e-15)\nGot:\n    (0.0, 0.0)\n**********************************************************************\n1 items had failures:\n   1 of   8 in __main__.example_171\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/leif/.sage//tmp/.doctest_polyhedra.py\n\t [166.0 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t  -long -force_lib \"devel/sage/sage/libs/cremona/newforms.pyx\"\n\tsage -t  -long -force_lib \"devel/sage/sage/functions/transcendental.py\"\n\tsage -t  -long -force_lib \"devel/sage/sage/misc/randstate.pyx\"\n\tsage -t  -long -force_lib \"devel/sage/sage/combinat/words/suffix_trees.py\"\n\tsage -t  -long -force_lib \"devel/sage/sage/combinat/words/nfactor_enumerable_word.py\"\n\tsage -t  -long -force_lib \"devel/sage/sage/rings/morphism.pyx\"\n\tsage -t  -long -force_lib \"devel/sage/sage/rings/real_mpfr.pyx\"\n\tsage -t  -long -force_lib \"devel/sage/sage/rings/homset.py\"\n\tsage -t  -long -force_lib \"devel/sage/sage/stats/intlist.pyx\"\n\tsage -t  -long -force_lib \"devel/sage/sage/schemes/generic/scheme.py\"\n\tsage -t  -long -force_lib \"devel/sage/sage/geometry/polyhedra.py\"\nTotal time for all tests: 26263.8 seconds\nmake: *** [testlong] Error 128\n\nreal\t439m23.357s\nuser\t393m40.644s\nsys\t31m7.485s\nleif@californication:~/Sage/sage-4.7.2.alpha2-gcc-4.5.1$ \n```\n\n(The tail of the log. More to come later.)\n\nNote that I didn't test in parallel, although with some other CPU-greedy process running, but time-outs are unlikely. Vanilla 4.7.2.alpha2 passed all tests in exactly the same setting (and I did rebuild all dependent packages when installing the Python 2.7 spkg, modulo missing extension module dependencies in `module_list.py`).",
    "created_at": "2011-08-29T02:59:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99416",
    "user": "leif"
}
```

So, I did test this with Sage 4.7.2.alpha2 on my "last" 32-bit machine, a Pentium4 Prescott (which has SSE3) running Ubuntu 9.04; my other Pentium4 (Northwood, without SSE3 / PNI) recently died, and I won't revive it in the near future.

The good news are: The patches all still apply to 4.7.2.alpha2, though many hunks with partially large offsets, but no fuzz.

The bad news: I expected some numerical noise because of 32-bit architecture with (there rather rare) SSE3 (`-mfpmath=sse`), but also experienced at least one segfault (in `sage/rings/homset.py`). I'll have to investigate the rest, for now just:

```
...
sage -t  -long -force_lib "devel/sage/sage/geometry/polyhedra.py"
**********************************************************************
File "/media/H-1TB-P6-linux2/Sage/sage-4.7.2.alpha2-gcc-4.5.1/devel/sage/sage/geometry/polyhedra.py", line 4948:
    sage: ppoints[0]
Expected:
    (-1.92296268638e-15, -1.92296268638e-15)
Got:
    (0.0, 0.0)
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_171
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/leif/.sage//tmp/.doctest_polyhedra.py
	 [166.0 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  -long -force_lib "devel/sage/sage/libs/cremona/newforms.pyx"
	sage -t  -long -force_lib "devel/sage/sage/functions/transcendental.py"
	sage -t  -long -force_lib "devel/sage/sage/misc/randstate.pyx"
	sage -t  -long -force_lib "devel/sage/sage/combinat/words/suffix_trees.py"
	sage -t  -long -force_lib "devel/sage/sage/combinat/words/nfactor_enumerable_word.py"
	sage -t  -long -force_lib "devel/sage/sage/rings/morphism.pyx"
	sage -t  -long -force_lib "devel/sage/sage/rings/real_mpfr.pyx"
	sage -t  -long -force_lib "devel/sage/sage/rings/homset.py"
	sage -t  -long -force_lib "devel/sage/sage/stats/intlist.pyx"
	sage -t  -long -force_lib "devel/sage/sage/schemes/generic/scheme.py"
	sage -t  -long -force_lib "devel/sage/sage/geometry/polyhedra.py"
Total time for all tests: 26263.8 seconds
make: *** [testlong] Error 128

real	439m23.357s
user	393m40.644s
sys	31m7.485s
leif@californication:~/Sage/sage-4.7.2.alpha2-gcc-4.5.1$ 
```

(The tail of the log. More to come later.)

Note that I didn't test in parallel, although with some other CPU-greedy process running, but time-outs are unlikely. Vanilla 4.7.2.alpha2 passed all tests in exactly the same setting (and I did rebuild all dependent packages when installing the Python 2.7 spkg, modulo missing extension module dependencies in `module_list.py`).



---

archive/issue_comments_099417.json:
```json
{
    "body": "Ok, **three** segfaults (two of them without backtrace / Sage message, for whatever reason), some Python ints too large (\"as usual\" I guess), some numerical noise, the rest apparently related to dictionaries / hashing(?).\n\nAttaching short logs of rerun tests (all reproducable)...",
    "created_at": "2011-08-29T03:32:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99417",
    "user": "leif"
}
```

Ok, **three** segfaults (two of them without backtrace / Sage message, for whatever reason), some Python ints too large ("as usual" I guess), some numerical noise, the rest apparently related to dictionaries / hashing(?).

Attaching short logs of rerun tests (all reproducable)...



---

archive/issue_comments_099418.json:
```json
{
    "body": "Attachment\n\nPentium4 Prescott (SSE3 / PNI, 32-bit), GCC 4.5.1, native code, `-mfpmath=sse`, Ubuntu 9.04 x86",
    "created_at": "2011-08-29T03:42:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99418",
    "user": "leif"
}
```

Attachment

Pentium4 Prescott (SSE3 / PNI, 32-bit), GCC 4.5.1, native code, `-mfpmath=sse`, Ubuntu 9.04 x86



---

archive/issue_comments_099419.json:
```json
{
    "body": "Pentium4 Prescott (SSE3 / PNI, 32-bit), GCC 4.5.1, native code, -mfpmath=sse, Ubuntu 9.04 x86 (The three segfaulting files tested in verbose mode.)",
    "created_at": "2011-08-29T04:20:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99419",
    "user": "leif"
}
```

Pentium4 Prescott (SSE3 / PNI, 32-bit), GCC 4.5.1, native code, -mfpmath=sse, Ubuntu 9.04 x86 (The three segfaulting files tested in verbose mode.)



---

archive/issue_comments_099420.json:
```json
{
    "body": "Attachment\n\nReplying to [comment:99 leif]:\n> Attaching short logs of rerun tests (all reproducable)...\n\nDone.\n\nHaha, the first segfault is an especially nice one:\n\n```\n...\n  10 tests in __main__.example_7\n   6 tests in __main__.example_8\n   7 tests in __main__.example_9\n511 tests in 55 items.\n511 passed and 0 failed.\nTest passed.\nSegmentation fault\n\t [9.8 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t -long -verbose \"devel/sage/sage/rings/morphism.pyx\"\nTotal time for all tests: 9.8 seconds\n\nreal\t0m10.013s\nuser\t0m6.980s\nsys\t0m1.068s\n```\n",
    "created_at": "2011-08-29T04:35:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99420",
    "user": "leif"
}
```

Attachment

Replying to [comment:99 leif]:
> Attaching short logs of rerun tests (all reproducable)...

Done.

Haha, the first segfault is an especially nice one:

```
...
  10 tests in __main__.example_7
   6 tests in __main__.example_8
   7 tests in __main__.example_9
511 tests in 55 items.
511 passed and 0 failed.
Test passed.
Segmentation fault
	 [9.8 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long -verbose "devel/sage/sage/rings/morphism.pyx"
Total time for all tests: 9.8 seconds

real	0m10.013s
user	0m6.980s
sys	0m1.068s
```




---

archive/issue_comments_099421.json:
```json
{
    "body": "Thanks leif. Nothing worrying there. There is a patch for sage/geometry/polyhedra.py but obviously it doesn't apply properly anymore. transcendantal.py, randstate.pyx and intlist.pyx are all already patched but may need more tweaking, I'd be grateful for the output of these.\n\n```\nsage -t  -long -force_lib \"devel/sage/sage/combinat/words/nfactor_enumerable_word.py\"\n```\n\nis known to fail but is probably a minor adjustment.\n\n```\nsage -t  -long -force_lib \"devel/sage/sage/combinat/words/suffix_trees.py\"\n```\n\nis new. The rest look like #11339 material.",
    "created_at": "2011-08-29T05:05:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99421",
    "user": "fbissey"
}
```

Thanks leif. Nothing worrying there. There is a patch for sage/geometry/polyhedra.py but obviously it doesn't apply properly anymore. transcendantal.py, randstate.pyx and intlist.pyx are all already patched but may need more tweaking, I'd be grateful for the output of these.

```
sage -t  -long -force_lib "devel/sage/sage/combinat/words/nfactor_enumerable_word.py"
```

is known to fail but is probably a minor adjustment.

```
sage -t  -long -force_lib "devel/sage/sage/combinat/words/suffix_trees.py"
```

is new. The rest look like #11339 material.



---

archive/issue_comments_099422.json:
```json
{
    "body": "Replying to [comment:101 fbissey]:\n> Thanks leif. Nothing worrying there. There is a patch for sage/geometry/polyhedra.py but obviously it doesn't apply properly anymore. transcendantal.py, randstate.pyx and intlist.pyx are all already patched but may need more tweaking, I'd be grateful for the output of these.\n\nThe failing doctests are all in [attachment:Doctest_failures_Sage-4.7.2.alpha2_Linux_x86_SSE3-individual_tests_rerun.log].\n\n> [...] The rest look like #11339 material.\n\nI'm just to apply the patches from there; the machine is dead slow, doing a `./sage -ba-force` atm to exclude missing extension module dependencies, as I've not built from scratch.",
    "created_at": "2011-08-29T05:48:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99422",
    "user": "leif"
}
```

Replying to [comment:101 fbissey]:
> Thanks leif. Nothing worrying there. There is a patch for sage/geometry/polyhedra.py but obviously it doesn't apply properly anymore. transcendantal.py, randstate.pyx and intlist.pyx are all already patched but may need more tweaking, I'd be grateful for the output of these.

The failing doctests are all in [attachment:Doctest_failures_Sage-4.7.2.alpha2_Linux_x86_SSE3-individual_tests_rerun.log].

> [...] The rest look like #11339 material.

I'm just to apply the patches from there; the machine is dead slow, doing a `./sage -ba-force` atm to exclude missing extension module dependencies, as I've not built from scratch.



---

archive/issue_comments_099423.json:
```json
{
    "body": "I was too fast. Some of the failures are already reported by Steve. I may try to update the patch set a bit tonight.",
    "created_at": "2011-08-29T06:50:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99423",
    "user": "fbissey"
}
```

I was too fast. Some of the failures are already reported by Steve. I may try to update the patch set a bit tonight.



---

archive/issue_comments_099424.json:
```json
{
    "body": "Just experienced some new(?) error when cloning the Sage library for #11339:\n\n```\n...\nbyte-compiling /home/leif/Sage/sage-4.7.2.alpha2-gcc-4.5.1/local/lib/python2.7/site-packages/sage/misc/copying.py to copying.pyc\nbyte-compiling /home/leif/Sage/sage-4.7.2.alpha2-gcc-4.5.1/local/lib/python2.7/site-packages/sage/version.py to version.pyc\nrunning install_egg_info\nRemoving /home/leif/Sage/sage-4.7.2.alpha2-gcc-4.5.1/local/lib/python2.7/site-packages/sage-0.0.0-py2.7.egg-info\nWriting /home/leif/Sage/sage-4.7.2.alpha2-gcc-4.5.1/local/lib/python2.7/site-packages/sage-0.0.0-py2.7.egg-info\nException in thread Thread-4 (most likely raised during interpreter shutdown):\nTraceback (most recent call last):\n  File \"/home/leif/Sage/sage-4.7.2.alpha2-gcc-4.5.1/local/lib/python/threading.py\", line 530, in __bootstrap_inner\n  File \"/home/leif/Sage/sage-4.7.2.alpha2-gcc-4.5.1/local/lib/python/threading.py\", line 483, in run\n  File \"/home/leif/Sage/sage-4.7.2.alpha2-gcc-4.5.1/local/lib/python/multiprocessing/pool.py\", line 272, in _handle_workers\n<type 'exceptions.TypeError'>: 'NoneType' object is not callable\nException in thread Thread-1 (most likely raised during interpreter shutdown):\nTraceback (most recent call last):\n  File \"/home/leif/Sage/sage-4.7.2.alpha2-gcc-4.5.1/local/lib/python/threading.py\", line 530, in __bootstrap_inner\n  File \"/home/leif/Sage/sage-4.7.2.alpha2-gcc-4.5.1/local/lib/python/threading.py\", line 483, in run\n  File \"/home/leif/Sage/sage-4.7.2.alpha2-gcc-4.5.1/local/lib/python/multiprocessing/pool.py\", line 272, in _handle_workers\n<type 'exceptions.TypeError'>: 'NoneType' object is not callable\n\nreal\t1m35.816s\nuser\t1m35.794s\nsys\t0m5.648s\n\nAfter cloning, if you change any Sage library files and want to rebuild\nthe html version of the reference manual, use the command\n    sage -docbuild reference html\n(after running 'sage -b').\n...\n```\n",
    "created_at": "2011-08-29T07:00:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99424",
    "user": "leif"
}
```

Just experienced some new(?) error when cloning the Sage library for #11339:

```
...
byte-compiling /home/leif/Sage/sage-4.7.2.alpha2-gcc-4.5.1/local/lib/python2.7/site-packages/sage/misc/copying.py to copying.pyc
byte-compiling /home/leif/Sage/sage-4.7.2.alpha2-gcc-4.5.1/local/lib/python2.7/site-packages/sage/version.py to version.pyc
running install_egg_info
Removing /home/leif/Sage/sage-4.7.2.alpha2-gcc-4.5.1/local/lib/python2.7/site-packages/sage-0.0.0-py2.7.egg-info
Writing /home/leif/Sage/sage-4.7.2.alpha2-gcc-4.5.1/local/lib/python2.7/site-packages/sage-0.0.0-py2.7.egg-info
Exception in thread Thread-4 (most likely raised during interpreter shutdown):
Traceback (most recent call last):
  File "/home/leif/Sage/sage-4.7.2.alpha2-gcc-4.5.1/local/lib/python/threading.py", line 530, in __bootstrap_inner
  File "/home/leif/Sage/sage-4.7.2.alpha2-gcc-4.5.1/local/lib/python/threading.py", line 483, in run
  File "/home/leif/Sage/sage-4.7.2.alpha2-gcc-4.5.1/local/lib/python/multiprocessing/pool.py", line 272, in _handle_workers
<type 'exceptions.TypeError'>: 'NoneType' object is not callable
Exception in thread Thread-1 (most likely raised during interpreter shutdown):
Traceback (most recent call last):
  File "/home/leif/Sage/sage-4.7.2.alpha2-gcc-4.5.1/local/lib/python/threading.py", line 530, in __bootstrap_inner
  File "/home/leif/Sage/sage-4.7.2.alpha2-gcc-4.5.1/local/lib/python/threading.py", line 483, in run
  File "/home/leif/Sage/sage-4.7.2.alpha2-gcc-4.5.1/local/lib/python/multiprocessing/pool.py", line 272, in _handle_workers
<type 'exceptions.TypeError'>: 'NoneType' object is not callable

real	1m35.816s
user	1m35.794s
sys	0m5.648s

After cloning, if you change any Sage library files and want to rebuild
the html version of the reference manual, use the command
    sage -docbuild reference html
(after running 'sage -b').
...
```




---

archive/issue_comments_099425.json:
```json
{
    "body": "Waaaaaah!\n\n```\nleif@californication:~/Sage/sage-4.7.2.alpha2-gcc-4.5.1/devel/sage-9958-11339$ ../../sage -hg import -v ~/Sage/patches/trac_11339_refcount_singular_polynomials.patch \napplying /home/leif/Sage/patches/trac_11339_refcount_singular_polynomials.patch\npatching file sage/rings/polynomial/multi_polynomial_libsingular.pxd\npatching file sage/rings/polynomial/multi_polynomial_libsingular.pyx\nHunk #13 FAILED at 727\nHunk #14 FAILED at 741\nHunk #15 FAILED at 763\nHunk #16 FAILED at 773\nHunk #17 FAILED at 825\nHunk #18 succeeded at 910 with fuzz 2 (offset 72 lines).\nHunk #19 FAILED at 875\nHunk #20 succeeded at 961 (offset 75 lines).\nHunk #21 succeeded at 980 (offset 75 lines).\nHunk #22 succeeded at 1006 (offset 75 lines).\n...\n```\n\n(The first patch still applies, with offsets.)\n\nI'm not going to fix that...",
    "created_at": "2011-08-29T07:09:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99425",
    "user": "leif"
}
```

Waaaaaah!

```
leif@californication:~/Sage/sage-4.7.2.alpha2-gcc-4.5.1/devel/sage-9958-11339$ ../../sage -hg import -v ~/Sage/patches/trac_11339_refcount_singular_polynomials.patch 
applying /home/leif/Sage/patches/trac_11339_refcount_singular_polynomials.patch
patching file sage/rings/polynomial/multi_polynomial_libsingular.pxd
patching file sage/rings/polynomial/multi_polynomial_libsingular.pyx
Hunk #13 FAILED at 727
Hunk #14 FAILED at 741
Hunk #15 FAILED at 763
Hunk #16 FAILED at 773
Hunk #17 FAILED at 825
Hunk #18 succeeded at 910 with fuzz 2 (offset 72 lines).
Hunk #19 FAILED at 875
Hunk #20 succeeded at 961 (offset 75 lines).
Hunk #21 succeeded at 980 (offset 75 lines).
Hunk #22 succeeded at 1006 (offset 75 lines).
...
```

(The first patch still applies, with offsets.)

I'm not going to fix that...



---

archive/issue_comments_099426.json:
```json
{
    "body": "Replying to [comment:101 fbissey]:\n> Thanks leif. Nothing worrying there. There is a patch for sage/geometry/polyhedra.py but obviously it doesn't apply properly anymore. transcendantal.py, randstate.pyx and intlist.pyx are all already patched but may need more tweaking, I'd be grateful for the output of these.\nI'm sure the polyhedra.py patch was needed at one time but it now (?) appears that \n\n```\n\n@@ -4946,7 +4946,7 @@\n         sage: proj = ProjectionFuncStereographic([1.1,1.1,1.1])\n         sage: ppoints = [proj(vector(x)) for x in cube]\n         sage: ppoints[0]\n-        (0.0, 0.0)\n+        (-1.92296268638e-15, -1.92296268638e-15)\n     \"\"\"\n     def __init__(self, projection_point):\n         \"\"\"\n```\n\n\nfrom trac_9958-fixing_numericalnoise-part1.patch is no longer needed.",
    "created_at": "2011-08-29T13:26:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99426",
    "user": "strogdon"
}
```

Replying to [comment:101 fbissey]:
> Thanks leif. Nothing worrying there. There is a patch for sage/geometry/polyhedra.py but obviously it doesn't apply properly anymore. transcendantal.py, randstate.pyx and intlist.pyx are all already patched but may need more tweaking, I'd be grateful for the output of these.
I'm sure the polyhedra.py patch was needed at one time but it now (?) appears that 

```

@@ -4946,7 +4946,7 @@
         sage: proj = ProjectionFuncStereographic([1.1,1.1,1.1])
         sage: ppoints = [proj(vector(x)) for x in cube]
         sage: ppoints[0]
-        (0.0, 0.0)
+        (-1.92296268638e-15, -1.92296268638e-15)
     """
     def __init__(self, projection_point):
         """
```


from trac_9958-fixing_numericalnoise-part1.patch is no longer needed.



---

archive/issue_comments_099427.json:
```json
{
    "body": "Replying to [comment:106 strogdon]:\n> Replying to [comment:101 fbissey]:\n> > Thanks leif. Nothing worrying there. There is a patch for sage/geometry/polyhedra.py but obviously it doesn't apply properly anymore. transcendantal.py, randstate.pyx and intlist.pyx are all already patched but may need more tweaking, I'd be grateful for the output of these.\n> I'm sure the polyhedra.py patch was needed at one time but it now (?) appears that \n> {{{\n> \n> `@``@` -4946,7 +4946,7 `@``@`\n>          sage: proj = ProjectionFuncStereographic([1.1,1.1,1.1])\n>          sage: ppoints = [proj(vector(x)) for x in cube]\n>          sage: ppoints[0]\n> -        (0.0, 0.0)\n> +        (-1.92296268638e-15, -1.92296268638e-15)\n>      \"\"\"\n>      def __init__(self, projection_point):\n>          \"\"\"\n> }}}\n> \n> from trac_9958-fixing_numericalnoise-part1.patch is no longer needed.\n\nYou are right I am reading the test results backwards. It now seems to go to 0 properly. One less patch in the patch and one less worry.",
    "created_at": "2011-08-29T13:39:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99427",
    "user": "fbissey"
}
```

Replying to [comment:106 strogdon]:
> Replying to [comment:101 fbissey]:
> > Thanks leif. Nothing worrying there. There is a patch for sage/geometry/polyhedra.py but obviously it doesn't apply properly anymore. transcendantal.py, randstate.pyx and intlist.pyx are all already patched but may need more tweaking, I'd be grateful for the output of these.
> I'm sure the polyhedra.py patch was needed at one time but it now (?) appears that 
> {{{
> 
> `@``@` -4946,7 +4946,7 `@``@`
>          sage: proj = ProjectionFuncStereographic([1.1,1.1,1.1])
>          sage: ppoints = [proj(vector(x)) for x in cube]
>          sage: ppoints[0]
> -        (0.0, 0.0)
> +        (-1.92296268638e-15, -1.92296268638e-15)
>      """
>      def __init__(self, projection_point):
>          """
> }}}
> 
> from trac_9958-fixing_numericalnoise-part1.patch is no longer needed.

You are right I am reading the test results backwards. It now seems to go to 0 properly. One less patch in the patch and one less worry.



---

archive/issue_comments_099428.json:
```json
{
    "body": "Okay, you can get a full list of current failure and what they looked like at [this link](http://sage.math.washington.edu/home/kcrisman/Failures.txt).  Some are definitely known above, but others may be unknown.  The timeouts are probably just due to this machine (and the Maxima one), but others I don't know whether they are here or #11339.",
    "created_at": "2011-08-29T19:37:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99428",
    "user": "kcrisman"
}
```

Okay, you can get a full list of current failure and what they looked like at [this link](http://sage.math.washington.edu/home/kcrisman/Failures.txt).  Some are definitely known above, but others may be unknown.  The timeouts are probably just due to this machine (and the Maxima one), but others I don't know whether they are here or #11339.



---

archive/issue_comments_099429.json:
```json
{
    "body": "fixing numerical noise part 1 - updated 20110830",
    "created_at": "2011-08-29T19:54:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99429",
    "user": "fbissey"
}
```

fixing numerical noise part 1 - updated 20110830



---

archive/issue_comments_099430.json:
```json
{
    "body": "Attachment\n\nUpdated the first patch for polyhedra.py, split transcendental.py in its own patch. I lowered the precision tested in the last numbers so that results from 32 and 64 bits are not different.",
    "created_at": "2011-08-29T19:59:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99430",
    "user": "fbissey"
}
```

Attachment

Updated the first patch for polyhedra.py, split transcendental.py in its own patch. I lowered the precision tested in the last numbers so that results from 32 and 64 bits are not different.



---

archive/issue_comments_099431.json:
```json
{
    "body": "Replying to [comment:108 kcrisman]:\n> Okay, you can get a full list of current failure and what they looked like at [this link](http://sage.math.washington.edu/home/kcrisman/Failures.txt).  Some are definitely known above, but others may be unknown.  The timeouts are probably just due to this machine (and the Maxima one), but others I don't know whether they are here or #11339.\n\nYou have some nasty stuff in polyhedra.py\n\n```\nFile \"/Users/student/Desktop/sage-4.7.2.alpha1/devel/sage/sage/geometry/polyhedra.py\", line 5250:\n    sage: _.show()\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/student/Desktop/sage-4.7.2.alpha1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/student/Desktop/sage-4.7.2.alpha1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/student/Desktop/sage-4.7.2.alpha1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_183[5]>\", line 1, in <module>\n        _.show()###line 5250:\n    sage: _.show()\n      File \"/Users/student/Desktop/sage-4.7.2.alpha1/local/lib/python/site-packages/sage/misc/displayhook.py\", line 174, in displayhook\n        print_obj(sys.stdout, obj)\n      File \"/Users/student/Desktop/sage-4.7.2.alpha1/local/lib/python/site-packages/sage/misc/displayhook.py\", line 142, in print_obj\n        print >>out_stream, `obj`\n      File \"base.pyx\", line 80, in sage.plot.plot3d.base.Graphics3d.__repr__ (sage/plot/plot3d/base.c:2526)\n      File \"base.pyx\", line 1124, in sage.plot.plot3d.base.Graphics3d.show (sage/plot/plot3d/base.c:10344)\n      File \"base.pyx\", line 663, in sage.plot.plot3d.base.Graphics3d.export_jmol (sage/plot/plot3d/base.c:5867)\n      File \"/Users/student/Desktop/sage-4.7.2.alpha1/local/lib/python2.7/zipfile.py\", line 1138, in writestr\n        self.fp.write(zinfo.FileHeader())\n      File \"/Users/student/Desktop/sage-4.7.2.alpha1/local/lib/python2.7/zipfile.py\", line 348, in FileHeader\n        len(filename), len(extra))\n    error: integer out of range for 'H' format code\n```\n\nYou get an extra digit in randstate compared to x86 :( [note to self it is in numerical_noise_part4].\n\nsage-inspect looks bad :( but not hopeless. The message is just overly long. I will have to postpone the rest for later.",
    "created_at": "2011-08-29T20:10:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99431",
    "user": "fbissey"
}
```

Replying to [comment:108 kcrisman]:
> Okay, you can get a full list of current failure and what they looked like at [this link](http://sage.math.washington.edu/home/kcrisman/Failures.txt).  Some are definitely known above, but others may be unknown.  The timeouts are probably just due to this machine (and the Maxima one), but others I don't know whether they are here or #11339.

You have some nasty stuff in polyhedra.py

```
File "/Users/student/Desktop/sage-4.7.2.alpha1/devel/sage/sage/geometry/polyhedra.py", line 5250:
    sage: _.show()
Exception raised:
    Traceback (most recent call last):
      File "/Users/student/Desktop/sage-4.7.2.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/student/Desktop/sage-4.7.2.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/student/Desktop/sage-4.7.2.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_183[5]>", line 1, in <module>
        _.show()###line 5250:
    sage: _.show()
      File "/Users/student/Desktop/sage-4.7.2.alpha1/local/lib/python/site-packages/sage/misc/displayhook.py", line 174, in displayhook
        print_obj(sys.stdout, obj)
      File "/Users/student/Desktop/sage-4.7.2.alpha1/local/lib/python/site-packages/sage/misc/displayhook.py", line 142, in print_obj
        print >>out_stream, `obj`
      File "base.pyx", line 80, in sage.plot.plot3d.base.Graphics3d.__repr__ (sage/plot/plot3d/base.c:2526)
      File "base.pyx", line 1124, in sage.plot.plot3d.base.Graphics3d.show (sage/plot/plot3d/base.c:10344)
      File "base.pyx", line 663, in sage.plot.plot3d.base.Graphics3d.export_jmol (sage/plot/plot3d/base.c:5867)
      File "/Users/student/Desktop/sage-4.7.2.alpha1/local/lib/python2.7/zipfile.py", line 1138, in writestr
        self.fp.write(zinfo.FileHeader())
      File "/Users/student/Desktop/sage-4.7.2.alpha1/local/lib/python2.7/zipfile.py", line 348, in FileHeader
        len(filename), len(extra))
    error: integer out of range for 'H' format code
```

You get an extra digit in randstate compared to x86 :( [note to self it is in numerical_noise_part4].

sage-inspect looks bad :( but not hopeless. The message is just overly long. I will have to postpone the rest for later.



---

archive/issue_comments_099432.json:
```json
{
    "body": "sage-inspect is actually an example merged in 4.7.2.alpha1 from #11298 it may not be a python2.7 problems unless you already tested that ticket. I wonder if #11734 would help, the result should be python code but you have cython code instead.",
    "created_at": "2011-08-29T22:17:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99432",
    "user": "fbissey"
}
```

sage-inspect is actually an example merged in 4.7.2.alpha1 from #11298 it may not be a python2.7 problems unless you already tested that ticket. I wonder if #11734 would help, the result should be python code but you have cython code instead.



---

archive/issue_comments_099433.json:
```json
{
    "body": "In polyhedra.py it looks like you have a problem with jmol printing 3D images to file. It involves zip, looking at the pyx there is an instance of testing zip. Could you paste the cython code that produced sage/plot/plot3d/base.c:5867 ?",
    "created_at": "2011-08-29T22:26:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99433",
    "user": "fbissey"
}
```

In polyhedra.py it looks like you have a problem with jmol printing 3D images to file. It involves zip, looking at the pyx there is an instance of testing zip. Could you paste the cython code that produced sage/plot/plot3d/base.c:5867 ?



---

archive/issue_comments_099434.json:
```json
{
    "body": "Attachment\n\nfix some 32/64 bits messages",
    "created_at": "2011-08-29T23:04:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99434",
    "user": "fbissey"
}
```

Attachment

fix some 32/64 bits messages



---

archive/issue_comments_099435.json:
```json
{
    "body": "all fixes to real_mpfr.pyx split from everything else",
    "created_at": "2011-08-29T23:05:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99435",
    "user": "fbissey"
}
```

all fixes to real_mpfr.pyx split from everything else



---

archive/issue_comments_099436.json:
```json
{
    "body": "Attachment\n\nsplit real_mpfr.pyx from the mixed fixes patch",
    "created_at": "2011-08-29T23:05:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99436",
    "user": "fbissey"
}
```

Attachment

split real_mpfr.pyx from the mixed fixes patch



---

archive/issue_comments_099437.json:
```json
{
    "body": "Attachment\n\nUpdated the patch set again. split real_mpfr.pyx from the mixedfix patch. The 32/64 bits issues reported is separate from the message that was already patched. Added a patch to fix 32/64 bit messages.",
    "created_at": "2011-08-29T23:09:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99437",
    "user": "fbissey"
}
```

Attachment

Updated the patch set again. split real_mpfr.pyx from the mixedfix patch. The 32/64 bits issues reported is separate from the message that was already patched. Added a patch to fix 32/64 bit messages.



---

archive/issue_comments_099438.json:
```json
{
    "body": "Replying to [comment:112 fbissey]:\n> In polyhedra.py it looks like you have a problem with jmol printing 3D images to file. It involves zip, looking at the pyx there is an instance of testing zip. Could you paste the cython code that produced sage/plot/plot3d/base.c:5867 ?\n\n```\n  /* \"sage/plot/plot3d/base.pyx\":663\n *         f.write(\"isosurface fullylit; pmesh o* fullylit; set antialiasdisplay on;\\n\")\n * \n *         render_params.output_archive.writestr('SCRIPT', f.getvalue())             # <<<<<<<<<<<<<<\n *         render_params.output_archive.close()\n * \n */\n  __pyx_t_3 = PyObject_GetAttr(__pyx_v_render_params, __pyx_n_s__output_archive); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 663; __pyx_clineno = __LINE__; goto __pyx_L1_error;}\n  __Pyx_GOTREF(__pyx_t_3);\n  __pyx_t_2 = PyObject_GetAttr(__pyx_t_3, __pyx_n_s__writestr); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 663; __pyx_clineno = __LINE__; goto __pyx_L1_error;}\n  __Pyx_GOTREF(__pyx_t_2);\n  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n  __pyx_t_3 = PyObject_GetAttr(__pyx_v_f, __pyx_n_s__getvalue); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 663; __pyx_clineno = __LINE__; goto __pyx_L1_error;}\n  __Pyx_GOTREF(__pyx_t_3);\n  __pyx_t_4 = PyObject_Call(__pyx_t_3, ((PyObject *)__pyx_empty_tuple), NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 663; __pyx_clineno = __LINE__; goto __pyx_L1_error;}\n  __Pyx_GOTREF(__pyx_t_4);\n  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;\n  __pyx_t_3 = PyTuple_New(2); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 663; __pyx_clineno = __LINE__; goto __pyx_L1_error;}\n  __Pyx_GOTREF(((PyObject *)__pyx_t_3));\n  __Pyx_INCREF(((PyObject *)__pyx_n_s__SCRIPT));\n  PyTuple_SET_ITEM(__pyx_t_3, 0, ((PyObject *)__pyx_n_s__SCRIPT));\n  __Pyx_GIVEREF(((PyObject *)__pyx_n_s__SCRIPT));\n  PyTuple_SET_ITEM(__pyx_t_3, 1, __pyx_t_4);\n  __Pyx_GIVEREF(__pyx_t_4);\n  __pyx_t_4 = 0;\n  __pyx_t_4 = PyObject_Call(__pyx_t_2, ((PyObject *)__pyx_t_3), NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 663; __pyx_clineno = __LINE__; goto __pyx_L1_error;}\n  __Pyx_GOTREF(__pyx_t_4);\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n  __Pyx_DECREF(((PyObject *)__pyx_t_3)); __pyx_t_3 = 0;\n  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;\n```\n\n5867 is \n\n```\n  __pyx_t_4 = PyObject_Call(__pyx_t_2, ((PyObject *)__pyx_t_3), NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 663; __pyx_clineno = __LINE__; goto __pyx_L1_error;}\n```\n\n\n----\nI was also surprised by the polyhedra.py additional weirdness.  Anything I can do to help identify it?  Warning: I'm planning on building and testing alpha2 *without* Python 2.7 now, which will tie up most resources on this machine for a couple days.",
    "created_at": "2011-08-30T16:04:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99438",
    "user": "kcrisman"
}
```

Replying to [comment:112 fbissey]:
> In polyhedra.py it looks like you have a problem with jmol printing 3D images to file. It involves zip, looking at the pyx there is an instance of testing zip. Could you paste the cython code that produced sage/plot/plot3d/base.c:5867 ?

```
  /* "sage/plot/plot3d/base.pyx":663
 *         f.write("isosurface fullylit; pmesh o* fullylit; set antialiasdisplay on;\n")
 * 
 *         render_params.output_archive.writestr('SCRIPT', f.getvalue())             # <<<<<<<<<<<<<<
 *         render_params.output_archive.close()
 * 
 */
  __pyx_t_3 = PyObject_GetAttr(__pyx_v_render_params, __pyx_n_s__output_archive); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 663; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_2 = PyObject_GetAttr(__pyx_t_3, __pyx_n_s__writestr); if (unlikely(!__pyx_t_2)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 663; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = PyObject_GetAttr(__pyx_v_f, __pyx_n_s__getvalue); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 663; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_4 = PyObject_Call(__pyx_t_3, ((PyObject *)__pyx_empty_tuple), NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 663; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = PyTuple_New(2); if (unlikely(!__pyx_t_3)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 663; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(((PyObject *)__pyx_t_3));
  __Pyx_INCREF(((PyObject *)__pyx_n_s__SCRIPT));
  PyTuple_SET_ITEM(__pyx_t_3, 0, ((PyObject *)__pyx_n_s__SCRIPT));
  __Pyx_GIVEREF(((PyObject *)__pyx_n_s__SCRIPT));
  PyTuple_SET_ITEM(__pyx_t_3, 1, __pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  __pyx_t_4 = 0;
  __pyx_t_4 = PyObject_Call(__pyx_t_2, ((PyObject *)__pyx_t_3), NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 663; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(((PyObject *)__pyx_t_3)); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
```

5867 is 

```
  __pyx_t_4 = PyObject_Call(__pyx_t_2, ((PyObject *)__pyx_t_3), NULL); if (unlikely(!__pyx_t_4)) {__pyx_filename = __pyx_f[0]; __pyx_lineno = 663; __pyx_clineno = __LINE__; goto __pyx_L1_error;}
```


----
I was also surprised by the polyhedra.py additional weirdness.  Anything I can do to help identify it?  Warning: I'm planning on building and testing alpha2 *without* Python 2.7 now, which will tie up most resources on this machine for a couple days.



---

archive/issue_comments_099439.json:
```json
{
    "body": "Replying to [comment:109 fbissey]:\n> Updated the first patch for polyhedra.py, split transcendental.py in its own patch. I lowered the precision tested in the last numbers so that results from 32 and 64 bits are not different.\nHere the fix_transcendental patch fixed the associated test on x86 but now the test fails on amd64:\n\n\n```\nsage -t -long  -force_lib devel/sage-main/sage/functions/transcendental.py\n**********************************************************************\nFile \"/storage/sage/sage-4.7.2.alpha2/devel/sage-main/sage/functions/transcendental.p\ny\", line 83:\n    sage: w = exponential_integral_1(2,4); w\nExpected:\n    [0.04890051070806112, 0.0037793524098489067, 0.00036008245216265873, 3.7665622843\n924...e-05]\nGot:\n    [0.04890051070806112, 0.0037793524098489063, 0.00036008245216265873, 3.7665622843\n924534e-05]\n**********************************************************************\n```\n\n\nThis is odd! I wonder what changed? Previously this test must have returned ...67 and not ...63 for it to pass.",
    "created_at": "2011-08-31T02:10:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99439",
    "user": "strogdon"
}
```

Replying to [comment:109 fbissey]:
> Updated the first patch for polyhedra.py, split transcendental.py in its own patch. I lowered the precision tested in the last numbers so that results from 32 and 64 bits are not different.
Here the fix_transcendental patch fixed the associated test on x86 but now the test fails on amd64:


```
sage -t -long  -force_lib devel/sage-main/sage/functions/transcendental.py
**********************************************************************
File "/storage/sage/sage-4.7.2.alpha2/devel/sage-main/sage/functions/transcendental.p
y", line 83:
    sage: w = exponential_integral_1(2,4); w
Expected:
    [0.04890051070806112, 0.0037793524098489067, 0.00036008245216265873, 3.7665622843
924...e-05]
Got:
    [0.04890051070806112, 0.0037793524098489063, 0.00036008245216265873, 3.7665622843
924534e-05]
**********************************************************************
```


This is odd! I wonder what changed? Previously this test must have returned ...67 and not ...63 for it to pass.



---

archive/issue_comments_099440.json:
```json
{
    "body": "Replying to [comment:115 strogdon]:\n> Replying to [comment:109 fbissey]:\n> > Updated the first patch for polyhedra.py, split transcendental.py in its own patch. I lowered the precision tested in the last numbers so that results from 32 and 64 bits are not different.\n> Here the fix_transcendental patch fixed the associated test on x86 but now the test fails on amd64:\n> \n> {{{\n> sage -t -long  -force_lib devel/sage-main/sage/functions/transcendental.py\n> **********************************************************************\n> File \"/storage/sage/sage-4.7.2.alpha2/devel/sage-main/sage/functions/transcendental.p\n> y\", line 83:\n>     sage: w = exponential_integral_1(2,4); w\n> Expected:\n>     [0.04890051070806112, 0.0037793524098489067, 0.00036008245216265873, 3.7665622843\n> 924...e-05]\n> Got:\n>     [0.04890051070806112, 0.0037793524098489063, 0.00036008245216265873, 3.7665622843\n> 924534e-05]\n> **********************************************************************\n> }}}\n> \n> This is odd! I wonder what changed? Previously this test must have returned ...67 and not ...63 for it to pass.\n\n\nIt's my fault for not noticing this difference between 32 and 64 bit results. It was there before but I didn't notice it. I thought the last number was the only thing different so when I truncated the last number to the common digits I dropped the difference between 32 and 64 bit. So it is entirely my fault.",
    "created_at": "2011-08-31T02:42:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99440",
    "user": "fbissey"
}
```

Replying to [comment:115 strogdon]:
> Replying to [comment:109 fbissey]:
> > Updated the first patch for polyhedra.py, split transcendental.py in its own patch. I lowered the precision tested in the last numbers so that results from 32 and 64 bits are not different.
> Here the fix_transcendental patch fixed the associated test on x86 but now the test fails on amd64:
> 
> {{{
> sage -t -long  -force_lib devel/sage-main/sage/functions/transcendental.py
> **********************************************************************
> File "/storage/sage/sage-4.7.2.alpha2/devel/sage-main/sage/functions/transcendental.p
> y", line 83:
>     sage: w = exponential_integral_1(2,4); w
> Expected:
>     [0.04890051070806112, 0.0037793524098489067, 0.00036008245216265873, 3.7665622843
> 924...e-05]
> Got:
>     [0.04890051070806112, 0.0037793524098489063, 0.00036008245216265873, 3.7665622843
> 924534e-05]
> **********************************************************************
> }}}
> 
> This is odd! I wonder what changed? Previously this test must have returned ...67 and not ...63 for it to pass.


It's my fault for not noticing this difference between 32 and 64 bit results. It was there before but I didn't notice it. I thought the last number was the only thing different so when I truncated the last number to the common digits I dropped the difference between 32 and 64 bit. So it is entirely my fault.



---

archive/issue_comments_099441.json:
```json
{
    "body": "Attachment\n\nfixing numerical noise in transcendental.py- split from numerical noise pt1 - updated 2011092",
    "created_at": "2011-09-01T23:36:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99441",
    "user": "fbissey"
}
```

Attachment

fixing numerical noise in transcendental.py- split from numerical noise pt1 - updated 2011092



---

archive/issue_comments_099442.json:
```json
{
    "body": "transcendental patch updated.",
    "created_at": "2011-09-01T23:37:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99442",
    "user": "fbissey"
}
```

transcendental patch updated.



---

archive/issue_comments_099443.json:
```json
{
    "body": "Replying to [comment:117 fbissey]:\n> transcendental patch updated.\n\nLiterally?",
    "created_at": "2011-09-02T01:15:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99443",
    "user": "leif"
}
```

Replying to [comment:117 fbissey]:
> transcendental patch updated.

Literally?



---

archive/issue_comments_099444.json:
```json
{
    "body": "Replying to [comment:118 leif]:\n> Replying to [comment:117 fbissey]:\n> > transcendental patch updated.\n> \n> Literally?\nLiterally.",
    "created_at": "2011-09-02T01:33:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99444",
    "user": "fbissey"
}
```

Replying to [comment:118 leif]:
> Replying to [comment:117 fbissey]:
> > transcendental patch updated.
> 
> Literally?
Literally.



---

archive/issue_comments_099445.json:
```json
{
    "body": "Just for reference, on the PPC machine all tests pass with alpha2 except three timeouts which are long-standing (I didn't bother to set `SAGE_TIMEOUT_LONG` but I've seen these many times).\n\nSo all the rest are due to this ticket or #11339.  \n\nWould it be helpful for me to do #11339 on this new build (without Python 2.7), or is that in limbo right now anyway?  Alternately, is there any way to decouple this ticket from that one?",
    "created_at": "2011-09-02T12:04:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99445",
    "user": "kcrisman"
}
```

Just for reference, on the PPC machine all tests pass with alpha2 except three timeouts which are long-standing (I didn't bother to set `SAGE_TIMEOUT_LONG` but I've seen these many times).

So all the rest are due to this ticket or #11339.  

Would it be helpful for me to do #11339 on this new build (without Python 2.7), or is that in limbo right now anyway?  Alternately, is there any way to decouple this ticket from that one?



---

archive/issue_comments_099446.json:
```json
{
    "body": "Replying to [comment:120 kcrisman]:\n> Just for reference, on the PPC machine all tests pass with alpha2 except three timeouts which are long-standing (I didn't bother to set `SAGE_TIMEOUT_LONG` but I've seen these many times).\n> \n> So all the rest are due to this ticket or #11339.  \n\nThat's a very useful point of reference. Thank you for providing it.\n\n> \n> Would it be helpful for me to do #11339 on this new build (without Python 2.7), or is that in limbo right now anyway?  Alternately, is there any way to decouple this ticket from that one?\n\nTechnically you can apply #11339 without python 2.7 - the behavior we want to correct is only revealed when we use python 2.7 but I guess it would be useful to know if there are any side effects if you apply the patch on a python 2.6 install. Bear in mind that the current patch are not necessarily the best solution to the problem, what's more they are a whack a mole game. Fix something here and some new fault appears in a completely unexpected location.",
    "created_at": "2011-09-02T12:57:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99446",
    "user": "fbissey"
}
```

Replying to [comment:120 kcrisman]:
> Just for reference, on the PPC machine all tests pass with alpha2 except three timeouts which are long-standing (I didn't bother to set `SAGE_TIMEOUT_LONG` but I've seen these many times).
> 
> So all the rest are due to this ticket or #11339.  

That's a very useful point of reference. Thank you for providing it.

> 
> Would it be helpful for me to do #11339 on this new build (without Python 2.7), or is that in limbo right now anyway?  Alternately, is there any way to decouple this ticket from that one?

Technically you can apply #11339 without python 2.7 - the behavior we want to correct is only revealed when we use python 2.7 but I guess it would be useful to know if there are any side effects if you apply the patch on a python 2.6 install. Bear in mind that the current patch are not necessarily the best solution to the problem, what's more they are a whack a mole game. Fix something here and some new fault appears in a completely unexpected location.



---

archive/issue_comments_099447.json:
```json
{
    "body": "I will update the python spkg to 2.7.3 when it will be released. 2.7.3 will include the patch to python that we have been carrying in sage for the longest time. See:\n[http://bugs.python.org/issue7689](http://bugs.python.org/issue7689)\n\nDoes anyone know if the apocalypse is about to happen?",
    "created_at": "2011-10-04T21:14:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99447",
    "user": "fbissey"
}
```

I will update the python spkg to 2.7.3 when it will be released. 2.7.3 will include the patch to python that we have been carrying in sage for the longest time. See:
[http://bugs.python.org/issue7689](http://bugs.python.org/issue7689)

Does anyone know if the apocalypse is about to happen?



---

archive/issue_comments_099448.json:
```json
{
    "body": "Fixes #1159, according to that ticket.",
    "created_at": "2011-10-18T18:28:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99448",
    "user": "jason"
}
```

Fixes #1159, according to that ticket.



---

archive/issue_comments_099449.json:
```json
{
    "body": "That's really weird. Some of the hashing problems I encounter with python 2.7 are almost the same as reported in [http://trac.sagemath.org/sage_trac/ticket/4957#comment:3](http://trac.sagemath.org/sage_trac/ticket/4957#comment:3)\n\n```\nsage -t -long -force_lib \"devel/sage-main/sage/rings/integer.pyx\"\n**********************************************************************\nFile \"/usr/share/sage/devel/sage-main/sage/rings/integer.pyx\", line 3046:\n    sage: n = -920390823904823094890238490238484; n.__hash__()\nExpected:\n    6874330978542788722   \nGot:\n    -2623069716\n**********************************************************************\nFile \"/usr/share/sage/devel/sage-main/sage/rings/integer.pyx\", line 3061:\n    sage: hash(n)\nExpected:\n    -9223372036854767616      \nGot:\n    8192\n**********************************************************************\nFile \"/usr/share/sage/devel/sage-main/sage/rings/integer.pyx\", line 3064:\n    sage: hash(n) == hash(int(n))\nExpected:\n    True\nGot:\n    False\n**********************************************************************\n```\n",
    "created_at": "2011-11-01T23:18:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99449",
    "user": "fbissey"
}
```

That's really weird. Some of the hashing problems I encounter with python 2.7 are almost the same as reported in [http://trac.sagemath.org/sage_trac/ticket/4957#comment:3](http://trac.sagemath.org/sage_trac/ticket/4957#comment:3)

```
sage -t -long -force_lib "devel/sage-main/sage/rings/integer.pyx"
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/rings/integer.pyx", line 3046:
    sage: n = -920390823904823094890238490238484; n.__hash__()
Expected:
    6874330978542788722   
Got:
    -2623069716
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/rings/integer.pyx", line 3061:
    sage: hash(n)
Expected:
    -9223372036854767616      
Got:
    8192
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/rings/integer.pyx", line 3064:
    sage: hash(n) == hash(int(n))
Expected:
    True
Got:
    False
**********************************************************************
```




---

archive/issue_comments_099450.json:
```json
{
    "body": "With python-2.6:\n\n```\nsage: n=2^63+2^13\nsage: n\n9223372036854784000\nsage: int(n)\n9223372036854784000L\nsage: hash(n)\n-9223372036854767616\nsage: hash(int(n))\n-9223372036854767616\n```\n\nwith python-2.7\n\n```\nsage: n=2^63+2^13\nsage: n\n9223372036854784000\nsage: hash(n)\n8192\nsage: int(n)\n9223372036854784000L\nsage: hash(int(n))\n-9223372036854767616\n```\n\nFurthermore in both case:\n\n```\nsage: type(n)\n<type 'sage.rings.integer.Integer'>\nsage: type(int(n))\n<type 'long'>\n```\n\nSo I would expect different hashes naively.",
    "created_at": "2011-11-02T01:48:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99450",
    "user": "fbissey"
}
```

With python-2.6:

```
sage: n=2^63+2^13
sage: n
9223372036854784000
sage: int(n)
9223372036854784000L
sage: hash(n)
-9223372036854767616
sage: hash(int(n))
-9223372036854767616
```

with python-2.7

```
sage: n=2^63+2^13
sage: n
9223372036854784000
sage: hash(n)
8192
sage: int(n)
9223372036854784000L
sage: hash(int(n))
-9223372036854767616
```

Furthermore in both case:

```
sage: type(n)
<type 'sage.rings.integer.Integer'>
sage: type(int(n))
<type 'long'>
```

So I would expect different hashes naively.



---

archive/issue_comments_099451.json:
```json
{
    "body": "Regarding\n\n```\nsage -t -long -force_lib \"devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py\"\n**********************************************************************\nFile \"/usr/share/sage/devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py\", line 20:\n    sage: it.next()\nExpected:\n    word: 6456\nGot:\n    word: 5645\n**********************************************************************\nFile \"/usr/share/sage/devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py\", line 22:\n    sage: it.next()\nExpected:\n    word: 5645\nGot:\n    word: 6456\n**********************************************************************\n```\n\nWith python-2.7\n\n```\nsage: w = Word([4,5,6])^7\nsage: w\nword: 456456456456456456456\nsage: it = w.factor_iterator(4)\nsage: it.next()\nword: 5645\nsage: it.next()\nword: 6456\nsage: it.next()\nword: 4564\n```\n\nwith python-2.6\n\n```\nsage: w = Word([4,5,6])^7\nsage: w\nword: 456456456456456456456\nsage: it = w.factor_iterator(4)\nsage: it.next()\nword: 6456\nsage: it.next()\nword: 5645\nsage: it.next()\nword: 4564\n```\n\nSo it looks like with python 2.6 we where moving in the series of number with a stride 2 while python 2.7 works through the sequence with a stride 1.",
    "created_at": "2011-11-02T02:02:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99451",
    "user": "fbissey"
}
```

Regarding

```
sage -t -long -force_lib "devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py"
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py", line 20:
    sage: it.next()
Expected:
    word: 6456
Got:
    word: 5645
**********************************************************************
File "/usr/share/sage/devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py", line 22:
    sage: it.next()
Expected:
    word: 5645
Got:
    word: 6456
**********************************************************************
```

With python-2.7

```
sage: w = Word([4,5,6])^7
sage: w
word: 456456456456456456456
sage: it = w.factor_iterator(4)
sage: it.next()
word: 5645
sage: it.next()
word: 6456
sage: it.next()
word: 4564
```

with python-2.6

```
sage: w = Word([4,5,6])^7
sage: w
word: 456456456456456456456
sage: it = w.factor_iterator(4)
sage: it.next()
word: 6456
sage: it.next()
word: 5645
sage: it.next()
word: 4564
```

So it looks like with python 2.6 we where moving in the series of number with a stride 2 while python 2.7 works through the sequence with a stride 1.



---

archive/issue_comments_099452.json:
```json
{
    "body": "Here\u00a0on x86 I get only two failures:\n\n\n```\n\nsage -t -long  -force_lib devel/sage-main/sage/misc/randstate.pyx\n**********************************************************************\nFile \"/storage/sage/sage-4.7.2.rc0/devel/sage-main/sage/misc/randstate.pyx\", line 61:\n    sage: rtest()\nExpected:\n    (978, 0.184109262667515, -3*x^2 - 1/12, (4,5), [ 0, 1, 1, 0, 0 ], 1161603091, 603\n59, 0.83350776541997362)\nGot:\n    (978, 0.184109262667515, -3*x^2 - 1/12, (4,5), [ 0, 1, 1, 0, 0 ], 1161603091, 603\n59, 0.8335077654199736)\n**********************************************************************\n```\n\n\nand \n\n\n```\nsage -t -long  -force_lib devel/sage-main/sage/matrix/matrix_double_dense.pyx\n**********************************************************************\nFile \"/storage/sage/sage-4.7.2.rc0/devel/sage-main/sage/matrix/matrix_double_dense.py\nx\", line 1046:\n    sage: A.singular_values(eps='junk')\nExpected:\n    Traceback (most recent call last):\n    ...\n    ValueError: invalid literal for float(): junk\nGot:\n    Traceback (most recent call last):\n      File \"/storage/sage/sage-4.7.2.rc0/local/bin/ncadoctest.py\", line 1231, in run_\none_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/storage/sage/sage-4.7.2.rc0/local/bin/sagedoctest.py\", line 38, in run_o\nne_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags\n)\n      File \"/storage/sage/sage-4.7.2.rc0/local/bin/ncadoctest.py\", line 1172, in run_\none_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_19[37]>\", line 1, in <module>\n        A.singular_values(eps='junk')###line 1046:\n    sage: A.singular_values(eps='junk')\n      File \"matrix_double_dense.pyx\", line 1075, in sage.matrix.matrix_double_dense.M\natrix_double_dense.singular_values (sage/matrix/matrix_double_dense.c:6338)\n        eps = RDF(eps)\n      File \"parent.pyx\", line 988, in sage.structure.parent.Parent.__call__ (sage/str\nucture/parent.c:7326)\n      File \"coerce_maps.pyx\", line 82, in sage.structure.coerce_maps.DefaultConvertMa\np_unique._call_ (sage/structure/coerce_maps.c:3268)\n      File \"coerce_maps.pyx\", line 77, in sage.structure.coerce_maps.DefaultConvertMa\np_unique._call_ (sage/structure/coerce_maps.c:3171)\n      File \"real_double.pyx\", line 548, in sage.rings.real_double.RealDoubleElement._\n_init__ (sage/rings/real_double.c:5567)\n    ValueError: could not convert string to float: junk\n**********************************************************************\n```\n\n\nThe latter also fails here the same way on amd64 and is documented on sage-devel\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/8e1d7f665ac5be37\n\nbut with some slight differences.",
    "created_at": "2011-11-02T05:01:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99452",
    "user": "strogdon"
}
```

Here on x86 I get only two failures:


```

sage -t -long  -force_lib devel/sage-main/sage/misc/randstate.pyx
**********************************************************************
File "/storage/sage/sage-4.7.2.rc0/devel/sage-main/sage/misc/randstate.pyx", line 61:
    sage: rtest()
Expected:
    (978, 0.184109262667515, -3*x^2 - 1/12, (4,5), [ 0, 1, 1, 0, 0 ], 1161603091, 603
59, 0.83350776541997362)
Got:
    (978, 0.184109262667515, -3*x^2 - 1/12, (4,5), [ 0, 1, 1, 0, 0 ], 1161603091, 603
59, 0.8335077654199736)
**********************************************************************
```


and 


```
sage -t -long  -force_lib devel/sage-main/sage/matrix/matrix_double_dense.pyx
**********************************************************************
File "/storage/sage/sage-4.7.2.rc0/devel/sage-main/sage/matrix/matrix_double_dense.py
x", line 1046:
    sage: A.singular_values(eps='junk')
Expected:
    Traceback (most recent call last):
    ...
    ValueError: invalid literal for float(): junk
Got:
    Traceback (most recent call last):
      File "/storage/sage/sage-4.7.2.rc0/local/bin/ncadoctest.py", line 1231, in run_
one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/storage/sage/sage-4.7.2.rc0/local/bin/sagedoctest.py", line 38, in run_o
ne_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags
)
      File "/storage/sage/sage-4.7.2.rc0/local/bin/ncadoctest.py", line 1172, in run_
one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_19[37]>", line 1, in <module>
        A.singular_values(eps='junk')###line 1046:
    sage: A.singular_values(eps='junk')
      File "matrix_double_dense.pyx", line 1075, in sage.matrix.matrix_double_dense.M
atrix_double_dense.singular_values (sage/matrix/matrix_double_dense.c:6338)
        eps = RDF(eps)
      File "parent.pyx", line 988, in sage.structure.parent.Parent.__call__ (sage/str
ucture/parent.c:7326)
      File "coerce_maps.pyx", line 82, in sage.structure.coerce_maps.DefaultConvertMa
p_unique._call_ (sage/structure/coerce_maps.c:3268)
      File "coerce_maps.pyx", line 77, in sage.structure.coerce_maps.DefaultConvertMa
p_unique._call_ (sage/structure/coerce_maps.c:3171)
      File "real_double.pyx", line 548, in sage.rings.real_double.RealDoubleElement._
_init__ (sage/rings/real_double.c:5567)
    ValueError: could not convert string to float: junk
**********************************************************************
```


The latter also fails here the same way on amd64 and is documented on sage-devel

http://groups.google.com/group/sage-devel/browse_thread/thread/8e1d7f665ac5be37

but with some slight differences.



---

archive/issue_comments_099453.json:
```json
{
    "body": "OK Steve, I got the matrix_double_dense but you don't get the numerical noise. I believe the noise may come from python-2.7.2. Interesting that the hashing and enumeration problem are 64bit only. I'll check on the mac.",
    "created_at": "2011-11-02T11:41:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99453",
    "user": "fbissey"
}
```

OK Steve, I got the matrix_double_dense but you don't get the numerical noise. I believe the noise may come from python-2.7.2. Interesting that the hashing and enumeration problem are 64bit only. I'll check on the mac.



---

archive/issue_comments_099454.json:
```json
{
    "body": "Fix doctest in matrix_double_dense.pyx about junk",
    "created_at": "2011-11-02T22:37:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99454",
    "user": "fbissey"
}
```

Fix doctest in matrix_double_dense.pyx about junk



---

archive/issue_comments_099455.json:
```json
{
    "body": "Attachment\n\nNew patch to fix the message about junk.",
    "created_at": "2011-11-02T22:38:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99455",
    "user": "fbissey"
}
```

Attachment

New patch to fix the message about junk.



---

archive/issue_comments_099456.json:
```json
{
    "body": "I have now split the hashing issue in #11986",
    "created_at": "2011-11-03T01:52:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99456",
    "user": "fbissey"
}
```

I have now split the hashing issue in #11986



---

archive/issue_comments_099457.json:
```json
{
    "body": "fix the doctest on enumeration order for 64bit system",
    "created_at": "2011-11-03T02:13:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99457",
    "user": "fbissey"
}
```

fix the doctest on enumeration order for 64bit system



---

archive/issue_comments_099458.json:
```json
{
    "body": "Attachment\n\nOne more patch added to fix combinat/words/nfactor_enumerable_word.py on 64 bit system. I believe is output is equivalent in both case so it is not important.",
    "created_at": "2011-11-03T02:15:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99458",
    "user": "fbissey"
}
```

Attachment

One more patch added to fix combinat/words/nfactor_enumerable_word.py on 64 bit system. I believe is output is equivalent in both case so it is not important.



---

archive/issue_comments_099459.json:
```json
{
    "body": "Removed old dependencies.",
    "created_at": "2011-11-03T21:16:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99459",
    "user": "jdemeyer"
}
```

Removed old dependencies.



---

archive/issue_comments_099460.json:
```json
{
    "body": "The spkg needs to be rebased to #11447.",
    "created_at": "2011-11-03T21:24:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99460",
    "user": "jdemeyer"
}
```

The spkg needs to be rebased to #11447.



---

archive/issue_comments_099461.json:
```json
{
    "body": "Permissions is the spkg should be 0644 (or 0755 for executables), currently many files are 0640 or 0750.",
    "created_at": "2011-11-03T21:26:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99461",
    "user": "jdemeyer"
}
```

Permissions is the spkg should be 0644 (or 0755 for executables), currently many files are 0640 or 0750.



---

archive/issue_comments_099462.json:
```json
{
    "body": "Replying to [comment:133 jdemeyer]:\n> The spkg needs to be rebased to #11447.\nI looked at that before making my spkg. I believe the strategy used in #11447 is in python-2.7. Someone with a debian system proves me wrong but I think that works out of the box.",
    "created_at": "2011-11-04T01:12:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99462",
    "user": "fbissey"
}
```

Replying to [comment:133 jdemeyer]:
> The spkg needs to be rebased to #11447.
I looked at that before making my spkg. I believe the strategy used in #11447 is in python-2.7. Someone with a debian system proves me wrong but I think that works out of the box.



---

archive/issue_comments_099463.json:
```json
{
    "body": "Replying to [comment:135 fbissey]:\n> Replying to [comment:133 jdemeyer]:\n> > The spkg needs to be rebased to #11447.\n> I looked at that before making my spkg. I believe the strategy used in #11447 is in python-2.7. Someone with a debian system proves me wrong but I think that works out of the box.\n\nWell, we did take the patch from Python upstream, but IIRC there are further changes to `spkg-install`, and the new spkg needs the previous one to be mentioned in `SPKG.txt` anyway (to pass the merger's sanity check).",
    "created_at": "2011-11-04T01:48:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99463",
    "user": "leif"
}
```

Replying to [comment:135 fbissey]:
> Replying to [comment:133 jdemeyer]:
> > The spkg needs to be rebased to #11447.
> I looked at that before making my spkg. I believe the strategy used in #11447 is in python-2.7. Someone with a debian system proves me wrong but I think that works out of the box.

Well, we did take the patch from Python upstream, but IIRC there are further changes to `spkg-install`, and the new spkg needs the previous one to be mentioned in `SPKG.txt` anyway (to pass the merger's sanity check).



---

archive/issue_comments_099464.json:
```json
{
    "body": "Indeed, there've been **a lot of** changes inbetween:\n\n```diff\ndiff -Nu python-2.7.1/spkg-install python-2.6.4.p11/spkg-install\n--- python-2.7.1/spkg-install\t2011-05-20 05:41:41.000000000 +0200\n+++ python-2.6.4.p11/spkg-install\t2011-07-05 10:46:40.000000000 +0200\n@@ -5,50 +5,127 @@\n \n CUR=`pwd`\n \n-if [ \"$SAGE_LOCAL\" = \"\" ]; then\n-   echo \"SAGE_LOCAL undefined ... exiting\";\n-   echo \"Maybe run 'sage -sh'?\"\n-   exit 1\n+if [ -z \"$SAGE_LOCAL\" ]; then\n+    echo >&2 \"SAGE_LOCAL undefined ... exiting\"\n+    echo >&2 \"Maybe run 'sage -sh'?\"\n+    exit 1\n fi\n \n # PATCH\n \n-# Due to issues building Python on Ubuntu 11.04, a file is patched\n-# on these systems. \n+# When building Python 2.6 on Debian and derivatives with multiarch,\n+# system library directories are not correctly setup.  This patch\n+# fixes this, with no-op on other systems.\n+# The fix requires 'dpkg-architecture' to be installed there though\n+# (see below).\n+echo \"Patching src/setup.py for multiarch.\"\n+patch -p0 < patches/setup.py.multiarch.patch\n+if [ $? -ne 0 ]; then\n+    echo >&2 \"Error patching src/setup.py\"\n+    exit 1\n+fi\n \n-if [ -f /etc/issue ] && grep \"Ubuntu 11.04\" /etc/issue ; then\n-   echo \"Patching src/Modules/Setup.dist as this is Ubuntu 11.04\"\n-   patch -p0 < patches/Modules.Setup.dist.patch\n+# Due to a python bug with Solaris \n+# see http://bugs.python.org/issue1759169\n+# it is necessary to apply a patch to configure.in\n+# then run autoconf. This not only generates a\n+# new 'configure' script, but some subdirectories too\n+# so these will be copied. \n+\n+if [ \"x`uname`\" = xSunOS ] ; then\n+   echo \"Applying a revised 'configure' script for Solaris\"\n+   echo \"See http://bugs.python.org/issue1759169\"\n+   echo \"http://trac.sagemath.org/sage_trac/ticket/7867\"\n+   cp -r patches/autom4te.cache patches/configure patches/configure.in src\n    if [ $? -ne 0 ]; then\n-      echo \"Error patching src/Modules/Setup.dist\"\n+      echo >&2 \"Failed to apply the Solaris patches needed for\"\n+      echo >&2 \"http://bugs.python.org/issue1759169\"\n+      echo >&2 \"http://trac.sagemath.org/sage_trac/ticket/7867\"\n       exit 1\n    fi\n+   echo \"Setting  HAVE_FD_TRANSFER=0 for Solaris to allow\"\n+   echo \"the python module '_multiprocessing' to build\" \n+   echo \"See: http://trac.sagemath.org/sage_trac/ticket/8440\"\n+   cp patches/setup.py src\n+   if [ $? -ne 0 ]; then\n+      echo >&2 \"Failed to apply the Solaris patch needed for\"\n+      echo >&2 \"http://trac.sagemath.org/sage_trac/ticket/8440\"\n+      exit 1\n+   fi\n+fi \n+\n+\n+cp patches/locale.py src/Lib/locale.py\n+if [ $? -ne 0 ]; then\n+    echo >&2 \"Error copying patched locale.py\"\n+    exit 1\n fi\n \n-patch -p0 < patches/Lib.distutils.command.sdist.patch\n+cp patches/Makefile.pre.in src/Makefile.pre.in\n if [ $? -ne 0 ]; then\n-    echo \"Error copying patched sdist.py\"\n+    echo >&2 \"Error copying patched Makefile.pre.in\"\n     exit 1\n fi\n \n-patch -p0 < patches/Lib.socket.patch\n+cp patches/sdist.py src/Lib/distutils/command/sdist.py\n if [ $? -ne 0 ]; then\n-    echo \"Error copying patched socket.py\"\n+    echo >&2 \"Error copying patched sdist.py\"\n     exit 1\n fi\n \n-patch -p0 < patches/dynamic_class_copyreg_py.patch\n+cp patches/socket.py src/Lib/socket.py\n if [ $? -ne 0 ]; then\n-    echo \"Error copying patched pickle.py\"\n+    echo >&2 \"Error copying patched socket.py\"\n     exit 1\n fi\n \n-patch -p0 < patches/dynamic_class_copyreg_c.patch\n+cp patches/pickle.py src/Lib/pickle.py\n if [ $? -ne 0 ]; then\n-    echo \"Error copying patched cPickle.c\"\n+    echo >&2 \"Error copying patched pickle.py\"\n     exit 1\n fi\n \n+cp patches/cPickle.c src/Modules/cPickle.c\n+if [ $? -ne 0 ]; then\n+    echo >&2 \"Error copying patched cPickle.c\"\n+    exit 1\n+fi\n+\n+# Due to a problem with _socket not building on OpenSolaris on x64\n+# see http://bugs.python.org/issue8852\n+# http://trac.sagemath.org/sage_trac/ticket/9041\n+# http://trac.sagemath.org/sage_trac/ticket/9022\n+# Modules/socketmodule.c needs patching. The patch consists of \n+# only checking if things are defined before trying to build with them\n+# so it is safe (and desirable) on any platform. \n+\n+cp patches/Modules.socketmodule.c src/Modules/socketmodule.c\n+if [ $? -ne 0 ]; then\n+    echo >&2 \"Error copying patched socketmodule.c\"\n+    exit 1\n+fi\n+\n+# The following patch for fixing broken readline behavior on Itanium\n+# Linux definitely does *not* work on anything else.\n+if [ \"`uname -m`\" = \"ia64\" -a \"`uname`\" = \"Linux\" ]; then\n+    echo \"Updating readline.c for Linux/Itanium\"\n+    cp patches/readline.c-Itanium-fix src/Modules/readline.c\n+else\n+    # Readline patch: http://bugs.python.org/file14599/python-2.6-readline.patch\n+    # Associated bug: http://bugs.python.org/issue5833\n+    #\n+    # Committed to Python as r75747 in the py26-maint branch, but not\n+    # in time for 2.6.4 -- so we can remove this patch the next time\n+    # we update Python in Sage.\n+    cp patches/readline.c-spacebug src/Modules/readline.c\n+fi\n+\n+if [ $? -ne 0 ]; then\n+    echo >&2 \"Error copying patched readline.c\"\n+    exit 1\n+fi\n+\n+\n # We are setting LDFLAGS and CPPFLAGS so that we pick up Sage's readline\n LDFLAGS=\"-L$SAGE_LOCAL/lib $LDFLAGS\"\n export LDFLAGS\n@@ -62,6 +139,23 @@\n     EXTRAFLAGS=\"--without-pymalloc\"; export EXTRAFLAGS\n fi\n \n+# Program around weird bug in build process:\n+#      Apparently if you have this:\n+#         export DISTUTILS_DEBUG=1\n+#      in your environment variables, the build craps out.  No idea why this\n+#       is.\n+#       -- Yi Qiang\n+#\n+# This bug was fixed in Python, but not yet in Python 2.6.4. So this fix\n+# can be removed the next time we upgrade our version of Python. See\n+#\n+#   http://bugs.python.org/issue6954\n+#\n+# for the fix.\n+#\n+unset DISTUTILS_DEBUG\n+\n+\n cd src\n \n touch Include/*\n@@ -93,27 +187,30 @@\n             --enable-unicode=ucs4\n         fi\n     else\n-        ./configure $EXTRAFLAGS --prefix=\"$SAGE_LOCAL\"  --enable-unicode=ucs4 CC=\"$CC $CFLAGS\" CXX=\"$CXX $CXXFLAGS\"\n+        ./configure $EXTRAFLAGS --prefix=\"$SAGE_LOCAL\"  --enable-unicode=ucs4 \\\n+            CC=\"$CC $CFLAGS\" CXX=\"$CXX $CXXFLAGS\"\n     fi\n \n \n     if [ $? -ne 0 ]; then\n-        echo \"Error configuring Python.\"\n+        echo >&2 \"Error configuring Python.\"\n         exit 1\n     fi\n \n     $MAKE\n     if [ $? -ne 0 ]; then\n-        echo \"Error building Python.\"\n+        echo >&2 \"Error building Python.\"\n         exit 1\n     fi\n \n     # running 'make install' in parallel is a bad, bad idea\n+    # FIXME: The proper way to disable parallel make is to use\n+    #        $MAKE -j1 ... (We rely on GNU make anyway).\n     MAKE=make; export MAKE\n     # the \"-i\" is crucial, esp. in the case of a major upgrade\n     make -i install\n     if [ $? -ne 0 ]; then\n-        echo \"Error installing Python.\"\n+        echo >&2 \"Error installing Python.\"\n         exit 1\n     fi\n }\n@@ -122,27 +219,28 @@\n # informative error message. This is helps in determining why the\n # configuration, compilation or installation failed. So put this before the\n # build() function.\n-set +e\n+set +e # This is redundant here, but doesn't hurt to keep it... ;-)\n \n build\n \n-cd $SAGE_LOCAL/lib\n+cd \"$SAGE_LOCAL/lib\"\n \n # move the python directory if we're upgrading from a version\n-# of sage with python 2.6\n-if [ -d python2.6/site-packages ]; then\n-   mv python2.6/site-packages python2.7/site-packages-old\n+# of sage with python 2.5\n+if [ -d python2.5/site-packages ]; then\n+   mv python2.5/site-packages python2.6/site-packages-old\n fi\n \n-rm -rf python/python2.7 python/python2.6 python/python2.5 python/python python python2.4 python2.5\n-ln -s python2.7 python\n+rm -rf python/python2.6 python/python2.5 python/python python python2.4 python2.5\n+ln -s python2.6 python\n if [ $? -ne 0 ]; then\n-    echo \"Error creating symbolic link\"\n+    echo >&2 \"Error creating symbolic link\"\n     exit 1\n fi\n \n # Sleeping for three seconds so that parallel 'make install' catches up\n # with the following test.\n+# XXX We have disabled parallel 'make install' above, but never mind.\n echo \"Sleeping for three seconds before testing python\"\n sleep 3\n \n@@ -150,12 +248,28 @@\n # All these modules are important and if any one \n # fails to build, Sage will not work. \n \n+import_errors=false\n for module in math hashlib crypt ; do \n    \"$SAGE_LOCAL/bin/python\" -c \"import $module\"\n    if [ $? -eq 0 ] ; then\n       echo \"$module module imported OK\"\n    else\n-      echo \"$module module failed to import\"\n-      exit 1\n+      echo >&2 \"$module module failed to import\"\n+      import_errors=true\n+      # exit 1 # not yet\n    fi\n done\n+\n+if $import_errors; then\n+    echo >&2 \"Error: One or more modules failed to import.\"\n+    # Check if we are on Debian or one of its derivatives:\n+    if command -v dpkg && ! command -v dpkg-architecture >/dev/null; then\n+        echo >&2 \"You may have to install 'dpkg-architecture'\"\n+        echo >&2 \"which is part of the Debian package 'dpkg-dev'.\"\n+        echo >&2 \"Try installing it by typing\"\n+        echo >&2 \"    sudo apt-get install dpkg-dev\"\n+        echo >&2 \"and rerun 'make'.\"\n+    fi\n+    exit 1\n+fi\n+\n```\n",
    "created_at": "2011-11-04T02:03:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99464",
    "user": "leif"
}
```

Indeed, there've been **a lot of** changes inbetween:

```diff
diff -Nu python-2.7.1/spkg-install python-2.6.4.p11/spkg-install
--- python-2.7.1/spkg-install	2011-05-20 05:41:41.000000000 +0200
+++ python-2.6.4.p11/spkg-install	2011-07-05 10:46:40.000000000 +0200
@@ -5,50 +5,127 @@
 
 CUR=`pwd`
 
-if [ "$SAGE_LOCAL" = "" ]; then
-   echo "SAGE_LOCAL undefined ... exiting";
-   echo "Maybe run 'sage -sh'?"
-   exit 1
+if [ -z "$SAGE_LOCAL" ]; then
+    echo >&2 "SAGE_LOCAL undefined ... exiting"
+    echo >&2 "Maybe run 'sage -sh'?"
+    exit 1
 fi
 
 # PATCH
 
-# Due to issues building Python on Ubuntu 11.04, a file is patched
-# on these systems. 
+# When building Python 2.6 on Debian and derivatives with multiarch,
+# system library directories are not correctly setup.  This patch
+# fixes this, with no-op on other systems.
+# The fix requires 'dpkg-architecture' to be installed there though
+# (see below).
+echo "Patching src/setup.py for multiarch."
+patch -p0 < patches/setup.py.multiarch.patch
+if [ $? -ne 0 ]; then
+    echo >&2 "Error patching src/setup.py"
+    exit 1
+fi
 
-if [ -f /etc/issue ] && grep "Ubuntu 11.04" /etc/issue ; then
-   echo "Patching src/Modules/Setup.dist as this is Ubuntu 11.04"
-   patch -p0 < patches/Modules.Setup.dist.patch
+# Due to a python bug with Solaris 
+# see http://bugs.python.org/issue1759169
+# it is necessary to apply a patch to configure.in
+# then run autoconf. This not only generates a
+# new 'configure' script, but some subdirectories too
+# so these will be copied. 
+
+if [ "x`uname`" = xSunOS ] ; then
+   echo "Applying a revised 'configure' script for Solaris"
+   echo "See http://bugs.python.org/issue1759169"
+   echo "http://trac.sagemath.org/sage_trac/ticket/7867"
+   cp -r patches/autom4te.cache patches/configure patches/configure.in src
    if [ $? -ne 0 ]; then
-      echo "Error patching src/Modules/Setup.dist"
+      echo >&2 "Failed to apply the Solaris patches needed for"
+      echo >&2 "http://bugs.python.org/issue1759169"
+      echo >&2 "http://trac.sagemath.org/sage_trac/ticket/7867"
       exit 1
    fi
+   echo "Setting  HAVE_FD_TRANSFER=0 for Solaris to allow"
+   echo "the python module '_multiprocessing' to build" 
+   echo "See: http://trac.sagemath.org/sage_trac/ticket/8440"
+   cp patches/setup.py src
+   if [ $? -ne 0 ]; then
+      echo >&2 "Failed to apply the Solaris patch needed for"
+      echo >&2 "http://trac.sagemath.org/sage_trac/ticket/8440"
+      exit 1
+   fi
+fi 
+
+
+cp patches/locale.py src/Lib/locale.py
+if [ $? -ne 0 ]; then
+    echo >&2 "Error copying patched locale.py"
+    exit 1
 fi
 
-patch -p0 < patches/Lib.distutils.command.sdist.patch
+cp patches/Makefile.pre.in src/Makefile.pre.in
 if [ $? -ne 0 ]; then
-    echo "Error copying patched sdist.py"
+    echo >&2 "Error copying patched Makefile.pre.in"
     exit 1
 fi
 
-patch -p0 < patches/Lib.socket.patch
+cp patches/sdist.py src/Lib/distutils/command/sdist.py
 if [ $? -ne 0 ]; then
-    echo "Error copying patched socket.py"
+    echo >&2 "Error copying patched sdist.py"
     exit 1
 fi
 
-patch -p0 < patches/dynamic_class_copyreg_py.patch
+cp patches/socket.py src/Lib/socket.py
 if [ $? -ne 0 ]; then
-    echo "Error copying patched pickle.py"
+    echo >&2 "Error copying patched socket.py"
     exit 1
 fi
 
-patch -p0 < patches/dynamic_class_copyreg_c.patch
+cp patches/pickle.py src/Lib/pickle.py
 if [ $? -ne 0 ]; then
-    echo "Error copying patched cPickle.c"
+    echo >&2 "Error copying patched pickle.py"
     exit 1
 fi
 
+cp patches/cPickle.c src/Modules/cPickle.c
+if [ $? -ne 0 ]; then
+    echo >&2 "Error copying patched cPickle.c"
+    exit 1
+fi
+
+# Due to a problem with _socket not building on OpenSolaris on x64
+# see http://bugs.python.org/issue8852
+# http://trac.sagemath.org/sage_trac/ticket/9041
+# http://trac.sagemath.org/sage_trac/ticket/9022
+# Modules/socketmodule.c needs patching. The patch consists of 
+# only checking if things are defined before trying to build with them
+# so it is safe (and desirable) on any platform. 
+
+cp patches/Modules.socketmodule.c src/Modules/socketmodule.c
+if [ $? -ne 0 ]; then
+    echo >&2 "Error copying patched socketmodule.c"
+    exit 1
+fi
+
+# The following patch for fixing broken readline behavior on Itanium
+# Linux definitely does *not* work on anything else.
+if [ "`uname -m`" = "ia64" -a "`uname`" = "Linux" ]; then
+    echo "Updating readline.c for Linux/Itanium"
+    cp patches/readline.c-Itanium-fix src/Modules/readline.c
+else
+    # Readline patch: http://bugs.python.org/file14599/python-2.6-readline.patch
+    # Associated bug: http://bugs.python.org/issue5833
+    #
+    # Committed to Python as r75747 in the py26-maint branch, but not
+    # in time for 2.6.4 -- so we can remove this patch the next time
+    # we update Python in Sage.
+    cp patches/readline.c-spacebug src/Modules/readline.c
+fi
+
+if [ $? -ne 0 ]; then
+    echo >&2 "Error copying patched readline.c"
+    exit 1
+fi
+
+
 # We are setting LDFLAGS and CPPFLAGS so that we pick up Sage's readline
 LDFLAGS="-L$SAGE_LOCAL/lib $LDFLAGS"
 export LDFLAGS
@@ -62,6 +139,23 @@
     EXTRAFLAGS="--without-pymalloc"; export EXTRAFLAGS
 fi
 
+# Program around weird bug in build process:
+#      Apparently if you have this:
+#         export DISTUTILS_DEBUG=1
+#      in your environment variables, the build craps out.  No idea why this
+#       is.
+#       -- Yi Qiang
+#
+# This bug was fixed in Python, but not yet in Python 2.6.4. So this fix
+# can be removed the next time we upgrade our version of Python. See
+#
+#   http://bugs.python.org/issue6954
+#
+# for the fix.
+#
+unset DISTUTILS_DEBUG
+
+
 cd src
 
 touch Include/*
@@ -93,27 +187,30 @@
             --enable-unicode=ucs4
         fi
     else
-        ./configure $EXTRAFLAGS --prefix="$SAGE_LOCAL"  --enable-unicode=ucs4 CC="$CC $CFLAGS" CXX="$CXX $CXXFLAGS"
+        ./configure $EXTRAFLAGS --prefix="$SAGE_LOCAL"  --enable-unicode=ucs4 \
+            CC="$CC $CFLAGS" CXX="$CXX $CXXFLAGS"
     fi
 
 
     if [ $? -ne 0 ]; then
-        echo "Error configuring Python."
+        echo >&2 "Error configuring Python."
         exit 1
     fi
 
     $MAKE
     if [ $? -ne 0 ]; then
-        echo "Error building Python."
+        echo >&2 "Error building Python."
         exit 1
     fi
 
     # running 'make install' in parallel is a bad, bad idea
+    # FIXME: The proper way to disable parallel make is to use
+    #        $MAKE -j1 ... (We rely on GNU make anyway).
     MAKE=make; export MAKE
     # the "-i" is crucial, esp. in the case of a major upgrade
     make -i install
     if [ $? -ne 0 ]; then
-        echo "Error installing Python."
+        echo >&2 "Error installing Python."
         exit 1
     fi
 }
@@ -122,27 +219,28 @@
 # informative error message. This is helps in determining why the
 # configuration, compilation or installation failed. So put this before the
 # build() function.
-set +e
+set +e # This is redundant here, but doesn't hurt to keep it... ;-)
 
 build
 
-cd $SAGE_LOCAL/lib
+cd "$SAGE_LOCAL/lib"
 
 # move the python directory if we're upgrading from a version
-# of sage with python 2.6
-if [ -d python2.6/site-packages ]; then
-   mv python2.6/site-packages python2.7/site-packages-old
+# of sage with python 2.5
+if [ -d python2.5/site-packages ]; then
+   mv python2.5/site-packages python2.6/site-packages-old
 fi
 
-rm -rf python/python2.7 python/python2.6 python/python2.5 python/python python python2.4 python2.5
-ln -s python2.7 python
+rm -rf python/python2.6 python/python2.5 python/python python python2.4 python2.5
+ln -s python2.6 python
 if [ $? -ne 0 ]; then
-    echo "Error creating symbolic link"
+    echo >&2 "Error creating symbolic link"
     exit 1
 fi
 
 # Sleeping for three seconds so that parallel 'make install' catches up
 # with the following test.
+# XXX We have disabled parallel 'make install' above, but never mind.
 echo "Sleeping for three seconds before testing python"
 sleep 3
 
@@ -150,12 +248,28 @@
 # All these modules are important and if any one 
 # fails to build, Sage will not work. 
 
+import_errors=false
 for module in math hashlib crypt ; do 
    "$SAGE_LOCAL/bin/python" -c "import $module"
    if [ $? -eq 0 ] ; then
       echo "$module module imported OK"
    else
-      echo "$module module failed to import"
-      exit 1
+      echo >&2 "$module module failed to import"
+      import_errors=true
+      # exit 1 # not yet
    fi
 done
+
+if $import_errors; then
+    echo >&2 "Error: One or more modules failed to import."
+    # Check if we are on Debian or one of its derivatives:
+    if command -v dpkg && ! command -v dpkg-architecture >/dev/null; then
+        echo >&2 "You may have to install 'dpkg-architecture'"
+        echo >&2 "which is part of the Debian package 'dpkg-dev'."
+        echo >&2 "Try installing it by typing"
+        echo >&2 "    sudo apt-get install dpkg-dev"
+        echo >&2 "and rerun 'make'."
+    fi
+    exit 1
+fi
+
```




---

archive/issue_comments_099465.json:
```json
{
    "body": "OK that's not a biggy while I had a look at #11447 I made my spkg before it was closed and possibly before it had reached its final shape. I wanted to wait for 2.7.3 but I will probably cut a 2.7.2 in which I will add this then. \n\nI am keen to have this landing ASAP but I would understand if the release manager only wants to do it in a alpha0. That's both a big change and a big patch set. My concern is that my last patch may not be adequate. Steve tested a number of configurations and the order this comes out are all over the place. I may have to make it random which is not nice.\n\nThe other concern is #11986 which looks like a blast from the past and I have no clues on either of them.",
    "created_at": "2011-11-04T02:07:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99465",
    "user": "fbissey"
}
```

OK that's not a biggy while I had a look at #11447 I made my spkg before it was closed and possibly before it had reached its final shape. I wanted to wait for 2.7.3 but I will probably cut a 2.7.2 in which I will add this then. 

I am keen to have this landing ASAP but I would understand if the release manager only wants to do it in a alpha0. That's both a big change and a big patch set. My concern is that my last patch may not be adequate. Steve tested a number of configurations and the order this comes out are all over the place. I may have to make it random which is not nice.

The other concern is #11986 which looks like a blast from the past and I have no clues on either of them.



---

archive/issue_comments_099466.json:
```json
{
    "body": "Replying to [comment:138 fbissey]:\n> OK that's not a biggy while I had a look at #11447 I made my spkg before it was closed and possibly before it had reached its final shape. I wanted to wait for 2.7.3 but I will probably cut a 2.7.2 in which I will add this then. \n> \n> I am keen to have this landing ASAP but I would understand if the release manager only wants to do it in a alpha0. That's both a big change and a big patch set.\n\nIf you can finish it, I'd be happy to merge it.  But to be realistic, I don't think this ticket is close to being finished.  There is a huge amount of patches which needs to be reviewed, there is still #11986, there is the rebasing to #11447, maybe testing will reveal breakage on some systems...",
    "created_at": "2011-11-04T09:24:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99466",
    "user": "jdemeyer"
}
```

Replying to [comment:138 fbissey]:
> OK that's not a biggy while I had a look at #11447 I made my spkg before it was closed and possibly before it had reached its final shape. I wanted to wait for 2.7.3 but I will probably cut a 2.7.2 in which I will add this then. 
> 
> I am keen to have this landing ASAP but I would understand if the release manager only wants to do it in a alpha0. That's both a big change and a big patch set.

If you can finish it, I'd be happy to merge it.  But to be realistic, I don't think this ticket is close to being finished.  There is a huge amount of patches which needs to be reviewed, there is still #11986, there is the rebasing to #11447, maybe testing will reveal breakage on some systems...



---

archive/issue_comments_099467.json:
```json
{
    "body": "There is a warning when building the reference manual:\n\n```\ndocstring of sage.crypto.boolean_function:3: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\n```\n",
    "created_at": "2011-11-04T10:10:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99467",
    "user": "jdemeyer"
}
```

There is a warning when building the reference manual:

```
docstring of sage.crypto.boolean_function:3: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
```




---

archive/issue_comments_099468.json:
```json
{
    "body": "Another minor comment: please use UTF8 in `SPKG.txt`.  Currently, \"Fran\u00e7ois\" is encoded as latin1.",
    "created_at": "2011-11-05T21:41:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99468",
    "user": "jdemeyer"
}
```

Another minor comment: please use UTF8 in `SPKG.txt`.  Currently, "François" is encoded as latin1.



---

archive/issue_comments_099469.json:
```json
{
    "body": "By the way: Python 2.7.2 was released on June 11th, 2011 so you might as well go for that.",
    "created_at": "2011-11-05T22:14:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99469",
    "user": "jdemeyer"
}
```

By the way: Python 2.7.2 was released on June 11th, 2011 so you might as well go for that.



---

archive/issue_comments_099470.json:
```json
{
    "body": "Replying to [comment:144 jdemeyer]:\n> By the way: Python 2.7.2 was released on June 11th, 2011 so you might as well go for that.\n\nsage-5.0 is probably more realistic. Thanks for the useful comments, I hadn't seen the warnings in the documentation, this probably could be spun out of this ticket as it is probably a problem in the existing doc - just silent with the current python. I really would like to go to 2.7.3 when it comes out but I'll make a stop 2.7.2. I have a heavy workload this week but I'll try to put the spkg together. I know from sage-on-gentto that there will be some more patching to be done unfortunately although in some case I think that would be just a band aid. So more dependencies may appear :(\n\nI am surprised at the \"latin-1\" encoding I am defaulting to UTF-8 and even my Changelogs now come correct everywhere.\n\nWe need someone with the know how to look at #11986.",
    "created_at": "2011-11-05T22:25:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99470",
    "user": "fbissey"
}
```

Replying to [comment:144 jdemeyer]:
> By the way: Python 2.7.2 was released on June 11th, 2011 so you might as well go for that.

sage-5.0 is probably more realistic. Thanks for the useful comments, I hadn't seen the warnings in the documentation, this probably could be spun out of this ticket as it is probably a problem in the existing doc - just silent with the current python. I really would like to go to 2.7.3 when it comes out but I'll make a stop 2.7.2. I have a heavy workload this week but I'll try to put the spkg together. I know from sage-on-gentto that there will be some more patching to be done unfortunately although in some case I think that would be just a band aid. So more dependencies may appear :(

I am surprised at the "latin-1" encoding I am defaulting to UTF-8 and even my Changelogs now come correct everywhere.

We need someone with the know how to look at #11986.



---

archive/issue_comments_099471.json:
```json
{
    "body": "Replying to [comment:145 fbissey]:\n> Replying to [comment:144 jdemeyer]:\n> > By the way: Python 2.7.2 was released on June 11th, 2011 so you might as well go for that.\n> \n> sage-5.0 is probably more realistic.\nEspecially since William essentially *defined* sage-5.0 as the release which will contain this ticket.\n\n> I hadn't seen the warnings in the documentation, this probably could be spun out of this ticket as it is probably a problem in the existing doc - just silent with the current python.\nTrue, but I have no idea how Python 2.7 has changed this particular doctest.  It could also be that something changed inside Sphinx or Cython because of Python 2.7.\n\n> I am surprised at the \"latin-1\" encoding I am defaulting to UTF-8 and even my Changelogs now come correct everywhere.\nAnd now you're punished for the rest of your live as a developer because your name is not ASCII (and please don't write \"Francois\", that just looks very wrong).\n\n> We need someone with the know how to look at #11986.\nI *might* have a look, but I don't want to promise anything.  In any case, once #11986 is really the only remaining issue, it will certainly get fixed.",
    "created_at": "2011-11-09T08:39:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99471",
    "user": "jdemeyer"
}
```

Replying to [comment:145 fbissey]:
> Replying to [comment:144 jdemeyer]:
> > By the way: Python 2.7.2 was released on June 11th, 2011 so you might as well go for that.
> 
> sage-5.0 is probably more realistic.
Especially since William essentially *defined* sage-5.0 as the release which will contain this ticket.

> I hadn't seen the warnings in the documentation, this probably could be spun out of this ticket as it is probably a problem in the existing doc - just silent with the current python.
True, but I have no idea how Python 2.7 has changed this particular doctest.  It could also be that something changed inside Sphinx or Cython because of Python 2.7.

> I am surprised at the "latin-1" encoding I am defaulting to UTF-8 and even my Changelogs now come correct everywhere.
And now you're punished for the rest of your live as a developer because your name is not ASCII (and please don't write "Francois", that just looks very wrong).

> We need someone with the know how to look at #11986.
I *might* have a look, but I don't want to promise anything.  In any case, once #11986 is really the only remaining issue, it will certainly get fixed.



---

archive/issue_comments_099472.json:
```json
{
    "body": "All right. Very busy week so far. I am removing the last patch and will spin it in a separate ticket because Steve did more testing and it appears that the test is somewhat random and was only working everywhere the same with python 2.6 by sheer luck. \n\nSteve had a few interesting suggestions for replacing the test but that's clearly another ticket on which we'll forward people who touched that file for comments.",
    "created_at": "2011-11-10T02:53:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99472",
    "user": "fbissey"
}
```

All right. Very busy week so far. I am removing the last patch and will spin it in a separate ticket because Steve did more testing and it appears that the test is somewhat random and was only working everywhere the same with python 2.6 by sheer luck. 

Steve had a few interesting suggestions for replacing the test but that's clearly another ticket on which we'll forward people who touched that file for comments.



---

archive/issue_comments_099473.json:
```json
{
    "body": "I finished updating the spkg to 2.7.2 in a moment of freedom. I called it 2.7.2.p0 as it has some patches in it. Hope all the permissions are right this time. And SPKG.txt is UTF-8 now.\n\nI will need to update one patch and I think add a new one. At least relative to 4.7.2, I am so bogged down in work that I haven't been working at all on 4.8.0 which may require new patches.",
    "created_at": "2011-11-21T00:55:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99473",
    "user": "fbissey"
}
```

I finished updating the spkg to 2.7.2 in a moment of freedom. I called it 2.7.2.p0 as it has some patches in it. Hope all the permissions are right this time. And SPKG.txt is UTF-8 now.

I will need to update one patch and I think add a new one. At least relative to 4.7.2, I am so bogged down in work that I haven't been working at all on 4.8.0 which may require new patches.



---

archive/issue_comments_099474.json:
```json
{
    "body": "fix pure assertErrors failures - updated for python-2.7.2",
    "created_at": "2011-11-24T21:33:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99474",
    "user": "fbissey"
}
```

fix pure assertErrors failures - updated for python-2.7.2



---

archive/issue_comments_099475.json:
```json
{
    "body": "Attachment\n\nfix sage_unittest.py failures - updated for python-2.7.2",
    "created_at": "2011-11-24T21:34:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99475",
    "user": "fbissey"
}
```

Attachment

fix sage_unittest.py failures - updated for python-2.7.2



---

archive/issue_comments_099476.json:
```json
{
    "body": "Attachment\n\nPatch set updated for python-2.7.2.",
    "created_at": "2011-11-24T21:35:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99476",
    "user": "fbissey"
}
```

Attachment

Patch set updated for python-2.7.2.



---

archive/issue_comments_099477.json:
```json
{
    "body": "Replying to [comment:148 fbissey]:\n> I finished updating the spkg to 2.7.2 in a moment of freedom. I called it 2.7.2.p0 as it has some patches in it. Hope all the permissions are right this time.\nUnfortunately, they are not.  I fixed this in [http://boxen.math.washington.edu/home/jdemeyer/spkg/python-2.7.2.p0.spkg](http://boxen.math.washington.edu/home/jdemeyer/spkg/python-2.7.2.p0.spkg)",
    "created_at": "2011-11-25T22:51:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99477",
    "user": "jdemeyer"
}
```

Replying to [comment:148 fbissey]:
> I finished updating the spkg to 2.7.2 in a moment of freedom. I called it 2.7.2.p0 as it has some patches in it. Hope all the permissions are right this time.
Unfortunately, they are not.  I fixed this in [http://boxen.math.washington.edu/home/jdemeyer/spkg/python-2.7.2.p0.spkg](http://boxen.math.washington.edu/home/jdemeyer/spkg/python-2.7.2.p0.spkg)



---

archive/issue_comments_099478.json:
```json
{
    "body": "Replying to [comment:151 jdemeyer]:\n> Replying to [comment:148 fbissey]:\n> > I finished updating the spkg to 2.7.2 in a moment of freedom. I called it 2.7.2.p0 as it has some patches in it. Hope all the permissions are right this time.\n> Unfortunately, they are not.  I fixed this in [http://boxen.math.washington.edu/home/jdemeyer/spkg/python-2.7.2.p0.spkg](http://boxen.math.washington.edu/home/jdemeyer/spkg/python-2.7.2.p0.spkg)\n\nOK. Was it the src folder and its content? Or did I forget something else in the spkg root folder?",
    "created_at": "2011-11-25T23:19:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99478",
    "user": "fbissey"
}
```

Replying to [comment:151 jdemeyer]:
> Replying to [comment:148 fbissey]:
> > I finished updating the spkg to 2.7.2 in a moment of freedom. I called it 2.7.2.p0 as it has some patches in it. Hope all the permissions are right this time.
> Unfortunately, they are not.  I fixed this in [http://boxen.math.washington.edu/home/jdemeyer/spkg/python-2.7.2.p0.spkg](http://boxen.math.washington.edu/home/jdemeyer/spkg/python-2.7.2.p0.spkg)

OK. Was it the src folder and its content? Or did I forget something else in the spkg root folder?



---

archive/issue_comments_099479.json:
```json
{
    "body": "Replying to [comment:153 fbissey]:\n> OK. Was it the src folder and its content?\nYes.  I solved this by doing `chmod ugo+rX -R .`\n\n> Or did I forget something else in the spkg root folder?\nAlso, yes.  spkg-check should be executable.",
    "created_at": "2011-11-25T23:24:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99479",
    "user": "jdemeyer"
}
```

Replying to [comment:153 fbissey]:
> OK. Was it the src folder and its content?
Yes.  I solved this by doing `chmod ugo+rX -R .`

> Or did I forget something else in the spkg root folder?
Also, yes.  spkg-check should be executable.



---

archive/issue_comments_099480.json:
```json
{
    "body": "This fails to build from scratch with sage-4.8.alpha2 on sage.math:\n\n```\ngcc  -pthread -DNDEBUG -g  -O3 -Wall -Wstrict-prototypes -L/scratch/jdemeyer/merger/sage-5.0/local/lib   Parser/acceler.o Parser/grammar1.\no Parser/listnode.o Parser/node.o Parser/parser.o Parser/parsetok.o Parser/bitset.o Parser/metagrammar.o Parser/firstsets.o Parser/grammar\n.o Parser/pgen.o Objects/obmalloc.o Python/mysnprintf.o Python/pyctype.o Parser/tokenizer_pgen.o Parser/printgrammar.o Parser/pgenmain.o -\nlpthread -ldl  -lutil -o Parser/pgen\nParser/pgen ./Grammar/Grammar ./Include/graminit.h ./Python/graminit.c\ntouch Parser/pgen.stamp\ngcc  -pthread -c -fno-strict-aliasing -g -O2 -DNDEBUG -g  -O3 -Wall -Wstrict-prototypes  -I. -IInclude -I./Include -I/scratch/jdemeyer/mer\nger/sage-5.0/local/include  -fPIC -DPy_BUILD_CORE -o Python/ast.o Python/ast.c\ngcc  -pthread -c -fno-strict-aliasing -g -O2 -DNDEBUG -g  -O3 -Wall -Wstrict-prototypes  -I. -IInclude -I./Include -I/scratch/jdemeyer/mer\nger/sage-5.0/local/include  -fPIC -DPy_BUILD_CORE -o Python/compile.o Python/compile.c\ngcc  -pthread -c -fno-strict-aliasing -g -O2 -DNDEBUG -g  -O3 -Wall -Wstrict-prototypes  -I. -IInclude -I./Include -I/scratch/jdemeyer/mer\nger/sage-5.0/local/include  -fPIC -DPy_BUILD_CORE -o Python/graminit.o Python/graminit.c\ngcc  -pthread -c -fno-strict-aliasing -g -O2 -DNDEBUG -g  -O3 -Wall -Wstrict-prototypes  -I. -IInclude -I./Include -I/scratch/jdemeyer/mer\nger/sage-5.0/local/include  -fPIC -DPy_BUILD_CORE -o Python/symtable.o Python/symtable.c\ngcc  -pthread -c -fno-strict-aliasing -g -O2 -DNDEBUG -g  -O3 -Wall -Wstrict-prototypes  -I. -IInclude -I./Include -I/scratch/jdemeyer/mer\nger/sage-5.0/local/include  -fPIC -DPy_BUILD_CORE \\\n              -DSVNVERSION=\"\\\"`LC_ALL=C svnversion .`\\\"\" \\\n              -DHGVERSION=\"\\\"`LC_ALL=C hg id -i .`\\\"\" \\\n              -DHGTAG=\"\\\"`LC_ALL=C hg id -t .`\\\"\" \\\n              -DHGBRANCH=\"\\\"`LC_ALL=C hg id -b .`\\\"\" \\\n              -o Modules/getbuildinfo.o ./Modules/getbuildinfo.c\nYou must compile Sage first using 'make' in the Sage root directory.\nYou must compile Sage first using 'make' in the Sage root directory.\nYou must compile Sage first using 'make' in the Sage root directory.\n<command-line>: warning: missing terminating \" character\n<command-line>:1:7: warning: missing terminating \" character\n<command-line>:2:10: warning: missing terminating \" character\n./Modules/getbuildinfo.c: In function 'Py_GetBuildInfo':\n./Modules/getbuildinfo.c:45: error: missing terminating \" character\n./Modules/getbuildinfo.c:45: error: expected expression before ')' token\n./Modules/getbuildinfo.c:46: error: missing terminating \" character\n./Modules/getbuildinfo.c:46: error: missing terminating \" character\n./Modules/getbuildinfo.c:47: error: missing terminating \" character\n./Modules/getbuildinfo.c:47: error: missing terminating \" character\n./Modules/getbuildinfo.c:53: error: 'buildinfo' undeclared (first use in this function)\n./Modules/getbuildinfo.c:53: error: (Each undeclared identifier is reported only once\n./Modules/getbuildinfo.c:53: error: for each function it appears in.)\n./Modules/getbuildinfo.c: In function '_Py_hgversion':\n./Modules/getbuildinfo.c:72: error: missing terminating \" character\n./Modules/getbuildinfo.c:72: warning: 'return' with no value, in function returning non-void\n./Modules/getbuildinfo.c: In function '_Py_hgidentifier':\n./Modules/getbuildinfo.c:79: error: missing terminating \" character\n./Modules/getbuildinfo.c:79: error: expected expression before ';' token\n./Modules/getbuildinfo.c:83: error: missing terminating \" character\n./Modules/getbuildinfo.c:83: error: expected expression before ';' token\nmake[2]: *** [Modules/getbuildinfo.o] Error 1\nmake[2]: Leaving directory `/mnt/usb1/scratch/jdemeyer/merger/sage-5.0/spkg/build/python-2.7.2.p0/src'\nError building Python.\n```\n\n\nMhy guess would be that `spkg-install` is trying to run Mercurial or something, which obviously fails because Mercurial has not been compiled yet (and it can't since it depends on Python).",
    "created_at": "2011-11-25T23:36:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99480",
    "user": "jdemeyer"
}
```

This fails to build from scratch with sage-4.8.alpha2 on sage.math:

```
gcc  -pthread -DNDEBUG -g  -O3 -Wall -Wstrict-prototypes -L/scratch/jdemeyer/merger/sage-5.0/local/lib   Parser/acceler.o Parser/grammar1.
o Parser/listnode.o Parser/node.o Parser/parser.o Parser/parsetok.o Parser/bitset.o Parser/metagrammar.o Parser/firstsets.o Parser/grammar
.o Parser/pgen.o Objects/obmalloc.o Python/mysnprintf.o Python/pyctype.o Parser/tokenizer_pgen.o Parser/printgrammar.o Parser/pgenmain.o -
lpthread -ldl  -lutil -o Parser/pgen
Parser/pgen ./Grammar/Grammar ./Include/graminit.h ./Python/graminit.c
touch Parser/pgen.stamp
gcc  -pthread -c -fno-strict-aliasing -g -O2 -DNDEBUG -g  -O3 -Wall -Wstrict-prototypes  -I. -IInclude -I./Include -I/scratch/jdemeyer/mer
ger/sage-5.0/local/include  -fPIC -DPy_BUILD_CORE -o Python/ast.o Python/ast.c
gcc  -pthread -c -fno-strict-aliasing -g -O2 -DNDEBUG -g  -O3 -Wall -Wstrict-prototypes  -I. -IInclude -I./Include -I/scratch/jdemeyer/mer
ger/sage-5.0/local/include  -fPIC -DPy_BUILD_CORE -o Python/compile.o Python/compile.c
gcc  -pthread -c -fno-strict-aliasing -g -O2 -DNDEBUG -g  -O3 -Wall -Wstrict-prototypes  -I. -IInclude -I./Include -I/scratch/jdemeyer/mer
ger/sage-5.0/local/include  -fPIC -DPy_BUILD_CORE -o Python/graminit.o Python/graminit.c
gcc  -pthread -c -fno-strict-aliasing -g -O2 -DNDEBUG -g  -O3 -Wall -Wstrict-prototypes  -I. -IInclude -I./Include -I/scratch/jdemeyer/mer
ger/sage-5.0/local/include  -fPIC -DPy_BUILD_CORE -o Python/symtable.o Python/symtable.c
gcc  -pthread -c -fno-strict-aliasing -g -O2 -DNDEBUG -g  -O3 -Wall -Wstrict-prototypes  -I. -IInclude -I./Include -I/scratch/jdemeyer/mer
ger/sage-5.0/local/include  -fPIC -DPy_BUILD_CORE \
              -DSVNVERSION="\"`LC_ALL=C svnversion .`\"" \
              -DHGVERSION="\"`LC_ALL=C hg id -i .`\"" \
              -DHGTAG="\"`LC_ALL=C hg id -t .`\"" \
              -DHGBRANCH="\"`LC_ALL=C hg id -b .`\"" \
              -o Modules/getbuildinfo.o ./Modules/getbuildinfo.c
You must compile Sage first using 'make' in the Sage root directory.
You must compile Sage first using 'make' in the Sage root directory.
You must compile Sage first using 'make' in the Sage root directory.
<command-line>: warning: missing terminating " character
<command-line>:1:7: warning: missing terminating " character
<command-line>:2:10: warning: missing terminating " character
./Modules/getbuildinfo.c: In function 'Py_GetBuildInfo':
./Modules/getbuildinfo.c:45: error: missing terminating " character
./Modules/getbuildinfo.c:45: error: expected expression before ')' token
./Modules/getbuildinfo.c:46: error: missing terminating " character
./Modules/getbuildinfo.c:46: error: missing terminating " character
./Modules/getbuildinfo.c:47: error: missing terminating " character
./Modules/getbuildinfo.c:47: error: missing terminating " character
./Modules/getbuildinfo.c:53: error: 'buildinfo' undeclared (first use in this function)
./Modules/getbuildinfo.c:53: error: (Each undeclared identifier is reported only once
./Modules/getbuildinfo.c:53: error: for each function it appears in.)
./Modules/getbuildinfo.c: In function '_Py_hgversion':
./Modules/getbuildinfo.c:72: error: missing terminating " character
./Modules/getbuildinfo.c:72: warning: 'return' with no value, in function returning non-void
./Modules/getbuildinfo.c: In function '_Py_hgidentifier':
./Modules/getbuildinfo.c:79: error: missing terminating " character
./Modules/getbuildinfo.c:79: error: expected expression before ';' token
./Modules/getbuildinfo.c:83: error: missing terminating " character
./Modules/getbuildinfo.c:83: error: expected expression before ';' token
make[2]: *** [Modules/getbuildinfo.o] Error 1
make[2]: Leaving directory `/mnt/usb1/scratch/jdemeyer/merger/sage-5.0/spkg/build/python-2.7.2.p0/src'
Error building Python.
```


Mhy guess would be that `spkg-install` is trying to run Mercurial or something, which obviously fails because Mercurial has not been compiled yet (and it can't since it depends on Python).



---

archive/issue_comments_099481.json:
```json
{
    "body": "The error above might be fixed by #5852...",
    "created_at": "2011-11-25T23:50:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99481",
    "user": "jdemeyer"
}
```

The error above might be fixed by #5852...



---

archive/issue_comments_099482.json:
```json
{
    "body": "The current spkg installs fine on OS X 10.6 and 10.7, at least when I do \"sage -f ...\" in an existing Sage installation.  I haven't tried building from scratch, and I haven't tried doctests or the patches yet.  Would it be possible to provide a single large patch in addition to the individual small ones?  That would be easier to apply for testing, while the small ones are easier to review.",
    "created_at": "2011-11-26T00:23:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99482",
    "user": "jhpalmieri"
}
```

The current spkg installs fine on OS X 10.6 and 10.7, at least when I do "sage -f ..." in an existing Sage installation.  I haven't tried building from scratch, and I haven't tried doctests or the patches yet.  Would it be possible to provide a single large patch in addition to the individual small ones?  That would be easier to apply for testing, while the small ones are easier to review.



---

archive/issue_comments_099483.json:
```json
{
    "body": "Replying to [comment:154 jdemeyer]:\n> Replying to [comment:153 fbissey]:\n> > OK. Was it the src folder and its content?\n> Yes.  I solved this by doing `chmod ugo+rX -R .`\n> \n> > Or did I forget something else in the spkg root folder?\n> Also, yes.  spkg-check should be executable.\nNever used symbolic mode of chmod, always octal. But this looks like it is more effective to get the directory permissions right. Darn spkg-check.\n\nThanks for the tips. Sorry for being a pest at times.\n\nI haven't tested the spkg from scratch on OSX I did on linux x86_64 and 4.8.alpha2.\nI will see what happens on my 10.5 machine later. 2.7.1 worked from scratch there i am sure. That looks very strange, can you link the full python building log?",
    "created_at": "2011-11-26T00:33:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99483",
    "user": "fbissey"
}
```

Replying to [comment:154 jdemeyer]:
> Replying to [comment:153 fbissey]:
> > OK. Was it the src folder and its content?
> Yes.  I solved this by doing `chmod ugo+rX -R .`
> 
> > Or did I forget something else in the spkg root folder?
> Also, yes.  spkg-check should be executable.
Never used symbolic mode of chmod, always octal. But this looks like it is more effective to get the directory permissions right. Darn spkg-check.

Thanks for the tips. Sorry for being a pest at times.

I haven't tested the spkg from scratch on OSX I did on linux x86_64 and 4.8.alpha2.
I will see what happens on my 10.5 machine later. 2.7.1 worked from scratch there i am sure. That looks very strange, can you link the full python building log?



---

archive/issue_comments_099484.json:
```json
{
    "body": "A build from scratch on OS X 10.6 worked just fine, by the way.",
    "created_at": "2011-11-26T03:28:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99484",
    "user": "jhpalmieri"
}
```

A build from scratch on OS X 10.6 worked just fine, by the way.



---

archive/issue_comments_099485.json:
```json
{
    "body": "There is still the docbuild warning:\n\n```\ndocstring of sage.crypto.boolean_function:3: WARNING: Block quote ends without a blank line; unexpected unindent.\n```\n\nI am investigating.",
    "created_at": "2011-11-26T09:32:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99485",
    "user": "jdemeyer"
}
```

There is still the docbuild warning:

```
docstring of sage.crypto.boolean_function:3: WARNING: Block quote ends without a blank line; unexpected unindent.
```

I am investigating.



---

archive/issue_comments_099486.json:
```json
{
    "body": "I absolutely do not understand the docbuild warning but created a ticket at #12085.",
    "created_at": "2011-11-26T10:07:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99486",
    "user": "jdemeyer"
}
```

I absolutely do not understand the docbuild warning but created a ticket at #12085.



---

archive/issue_comments_099487.json:
```json
{
    "body": "Just an idea! This is because it wants to execute some mercurial commands to find if there are tags in the source. If we were to set \n\n```\nDHGVERSION\nDHGTAG\nDHGBRANCH\n```\n\nTo something or even nothing we may not have this problem. A normal run with a system mercurial installed looks like:\n\n```\nx86_64-pc-linux-gnu-gcc -pthread -c -fno-strict-aliasing -O2 -pipe -march=native -fwrapv -DNDEBUG   -I. -IInclude -I./Include  -fPIC -DPy_BUILD_CORE \\\n      -DSVNVERSION=\"\\\"`LC_ALL=C svnversion .`\\\"\" \\\n      -DHGVERSION=\"\\\"`LC_ALL=C hg id -i .`\\\"\" \\\n      -DHGTAG=\"\\\"`LC_ALL=C hg id -t .`\\\"\" \\\n      -DHGBRANCH=\"\\\"`LC_ALL=C hg id -b .`\\\"\" \\\n      -o Modules/getbuildinfo.o ./Modules/getbuildinfo.c\nabort: repository . not found!\nabort: repository . not found!\nabort: repository . not found!\n```\n\nI will try to see if I can fit that in the spkg.",
    "created_at": "2011-11-26T18:50:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99487",
    "user": "fbissey"
}
```

Just an idea! This is because it wants to execute some mercurial commands to find if there are tags in the source. If we were to set 

```
DHGVERSION
DHGTAG
DHGBRANCH
```

To something or even nothing we may not have this problem. A normal run with a system mercurial installed looks like:

```
x86_64-pc-linux-gnu-gcc -pthread -c -fno-strict-aliasing -O2 -pipe -march=native -fwrapv -DNDEBUG   -I. -IInclude -I./Include  -fPIC -DPy_BUILD_CORE \
      -DSVNVERSION="\"`LC_ALL=C svnversion .`\"" \
      -DHGVERSION="\"`LC_ALL=C hg id -i .`\"" \
      -DHGTAG="\"`LC_ALL=C hg id -t .`\"" \
      -DHGBRANCH="\"`LC_ALL=C hg id -b .`\"" \
      -o Modules/getbuildinfo.o ./Modules/getbuildinfo.c
abort: repository . not found!
abort: repository . not found!
abort: repository . not found!
```

I will try to see if I can fit that in the spkg.



---

archive/issue_comments_099488.json:
```json
{
    "body": "Replying to [comment:163 fbissey]:\n> I will try to see if I can fit that in the spkg.\n\nNo, I would leave that alone.  With #5852, it will build properly.  Since you get errors anyway with the system Mercurial, apparently it's not a problem that `hg` fails.",
    "created_at": "2011-11-26T18:55:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99488",
    "user": "jdemeyer"
}
```

Replying to [comment:163 fbissey]:
> I will try to see if I can fit that in the spkg.

No, I would leave that alone.  With #5852, it will build properly.  Since you get errors anyway with the system Mercurial, apparently it's not a problem that `hg` fails.



---

archive/issue_comments_099489.json:
```json
{
    "body": "If you insist but it would be easy to path Makefile.pre.in to prevent this from happening. It is mainly used to get pre-release version info if you checked out python source from hg. It is supposed to fail if you are using a properly released tarball.",
    "created_at": "2011-11-26T19:03:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99489",
    "user": "fbissey"
}
```

If you insist but it would be easy to path Makefile.pre.in to prevent this from happening. It is mainly used to get pre-release version info if you checked out python source from hg. It is supposed to fail if you are using a properly released tarball.



---

archive/issue_comments_099490.json:
```json
{
    "body": "Replying to [comment:165 fbissey]:\n> If you insist\nI will **not** insist: if you want to make the patch, go ahead.",
    "created_at": "2011-11-26T19:53:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99490",
    "user": "jdemeyer"
}
```

Replying to [comment:165 fbissey]:
> If you insist
I will **not** insist: if you want to make the patch, go ahead.



---

archive/issue_comments_099491.json:
```json
{
    "body": "I may try something more subtle first. Makefile.pre.in has\n\n```\nSVNVERSION=\t@SVNVERSION@\nHGVERSION=\t@HGVERSION@\nHGTAG=\t\t@HGTAG@\nHGBRANCH=\t@HGBRANCH@\n```\n\nand\n\n```\n\t$(CC) -c $(PY_CFLAGS) \\\n\t      -DSVNVERSION=\"\\\"`LC_ALL=C $(SVNVERSION)`\\\"\" \\\n\t      -DHGVERSION=\"\\\"`LC_ALL=C $(HGVERSION)`\\\"\" \\\n\t      -DHGTAG=\"\\\"`LC_ALL=C $(HGTAG)`\\\"\" \\\n\t      -DHGBRANCH=\"\\\"`LC_ALL=C $(HGBRANCH)`\\\"\" \\\n\t      -o $@ $(srcdir)/Modules/getbuildinfo.c\n```\n\nlater so exporting HG* to something like /bin/true on non-windows OS would presumably solve the problem. But just patching to pass empty strings in the later would probably be safe everywhere.",
    "created_at": "2011-11-26T20:51:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99491",
    "user": "fbissey"
}
```

I may try something more subtle first. Makefile.pre.in has

```
SVNVERSION=	@SVNVERSION@
HGVERSION=	@HGVERSION@
HGTAG=		@HGTAG@
HGBRANCH=	@HGBRANCH@
```

and

```
	$(CC) -c $(PY_CFLAGS) \
	      -DSVNVERSION="\"`LC_ALL=C $(SVNVERSION)`\"" \
	      -DHGVERSION="\"`LC_ALL=C $(HGVERSION)`\"" \
	      -DHGTAG="\"`LC_ALL=C $(HGTAG)`\"" \
	      -DHGBRANCH="\"`LC_ALL=C $(HGBRANCH)`\"" \
	      -o $@ $(srcdir)/Modules/getbuildinfo.c
```

later so exporting HG* to something like /bin/true on non-windows OS would presumably solve the problem. But just patching to pass empty strings in the later would probably be safe everywhere.



---

archive/issue_comments_099492.json:
```json
{
    "body": "The first patch doesn't apply in 4.8.alpha3 because of the changes in #12047. New patches will come some. There may be other surprises.",
    "created_at": "2011-12-05T02:18:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99492",
    "user": "fbissey"
}
```

The first patch doesn't apply in 4.8.alpha3 because of the changes in #12047. New patches will come some. There may be other surprises.



---

archive/issue_comments_099493.json:
```json
{
    "body": "Updated the first patch. Haven't been able to test things to find any new problems yet.",
    "created_at": "2011-12-05T11:04:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99493",
    "user": "fbissey"
}
```

Updated the first patch. Haven't been able to test things to find any new problems yet.



---

archive/issue_comments_099494.json:
```json
{
    "body": "There are a few test failures on a Pentium 4 32-bit Linux system with sage-4.8.alpha2 + #9958 + #11986:\n\n```\nsage -t  --long -force_lib devel/sage/sage/combinat/words/suffix_trees.py\n**********************************************************************\nFile \"/home/jdemeyer/sage-5.0/devel/sage-main/sage/combinat/words/suffix_trees.py\", line 1323:\n    sage: t.trie_type_dict() == dict([[(0, W(\"a\")), 4], [(0, W(\"b\")), 3], [(3, W(\"a\")), 2], [(4, W(\"b\")), 5], [(5, W(\"a\")), 1]])\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nsage -t  --long -force_lib devel/sage/sage/misc/randstate.pyx\n**********************************************************************\nFile \"/home/jdemeyer/sage-5.0/devel/sage-main/sage/misc/randstate.pyx\", line 61:\n    sage: rtest()\nExpected:\n    (978, 0.184109262667515, -3*x^2 - 1/12, (4,5), [ 0, 1, 1, 0, 0 ], 1161603091, 60359, 0.83350776541997362)\nGot:\n    (978, 0.184109262667515, -3*x^2 - 1/12, (4,5), [ 0, 1, 1, 0, 0 ], 1161603091, 60359, 0.8335077654199736)\n**********************************************************************\nsage -t  --long -force_lib devel/sage/sage/combinat/words/nfactor_enumerable_word.py\n**********************************************************************\nFile \"/home/jdemeyer/sage-5.0/devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py\", line 20:\n    sage: it.next()\nExpected:\n    word: 6456\nGot:\n    word: 4564\n**********************************************************************\nFile \"/home/jdemeyer/sage-5.0/devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py\", line 23:\n    sage: it.next()\nExpected:\n    word: 5645\nGot:\n    word: 6456\n**********************************************************************\nFile \"/home/jdemeyer/sage-5.0/devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py\", line 26:\n    sage: it.next()\nExpected:\n    word: 4564\nGot:\n    word: 5645\n**********************************************************************\n```\n",
    "created_at": "2011-12-05T11:25:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99494",
    "user": "jdemeyer"
}
```

There are a few test failures on a Pentium 4 32-bit Linux system with sage-4.8.alpha2 + #9958 + #11986:

```
sage -t  --long -force_lib devel/sage/sage/combinat/words/suffix_trees.py
**********************************************************************
File "/home/jdemeyer/sage-5.0/devel/sage-main/sage/combinat/words/suffix_trees.py", line 1323:
    sage: t.trie_type_dict() == dict([[(0, W("a")), 4], [(0, W("b")), 3], [(3, W("a")), 2], [(4, W("b")), 5], [(5, W("a")), 1]])
Expected:
    True
Got:
    False
**********************************************************************
sage -t  --long -force_lib devel/sage/sage/misc/randstate.pyx
**********************************************************************
File "/home/jdemeyer/sage-5.0/devel/sage-main/sage/misc/randstate.pyx", line 61:
    sage: rtest()
Expected:
    (978, 0.184109262667515, -3*x^2 - 1/12, (4,5), [ 0, 1, 1, 0, 0 ], 1161603091, 60359, 0.83350776541997362)
Got:
    (978, 0.184109262667515, -3*x^2 - 1/12, (4,5), [ 0, 1, 1, 0, 0 ], 1161603091, 60359, 0.8335077654199736)
**********************************************************************
sage -t  --long -force_lib devel/sage/sage/combinat/words/nfactor_enumerable_word.py
**********************************************************************
File "/home/jdemeyer/sage-5.0/devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py", line 20:
    sage: it.next()
Expected:
    word: 6456
Got:
    word: 4564
**********************************************************************
File "/home/jdemeyer/sage-5.0/devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py", line 23:
    sage: it.next()
Expected:
    word: 5645
Got:
    word: 6456
**********************************************************************
File "/home/jdemeyer/sage-5.0/devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py", line 26:
    sage: it.next()
Expected:
    word: 4564
Got:
    word: 5645
**********************************************************************
```




---

archive/issue_comments_099495.json:
```json
{
    "body": "I have made a patch for the Integer hashing, see #11986.",
    "created_at": "2011-12-05T11:26:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99495",
    "user": "jdemeyer"
}
```

I have made a patch for the Integer hashing, see #11986.



---

archive/issue_comments_099496.json:
```json
{
    "body": "I have seen your patch in #11986 that's a good rewrite of the hashing in question, the -1 bit is particularly tricky. I mentioned it before but we probably need a different approach for combinat/words/nfactor_enumerable_word.py, the sequence is pretty much random depending on arch and other factors it seems. The randstate.pyx must have escaped [http://trac.sagemath.org/sage_trac/attachment/ticket/9958/trac_9958-fixing_numericalnoise-part4.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/9958/trac_9958-fixing_numericalnoise-part4.patch) because the test results are identical to some performed later in the same file. I'll correct that shortly. \n\nThe suffix_trees.pyx rings a bell but I cannot remember where and when.",
    "created_at": "2011-12-05T11:48:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99496",
    "user": "fbissey"
}
```

I have seen your patch in #11986 that's a good rewrite of the hashing in question, the -1 bit is particularly tricky. I mentioned it before but we probably need a different approach for combinat/words/nfactor_enumerable_word.py, the sequence is pretty much random depending on arch and other factors it seems. The randstate.pyx must have escaped [http://trac.sagemath.org/sage_trac/attachment/ticket/9958/trac_9958-fixing_numericalnoise-part4.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/9958/trac_9958-fixing_numericalnoise-part4.patch) because the test results are identical to some performed later in the same file. I'll correct that shortly. 

The suffix_trees.pyx rings a bell but I cannot remember where and when.



---

archive/issue_comments_099497.json:
```json
{
    "body": "ha [http://trac.sagemath.org/sage_trac/ticket/9958#comment:18](http://trac.sagemath.org/sage_trac/ticket/9958#comment:18) is where I had suffix_trees.pyx before. I don't have a 32 bit linux box anymore so it is more difficult. I note they were two you only see one now.",
    "created_at": "2011-12-05T11:51:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99497",
    "user": "fbissey"
}
```

ha [http://trac.sagemath.org/sage_trac/ticket/9958#comment:18](http://trac.sagemath.org/sage_trac/ticket/9958#comment:18) is where I had suffix_trees.pyx before. I don't have a 32 bit linux box anymore so it is more difficult. I note they were two you only see one now.



---

archive/issue_comments_099498.json:
```json
{
    "body": "I need a kind soul with 32 bit linux system to explore the suffix tree issue, the doctest is as follow:\n\n```\n            sage: from sage.combinat.words.suffix_trees import ImplicitSuffixTree, SuffixTrie\n            sage: W = Words(\"ab\")\n            sage: t = ImplicitSuffixTree(W(\"aba\"))\n            sage: t.trie_type_dict() == dict([[(0, W(\"a\")), 4], [(0, W(\"b\")), 3], [(3, W(\"a\")), 2], [(4, W(\"b\")), 5], [(5, W(\"a\")), 1]])\n            True\n```\n\nIt would be helpful to get the values of \"W\", \"t\" and \"t.trie_type_dict()\" on python-2.6 and 2.7. Then we can make a decision on whether the answer we get with python-2.7 is equivalent to the current output or not.",
    "created_at": "2011-12-05T21:18:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99498",
    "user": "fbissey"
}
```

I need a kind soul with 32 bit linux system to explore the suffix tree issue, the doctest is as follow:

```
            sage: from sage.combinat.words.suffix_trees import ImplicitSuffixTree, SuffixTrie
            sage: W = Words("ab")
            sage: t = ImplicitSuffixTree(W("aba"))
            sage: t.trie_type_dict() == dict([[(0, W("a")), 4], [(0, W("b")), 3], [(3, W("a")), 2], [(4, W("b")), 5], [(5, W("a")), 1]])
            True
```

It would be helpful to get the values of "W", "t" and "t.trie_type_dict()" on python-2.6 and 2.7. Then we can make a decision on whether the answer we get with python-2.7 is equivalent to the current output or not.



---

archive/issue_comments_099499.json:
```json
{
    "body": "Here (x86) with sage-4.8.alpha3 + #9958 + #11986 the suffix_trees test passes:\n\n\n```\n./sage -t  -long -force_lib devel/sage/sage/combinat/words/suffix_trees.py\nsage -t -long -force_lib \"devel/sage/sage/combinat/words/suffix_trees.py\"\n         [5.1 s]\n \n----------------------------------------------------------------------\nAll tests passed!\n```\n\n\nThe requested values are:\n\n\n```\nsage: W\nWords over Ordered Alphabet ['a', 'b']\nsage: t\nImplicit Suffix Tree of the word: aba\nsage: t.trie_type_dict()\n{(4, word: b): 5, (0, word: a): 4, (0, word: b): 3, (5, word: a): 1, (3, word: a): 2}\n```\n\n\nFWIW, on amd64 the test fails with the same sage-4.8.alpha3 + #9958 + #11986",
    "created_at": "2011-12-05T21:57:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99499",
    "user": "strogdon"
}
```

Here (x86) with sage-4.8.alpha3 + #9958 + #11986 the suffix_trees test passes:


```
./sage -t  -long -force_lib devel/sage/sage/combinat/words/suffix_trees.py
sage -t -long -force_lib "devel/sage/sage/combinat/words/suffix_trees.py"
         [5.1 s]
 
----------------------------------------------------------------------
All tests passed!
```


The requested values are:


```
sage: W
Words over Ordered Alphabet ['a', 'b']
sage: t
Implicit Suffix Tree of the word: aba
sage: t.trie_type_dict()
{(4, word: b): 5, (0, word: a): 4, (0, word: b): 3, (5, word: a): 1, (3, word: a): 2}
```


FWIW, on amd64 the test fails with the same sage-4.8.alpha3 + #9958 + #11986



---

archive/issue_comments_099500.json:
```json
{
    "body": "On sage.math (x86_64 Linux), sage-4.8.alpha3 + #12106 (unrelated) + #9958 + #11986 gives errors in two files:\n\n```\nsage -t  -force_lib devel/sage/sage/matrix/matrix_mod2e_dense.pyx\n**********************************************************************\nFile \"/mnt/usb1/scratch/jdemeyer/merger/sage-5.0/devel/sage-main/sage/matrix/matrix_mod2e_dense.pyx\", line 790:\n    sage: float(A.density())\nExpected:\n    0.099738...\nGot:\n    0.099739\n**********************************************************************\nFile \"/mnt/usb1/scratch/jdemeyer/merger/sage-5.0/devel/sage-main/sage/matrix/matrix_mod2e_dense.pyx\", line 798:\n    sage: float(A.density())\nExpected:\n    0.499759...\nGot:\n    0.49976\n**********************************************************************\n```\n\n(related ticket: #9562)\nand\n\n```\nsage -t  -force_lib devel/sage/sage/gsl/integration.pyx\n**********************************************************************\nFile \"/mnt/usb1/scratch/jdemeyer/merger/sage-5.0/devel/sage-main/sage/gsl/integration.pyx\", line 110:\n    sage: numerical_integral(x^2, 0, 1, max_points=100)\nExpected:\n    (0.33333333333333331, 3.7007434154171879e-15)\nGot:\n    (0.3333333333333333, 3.700743415417188e-15)\n**********************************************************************\nFile \"/mnt/usb1/scratch/jdemeyer/merger/sage-5.0/devel/sage-main/sage/gsl/integration.pyx\", line 115:\n    sage: numerical_integral(sin(x)^3 + sin(x),  0, pi)\nExpected:\n    (3.333333333333333, 3.7007434154171883e-14)\nGot:\n    (3.333333333333333, 3.700743415417188e-14)\n**********************************************************************\nFile \"/mnt/usb1/scratch/jdemeyer/merger/sage-5.0/devel/sage-main/sage/gsl/integration.pyx\", line 120:\n    sage: numerical_integral(lambda x: sin(x)^3 + sin(x),  0, pi)\nExpected:\n    (3.333333333333333, 3.7007434154171883e-14)\nGot:\n    (3.333333333333333, 3.700743415417188e-14)\n**********************************************************************\nFile \"/mnt/usb1/scratch/jdemeyer/merger/sage-5.0/devel/sage-main/sage/gsl/integration.pyx\", line 131:\n    sage: numerical_integral(f, 0, 1, max_points=200, eps_abs=1e-7, eps_rel=1e-7, rule=4)\nExpected:\n    (0.33333333333333331, 3.7007434154171879e-15)\nGot:\n    (0.3333333333333333, 3.700743415417188e-15)\n**********************************************************************\nFile \"/mnt/usb1/scratch/jdemeyer/merger/sage-5.0/devel/sage-main/sage/gsl/integration.pyx\", line 172:\n    sage: exp(-1/x).nintegral(x, 1, 2)  # via maxima\nExpected:\n    (0.50479221787318396, 5.6043194293440752e-15, 21, 0)\nGot:\n    (0.504792217873184, 5.604319429344075e-15, 21, 0)\n**********************************************************************\n```\n\n(related ticket: #12047)\n\nAlso, the spkg should be rebased to #12096.",
    "created_at": "2011-12-05T22:20:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99500",
    "user": "jdemeyer"
}
```

On sage.math (x86_64 Linux), sage-4.8.alpha3 + #12106 (unrelated) + #9958 + #11986 gives errors in two files:

```
sage -t  -force_lib devel/sage/sage/matrix/matrix_mod2e_dense.pyx
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/merger/sage-5.0/devel/sage-main/sage/matrix/matrix_mod2e_dense.pyx", line 790:
    sage: float(A.density())
Expected:
    0.099738...
Got:
    0.099739
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/merger/sage-5.0/devel/sage-main/sage/matrix/matrix_mod2e_dense.pyx", line 798:
    sage: float(A.density())
Expected:
    0.499759...
Got:
    0.49976
**********************************************************************
```

(related ticket: #9562)
and

```
sage -t  -force_lib devel/sage/sage/gsl/integration.pyx
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/merger/sage-5.0/devel/sage-main/sage/gsl/integration.pyx", line 110:
    sage: numerical_integral(x^2, 0, 1, max_points=100)
Expected:
    (0.33333333333333331, 3.7007434154171879e-15)
Got:
    (0.3333333333333333, 3.700743415417188e-15)
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/merger/sage-5.0/devel/sage-main/sage/gsl/integration.pyx", line 115:
    sage: numerical_integral(sin(x)^3 + sin(x),  0, pi)
Expected:
    (3.333333333333333, 3.7007434154171883e-14)
Got:
    (3.333333333333333, 3.700743415417188e-14)
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/merger/sage-5.0/devel/sage-main/sage/gsl/integration.pyx", line 120:
    sage: numerical_integral(lambda x: sin(x)^3 + sin(x),  0, pi)
Expected:
    (3.333333333333333, 3.7007434154171883e-14)
Got:
    (3.333333333333333, 3.700743415417188e-14)
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/merger/sage-5.0/devel/sage-main/sage/gsl/integration.pyx", line 131:
    sage: numerical_integral(f, 0, 1, max_points=200, eps_abs=1e-7, eps_rel=1e-7, rule=4)
Expected:
    (0.33333333333333331, 3.7007434154171879e-15)
Got:
    (0.3333333333333333, 3.700743415417188e-15)
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/merger/sage-5.0/devel/sage-main/sage/gsl/integration.pyx", line 172:
    sage: exp(-1/x).nintegral(x, 1, 2)  # via maxima
Expected:
    (0.50479221787318396, 5.6043194293440752e-15, 21, 0)
Got:
    (0.504792217873184, 5.604319429344075e-15, 21, 0)
**********************************************************************
```

(related ticket: #12047)

Also, the spkg should be rebased to #12096.



---

archive/issue_comments_099501.json:
```json
{
    "body": "I get on 32-bit i386 Linux with sage-4.8.alpha2 + various patches including #9958:\n\n```\nsage: from sage.combinat.words.suffix_trees import ImplicitSuffixTree, SuffixTrie\nsage: W = Words(\"ab\")\nsage: t = ImplicitSuffixTree(W(\"aba\"))\nsage: W\nWords over Ordered Alphabet ['a', 'b']\nsage: t\nImplicit Suffix Tree of the word: aba\nsage: t.trie_type_dict()\n{(4, word: a): 1, (0, word: b): 5, (0, word: a): 3, (5, word: a): 2, (3, word: b): 4}\n```\n",
    "created_at": "2011-12-05T22:24:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99501",
    "user": "jdemeyer"
}
```

I get on 32-bit i386 Linux with sage-4.8.alpha2 + various patches including #9958:

```
sage: from sage.combinat.words.suffix_trees import ImplicitSuffixTree, SuffixTrie
sage: W = Words("ab")
sage: t = ImplicitSuffixTree(W("aba"))
sage: W
Words over Ordered Alphabet ['a', 'b']
sage: t
Implicit Suffix Tree of the word: aba
sage: t.trie_type_dict()
{(4, word: a): 1, (0, word: b): 5, (0, word: a): 3, (5, word: a): 2, (3, word: b): 4}
```




---

archive/issue_comments_099502.json:
```json
{
    "body": "thanks for all that feedback. I knew there would be new stuff. I unfortunately (like all of us) not enough time to do things in a speedy fashion. I am bogged down as well with the sage-on-gentoo version of alpha3 not wanting to play nice with #4260 [https://github.com/cschwan/sage-on-gentoo/issues/108](https://github.com/cschwan/sage-on-gentoo/issues/108) and it annoys me.",
    "created_at": "2011-12-05T22:52:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99502",
    "user": "fbissey"
}
```

thanks for all that feedback. I knew there would be new stuff. I unfortunately (like all of us) not enough time to do things in a speedy fashion. I am bogged down as well with the sage-on-gentoo version of alpha3 not wanting to play nice with #4260 [https://github.com/cschwan/sage-on-gentoo/issues/108](https://github.com/cschwan/sage-on-gentoo/issues/108) and it annoys me.



---

archive/issue_comments_099503.json:
```json
{
    "body": "Replying to [comment:180 fbissey]:\n> I am bogged down as well with the sage-on-gentoo version of alpha3 not wanting to play nice with #4260 [https://github.com/cschwan/sage-on-gentoo/issues/108](https://github.com/cschwan/sage-on-gentoo/issues/108) and it annoys me.\n\nDoes vanilla Sage build and run on that same machine with the same compiler?  Be sure to try a different gcc version, Linbox seems to be sensitive to that.",
    "created_at": "2011-12-05T22:59:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99503",
    "user": "jdemeyer"
}
```

Replying to [comment:180 fbissey]:
> I am bogged down as well with the sage-on-gentoo version of alpha3 not wanting to play nice with #4260 [https://github.com/cschwan/sage-on-gentoo/issues/108](https://github.com/cschwan/sage-on-gentoo/issues/108) and it annoys me.

Does vanilla Sage build and run on that same machine with the same compiler?  Be sure to try a different gcc version, Linbox seems to be sensitive to that.



---

archive/issue_comments_099504.json:
```json
{
    "body": "On x86 with sage-4.8.alpha3 + #9958 + #11986 I have the following failures:\n\n\n```\nsage -t -long  -force_lib devel/sage-main/sage/gsl/integration.pyx\n**********************************************************************\nFile \"/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/gsl/integration.pyx\", line 110:\n    sage: numerical_integral(x^2, 0, 1, max_points=100)\nExpected:\n    (0.33333333333333331, 3.7007434154171879e-15)\nGot:\n    (0.3333333333333333, 3.700743415417188e-15)\n**********************************************************************\nFile \"/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/gsl/integration.pyx\", line 115:\n    sage: numerical_integral(sin(x)^3 + sin(x),  0, pi)\nExpected:\n    (3.333333333333333, 3.7007434154171883e-14)\nGot:\n    (3.333333333333333, 3.700743415417188e-14)\n**********************************************************************\nFile \"/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/gsl/integration.pyx\", line 120:\n    sage: numerical_integral(lambda x: sin(x)^3 + sin(x),  0, pi)\nExpected:\n    (3.333333333333333, 3.7007434154171883e-14)\nGot:\n    (3.333333333333333, 3.700743415417188e-14)\n**********************************************************************\nFile \"/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/gsl/integration.pyx\", line 131:\n    sage: numerical_integral(f, 0, 1, max_points=200, eps_abs=1e-7, eps_rel=1e-7, rule=4)\nExpected:\n    (0.33333333333333331, 3.7007434154171879e-15)\nGot:\n    (0.3333333333333333, 3.700743415417188e-15)\n**********************************************************************\nFile \"/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/gsl/integration.pyx\", line 172:\n    sage: exp(-1/x).nintegral(x, 1, 2)  # via maxima\nExpected:\n    (0.50479221787318396, 5.6043194293440752e-15, 21, 0)\nGot:\n    (0.504792217873184, 5.604319429344075e-15, 21, 0)\n**********************************************************************\n```\n\n\n```\nsage -t -long  -force_lib devel/sage-main/sage/misc/randstate.pyx\n**********************************************************************\nFile \"/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/misc/randstate.pyx\", line 61:\n    sage: rtest()\nExpected:\n    (978, 0.184109262667515, -3*x^2 - 1/12, (4,5), [ 0, 1, 1, 0, 0 ], 1161603091, 60359, 0.83350776541997362)\nGot:\n    (978, 0.184109262667515, -3*x^2 - 1/12, (4,5), [ 0, 1, 1, 0, 0 ], 1161603091, 60359, 0.8335077654199736)\n**********************************************************************\n```\n\n\n```\nsage -t -long  -force_lib devel/sage-main/sage/matrix/matrix_mod2e_dense.pyx\n**********************************************************************\nFile \"/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/matrix/matrix_mod2e_dense.pyx\", line 790:\n    sage: float(A.density())\nExpected:\n    0.099738...\nGot:\n    0.099739\n**********************************************************************\nFile \"/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/matrix/matrix_mod2e_dense.pyx\", line 798:\n    sage: float(A.density())\nExpected:\n    0.499759...\nGot:\n    0.49976\n**********************************************************************\n```\n\n\n```\nsage -t -long  -force_lib devel/sage-main/sage/functions/transcendental.py\n**********************************************************************\nFile \"/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/functions/transcendental.py\", line 80:\n    sage: w = exponential_integral_1(2,4); w\nExpected:\n    [0.04890051070806112, 0.0037793524098489067, 0.00036008245216265873, 3.7665622843924751e-05]\nGot:\n    [0.04890051070806112, 0.0037793524098489067, 0.00036008245216265873, 3.766562284392475e-05]\n**********************************************************************\n```\n",
    "created_at": "2011-12-05T23:09:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99504",
    "user": "strogdon"
}
```

On x86 with sage-4.8.alpha3 + #9958 + #11986 I have the following failures:


```
sage -t -long  -force_lib devel/sage-main/sage/gsl/integration.pyx
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/gsl/integration.pyx", line 110:
    sage: numerical_integral(x^2, 0, 1, max_points=100)
Expected:
    (0.33333333333333331, 3.7007434154171879e-15)
Got:
    (0.3333333333333333, 3.700743415417188e-15)
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/gsl/integration.pyx", line 115:
    sage: numerical_integral(sin(x)^3 + sin(x),  0, pi)
Expected:
    (3.333333333333333, 3.7007434154171883e-14)
Got:
    (3.333333333333333, 3.700743415417188e-14)
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/gsl/integration.pyx", line 120:
    sage: numerical_integral(lambda x: sin(x)^3 + sin(x),  0, pi)
Expected:
    (3.333333333333333, 3.7007434154171883e-14)
Got:
    (3.333333333333333, 3.700743415417188e-14)
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/gsl/integration.pyx", line 131:
    sage: numerical_integral(f, 0, 1, max_points=200, eps_abs=1e-7, eps_rel=1e-7, rule=4)
Expected:
    (0.33333333333333331, 3.7007434154171879e-15)
Got:
    (0.3333333333333333, 3.700743415417188e-15)
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/gsl/integration.pyx", line 172:
    sage: exp(-1/x).nintegral(x, 1, 2)  # via maxima
Expected:
    (0.50479221787318396, 5.6043194293440752e-15, 21, 0)
Got:
    (0.504792217873184, 5.604319429344075e-15, 21, 0)
**********************************************************************
```


```
sage -t -long  -force_lib devel/sage-main/sage/misc/randstate.pyx
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/misc/randstate.pyx", line 61:
    sage: rtest()
Expected:
    (978, 0.184109262667515, -3*x^2 - 1/12, (4,5), [ 0, 1, 1, 0, 0 ], 1161603091, 60359, 0.83350776541997362)
Got:
    (978, 0.184109262667515, -3*x^2 - 1/12, (4,5), [ 0, 1, 1, 0, 0 ], 1161603091, 60359, 0.8335077654199736)
**********************************************************************
```


```
sage -t -long  -force_lib devel/sage-main/sage/matrix/matrix_mod2e_dense.pyx
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/matrix/matrix_mod2e_dense.pyx", line 790:
    sage: float(A.density())
Expected:
    0.099738...
Got:
    0.099739
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/matrix/matrix_mod2e_dense.pyx", line 798:
    sage: float(A.density())
Expected:
    0.499759...
Got:
    0.49976
**********************************************************************
```


```
sage -t -long  -force_lib devel/sage-main/sage/functions/transcendental.py
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/functions/transcendental.py", line 80:
    sage: w = exponential_integral_1(2,4); w
Expected:
    [0.04890051070806112, 0.0037793524098489067, 0.00036008245216265873, 3.7665622843924751e-05]
Got:
    [0.04890051070806112, 0.0037793524098489067, 0.00036008245216265873, 3.766562284392475e-05]
**********************************************************************
```




---

archive/issue_comments_099505.json:
```json
{
    "body": "I now understand why you removed the transcendental patch Jereon some bits ended in my revised trac_9958-fixing_numericalnoise-part1_p2.patch when they shouldn't have. That's what is happening to Steve. I will rectify that. \n\nI removed the gsl bits because of #12047 so that has to be redone.\n\nAnd I haven't had time to try vanilla yet but it is on my TODO list and I suspect g++ too.",
    "created_at": "2011-12-06T00:43:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99505",
    "user": "fbissey"
}
```

I now understand why you removed the transcendental patch Jereon some bits ended in my revised trac_9958-fixing_numericalnoise-part1_p2.patch when they shouldn't have. That's what is happening to Steve. I will rectify that. 

I removed the gsl bits because of #12047 so that has to be redone.

And I haven't had time to try vanilla yet but it is on my TODO list and I suspect g++ too.



---

archive/issue_comments_099506.json:
```json
{
    "body": "fixing numerical noise part 1 - updated for 4.8.alpha3",
    "created_at": "2011-12-06T00:53:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99506",
    "user": "fbissey"
}
```

fixing numerical noise part 1 - updated for 4.8.alpha3



---

archive/issue_comments_099507.json:
```json
{
    "body": "Attachment\n\nupdated the first patch and readded the transcendental patch to the list.",
    "created_at": "2011-12-06T00:55:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99507",
    "user": "fbissey"
}
```

Attachment

updated the first patch and readded the transcendental patch to the list.



---

archive/issue_comments_099508.json:
```json
{
    "body": "For suffix_tree it looks like your two values don't agree:\n\n```\n{(4, word: a): 1, (0, word: b): 5, (0, word: a): 3, (5, word: a): 2, (3, word: b): 4}\n{(4, word: b): 5, (0, word: a): 4, (0, word: b): 3, (5, word: a): 1, (3, word: a): 2}\n```\n\nIf we add that I don't see it on OS X x86 that looks bad. I also have an x86_64 machine where the value is the same as Jeroen and the test fails. Steve get the right value on the other hand so there is something going there.",
    "created_at": "2011-12-06T01:35:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99508",
    "user": "fbissey"
}
```

For suffix_tree it looks like your two values don't agree:

```
{(4, word: a): 1, (0, word: b): 5, (0, word: a): 3, (5, word: a): 2, (3, word: b): 4}
{(4, word: b): 5, (0, word: a): 4, (0, word: b): 3, (5, word: a): 1, (3, word: a): 2}
```

If we add that I don't see it on OS X x86 that looks bad. I also have an x86_64 machine where the value is the same as Jeroen and the test fails. Steve get the right value on the other hand so there is something going there.



---

archive/issue_comments_099509.json:
```json
{
    "body": "Attachment\n\nfix numerical noise in gsl/integration.pyx",
    "created_at": "2011-12-06T01:37:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99509",
    "user": "fbissey"
}
```

Attachment

fix numerical noise in gsl/integration.pyx



---

archive/issue_comments_099510.json:
```json
{
    "body": "Attachment\n\nfix numerical noise introduced by m4rie",
    "created_at": "2011-12-06T01:38:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99510",
    "user": "fbissey"
}
```

Attachment

fix numerical noise introduced by m4rie



---

archive/issue_comments_099511.json:
```json
{
    "body": "Added two new patches for gsl integration and m4rie tickets merged in 4.8.alpha3.",
    "created_at": "2011-12-06T01:40:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99511",
    "user": "fbissey"
}
```

Added two new patches for gsl integration and m4rie tickets merged in 4.8.alpha3.



---

archive/issue_comments_099512.json:
```json
{
    "body": "Rebased the spkg against #12096.",
    "created_at": "2011-12-06T03:41:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99512",
    "user": "fbissey"
}
```

Rebased the spkg against #12096.



---

archive/issue_comments_099513.json:
```json
{
    "body": "Attachment\n\nDiff for the Python spkg, for review only",
    "created_at": "2011-12-06T08:43:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99513",
    "user": "jdemeyer"
}
```

Attachment

Diff for the Python spkg, for review only



---

archive/issue_comments_099514.json:
```json
{
    "body": "Everything passes against sage-4.8.alpha3 on 64bit.  Yay!",
    "created_at": "2011-12-06T17:19:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99514",
    "user": "jdemeyer"
}
```

Everything passes against sage-4.8.alpha3 on 64bit.  Yay!



---

archive/issue_comments_099515.json:
```json
{
    "body": "I forgot to add a new bit for randstate.pyx on 32 bit. I'll do that later but I know it is missing. Should we involve someone from combinatronics to get to the bottom of suffix_tree and nfactor_enumerate_word?",
    "created_at": "2011-12-06T19:45:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99515",
    "user": "fbissey"
}
```

I forgot to add a new bit for randstate.pyx on 32 bit. I'll do that later but I know it is missing. Should we involve someone from combinatronics to get to the bottom of suffix_tree and nfactor_enumerate_word?



---

archive/issue_comments_099516.json:
```json
{
    "body": "Replying to [comment:189 fbissey]:\n> Should we involve someone from combinatronics to get to the bottom of suffix_tree and nfactor_enumerate_word?\nSounds good, try to send an email to sage-devel.",
    "created_at": "2011-12-06T19:55:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99516",
    "user": "jdemeyer"
}
```

Replying to [comment:189 fbissey]:
> Should we involve someone from combinatronics to get to the bottom of suffix_tree and nfactor_enumerate_word?
Sounds good, try to send an email to sage-devel.



---

archive/issue_comments_099517.json:
```json
{
    "body": "For the sake of completeness, I now have\n\n32bit: one failure\n\n\n```\nsage -t -long  -force_lib devel/sage-main/sage/misc/randstate.pyx\n```\n\nwhich was mentioned above.\n\n64bit: two failures\n\n\n```\n\nsage -t -long  -force_lib devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py\n**********************************************************************\nFile \"/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/combinat/words/nfactor_enumerable\n_word.py\", line 20:\n    sage: it.next()\nExpected:\n    word: 5645\nGot:\n    word: 4564\n**********************************************************************\nFile \"/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/combinat/words/nfactor_enumerable\n_word.py\", line 23:\n    sage: it.next()\nExpected:\n    word: 6456\nGot:\n    word: 5645\n**********************************************************************\nFile \"/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/combinat/words/nfactor_enumerable\n_word.py\", line 26:\n    sage: it.next()\nExpected:\n    word: 4564\nGot:\n    word: 6456\n**********************************************************************\n\n\nsage -t -long  -force_lib devel/sage-main/sage/combinat/words/suffix_trees.py\n**********************************************************************\nFile \"/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/combinat/words/suffix_trees.py\",\nline 1323:\n    sage: t.trie_type_dict() == dict([[(0, W(\"a\")), 4], [(0, W(\"b\")), 3], [(3, W(\"a\")), 2]\n, [(4, W(\"b\")), 5], [(5, W(\"a\")), 1]])\nExpected:\n    True\nGot:\n    False\n**********************************************************************\n```\n\nwhich have been mentioned previously.",
    "created_at": "2011-12-06T20:21:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99517",
    "user": "strogdon"
}
```

For the sake of completeness, I now have

32bit: one failure


```
sage -t -long  -force_lib devel/sage-main/sage/misc/randstate.pyx
```

which was mentioned above.

64bit: two failures


```

sage -t -long  -force_lib devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/combinat/words/nfactor_enumerable
_word.py", line 20:
    sage: it.next()
Expected:
    word: 5645
Got:
    word: 4564
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/combinat/words/nfactor_enumerable
_word.py", line 23:
    sage: it.next()
Expected:
    word: 6456
Got:
    word: 5645
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/combinat/words/nfactor_enumerable
_word.py", line 26:
    sage: it.next()
Expected:
    word: 4564
Got:
    word: 6456
**********************************************************************


sage -t -long  -force_lib devel/sage-main/sage/combinat/words/suffix_trees.py
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/combinat/words/suffix_trees.py",
line 1323:
    sage: t.trie_type_dict() == dict([[(0, W("a")), 4], [(0, W("b")), 3], [(3, W("a")), 2]
, [(4, W("b")), 5], [(5, W("a")), 1]])
Expected:
    True
Got:
    False
**********************************************************************
```

which have been mentioned previously.



---

archive/issue_comments_099518.json:
```json
{
    "body": "This ticket made me notice a bug with the L-series of Eisenstein series: #12124.  With that ticket applied, the patch to `sage/modular/modform/eis_series.py` here can be removed.",
    "created_at": "2011-12-06T20:53:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99518",
    "user": "jdemeyer"
}
```

This ticket made me notice a bug with the L-series of Eisenstein series: #12124.  With that ticket applied, the patch to `sage/modular/modform/eis_series.py` here can be removed.



---

archive/issue_comments_099519.json:
```json
{
    "body": "First of all, I'm not an expert of combinatorics on word. So I'd rather\nSebastien Labbe to jump in the discussion. I just trying to help.\n\n> 64bit: two failures\n\n```\nsage -t -long  -force_lib devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py\n**********************************************************************\nFile \"/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/combinat/words/nfactor_enumerable\n_word.py\", line 20:\n    sage: it.next()\nExpected:\n    word: 5645\nGot:\n    word: 4564\n**********************************************************************\nFile \"/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/combinat/words/nfactor_enumerable\n_word.py\", line 23:\n    sage: it.next()\nExpected:\n    word: 6456\nGot:\n    word: 5645\n**********************************************************************\nFile \"/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/combinat/words/nfactor_enumerable\n_word.py\", line 26:\n    sage: it.next()\nExpected:\n    word: 4564\nGot:\n    word: 6456\n**********************************************************************\n```\n\n\nThis first failure is not a problem. The iterator here is extracted from a\ndict of dict so it is not unexpected to have a random order. Fixing the test\nof marking it at random should be ok. This test is an explanation for the\nuser, the real feature is tested further in the file.\n\n\n> which have been mentioned previously.\n\n```\n{(4, word: a): 1, (0, word: b): 5, (0, word: a): 3, (5, word: a): 2, (3, word: b): 4}\n{(4, word: b): 5, (0, word: a): 4, (0, word: b): 3, (5, word: a): 1, (3, word: a): 2}\n```\n\n\nThis one is more tricky: As far as I understand, both result are perfectly\nlegible: the second is the same as the first after applying the following\ncyclic permutation (3,4,5). The numbering is random. So (again as far as I\nunderstand), the problem in only created by the cross-platform non-determinism\nof the set/dict data structure. I'm not sure here what is the best fix.\n\nCheers,\n\nFlorent",
    "created_at": "2011-12-07T22:27:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99519",
    "user": "hivert"
}
```

First of all, I'm not an expert of combinatorics on word. So I'd rather
Sebastien Labbe to jump in the discussion. I just trying to help.

> 64bit: two failures

```
sage -t -long  -force_lib devel/sage-main/sage/combinat/words/nfactor_enumerable_word.py
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/combinat/words/nfactor_enumerable
_word.py", line 20:
    sage: it.next()
Expected:
    word: 5645
Got:
    word: 4564
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/combinat/words/nfactor_enumerable
_word.py", line 23:
    sage: it.next()
Expected:
    word: 6456
Got:
    word: 5645
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-main/sage/combinat/words/nfactor_enumerable
_word.py", line 26:
    sage: it.next()
Expected:
    word: 4564
Got:
    word: 6456
**********************************************************************
```


This first failure is not a problem. The iterator here is extracted from a
dict of dict so it is not unexpected to have a random order. Fixing the test
of marking it at random should be ok. This test is an explanation for the
user, the real feature is tested further in the file.


> which have been mentioned previously.

```
{(4, word: a): 1, (0, word: b): 5, (0, word: a): 3, (5, word: a): 2, (3, word: b): 4}
{(4, word: b): 5, (0, word: a): 4, (0, word: b): 3, (5, word: a): 1, (3, word: a): 2}
```


This one is more tricky: As far as I understand, both result are perfectly
legible: the second is the same as the first after applying the following
cyclic permutation (3,4,5). The numbering is random. So (again as far as I
understand), the problem in only created by the cross-platform non-determinism
of the set/dict data structure. I'm not sure here what is the best fix.

Cheers,

Florent



---

archive/issue_comments_099520.json:
```json
{
    "body": "Thank you Florent, that is helpful. We kind of worked out that word was OK but we thought we could have a better test. If you think that's ok to mark it random I think we'll do that with some explanation.\n\nThe fact that both output in suffix_tree are legit is good to know. We can probably work around that. We may even have a complete patch set by Monday, cross fingers.",
    "created_at": "2011-12-08T00:52:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99520",
    "user": "fbissey"
}
```

Thank you Florent, that is helpful. We kind of worked out that word was OK but we thought we could have a better test. If you think that's ok to mark it random I think we'll do that with some explanation.

The fact that both output in suffix_tree are legit is good to know. We can probably work around that. We may even have a complete patch set by Monday, cross fingers.



---

archive/issue_comments_099521.json:
```json
{
    "body": "Upgraded succesfully from sage-4.6.2, all tests pass except for the known problematic tests.",
    "created_at": "2011-12-09T21:42:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99521",
    "user": "jdemeyer"
}
```

Upgraded succesfully from sage-4.6.2, all tests pass except for the known problematic tests.



---

archive/issue_comments_099522.json:
```json
{
    "body": "I'll work on the remaining tests tomorrow, I hope. I will remove the eis_series.py and see if I can review #12124 as well. I looks like the python spkg will need rebasing again with #12131.",
    "created_at": "2011-12-10T11:21:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99522",
    "user": "fbissey"
}
```

I'll work on the remaining tests tomorrow, I hope. I will remove the eis_series.py and see if I can review #12124 as well. I looks like the python spkg will need rebasing again with #12131.



---

archive/issue_comments_099523.json:
```json
{
    "body": "Replying to [comment:196 fbissey]:\n> I'll work on the remaining tests tomorrow, I hope.\nThat would be great!  I would love to see this finished in time, such that the next release can really be sage-5.0.",
    "created_at": "2011-12-10T20:27:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99523",
    "user": "jdemeyer"
}
```

Replying to [comment:196 fbissey]:
> I'll work on the remaining tests tomorrow, I hope.
That would be great!  I would love to see this finished in time, such that the next release can really be sage-5.0.



---

archive/issue_comments_099524.json:
```json
{
    "body": "Attachment\n\ntest against more valid dictionaries in suffix_trees",
    "created_at": "2011-12-10T22:12:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99524",
    "user": "fbissey"
}
```

Attachment

test against more valid dictionaries in suffix_trees



---

archive/issue_comments_099525.json:
```json
{
    "body": "fix all numerical noise in randstate",
    "created_at": "2011-12-10T22:13:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99525",
    "user": "fbissey"
}
```

fix all numerical noise in randstate



---

archive/issue_comments_099526.json:
```json
{
    "body": "Attachment\n\nfixing numerical noise part 1 - updated 20111211: separate randstate and eis_modn_series",
    "created_at": "2011-12-10T22:14:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99526",
    "user": "fbissey"
}
```

Attachment

fixing numerical noise part 1 - updated 20111211: separate randstate and eis_modn_series



---

archive/issue_comments_099527.json:
```json
{
    "body": "Attachment\n\nupdating the patch set with a tentative solution for suffix_trees. It may not be exhaustive of all possible answers though. If we are going for it for the next release I can redo the python spkg to fix the lib/lib64 from #12131.\n\nPutting to need review :)",
    "created_at": "2011-12-10T22:22:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99527",
    "user": "fbissey"
}
```

Attachment

updating the patch set with a tentative solution for suffix_trees. It may not be exhaustive of all possible answers though. If we are going for it for the next release I can redo the python spkg to fix the lib/lib64 from #12131.

Putting to need review :)



---

archive/issue_comments_099528.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-12-10T22:22:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99528",
    "user": "fbissey"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_099529.json:
```json
{
    "body": "Hi,\n\nI just read randomly sage-devel (I was away from sage development for several weeks) and saw that the discussion about upgrading to 2.7 was having problem with some files I am related with (suffix_tree.py nfactor_enumerable_word.py). I still don't understand the dict problem for suffix tree (one minute was not enough). I will look into that to avoid similar problem in the future. If something else pops up in those file, I can do the fix next time.\n\nS\u00e9bastien",
    "created_at": "2011-12-10T22:54:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99529",
    "user": "slabbe"
}
```

Hi,

I just read randomly sage-devel (I was away from sage development for several weeks) and saw that the discussion about upgrading to 2.7 was having problem with some files I am related with (suffix_tree.py nfactor_enumerable_word.py). I still don't understand the dict problem for suffix tree (one minute was not enough). I will look into that to avoid similar problem in the future. If something else pops up in those file, I can do the fix next time.

Sébastien



---

archive/issue_comments_099530.json:
```json
{
    "body": "Your input on the matter is welcome. According to Florent, the problem in suffix_trees is that there are several equivalent answers and some platforms now give a different one than the one you originally tested for. Note that we don't know what the trigger is for having a different answer it is not a 32/64 bit separation as we have seen both answers on the two kinds of systems.",
    "created_at": "2011-12-10T23:03:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99530",
    "user": "fbissey"
}
```

Your input on the matter is welcome. According to Florent, the problem in suffix_trees is that there are several equivalent answers and some platforms now give a different one than the one you originally tested for. Note that we don't know what the trigger is for having a different answer it is not a 32/64 bit separation as we have seen both answers on the two kinds of systems.



---

archive/issue_comments_099531.json:
```json
{
    "body": "Actually, you should have a look at what I did for both of these in [attachment:trac_9958-nfactor_enumerable_word-randomness.patch] and [attachment:trac_9958-suffix_trees-variations.patch]. If you could give your opinion on the patches or if you want to submit patches of your own it would be appreciated.",
    "created_at": "2011-12-11T00:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99531",
    "user": "fbissey"
}
```

Actually, you should have a look at what I did for both of these in [attachment:trac_9958-nfactor_enumerable_word-randomness.patch] and [attachment:trac_9958-suffix_trees-variations.patch]. If you could give your opinion on the patches or if you want to submit patches of your own it would be appreciated.



---

archive/issue_comments_099532.json:
```json
{
    "body": "With the current update I have the following failures:\n\n\n```\n32bit\nsage -t -long  -force_lib devel/sage-9958/sage/combinat/words/nfactor_enumerable_word\n.py\n**********************************************************************\nFile \"/storage/sage/sage-4.8.alpha3/devel/sage-9958/sage/combinat/words/nfactor_enume\nrable_word.py\", line 23:\n    sage: it.next()\nExpected:\n    word: 6456     # random\nGot:\n    word: 6456\n**********************************************************************\nFile \"/storage/sage/sage-4.8.alpha3/devel/sage-9958/sage/combinat/words/nfactor_enume\nrable_word.py\", line 25:\n    sage: it.next()\nExpected:\n    word: 5645     # random\nGot:\n    word: 5645\n**********************************************************************\nFile \"/storage/sage/sage-4.8.alpha3/devel/sage-9958/sage/combinat/words/nfactor_enume\nrable_word.py\", line 27:\n    sage: it.next()\nExpected:\n    word: 4564     # random\nGot:\n    word: 4564\n**********************************************************************\n\n64bit\n\nsage -t -long  -force_lib devel/sage-9958/sage/combinat/words/nfactor_enumerable_word\n.py\n**********************************************************************\nFile \"/storage/sage/sage-4.8.alpha3/devel/sage-9958/sage/combinat/words/nfactor_enume\nrable_word.py\", line 23:\n    sage: it.next()\nExpected:\n    word: 6456     # random\nGot:\n    word: 4564\n**********************************************************************\nFile \"/storage/sage/sage-4.8.alpha3/devel/sage-9958/sage/combinat/words/nfactor_enume\nrable_word.py\", line 25:\n    sage: it.next()\nExpected:\n    word: 5645     # random\nGot:\n    word: 5645\n**********************************************************************\nFile \"/storage/sage/sage-4.8.alpha3/devel/sage-9958/sage/combinat/words/nfactor_enume\nrable_word.py\", line 27:\n    sage: it.next()\nExpected:\n    word: 4564     # random\nGot:\n    word: 6456\n**********************************************************************\n```\n\nand on 32bit and 64bit\n\n\n```\n\nsage -t -long  -force_lib devel/sage-9958/sage/misc/randstate.pyx\n**********************************************************************\nFile \"/storage/sage/sage-4.8.alpha3/devel/sage-9958/sage/misc/randstate.pyx\", line 15\n3:\n    sage: random(), getrandbits(20), uniform(5.0, 10.0), normalvariate(0, 1)\nExpected:\n    (0.82940228518742587, 624859L, 5.77894484361117, -0.42013668263087578)\nGot:\n    (0.8294022851874259, 624859L, 5.77894484361117, -0.4201366826308758)\n**********************************************************************\n```\n\nI don't recall previously seeing this particular randstate.pyx failure. Perhaps I've missed something.",
    "created_at": "2011-12-11T07:07:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99532",
    "user": "strogdon"
}
```

With the current update I have the following failures:


```
32bit
sage -t -long  -force_lib devel/sage-9958/sage/combinat/words/nfactor_enumerable_word
.py
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-9958/sage/combinat/words/nfactor_enume
rable_word.py", line 23:
    sage: it.next()
Expected:
    word: 6456     # random
Got:
    word: 6456
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-9958/sage/combinat/words/nfactor_enume
rable_word.py", line 25:
    sage: it.next()
Expected:
    word: 5645     # random
Got:
    word: 5645
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-9958/sage/combinat/words/nfactor_enume
rable_word.py", line 27:
    sage: it.next()
Expected:
    word: 4564     # random
Got:
    word: 4564
**********************************************************************

64bit

sage -t -long  -force_lib devel/sage-9958/sage/combinat/words/nfactor_enumerable_word
.py
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-9958/sage/combinat/words/nfactor_enume
rable_word.py", line 23:
    sage: it.next()
Expected:
    word: 6456     # random
Got:
    word: 4564
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-9958/sage/combinat/words/nfactor_enume
rable_word.py", line 25:
    sage: it.next()
Expected:
    word: 5645     # random
Got:
    word: 5645
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-9958/sage/combinat/words/nfactor_enume
rable_word.py", line 27:
    sage: it.next()
Expected:
    word: 4564     # random
Got:
    word: 6456
**********************************************************************
```

and on 32bit and 64bit


```

sage -t -long  -force_lib devel/sage-9958/sage/misc/randstate.pyx
**********************************************************************
File "/storage/sage/sage-4.8.alpha3/devel/sage-9958/sage/misc/randstate.pyx", line 15
3:
    sage: random(), getrandbits(20), uniform(5.0, 10.0), normalvariate(0, 1)
Expected:
    (0.82940228518742587, 624859L, 5.77894484361117, -0.42013668263087578)
Got:
    (0.8294022851874259, 624859L, 5.77894484361117, -0.4201366826308758)
**********************************************************************
```

I don't recall previously seeing this particular randstate.pyx failure. Perhaps I've missed something.



---

archive/issue_comments_099533.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-12-11T09:59:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99533",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_099534.json:
```json
{
    "body": "Yeah, the `#random` should be on the line with the command to execute, not the result.",
    "created_at": "2011-12-11T09:59:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99534",
    "user": "jdemeyer"
}
```

Yeah, the `#random` should be on the line with the command to execute, not the result.



---

archive/issue_comments_099535.json:
```json
{
    "body": "I had to make that mistake :(\n\nThe last randstate.pyx one is definitely new, I am sure it didn't happen before.",
    "created_at": "2011-12-11T11:28:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99535",
    "user": "fbissey"
}
```

I had to make that mistake :(

The last randstate.pyx one is definitely new, I am sure it didn't happen before.



---

archive/issue_comments_099536.json:
```json
{
    "body": "Attachment\n\ntake into account the randomness of it.next sequence of call - put random in the right place this time.",
    "created_at": "2011-12-11T11:32:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99536",
    "user": "fbissey"
}
```

Attachment

take into account the randomness of it.next sequence of call - put random in the right place this time.



---

archive/issue_comments_099537.json:
```json
{
    "body": "OK I replaced the trac_9958-nfactor_enumerable_word-randomness.patch in place. So random should be in the right place now. I am looking to see if I can reproduce this particular randstate.pyx problem.",
    "created_at": "2011-12-11T11:34:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99537",
    "user": "fbissey"
}
```

OK I replaced the trac_9958-nfactor_enumerable_word-randomness.patch in place. So random should be in the right place now. I am looking to see if I can reproduce this particular randstate.pyx problem.



---

archive/issue_comments_099538.json:
```json
{
    "body": "I missed a line in randstate! And you cut the last digit of the line number Steve, now that caused me some confusion. Updating shortly.",
    "created_at": "2011-12-11T11:43:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99538",
    "user": "fbissey"
}
```

I missed a line in randstate! And you cut the last digit of the line number Steve, now that caused me some confusion. Updating shortly.



---

archive/issue_comments_099539.json:
```json
{
    "body": "Attachment\n\nfix all numerical noise in randstate",
    "created_at": "2011-12-11T11:50:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99539",
    "user": "fbissey"
}
```

Attachment

fix all numerical noise in randstate



---

archive/issue_comments_099540.json:
```json
{
    "body": "OK new randstate patch, this time it is even a .patch instead of .pyx. Thanks for pointing out those mistakes.",
    "created_at": "2011-12-11T11:51:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99540",
    "user": "fbissey"
}
```

OK new randstate patch, this time it is even a .patch instead of .pyx. Thanks for pointing out those mistakes.



---

archive/issue_comments_099541.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-12-11T11:51:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99541",
    "user": "fbissey"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_099542.json:
```json
{
    "body": "OK, #9958 + #11986 + #12124, all tests pass here on 32bit and 64bit machines. Is it too early for champagne?",
    "created_at": "2011-12-11T19:00:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99542",
    "user": "strogdon"
}
```

OK, #9958 + #11986 + #12124, all tests pass here on 32bit and 64bit machines. Is it too early for champagne?



---

archive/issue_comments_099543.json:
```json
{
    "body": "Unfortunately, I'd say it is too early. We need Karl to test it on his old ppc OS X 10.4 mac and a run on solaris is also in order. I removed a patch for ia64 that didn't obviously port to python-2.7 so a look at that platform is also in order. In the mean time we can review #11986 and #12124 which I think can be done independently.\n\nWe could even split the combinat patches as they should work with python-2.6. It just there is nothing obvious to fix there.",
    "created_at": "2011-12-11T21:08:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99543",
    "user": "fbissey"
}
```

Unfortunately, I'd say it is too early. We need Karl to test it on his old ppc OS X 10.4 mac and a run on solaris is also in order. I removed a patch for ia64 that didn't obviously port to python-2.7 so a look at that platform is also in order. In the mean time we can review #11986 and #12124 which I think can be done independently.

We could even split the combinat patches as they should work with python-2.6. It just there is nothing obvious to fix there.



---

archive/issue_comments_099544.json:
```json
{
    "body": "As I have said before, testing is easy.  I am currently running tests for the upcoming sage-4.8.alpha4, but after that, I could test the new Python on various systems.\n\nBut still, somebody needs to actually *look* at the patches and verify that they make sense.",
    "created_at": "2011-12-11T21:18:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99544",
    "user": "jdemeyer"
}
```

As I have said before, testing is easy.  I am currently running tests for the upcoming sage-4.8.alpha4, but after that, I could test the new Python on various systems.

But still, somebody needs to actually *look* at the patches and verify that they make sense.



---

archive/issue_comments_099545.json:
```json
{
    "body": "OK Jeroen, that's a boring task for someone most of them are of the form:\n\n```\ndiff --git a/sage/misc/sage_unittest.py b/sage/misc/sage_unittest.py\n--- a/sage/misc/sage_unittest.py\n+++ b/sage/misc/sage_unittest.py\n@@ -201,12 +201,12 @@\n             Failure in _test_b:\n             Traceback (most recent call last):\n               ...\n-            AssertionError\n+            AssertionError: None\n             ------------------------------------------------------------\n             Failure in _test_d:\n             Traceback (most recent call last):\n               ...\n-            AssertionError\n+            AssertionError: None\n             ------------------------------------------------------------\n             Failure in _test_pickling:\n             Traceback (most recent call last):\n@@ -220,14 +220,14 @@\n             running ._test_b() . . . fail\n             Traceback (most recent call last):\n               ...\n-            AssertionError\n+            AssertionError: None\n             ------------------------------------------------------------\n             running ._test_c() . . . pass\n             running ._test_category() . . . pass\n             running ._test_d() . . . fail\n             Traceback (most recent call last):\n               ...\n-            AssertionError\n+            AssertionError: None\n             ------------------------------------------------------------\n             running ._test_not_implemented_methods() . . . pass\n             running ._test_pickling() . . . fail\n@@ -249,7 +249,7 @@\n               File ..., in _test_b\n                 def _test_b(self, tester): tester.fail()\n               ...\n-            AssertionError\n+            AssertionError: None\n \n         In conjonction with ``%pdb on``, this allows for the debbuger\n         to jump directly to the first failure location.\n@@ -311,7 +311,7 @@\n         sage: tester.assert_(1 == 0)\n         Traceback (most recent call last):\n         ...\n-        AssertionError\n+        AssertionError: False is not true\n         sage: tester.assert_(1 == 0, \"this is expected to fail\")\n         Traceback (most recent call last):\n         ...\n```\n\nand other numerical noise niceties cutting one digit and sometimes the rounding makes a lot of digits disappear (and it looks better actually), for example in plot/colors.py\n\n```\n@@ -290,23 +290,23 @@\n \n         sage: from sage.plot.colors import rgbcolor\n         sage: rgbcolor(Color(0.25, 0.4, 0.9))\n-        (0.25, 0.40000000000000002, 0.90000000000000002)\n+        (0.25, 0.4, 0.9)\n         sage: rgbcolor('purple')\n```\n\nOnly the two combinat patches are a bit more subtle.",
    "created_at": "2011-12-11T21:33:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99545",
    "user": "fbissey"
}
```

OK Jeroen, that's a boring task for someone most of them are of the form:

```
diff --git a/sage/misc/sage_unittest.py b/sage/misc/sage_unittest.py
--- a/sage/misc/sage_unittest.py
+++ b/sage/misc/sage_unittest.py
@@ -201,12 +201,12 @@
             Failure in _test_b:
             Traceback (most recent call last):
               ...
-            AssertionError
+            AssertionError: None
             ------------------------------------------------------------
             Failure in _test_d:
             Traceback (most recent call last):
               ...
-            AssertionError
+            AssertionError: None
             ------------------------------------------------------------
             Failure in _test_pickling:
             Traceback (most recent call last):
@@ -220,14 +220,14 @@
             running ._test_b() . . . fail
             Traceback (most recent call last):
               ...
-            AssertionError
+            AssertionError: None
             ------------------------------------------------------------
             running ._test_c() . . . pass
             running ._test_category() . . . pass
             running ._test_d() . . . fail
             Traceback (most recent call last):
               ...
-            AssertionError
+            AssertionError: None
             ------------------------------------------------------------
             running ._test_not_implemented_methods() . . . pass
             running ._test_pickling() . . . fail
@@ -249,7 +249,7 @@
               File ..., in _test_b
                 def _test_b(self, tester): tester.fail()
               ...
-            AssertionError
+            AssertionError: None
 
         In conjonction with ``%pdb on``, this allows for the debbuger
         to jump directly to the first failure location.
@@ -311,7 +311,7 @@
         sage: tester.assert_(1 == 0)
         Traceback (most recent call last):
         ...
-        AssertionError
+        AssertionError: False is not true
         sage: tester.assert_(1 == 0, "this is expected to fail")
         Traceback (most recent call last):
         ...
```

and other numerical noise niceties cutting one digit and sometimes the rounding makes a lot of digits disappear (and it looks better actually), for example in plot/colors.py

```
@@ -290,23 +290,23 @@
 
         sage: from sage.plot.colors import rgbcolor
         sage: rgbcolor(Color(0.25, 0.4, 0.9))
-        (0.25, 0.40000000000000002, 0.90000000000000002)
+        (0.25, 0.4, 0.9)
         sage: rgbcolor('purple')
```

Only the two combinat patches are a bit more subtle.



---

archive/issue_comments_099546.json:
```json
{
    "body": "Replying to [comment:209 fbissey]:\n> Unfortunately, I'd say it is too early. We need Karl to test it on his old ppc OS X 10.4 mac and a run on solaris is also in order.\nIs this all based on 4.8.alpha3?  I can try to do this starting today.  Jeroen might be done before me, though :) at least by the time I finish applying ALL of these patches.",
    "created_at": "2011-12-12T13:55:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99546",
    "user": "kcrisman"
}
```

Replying to [comment:209 fbissey]:
> Unfortunately, I'd say it is too early. We need Karl to test it on his old ppc OS X 10.4 mac and a run on solaris is also in order.
Is this all based on 4.8.alpha3?  I can try to do this starting today.  Jeroen might be done before me, though :) at least by the time I finish applying ALL of these patches.



---

archive/issue_comments_099547.json:
```json
{
    "body": "It should apply to 4.8.alpha3, apply #11986 + #12124 also.",
    "created_at": "2011-12-12T20:27:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99547",
    "user": "fbissey"
}
```

It should apply to 4.8.alpha3, apply #11986 + #12124 also.



---

archive/issue_comments_099548.json:
```json
{
    "body": "Replying to [comment:212 kcrisman]:\n> Replying to [comment:209 fbissey]:\n> > Unfortunately, I'd say it is too early. We need Karl to test it on his old ppc OS X 10.4 mac and a run on solaris is also in order.\n> Is this all based on 4.8.alpha3?  I can try to do this starting today.  Jeroen might be done before me, though :)\nGo ahead, I'm currently tackling other beasts...",
    "created_at": "2011-12-13T08:16:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99548",
    "user": "jdemeyer"
}
```

Replying to [comment:212 kcrisman]:
> Replying to [comment:209 fbissey]:
> > Unfortunately, I'd say it is too early. We need Karl to test it on his old ppc OS X 10.4 mac and a run on solaris is also in order.
> Is this all based on 4.8.alpha3?  I can try to do this starting today.  Jeroen might be done before me, though :)
Go ahead, I'm currently tackling other beasts...



---

archive/issue_comments_099549.json:
```json
{
    "body": "Replying to [comment:201 fbissey]:\n> Actually, you should have a look at what I did for both of these in [attachment:trac_9958-nfactor_enumerable_word-randomness.patch] and [attachment:trac_9958-suffix_trees-variations.patch]. If you could give your opinion on the patches or if you want to submit patches of your own it would be appreciated.\n\nHi,\n\nI just look at the suffix tree code (written not by me but by Franco Saliola). The method `trie_type_dict` is not used anywhere in the file neither in `sage/combinat/words` neither in all Sage I would guess. So, it's kind of difficult to guess what the result should be (input and output blocks are absent in documentation). I think that method was used by Franco to compare the implementation of `ImplicitSuffixTree` with that of `SuffixTrie` but not seriously because the output is not practical (one can't create a `DiGraph` out of it).\n\nAnyway, there are two loops in that method that both go through `.iteritems()` of a dictionary... Integer indexes present in the result depends on the ordering of those two loops. So, it is possible that a third different result is obtained in some other machine or system today or later. I just made a patch which should be more durable in the long term.\n\nFor the nfactor enumerable file, the fix is perfect.",
    "created_at": "2011-12-13T17:20:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99549",
    "user": "slabbe"
}
```

Replying to [comment:201 fbissey]:
> Actually, you should have a look at what I did for both of these in [attachment:trac_9958-nfactor_enumerable_word-randomness.patch] and [attachment:trac_9958-suffix_trees-variations.patch]. If you could give your opinion on the patches or if you want to submit patches of your own it would be appreciated.

Hi,

I just look at the suffix tree code (written not by me but by Franco Saliola). The method `trie_type_dict` is not used anywhere in the file neither in `sage/combinat/words` neither in all Sage I would guess. So, it's kind of difficult to guess what the result should be (input and output blocks are absent in documentation). I think that method was used by Franco to compare the implementation of `ImplicitSuffixTree` with that of `SuffixTrie` but not seriously because the output is not practical (one can't create a `DiGraph` out of it).

Anyway, there are two loops in that method that both go through `.iteritems()` of a dictionary... Integer indexes present in the result depends on the ordering of those two loops. So, it is possible that a third different result is obtained in some other machine or system today or later. I just made a patch which should be more durable in the long term.

For the nfactor enumerable file, the fix is perfect.



---

archive/issue_comments_099550.json:
```json
{
    "body": "Fix machine dependant doctest in suffix tree",
    "created_at": "2011-12-13T17:23:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99550",
    "user": "slabbe"
}
```

Fix machine dependant doctest in suffix tree



---

archive/issue_comments_099551.json:
```json
{
    "body": "Attachment\n\n> > > Unfortunately, I'd say it is too early. We need Karl to test it on his old ppc OS X 10.4 mac and a run on solaris is also in order.\n> > Is this all based on 4.8.alpha3?  I can try to do this starting today.  Jeroen might be done before me, though :)\n> Go ahead, I'm currently tackling other beasts...\nOkay, at least everything applies and builds from this and the two other tickets.  (Note that #11986 is listed as a dependency of **and** for #9958.)\n\nSo presumably sometime tomorrow I can report back.  So far six files having tested well...",
    "created_at": "2011-12-13T18:23:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99551",
    "user": "kcrisman"
}
```

Attachment

> > > Unfortunately, I'd say it is too early. We need Karl to test it on his old ppc OS X 10.4 mac and a run on solaris is also in order.
> > Is this all based on 4.8.alpha3?  I can try to do this starting today.  Jeroen might be done before me, though :)
> Go ahead, I'm currently tackling other beasts...
Okay, at least everything applies and builds from this and the two other tickets.  (Note that #11986 is listed as a dependency of **and** for #9958.)

So presumably sometime tomorrow I can report back.  So far six files having tested well...



---

archive/issue_comments_099552.json:
```json
{
    "body": "Replying to [comment:216 slabbe]:\n> Anyway, there are two loops in that method that both go through `.iteritems()` of a dictionary... Integer indexes present in the result depends on the ordering of those two loops. So, it is possible that a third different result is obtained in some other machine or system today or later. I just made a patch which should be more durable in the long term.\n> \n> For the nfactor enumerable file, the fix is perfect.\n\nThanks. I thought there could be a third possible results from Florent's comments (permutation (3,4,5)) but couldn't figure what it would look like. Happy to have some serious review for that bit.",
    "created_at": "2011-12-13T18:32:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99552",
    "user": "fbissey"
}
```

Replying to [comment:216 slabbe]:
> Anyway, there are two loops in that method that both go through `.iteritems()` of a dictionary... Integer indexes present in the result depends on the ordering of those two loops. So, it is possible that a third different result is obtained in some other machine or system today or later. I just made a patch which should be more durable in the long term.
> 
> For the nfactor enumerable file, the fix is perfect.

Thanks. I thought there could be a third possible results from Florent's comments (permutation (3,4,5)) but couldn't figure what it would look like. Happy to have some serious review for that bit.



---

archive/issue_comments_099553.json:
```json
{
    "body": "OK the upgrade of R in #12057 shipped with 4.8.alpha4 makes a small bit of patch for r.py obsolete. Updating it shortly.",
    "created_at": "2011-12-13T21:08:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99553",
    "user": "fbissey"
}
```

OK the upgrade of R in #12057 shipped with 4.8.alpha4 makes a small bit of patch for r.py obsolete. Updating it shortly.



---

archive/issue_comments_099554.json:
```json
{
    "body": "Attachment\n\nfixing numerical noise part 1 - updated 20111214 for 4.8.alpha4",
    "created_at": "2011-12-13T21:11:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99554",
    "user": "fbissey"
}
```

Attachment

fixing numerical noise part 1 - updated 20111214 for 4.8.alpha4



---

archive/issue_comments_099555.json:
```json
{
    "body": "First patch updated. I don't think there will be any more changes because of 4.8.alpha4 but I could be wrong.",
    "created_at": "2011-12-13T21:12:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99555",
    "user": "fbissey"
}
```

First patch updated. I don't think there will be any more changes because of 4.8.alpha4 but I could be wrong.



---

archive/issue_comments_099556.json:
```json
{
    "body": "It looks like a slight modification is still needed in interfaces/r.py. On both x86 and amd64 I get\n\n\n```\nsage -t -long  -force_lib devel/sage-main/sage/interfaces/r.py\n**********************************************************************\nFile \"/storage/sage/sage-4.8.alpha4/devel/sage-main/sage/interfaces/r.py\", line 173:\n    sage: sum(rr._sage_())\nExpected:\n    9.97721251689810...\nGot:\n    9.97721251689811\n**********************************************************************\n```\n\nattachment:trac_9958-suffix_trees-variations-sl.patch:ticket:9958 was used in the tests.",
    "created_at": "2011-12-14T02:08:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99556",
    "user": "strogdon"
}
```

It looks like a slight modification is still needed in interfaces/r.py. On both x86 and amd64 I get


```
sage -t -long  -force_lib devel/sage-main/sage/interfaces/r.py
**********************************************************************
File "/storage/sage/sage-4.8.alpha4/devel/sage-main/sage/interfaces/r.py", line 173:
    sage: sum(rr._sage_())
Expected:
    9.97721251689810...
Got:
    9.97721251689811
**********************************************************************
```

attachment:trac_9958-suffix_trees-variations-sl.patch:ticket:9958 was used in the tests.



---

archive/issue_comments_099557.json:
```json
{
    "body": "I have seen it on my sage-on-gentoo test run but I hadn't tried yet on a vanilla to check if it was caused by other gentoo stuff. I will add a small patch ASAP.",
    "created_at": "2011-12-14T02:22:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99557",
    "user": "fbissey"
}
```

I have seen it on my sage-on-gentoo test run but I hadn't tried yet on a vanilla to check if it was caused by other gentoo stuff. I will add a small patch ASAP.



---

archive/issue_comments_099558.json:
```json
{
    "body": "Attachment\n\nnumerical noise in interface/r.py updated for R-2.14.0",
    "created_at": "2011-12-14T03:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99558",
    "user": "fbissey"
}
```

Attachment

numerical noise in interface/r.py updated for R-2.14.0



---

archive/issue_comments_099559.json:
```json
{
    "body": "New patch included for interface/r.py in 4.8.alpha4.",
    "created_at": "2011-12-14T03:22:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99559",
    "user": "fbissey"
}
```

New patch included for interface/r.py in 4.8.alpha4.



---

archive/issue_comments_099560.json:
```json
{
    "body": "How do we test this ticket?  Is it enough to untar a fresh tarball of the 4.8.alpha4 source, replace the existing python spkg with the one from this ticket, and do a normal make?  Then apply the patches to the sage library and run doctests?\n\nOn OSX 10.6.8, I tried downloading a fresh copy of 4.8.alpha4, putting this python spkg in the spkg/standard directory and deleting the old python spkg.  I ended up getting a build error, seemingly right after I finished building scipy (even though scipy said it was built succesfully, but I was also building spkgs in parallel).  I typed \"make\" again to restart the process and the same thing happened after rpy built---it said rpy was built successfully, but then it stopped the build, saying \"Error building Sage\".",
    "created_at": "2011-12-14T10:02:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99560",
    "user": "jason"
}
```

How do we test this ticket?  Is it enough to untar a fresh tarball of the 4.8.alpha4 source, replace the existing python spkg with the one from this ticket, and do a normal make?  Then apply the patches to the sage library and run doctests?

On OSX 10.6.8, I tried downloading a fresh copy of 4.8.alpha4, putting this python spkg in the spkg/standard directory and deleting the old python spkg.  I ended up getting a build error, seemingly right after I finished building scipy (even though scipy said it was built succesfully, but I was also building spkgs in parallel).  I typed "make" again to restart the process and the same thing happened after rpy built---it said rpy was built successfully, but then it stopped the build, saying "Error building Sage".



---

archive/issue_comments_099561.json:
```json
{
    "body": "Replying to [comment:224 jason]:\n> How do we test this ticket?  Is it enough to untar a fresh tarball of the 4.8.alpha4 source, replace the existing python spkg with the one from this ticket, and do a normal make?  Then apply the patches to the sage library and run doctests?\n> \n\nYes that's how you should do it.\n\n> On OSX 10.6.8, I tried downloading a fresh copy of 4.8.alpha4, putting this python spkg in the spkg/standard directory and deleting the old python spkg.  I ended up getting a build error, seemingly right after I finished building scipy (even though scipy said it was built succesfully, but I was also building spkgs in parallel).  I typed \"make\" again to restart the process and the same thing happened after rpy built---it said rpy was built successfully, but then it stopped the build, saying \"Error building Sage\".\n> \n\nCould you post the log for the build of python somewhere? scipy and rpy are built after sage (or at least they can be since they are runtime and not buildtime dependencies) so it is possible you were building sage itself at the same time. Is there a log for the sage spkg (in spkg/log)?",
    "created_at": "2011-12-14T11:51:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99561",
    "user": "fbissey"
}
```

Replying to [comment:224 jason]:
> How do we test this ticket?  Is it enough to untar a fresh tarball of the 4.8.alpha4 source, replace the existing python spkg with the one from this ticket, and do a normal make?  Then apply the patches to the sage library and run doctests?
> 

Yes that's how you should do it.

> On OSX 10.6.8, I tried downloading a fresh copy of 4.8.alpha4, putting this python spkg in the spkg/standard directory and deleting the old python spkg.  I ended up getting a build error, seemingly right after I finished building scipy (even though scipy said it was built succesfully, but I was also building spkgs in parallel).  I typed "make" again to restart the process and the same thing happened after rpy built---it said rpy was built successfully, but then it stopped the build, saying "Error building Sage".
> 

Could you post the log for the build of python somewhere? scipy and rpy are built after sage (or at least they can be since they are runtime and not buildtime dependencies) so it is possible you were building sage itself at the same time. Is there a log for the sage spkg (in spkg/log)?



---

archive/issue_comments_099562.json:
```json
{
    "body": "I posted the install.log here: http://sage.math.washington.edu/home/jason/sage-4.8.alpha4-python2.7-install.log.bz2\n\nIf you search for \"Error building Sage\", you'll see the multiple times I restarted the build (that message appeared after each time I restarted the build).\n\nHere's the list of spkg logs I have:\n\n\n```\n\nsage-4.8.alpha4newpython/spkg/logs% ls\natlas-3.8.4.log                gdmodule-0.56.p7.log           moin-1.9.1.p2.log              ratpoints-2.1.3.p1.log\nblas-20070724.log              genus2reduction-0.3.p8.log     mpfi-1.3.4-cvs20071125.p8.log  readline-6.2.p1.log\nboehm_gc-7.2.alpha6.p1.log     gfan-0.4plus.p1.log            mpfr-2.4.2.log                 rpy2-2.0.8.log\nboost-cropped-1.34.1.log       givaro-3.2.13rc2.p2.log        mpir-2.1.3.p8.log              rubiks-20070912.p17.log\nbzip2-1.0.5.log                glpk-4.44.log                  mpmath-0.17.log                sage_root-4.8.alpha4.log\ncddlib-094f.p8.log             gnutls-2.2.1.p5.log            networkx-1.2.p1.log            sage_scripts-4.8.alpha4.log\ncephes-2.8.log                 graphs-20070722.p1.log         ntl-5.5.2.log                  sagenb-0.8.25.log\ncliquer-1.2.p10.log            gsl-1.15.log                   numpy-1.5.1.log                scipy-0.9.p1.log\nconway_polynomials-0.2.log     iconv-1.13.1.p3.log            opencdk-0.6.6.p5.log           scons-1.2.0.log\ncvxopt-1.1.3.log               iml-1.0.1.p13.log              palp-1.1.p3.log                setuptools-0.6.16.log\ncython-0.15.1.log              ipython-0.10.2.p0.log          pari-2.5.0.p2.log              singular-3-1-3-3.p2.log\ndir-0.1.log                    jinja2-2.5.5.log               patch-2.5.9.p2.log             sphinx-1.1.2.p0.log\ndocutils-0.7.p0.log            lapack-20071123.p2.log         pexpect-2.0.p4.log             sqlalchemy-0.5.8.log\necl-11.1.2.cvs20111120.p0.log  lcalc-1.23.p9.log              pil-1.1.6.p4.log               sqlite-3.7.5.log\neclib-20100711.p0.log          libfplll-3.0.12.p1.log         polybori-0.7.1.p6.log          symmetrica-2.0.p7.log\necm-6.3.p2.log                 libgcrypt-1.4.4.p3.log         polytopes_db-20100210.log      sympow-1.018.1.p9.log\nelliptic_curves-0.3.log        libgpg_error-1.6.p3.log        ppl-0.11.2.log                 sympy-0.7.1.log\nextcode-4.8.alpha4.log         libm4ri-20111004.log           prereq-0.9.log                 tachyon-0.98.9.p5.log\nf2c-20070816.p2.log            libm4rie-20111004.log          pycrypto-2.1.0.log             termcap-1.3.1.p1.log\nflint-1.5.0.p10.log            libpng-1.2.35.p3.log           pygments-1.3.1.p0.log          twisted-9.0.p2.log\nflintqs-20070817.p6.log        linbox-1.1.6.p5.log            pynac-0.2.3.log                zlib-1.2.5.p0.log\nfortran-20100629.log           matplotlib-1.0.1.p0.log        python-2.7.2.p0.log            zn_poly-0.9.p5.log\nfreetype-2.3.5.p3.log          maxima-5.23.2.p2.log           python_gnutls-1.1.4.p7.log     zodb3-3.7.0.p4.log\ngd-2.0.35.p5.log               mercurial-1.8.4.log            r-2.14.0.p0.log\n```\n",
    "created_at": "2011-12-14T14:20:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99562",
    "user": "jason"
}
```

I posted the install.log here: http://sage.math.washington.edu/home/jason/sage-4.8.alpha4-python2.7-install.log.bz2

If you search for "Error building Sage", you'll see the multiple times I restarted the build (that message appeared after each time I restarted the build).

Here's the list of spkg logs I have:


```

sage-4.8.alpha4newpython/spkg/logs% ls
atlas-3.8.4.log                gdmodule-0.56.p7.log           moin-1.9.1.p2.log              ratpoints-2.1.3.p1.log
blas-20070724.log              genus2reduction-0.3.p8.log     mpfi-1.3.4-cvs20071125.p8.log  readline-6.2.p1.log
boehm_gc-7.2.alpha6.p1.log     gfan-0.4plus.p1.log            mpfr-2.4.2.log                 rpy2-2.0.8.log
boost-cropped-1.34.1.log       givaro-3.2.13rc2.p2.log        mpir-2.1.3.p8.log              rubiks-20070912.p17.log
bzip2-1.0.5.log                glpk-4.44.log                  mpmath-0.17.log                sage_root-4.8.alpha4.log
cddlib-094f.p8.log             gnutls-2.2.1.p5.log            networkx-1.2.p1.log            sage_scripts-4.8.alpha4.log
cephes-2.8.log                 graphs-20070722.p1.log         ntl-5.5.2.log                  sagenb-0.8.25.log
cliquer-1.2.p10.log            gsl-1.15.log                   numpy-1.5.1.log                scipy-0.9.p1.log
conway_polynomials-0.2.log     iconv-1.13.1.p3.log            opencdk-0.6.6.p5.log           scons-1.2.0.log
cvxopt-1.1.3.log               iml-1.0.1.p13.log              palp-1.1.p3.log                setuptools-0.6.16.log
cython-0.15.1.log              ipython-0.10.2.p0.log          pari-2.5.0.p2.log              singular-3-1-3-3.p2.log
dir-0.1.log                    jinja2-2.5.5.log               patch-2.5.9.p2.log             sphinx-1.1.2.p0.log
docutils-0.7.p0.log            lapack-20071123.p2.log         pexpect-2.0.p4.log             sqlalchemy-0.5.8.log
ecl-11.1.2.cvs20111120.p0.log  lcalc-1.23.p9.log              pil-1.1.6.p4.log               sqlite-3.7.5.log
eclib-20100711.p0.log          libfplll-3.0.12.p1.log         polybori-0.7.1.p6.log          symmetrica-2.0.p7.log
ecm-6.3.p2.log                 libgcrypt-1.4.4.p3.log         polytopes_db-20100210.log      sympow-1.018.1.p9.log
elliptic_curves-0.3.log        libgpg_error-1.6.p3.log        ppl-0.11.2.log                 sympy-0.7.1.log
extcode-4.8.alpha4.log         libm4ri-20111004.log           prereq-0.9.log                 tachyon-0.98.9.p5.log
f2c-20070816.p2.log            libm4rie-20111004.log          pycrypto-2.1.0.log             termcap-1.3.1.p1.log
flint-1.5.0.p10.log            libpng-1.2.35.p3.log           pygments-1.3.1.p0.log          twisted-9.0.p2.log
flintqs-20070817.p6.log        linbox-1.1.6.p5.log            pynac-0.2.3.log                zlib-1.2.5.p0.log
fortran-20100629.log           matplotlib-1.0.1.p0.log        python-2.7.2.p0.log            zn_poly-0.9.p5.log
freetype-2.3.5.p3.log          maxima-5.23.2.p2.log           python_gnutls-1.1.4.p7.log     zodb3-3.7.0.p4.log
gd-2.0.35.p5.log               mercurial-1.8.4.log            r-2.14.0.p0.log
```




---

archive/issue_comments_099563.json:
```json
{
    "body": "All is well on the PPC OS X front, even with the r.py, amazingly; it failed the first time but passed on a rerun.",
    "created_at": "2011-12-14T21:15:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99563",
    "user": "kcrisman"
}
```

All is well on the PPC OS X front, even with the r.py, amazingly; it failed the first time but passed on a rerun.



---

archive/issue_comments_099564.json:
```json
{
    "body": "Jason the log you sent is not very useful, at least I cannot easily find something interesting. Could you provide the following:\n\n* python-2.7.2.p0.log\n* polybori-0.7.1.p6.log\n* ppl-0.11.2.log\n* pynac-0.2.3.log\n\nThat's a shot in the dark so far. But the building of sage never started as there is no log for sage itself.\n\nI digged a little bit more before posting it looks like R fails to build so I want to see r-2.14.0.p0.log but that may be a separate issue from python. matplotlib seems to fail to build too so I want matplotlib-1.0.1.p0.log and now we are talking real potential python trouble.",
    "created_at": "2011-12-14T22:46:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99564",
    "user": "fbissey"
}
```

Jason the log you sent is not very useful, at least I cannot easily find something interesting. Could you provide the following:

* python-2.7.2.p0.log
* polybori-0.7.1.p6.log
* ppl-0.11.2.log
* pynac-0.2.3.log

That's a shot in the dark so far. But the building of sage never started as there is no log for sage itself.

I digged a little bit more before posting it looks like R fails to build so I want to see r-2.14.0.p0.log but that may be a separate issue from python. matplotlib seems to fail to build too so I want matplotlib-1.0.1.p0.log and now we are talking real potential python trouble.



---

archive/issue_comments_099565.json:
```json
{
    "body": "I'm going to try this with \n\n```\nexport MAKE=\"make -j2\"\n```\n\non the same platform and report back.",
    "created_at": "2011-12-15T01:30:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99565",
    "user": "kcrisman"
}
```

I'm going to try this with 

```
export MAKE="make -j2"
```

on the same platform and report back.



---

archive/issue_comments_099566.json:
```json
{
    "body": "First, here are my standard build environment settings:\n\n\n```\nexport SAGE_MATPLOTLIB_GUI=yes\nexport SAGE_PARALLEL_SPKG_BUILD=yes     \nexport MAKE=\"make -j6\"    \nexport SAGE_SPKG_INSTALL_DOCS=yes\n```\n\n\nAll the requested logs are tarred up at http://sage.math.washington.edu/home/jason/newpython-spkg-logs.tar.gz",
    "created_at": "2011-12-15T02:49:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99566",
    "user": "jason"
}
```

First, here are my standard build environment settings:


```
export SAGE_MATPLOTLIB_GUI=yes
export SAGE_PARALLEL_SPKG_BUILD=yes     
export MAKE="make -j6"    
export SAGE_SPKG_INSTALL_DOCS=yes
```


All the requested logs are tarred up at http://sage.math.washington.edu/home/jason/newpython-spkg-logs.tar.gz



---

archive/issue_comments_099567.json:
```json
{
    "body": "Tonight, I'll try building again without setting any of those environment variables to see if it succeeds with a \"stock\" build.",
    "created_at": "2011-12-15T02:51:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99567",
    "user": "jason"
}
```

Tonight, I'll try building again without setting any of those environment variables to see if it succeeds with a "stock" build.



---

archive/issue_comments_099568.json:
```json
{
    "body": "Replying to [comment:229 kcrisman]:\n> I'm going to try this with \n\n```\n> export MAKE=\"make -j2\"\n```\n\n> on the same platform and report back. \n\nInterestingly, Scipy and R are definitely (right now) building before Sage.  And they usually do not, for sure not Scipy, on my ancient older Mac.  \n\nScipy has successfully installed, as has matplotlib.  R takes forever but so far is fine.  Maybe it was \"just a race condition\"?",
    "created_at": "2011-12-15T02:56:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99568",
    "user": "kcrisman"
}
```

Replying to [comment:229 kcrisman]:
> I'm going to try this with 

```
> export MAKE="make -j2"
```

> on the same platform and report back. 

Interestingly, Scipy and R are definitely (right now) building before Sage.  And they usually do not, for sure not Scipy, on my ancient older Mac.  

Scipy has successfully installed, as has matplotlib.  R takes forever but so far is fine.  Maybe it was "just a race condition"?



---

archive/issue_comments_099569.json:
```json
{
    "body": "I bet the matplotlib error shows up for me because I define SAGE_MATPLOTLIB_GUI (so that matplotlib tries to build the GUI backends).",
    "created_at": "2011-12-15T03:02:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99569",
    "user": "jason"
}
```

I bet the matplotlib error shows up for me because I define SAGE_MATPLOTLIB_GUI (so that matplotlib tries to build the GUI backends).



---

archive/issue_comments_099570.json:
```json
{
    "body": "It is quite possibly something broken with the GUI from what I can see of your original log. scipy can build whenever after numpy independently of sage so I don't see a problem there.",
    "created_at": "2011-12-15T03:04:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99570",
    "user": "fbissey"
}
```

It is quite possibly something broken with the GUI from what I can see of your original log. scipy can build whenever after numpy independently of sage so I don't see a problem there.



---

archive/issue_comments_099571.json:
```json
{
    "body": "Yes I think matplotlib cannot find tk. We may want to look at this in depth on OS X.",
    "created_at": "2011-12-15T03:06:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99571",
    "user": "fbissey"
}
```

Yes I think matplotlib cannot find tk. We may want to look at this in depth on OS X.



---

archive/issue_comments_099572.json:
```json
{
    "body": "The matplotlib error is fixed upstream: https://github.com/matplotlib/matplotlib/issues/139",
    "created_at": "2011-12-15T03:12:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99572",
    "user": "jason"
}
```

The matplotlib error is fixed upstream: https://github.com/matplotlib/matplotlib/issues/139



---

archive/issue_comments_099573.json:
```json
{
    "body": "Very good, we may want to bump the spkg to 1.1.0 then. From my sage-on-gentoo experience there is just one minor doctest failure from matplotli-1.1.0\n\n```\nsage -t -long -force_lib \"devel/sage/sage/plot/colors.py\"   \n**********************************************************************\nFile \"/usr/share/sage/devel/sage/sage/plot/colors.py\", line 1241:\n    sage: len(maps.maps)\nExpected:\n    134\nGot:\n    138\n**********************************************************************\nFile \"/usr/share/sage/devel/sage/sage/plot/colors.py\", line 1285:\n    sage: len(maps)\nExpected:\n    134\nGot:\n    138\n**********************************************************************\n```\n\nFairly standard each time we bump matplotlib or almost.\n\nYou R package definitely broke the first time around. I am fairly sure this is a parallel make issue. I have seen at least one instance that I suspect is parallel make on Gentoo. Of course given that it stop because of\n\n```\nmake[6]: gcc: Resource temporarily unavailable\n```\n\nI think, we may have something else altogether. It should go into a separate ticket.",
    "created_at": "2011-12-15T03:22:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99573",
    "user": "fbissey"
}
```

Very good, we may want to bump the spkg to 1.1.0 then. From my sage-on-gentoo experience there is just one minor doctest failure from matplotli-1.1.0

```
sage -t -long -force_lib "devel/sage/sage/plot/colors.py"   
**********************************************************************
File "/usr/share/sage/devel/sage/sage/plot/colors.py", line 1241:
    sage: len(maps.maps)
Expected:
    134
Got:
    138
**********************************************************************
File "/usr/share/sage/devel/sage/sage/plot/colors.py", line 1285:
    sage: len(maps)
Expected:
    134
Got:
    138
**********************************************************************
```

Fairly standard each time we bump matplotlib or almost.

You R package definitely broke the first time around. I am fairly sure this is a parallel make issue. I have seen at least one instance that I suspect is parallel make on Gentoo. Of course given that it stop because of

```
make[6]: gcc: Resource temporarily unavailable
```

I think, we may have something else altogether. It should go into a separate ticket.



---

archive/issue_comments_099574.json:
```json
{
    "body": "Do you already have a 1.1.0 spkg?  I'm working on one right now, but you already have one...",
    "created_at": "2011-12-15T03:24:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99574",
    "user": "jason"
}
```

Do you already have a 1.1.0 spkg?  I'm working on one right now, but you already have one...



---

archive/issue_comments_099575.json:
```json
{
    "body": "> Scipy has successfully installed, as has matplotlib.  R takes forever but so far is fine.  Maybe it was \"just a race condition\"?\n\n*Everything* built before the Sage library except Gap and SageTeX.  No problems.  I say this shouldn't keep the Python upgrade out, or?",
    "created_at": "2011-12-15T03:29:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99575",
    "user": "kcrisman"
}
```

> Scipy has successfully installed, as has matplotlib.  R takes forever but so far is fine.  Maybe it was "just a race condition"?

*Everything* built before the Sage library except Gap and SageTeX.  No problems.  I say this shouldn't keep the Python upgrade out, or?



---

archive/issue_comments_099576.json:
```json
{
    "body": "Replying to [comment:238 jason]:\n> Do you already have a 1.1.0 spkg?  I'm working on one right now, but you already have one...\n\nI don't have one. I don't need one for sage-on-gentoo as I am using system packages. You go ahead and create a ticket to upgrade matplotlib. I say it is a show stopper because it would happen on other platforms. Hopefully we can review it quickly.",
    "created_at": "2011-12-15T03:31:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99576",
    "user": "fbissey"
}
```

Replying to [comment:238 jason]:
> Do you already have a 1.1.0 spkg?  I'm working on one right now, but you already have one...

I don't have one. I don't need one for sage-on-gentoo as I am using system packages. You go ahead and create a ticket to upgrade matplotlib. I say it is a show stopper because it would happen on other platforms. Hopefully we can review it quickly.



---

archive/issue_comments_099577.json:
```json
{
    "body": "Replying to [comment:240 fbissey]:\n> Replying to [comment:238 jason]:\n> > Do you already have a 1.1.0 spkg?  I'm working on one right now, but you already have one...\n> \n> I don't have one. I don't need one for sage-on-gentoo as I am using system packages. You go ahead and create a ticket to upgrade matplotlib. I say it is a show stopper because it would happen on other platforms. Hopefully we can review it quickly.\n\nWhat about just making a patch upgrade with [the 1.5-liner](https://github.com/matplotlib/matplotlib/commit/e4a34df93f6) rather than making a whole new package which would require even MORE testing?  Plus, then you don't have to worry about getting those four extra colormaps :)  Anyway, I feel this is easier and more reasonable just to get this in 5.0.alpha0 (or whatever release is next for such a big spkg change as this ticket).",
    "created_at": "2011-12-15T03:47:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99577",
    "user": "kcrisman"
}
```

Replying to [comment:240 fbissey]:
> Replying to [comment:238 jason]:
> > Do you already have a 1.1.0 spkg?  I'm working on one right now, but you already have one...
> 
> I don't have one. I don't need one for sage-on-gentoo as I am using system packages. You go ahead and create a ticket to upgrade matplotlib. I say it is a show stopper because it would happen on other platforms. Hopefully we can review it quickly.

What about just making a patch upgrade with [the 1.5-liner](https://github.com/matplotlib/matplotlib/commit/e4a34df93f6) rather than making a whole new package which would require even MORE testing?  Plus, then you don't have to worry about getting those four extra colormaps :)  Anyway, I feel this is easier and more reasonable just to get this in 5.0.alpha0 (or whatever release is next for such a big spkg change as this ticket).



---

archive/issue_comments_099578.json:
```json
{
    "body": "I have no objections to that. Faster is better in that case because we really want to land this quickly because every other moves of the tree makes me rewrite stuff. It start to be hard to manage.",
    "created_at": "2011-12-15T03:54:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99578",
    "user": "fbissey"
}
```

I have no objections to that. Faster is better in that case because we really want to land this quickly because every other moves of the tree makes me rewrite stuff. It start to be hard to manage.



---

archive/issue_comments_099579.json:
```json
{
    "body": "I added a link to a patched version of the current matplotlib spkg.  I also added the diff as an information-only patch above.  Independent from this fix, I've also made a matplotlib 1.1.0 spkg, which also fixes the problem, but may need more testing than this very slight change to the existing matplotlib spkg.",
    "created_at": "2011-12-15T06:24:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99579",
    "user": "jason"
}
```

I added a link to a patched version of the current matplotlib spkg.  I also added the diff as an information-only patch above.  Independent from this fix, I've also made a matplotlib 1.1.0 spkg, which also fixes the problem, but may need more testing than this very slight change to the existing matplotlib spkg.



---

archive/issue_comments_099580.json:
```json
{
    "body": "By the way, the matplotlib 1.1.0 spkg is at #11915, but the spkg here should be sufficient.",
    "created_at": "2011-12-15T06:49:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99580",
    "user": "jason"
}
```

By the way, the matplotlib 1.1.0 spkg is at #11915, but the spkg here should be sufficient.



---

archive/issue_comments_099581.json:
```json
{
    "body": "#12131 has been merged, I'll rebase the python spkg by next Monday hopefully.",
    "created_at": "2011-12-15T11:50:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99581",
    "user": "fbissey"
}
```

#12131 has been merged, I'll rebase the python spkg by next Monday hopefully.



---

archive/issue_comments_099582.json:
```json
{
    "body": "Using the new matplotlib-1.0.1.p1.spkg above, and my standard build environment variables:\n\n\n```\nexport SAGE_MATPLOTLIB_GUI=yes\nexport SAGE_PARALLEL_SPKG_BUILD=yes     \nexport MAKE=\"make -j6\"    \nexport SAGE_SPKG_INSTALL_DOCS=yes\n```\n\n\nEverything except R builds nicely.  R still has that message about resources not being available (something about fork).  I then changed MAKE to \"make -j2\" and restarted the make and everything finished just fine.  Again, on OSX 10.6.8 (4G of memory).\n\nThat's a bummer that make -j6 doesn't work.  Regular old 4.8.alpha4 built fine, so I don't think it's just the new R spkg.  I'll try building fresh one more time, but with MAKE=make -j4 just to check things out.",
    "created_at": "2011-12-15T13:36:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99582",
    "user": "jason"
}
```

Using the new matplotlib-1.0.1.p1.spkg above, and my standard build environment variables:


```
export SAGE_MATPLOTLIB_GUI=yes
export SAGE_PARALLEL_SPKG_BUILD=yes     
export MAKE="make -j6"    
export SAGE_SPKG_INSTALL_DOCS=yes
```


Everything except R builds nicely.  R still has that message about resources not being available (something about fork).  I then changed MAKE to "make -j2" and restarted the make and everything finished just fine.  Again, on OSX 10.6.8 (4G of memory).

That's a bummer that make -j6 doesn't work.  Regular old 4.8.alpha4 built fine, so I don't think it's just the new R spkg.  I'll try building fresh one more time, but with MAKE=make -j4 just to check things out.



---

archive/issue_comments_099583.json:
```json
{
    "body": "The matplotlib spkg at #11915 is ready for review (and depends on the #11976, also ready for review).  Instead of using the matplotlib-1.0.1.p1.spkg above, it would be preferable to review and merge #11976 and #11915.",
    "created_at": "2011-12-15T18:18:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99583",
    "user": "jason"
}
```

The matplotlib spkg at #11915 is ready for review (and depends on the #11976, also ready for review).  Instead of using the matplotlib-1.0.1.p1.spkg above, it would be preferable to review and merge #11976 and #11915.



---

archive/issue_comments_099584.json:
```json
{
    "body": "Okay, I started with 4.8.alpha4, added the new python spkg from this ticket, the new matplotlib spkg from #11915, applied all of the patches from this ticket, #11976, #11986, and #12124.  I have a tarball with all of these:\n\n[http://sage.math.washington.edu/home/palmieri/misc/9958/sage-4.8.alpha4-9958.tar](http://sage.math.washington.edu/home/palmieri/misc/9958/sage-4.8.alpha4-9958.tar)\n\nalong with an upgrade path:\n\n[http://sage.math.washington.edu/home/palmieri/misc/9958/sage-4.8.alpha4-9958/](http://sage.math.washington.edu/home/palmieri/misc/9958/sage-4.8.alpha4-9958/)\n\nfor testing.",
    "created_at": "2011-12-15T19:49:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99584",
    "user": "jhpalmieri"
}
```

Okay, I started with 4.8.alpha4, added the new python spkg from this ticket, the new matplotlib spkg from #11915, applied all of the patches from this ticket, #11976, #11986, and #12124.  I have a tarball with all of these:

[http://sage.math.washington.edu/home/palmieri/misc/9958/sage-4.8.alpha4-9958.tar](http://sage.math.washington.edu/home/palmieri/misc/9958/sage-4.8.alpha4-9958.tar)

along with an upgrade path:

[http://sage.math.washington.edu/home/palmieri/misc/9958/sage-4.8.alpha4-9958/](http://sage.math.washington.edu/home/palmieri/misc/9958/sage-4.8.alpha4-9958/)

for testing.



---

archive/issue_comments_099585.json:
```json
{
    "body": "Did you also apply the patch from #11915?",
    "created_at": "2011-12-15T21:39:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99585",
    "user": "jason"
}
```

Did you also apply the patch from #11915?



---

archive/issue_comments_099586.json:
```json
{
    "body": "No, looks like I missed that one.",
    "created_at": "2011-12-15T22:59:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99586",
    "user": "jhpalmieri"
}
```

No, looks like I missed that one.



---

archive/issue_comments_099587.json:
```json
{
    "body": "Okay, here are versions including the patch from #11915:\n\n- [http://sage.math.washington.edu/home/palmieri/misc/9958/sage-4.8.a4-9958.tar](http://sage.math.washington.edu/home/palmieri/misc/9958/sage-4.8.a4-9958.tar)\n- [http://sage.math.washington.edu/home/palmieri/misc/9958/sage-4.8.a4-9958/](http://sage.math.washington.edu/home/palmieri/misc/9958/sage-4.8.a4-9958/)",
    "created_at": "2011-12-16T00:50:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99587",
    "user": "jhpalmieri"
}
```

Okay, here are versions including the patch from #11915:

- [http://sage.math.washington.edu/home/palmieri/misc/9958/sage-4.8.a4-9958.tar](http://sage.math.washington.edu/home/palmieri/misc/9958/sage-4.8.a4-9958.tar)
- [http://sage.math.washington.edu/home/palmieri/misc/9958/sage-4.8.a4-9958/](http://sage.math.washington.edu/home/palmieri/misc/9958/sage-4.8.a4-9958/)



---

archive/issue_comments_099588.json:
```json
{
    "body": "I took jhpalmieri's original tarball, applied the patch from #11915 myself, built it with these settings:\n\n\n```\nSAGE_MATPLOTLIB_GUI=yes\nSAGE_PARALLEL_SPKG_BUILD=yes\nMAKE=make -j12\nSAGE_SPKG_INSTALL_DOCS=yes\n```\n\n\non Ubuntu 10.04.  Everything built fine, and make ptestlong passed all tests. Yeah!",
    "created_at": "2011-12-16T16:14:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99588",
    "user": "jason"
}
```

I took jhpalmieri's original tarball, applied the patch from #11915 myself, built it with these settings:


```
SAGE_MATPLOTLIB_GUI=yes
SAGE_PARALLEL_SPKG_BUILD=yes
MAKE=make -j12
SAGE_SPKG_INSTALL_DOCS=yes
```


on Ubuntu 10.04.  Everything built fine, and make ptestlong passed all tests. Yeah!



---

archive/issue_comments_099589.json:
```json
{
    "body": "What remains to be done here for positive review?",
    "created_at": "2011-12-20T02:33:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99589",
    "user": "kcrisman"
}
```

What remains to be done here for positive review?



---

archive/issue_comments_099590.json:
```json
{
    "body": "Replying to [comment:258 kcrisman]:\n> What remains to be done here for positive review?\n\nFirst I have to rebase the python spkg to #12131. Second there is a new matplotlib spkg currently merged in 4.8.alpha5 (unreleased) that needs review in #11915. Then someone has to look at the patches to make sure they are not completely stupid (long tiedous job).\n\nThen we can move this to a positive review. I was hoping to be able to to rebase the spkg on Sunday but it didn't happen. I am busy doing a bit of code for my paid work but once it is done. I'll go for it, that may be tomorrow in my time zone.",
    "created_at": "2011-12-20T02:43:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99590",
    "user": "fbissey"
}
```

Replying to [comment:258 kcrisman]:
> What remains to be done here for positive review?

First I have to rebase the python spkg to #12131. Second there is a new matplotlib spkg currently merged in 4.8.alpha5 (unreleased) that needs review in #11915. Then someone has to look at the patches to make sure they are not completely stupid (long tiedous job).

Then we can move this to a positive review. I was hoping to be able to to rebase the spkg on Sunday but it didn't happen. I am busy doing a bit of code for my paid work but once it is done. I'll go for it, that may be tomorrow in my time zone.



---

archive/issue_comments_099591.json:
```json
{
    "body": "python-2.7.2.p0 spkg rebased and available.",
    "created_at": "2011-12-20T21:28:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99591",
    "user": "fbissey"
}
```

python-2.7.2.p0 spkg rebased and available.



---

archive/issue_comments_099592.json:
```json
{
    "body": "#11986 also needs review. It looks like it may need to go at the same time as python 2.7 as my own testing with python 2.6 on linux amd64 was not positive but everything is smooth with python 2.7.",
    "created_at": "2011-12-20T22:16:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99592",
    "user": "fbissey"
}
```

#11986 also needs review. It looks like it may need to go at the same time as python 2.7 as my own testing with python 2.6 on linux amd64 was not positive but everything is smooth with python 2.7.



---

archive/issue_comments_099593.json:
```json
{
    "body": "For sage-4.8.alpha4 with tickets #9958 + #11986 + #12124 + #11976 + #11915 all tests pass on x86 and on amd64 there is one TIME OUT\n\n```\nsage -t -long  -force_lib devel/sage-matplotlib-1.1.0/sage/interfaces/ecm.py\n*** *** Error: TIMED OUT! PROCESS KILLED! *** ***\n\n         [1800.2 s]\n```\n\nThe test did pass when run individually. I'm sure this is due to running the tests in parallel. I've seen it before, not with this ticket, but with sage-on-gentoo builds.",
    "created_at": "2011-12-21T01:14:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99593",
    "user": "strogdon"
}
```

For sage-4.8.alpha4 with tickets #9958 + #11986 + #12124 + #11976 + #11915 all tests pass on x86 and on amd64 there is one TIME OUT

```
sage -t -long  -force_lib devel/sage-matplotlib-1.1.0/sage/interfaces/ecm.py
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***

         [1800.2 s]
```

The test did pass when run individually. I'm sure this is due to running the tests in parallel. I've seen it before, not with this ticket, but with sage-on-gentoo builds.



---

archive/issue_comments_099594.json:
```json
{
    "body": "Replying to [comment:262 strogdon]:\n> For sage-4.8.alpha4 with tickets #9958 + #11986 + #12124 + #11976 + #11915 all tests pass on x86 and on amd64 there is one TIME OUT\n> {{{\n> sage -t -long  -force_lib devel/sage-matplotlib-1.1.0/sage/interfaces/ecm.py\n> *** *** Error: TIMED OUT! PROCESS KILLED! *** ***\n> \n>          [1800.2 s]\n> }}}\n> The test did pass when run individually. I'm sure this is due to running the tests in parallel. I've seen it before, not with this ticket, but with sage-on-gentoo builds.\n\nI have seen it before too - in parallel tests as well. It seems that ecm can be a bad boy, not sure what to do about it but that would be outside of the scope of this ticket in my opinion.\n\nSteve, did you do any test of #11986 with python-2.6?",
    "created_at": "2011-12-21T01:26:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99594",
    "user": "fbissey"
}
```

Replying to [comment:262 strogdon]:
> For sage-4.8.alpha4 with tickets #9958 + #11986 + #12124 + #11976 + #11915 all tests pass on x86 and on amd64 there is one TIME OUT
> {{{
> sage -t -long  -force_lib devel/sage-matplotlib-1.1.0/sage/interfaces/ecm.py
> *** *** Error: TIMED OUT! PROCESS KILLED! *** ***
> 
>          [1800.2 s]
> }}}
> The test did pass when run individually. I'm sure this is due to running the tests in parallel. I've seen it before, not with this ticket, but with sage-on-gentoo builds.

I have seen it before too - in parallel tests as well. It seems that ecm can be a bad boy, not sure what to do about it but that would be outside of the scope of this ticket in my opinion.

Steve, did you do any test of #11986 with python-2.6?



---

archive/issue_comments_099595.json:
```json
{
    "body": "Replying to [comment:263 fbissey]:\n> Steve, did you do any test of #11986 with python-2.6?\nNo, I haven't done that with python-2.6. I will do it, but hopefully someone beats me to it.",
    "created_at": "2011-12-21T01:48:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99595",
    "user": "strogdon"
}
```

Replying to [comment:263 fbissey]:
> Steve, did you do any test of #11986 with python-2.6?
No, I haven't done that with python-2.6. I will do it, but hopefully someone beats me to it.



---

archive/issue_comments_099596.json:
```json
{
    "body": "Upgrading from sage-4.5 fails with:\n\n```\nTesting that Sage starts...\n[2012-01-03 13:47:34]\nTraceback (most recent call last):\n  File \"/mnt/usb1/scratch/jdemeyer/sage-4.5-python27/local/bin/sage-eval\", line 4, in <module>\n    from sage.all import *\n  File \"/mnt/usb1/scratch/jdemeyer/sage-4.5-python27/local/lib/python2.7/site-packages/sage/all.py\", line 75, in <module>\n    from sage.matrix.all     import *\n  File \"/mnt/usb1/scratch/jdemeyer/sage-4.5-python27/local/lib/python2.7/site-packages/sage/matrix/all.py\", line 1, in <module>\n    from matrix_space import MatrixSpace, is_MatrixSpace\n  File \"/mnt/usb1/scratch/jdemeyer/sage-4.5-python27/local/lib/python2.7/site-packages/sage/matrix/matrix_space.py\", line 37, in <module>\n    import matrix_modn_dense\n  File \"matrix_modn_dense.pyx\", line 1, in init sage.matrix.matrix_modn_dense (sage/matrix/matrix_modn_dense.c:15026)\nAttributeError: 'module' object has no attribute 'Matrix_dense'\nSage failed to start up.\nPlease email sage-devel (http://groups.google.com/group/sage-devel)\nexplaining the problem and send the log file\n  /mnt/usb1/scratch/jdemeyer/sage-4.5-python27/start.log\nDescribe your computer, operating system, etc.\n```\n\n\nAfter `sage -ba-force`, it works again.",
    "created_at": "2012-01-03T13:17:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99596",
    "user": "jdemeyer"
}
```

Upgrading from sage-4.5 fails with:

```
Testing that Sage starts...
[2012-01-03 13:47:34]
Traceback (most recent call last):
  File "/mnt/usb1/scratch/jdemeyer/sage-4.5-python27/local/bin/sage-eval", line 4, in <module>
    from sage.all import *
  File "/mnt/usb1/scratch/jdemeyer/sage-4.5-python27/local/lib/python2.7/site-packages/sage/all.py", line 75, in <module>
    from sage.matrix.all     import *
  File "/mnt/usb1/scratch/jdemeyer/sage-4.5-python27/local/lib/python2.7/site-packages/sage/matrix/all.py", line 1, in <module>
    from matrix_space import MatrixSpace, is_MatrixSpace
  File "/mnt/usb1/scratch/jdemeyer/sage-4.5-python27/local/lib/python2.7/site-packages/sage/matrix/matrix_space.py", line 37, in <module>
    import matrix_modn_dense
  File "matrix_modn_dense.pyx", line 1, in init sage.matrix.matrix_modn_dense (sage/matrix/matrix_modn_dense.c:15026)
AttributeError: 'module' object has no attribute 'Matrix_dense'
Sage failed to start up.
Please email sage-devel (http://groups.google.com/group/sage-devel)
explaining the problem and send the log file
  /mnt/usb1/scratch/jdemeyer/sage-4.5-python27/start.log
Describe your computer, operating system, etc.
```


After `sage -ba-force`, it works again.



---

archive/issue_comments_099597.json:
```json
{
    "body": "Replying to [comment:265 jdemeyer]:\n> Upgrading from sage-4.5 fails with:\n> {{{\n> Testing that Sage starts...\n> [2012-01-03 13:47:34]\n> Traceback (most recent call last):\n>   File \"/mnt/usb1/scratch/jdemeyer/sage-4.5-python27/local/bin/sage-eval\", line 4, in <module>\n>     from sage.all import *\n>   File \"/mnt/usb1/scratch/jdemeyer/sage-4.5-python27/local/lib/python2.7/site-packages/sage/all.py\", line 75, in <module>\n>     from sage.matrix.all     import *\n>   File \"/mnt/usb1/scratch/jdemeyer/sage-4.5-python27/local/lib/python2.7/site-packages/sage/matrix/all.py\", line 1, in <module>\n>     from matrix_space import MatrixSpace, is_MatrixSpace\n>   File \"/mnt/usb1/scratch/jdemeyer/sage-4.5-python27/local/lib/python2.7/site-packages/sage/matrix/matrix_space.py\", line 37, in <module>\n>     import matrix_modn_dense\n>   File \"matrix_modn_dense.pyx\", line 1, in init sage.matrix.matrix_modn_dense (sage/matrix/matrix_modn_dense.c:15026)\n> AttributeError: 'module' object has no attribute 'Matrix_dense'\n> Sage failed to start up.\n> Please email sage-devel (http://groups.google.com/group/sage-devel)\n> explaining the problem and send the log file\n>   /mnt/usb1/scratch/jdemeyer/sage-4.5-python27/start.log\n> Describe your computer, operating system, etc.\n> }}}\n> \n> After `sage -ba-force`, it works again.\n\nQuite weird. You would think those particular libraries would have been rebuilt already after the linbox upgrade at least. Shouldn't a complete rebuild of sage occur after a python upgrade? In any case that seems mild for upgrading from 4.5 which was released on June 2010 many versions away.",
    "created_at": "2012-01-04T01:35:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99597",
    "user": "fbissey"
}
```

Replying to [comment:265 jdemeyer]:
> Upgrading from sage-4.5 fails with:
> {{{
> Testing that Sage starts...
> [2012-01-03 13:47:34]
> Traceback (most recent call last):
>   File "/mnt/usb1/scratch/jdemeyer/sage-4.5-python27/local/bin/sage-eval", line 4, in <module>
>     from sage.all import *
>   File "/mnt/usb1/scratch/jdemeyer/sage-4.5-python27/local/lib/python2.7/site-packages/sage/all.py", line 75, in <module>
>     from sage.matrix.all     import *
>   File "/mnt/usb1/scratch/jdemeyer/sage-4.5-python27/local/lib/python2.7/site-packages/sage/matrix/all.py", line 1, in <module>
>     from matrix_space import MatrixSpace, is_MatrixSpace
>   File "/mnt/usb1/scratch/jdemeyer/sage-4.5-python27/local/lib/python2.7/site-packages/sage/matrix/matrix_space.py", line 37, in <module>
>     import matrix_modn_dense
>   File "matrix_modn_dense.pyx", line 1, in init sage.matrix.matrix_modn_dense (sage/matrix/matrix_modn_dense.c:15026)
> AttributeError: 'module' object has no attribute 'Matrix_dense'
> Sage failed to start up.
> Please email sage-devel (http://groups.google.com/group/sage-devel)
> explaining the problem and send the log file
>   /mnt/usb1/scratch/jdemeyer/sage-4.5-python27/start.log
> Describe your computer, operating system, etc.
> }}}
> 
> After `sage -ba-force`, it works again.

Quite weird. You would think those particular libraries would have been rebuilt already after the linbox upgrade at least. Shouldn't a complete rebuild of sage occur after a python upgrade? In any case that seems mild for upgrading from 4.5 which was released on June 2010 many versions away.



---

archive/issue_comments_099598.json:
```json
{
    "body": "Replying to [comment:266 fbissey]:\n> Shouldn't a complete rebuild of sage occur after a python upgrade?\nI guess it should.  Do you know how to make this happen?",
    "created_at": "2012-01-04T07:31:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99598",
    "user": "jdemeyer"
}
```

Replying to [comment:266 fbissey]:
> Shouldn't a complete rebuild of sage occur after a python upgrade?
I guess it should.  Do you know how to make this happen?



---

archive/issue_comments_099599.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-01-04T07:31:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99599",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_099600.json:
```json
{
    "body": "Attachment\n\nDiff for the Python spkg (without deleted files), for review only",
    "created_at": "2012-01-04T10:40:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99600",
    "user": "jdemeyer"
}
```

Attachment

Diff for the Python spkg (without deleted files), for review only



---

archive/issue_comments_099601.json:
```json
{
    "body": "Upgrading fixed by deleting\n\n```\n$SAGE_ROOT/devel/sage-*/build\n```\n\nwhen an old version of Python is detected.\n\nNew spkg: [http://boxen.math.washington.edu/home/jdemeyer/spkg/python-2.7.2.p1.spkg](http://boxen.math.washington.edu/home/jdemeyer/spkg/python-2.7.2.p1.spkg)",
    "created_at": "2012-01-04T19:06:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99601",
    "user": "jdemeyer"
}
```

Upgrading fixed by deleting

```
$SAGE_ROOT/devel/sage-*/build
```

when an old version of Python is detected.

New spkg: [http://boxen.math.washington.edu/home/jdemeyer/spkg/python-2.7.2.p1.spkg](http://boxen.math.washington.edu/home/jdemeyer/spkg/python-2.7.2.p1.spkg)



---

archive/issue_comments_099602.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-01-04T19:06:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99602",
    "user": "jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_099603.json:
```json
{
    "body": "Diff for the Python spkg 2.7.2.p0 -> 2.7.2.p1, for review only",
    "created_at": "2012-01-04T19:07:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99603",
    "user": "jdemeyer"
}
```

Diff for the Python spkg 2.7.2.p0 -> 2.7.2.p1, for review only



---

archive/issue_comments_099604.json:
```json
{
    "body": "Attachment\n\n**positive_review** to the spkg, modulo my changes in the 2.7.2.p1 package.",
    "created_at": "2012-01-04T19:08:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99604",
    "user": "jdemeyer"
}
```

Attachment

**positive_review** to the spkg, modulo my changes in the 2.7.2.p1 package.



---

archive/issue_comments_099605.json:
```json
{
    "body": "Looks good to me. I didn't notice I missed a patch in the stuff I removed. Anyway I'll be on low activity because my home computer has given up the ghost (writing from an old box cobbled together running puppy 4.00 from a _1_GB hard drive) and I am on leave.",
    "created_at": "2012-01-05T02:52:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99605",
    "user": "fbissey"
}
```

Looks good to me. I didn't notice I missed a patch in the stuff I removed. Anyway I'll be on low activity because my home computer has given up the ghost (writing from an old box cobbled together running puppy 4.00 from a _1_GB hard drive) and I am on leave.



---

archive/issue_comments_099606.json:
```json
{
    "body": "Attachment",
    "created_at": "2012-01-05T15:13:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99606",
    "user": "jdemeyer"
}
```

Attachment



---

archive/issue_comments_099607.json:
```json
{
    "body": "Attachment",
    "created_at": "2012-01-05T15:13:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99607",
    "user": "jdemeyer"
}
```

Attachment



---

archive/issue_comments_099608.json:
```json
{
    "body": "Attachment\n\nFolded all the patches into only four patches.",
    "created_at": "2012-01-05T15:15:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99608",
    "user": "jdemeyer"
}
```

Attachment

Folded all the patches into only four patches.



---

archive/issue_comments_099609.json:
```json
{
    "body": "Replying to [comment:272 fbissey]:\n> Looks good to me.\n\nMeaning \"positive review\"? :-)",
    "created_at": "2012-01-05T16:09:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99609",
    "user": "jdemeyer"
}
```

Replying to [comment:272 fbissey]:
> Looks good to me.

Meaning "positive review"? :-)



---

archive/issue_comments_099610.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-01-05T21:36:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99610",
    "user": "fbissey"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_099611.json:
```json
{
    "body": "Replying to [comment:274 jdemeyer]:\n> Replying to [comment:272 fbissey]:\n> > Looks good to me.\n> \n> Meaning \"positive review\"? :-)\nAbsolutely positive! Hopefully nothing will happen to make us break or add to those 4 megapatches.",
    "created_at": "2012-01-05T21:36:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99611",
    "user": "fbissey"
}
```

Replying to [comment:274 jdemeyer]:
> Replying to [comment:272 fbissey]:
> > Looks good to me.
> 
> Meaning "positive review"? :-)
Absolutely positive! Hopefully nothing will happen to make us break or add to those 4 megapatches.



---

archive/issue_comments_099612.json:
```json
{
    "body": "[attachment:9958_combinat.patch] is the only non-trivial change I guess, but has been discussed well in the comments on this ticket.  Potentially, the `trie_type_dict()` test might yield other results, but we can still change the test in that case.  Anyway, that method is nowhere called in the Sage library.",
    "created_at": "2012-01-05T22:09:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99612",
    "user": "jdemeyer"
}
```

[attachment:9958_combinat.patch] is the only non-trivial change I guess, but has been discussed well in the comments on this ticket.  Potentially, the `trie_type_dict()` test might yield other results, but we can still change the test in that case.  Anyway, that method is nowhere called in the Sage library.



---

archive/issue_comments_099613.json:
```json
{
    "body": "Replying to [comment:276 jdemeyer]:\n> [attachment:9958_combinat.patch] is the only non-trivial change I guess, but has been discussed well in the comments on this ticket.  Potentially, the `trie_type_dict()` test might yield other results, but we can still change the test in that case.  Anyway, that method is nowhere called in the Sage library.\n\nI didn't notice you had listed this particular patch. Why not use [attachment:trac_9958-suffix_trees-variations-sl.patch] from S\u00e9bastien Labb\u00e9 instead? It is more foolproof.",
    "created_at": "2012-01-05T22:18:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99613",
    "user": "fbissey"
}
```

Replying to [comment:276 jdemeyer]:
> [attachment:9958_combinat.patch] is the only non-trivial change I guess, but has been discussed well in the comments on this ticket.  Potentially, the `trie_type_dict()` test might yield other results, but we can still change the test in that case.  Anyway, that method is nowhere called in the Sage library.

I didn't notice you had listed this particular patch. Why not use [attachment:trac_9958-suffix_trees-variations-sl.patch] from Sébastien Labbé instead? It is more foolproof.



---

archive/issue_comments_099614.json:
```json
{
    "body": "I obviously meant to use S\u00e9bastien Labb\u00e9's patch for suffix_tree, we can still use the other patch for nfactor_enumerable_word.py, S\u00e9bastien think that patch is perfect which I count as a positive review of it.",
    "created_at": "2012-01-05T22:25:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99614",
    "user": "fbissey"
}
```

I obviously meant to use Sébastien Labbé's patch for suffix_tree, we can still use the other patch for nfactor_enumerable_word.py, Sébastien think that patch is perfect which I count as a positive review of it.



---

archive/issue_comments_099615.json:
```json
{
    "body": "Replying to [comment:277 fbissey]:\n> I didn't notice you had listed this particular patch. Why not use [attachment:trac_9958-suffix_trees-variations-sl.patch] from S\u00e9bastien Labb\u00e9 instead? It is more foolproof.\nI overlooked that patch, it was not in the list of patches to be applied.  I agree it is better.",
    "created_at": "2012-01-05T22:39:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99615",
    "user": "jdemeyer"
}
```

Replying to [comment:277 fbissey]:
> I didn't notice you had listed this particular patch. Why not use [attachment:trac_9958-suffix_trees-variations-sl.patch] from Sébastien Labbé instead? It is more foolproof.
I overlooked that patch, it was not in the list of patches to be applied.  I agree it is better.



---

archive/issue_comments_099616.json:
```json
{
    "body": "Attachment\n\nReplying to [comment:279 jdemeyer]:\n> Replying to [comment:277 fbissey]:\n> > I didn't notice you had listed this particular patch. Why not use [attachment:trac_9958-suffix_trees-variations-sl.patch] from S\u00e9bastien Labb\u00e9 instead? It is more foolproof.\n> I overlooked that patch, it was not in the list of patches to be applied.  I agree it is better.\n\nIt was [http://trac.sagemath.org/sage_trac/ticket/9958?action=diff&version=273](http://trac.sagemath.org/sage_trac/ticket/9958?action=diff&version=273) but never mind we have it now.",
    "created_at": "2012-01-05T22:45:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99616",
    "user": "fbissey"
}
```

Attachment

Replying to [comment:279 jdemeyer]:
> Replying to [comment:277 fbissey]:
> > I didn't notice you had listed this particular patch. Why not use [attachment:trac_9958-suffix_trees-variations-sl.patch] from Sébastien Labbé instead? It is more foolproof.
> I overlooked that patch, it was not in the list of patches to be applied.  I agree it is better.

It was [http://trac.sagemath.org/sage_trac/ticket/9958?action=diff&version=273](http://trac.sagemath.org/sage_trac/ticket/9958?action=diff&version=273) but never mind we have it now.



---

archive/issue_comments_099617.json:
```json
{
    "body": "Replying to [comment:280 fbissey]:\n> It was [http://trac.sagemath.org/sage_trac/ticket/9958?action=diff&version=273](http://trac.sagemath.org/sage_trac/ticket/9958?action=diff&version=273) but never mind we have it now.\nLook more carefully, it wasn't :-)",
    "created_at": "2012-01-05T22:49:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99617",
    "user": "jdemeyer"
}
```

Replying to [comment:280 fbissey]:
> It was [http://trac.sagemath.org/sage_trac/ticket/9958?action=diff&version=273](http://trac.sagemath.org/sage_trac/ticket/9958?action=diff&version=273) but never mind we have it now.
Look more carefully, it wasn't :-)



---

archive/issue_comments_099618.json:
```json
{
    "body": "You are right I put the wrong patch in the list actually I never updated the list to include the right one, complete oversight. It's good that we are getting this merged now before more confusion arise from the number of patches attached.",
    "created_at": "2012-01-05T23:33:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99618",
    "user": "fbissey"
}
```

You are right I put the wrong patch in the list actually I never updated the list to include the right one, complete oversight. It's good that we are getting this merged now before more confusion arise from the number of patches attached.



---

archive/issue_comments_099619.json:
```json
{
    "body": "Fran\u00e7ois and others: thank you for all of the work you did on this ticket.",
    "created_at": "2012-01-05T23:59:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99619",
    "user": "jhpalmieri"
}
```

François and others: thank you for all of the work you did on this ticket.



---

archive/issue_comments_099620.json:
```json
{
    "body": "Hi, \n\nI am removing my name from the authors list. For three lines of code I wrote, I don't feel as an author at all for such an important ticket. Being a reviewer of the small combinat part is enough and more appropriate.\n\nS\u00e9bastien",
    "created_at": "2012-01-09T03:51:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99620",
    "user": "slabbe"
}
```

Hi, 

I am removing my name from the authors list. For three lines of code I wrote, I don't feel as an author at all for such an important ticket. Being a reviewer of the small combinat part is enough and more appropriate.

Sébastien



---

archive/issue_comments_099621.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-01-15T21:55:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99621",
    "user": "jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_099622.json:
```json
{
    "body": "Just as FYI, though I doubt it matters since the patch still applies, I get\n\n```\npatching file Lib/distutils/command/sdist.py\nHunk #1 succeeded at 327 (offset 3 lines).\nHunk #2 succeeded at 342 (offset 3 lines).\n```\n\nbefore the other patches and configuration.",
    "created_at": "2012-01-19T01:40:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99622",
    "user": "kcrisman"
}
```

Just as FYI, though I doubt it matters since the patch still applies, I get

```
patching file Lib/distutils/command/sdist.py
Hunk #1 succeeded at 327 (offset 3 lines).
Hunk #2 succeeded at 342 (offset 3 lines).
```

before the other patches and configuration.



---

archive/issue_comments_099623.json:
```json
{
    "body": "Doesn't matter anymore indeed, we have it merged in 5.0.beta0 finally. I am personally moving to #11705 and #11334 unless something very bad happen.",
    "created_at": "2012-01-19T01:58:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99623",
    "user": "fbissey"
}
```

Doesn't matter anymore indeed, we have it merged in 5.0.beta0 finally. I am personally moving to #11705 and #11334 unless something very bad happen.



---

archive/issue_comments_099624.json:
```json
{
    "body": "Replying to [comment:286 kcrisman]:\n> Just as FYI, though I doubt it matters since the patch still applies, I get\n> {{{\n> patching file Lib/distutils/command/sdist.py\n> Hunk #1 succeeded at 327 (offset 3 lines).\n> Hunk #2 succeeded at 342 (offset 3 lines).\n> }}}\n\nNot a big deal.  The patch still applies perfectly.",
    "created_at": "2012-01-19T08:10:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9957",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9957#issuecomment-99624",
    "user": "jdemeyer"
}
```

Replying to [comment:286 kcrisman]:
> Just as FYI, though I doubt it matters since the patch still applies, I get
> {{{
> patching file Lib/distutils/command/sdist.py
> Hunk #1 succeeded at 327 (offset 3 lines).
> Hunk #2 succeeded at 342 (offset 3 lines).
> }}}

Not a big deal.  The patch still applies perfectly.
