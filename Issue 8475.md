# Issue 8475: Pickling of _python_object_alphabet is broken.

archive/issues_008475.json:
```json
{
    "body": "Assignee: hivert\n\nKeywords: pickling nested classes\n\nThanks to #7448 and #8452, on can trace unpicklable class throughout sage. Here is one:\n\n```\nsage: sage: W = Words()\nsage: sage: A = W._python_object_alphabet()\nsage: TestSuite(A).run(verbose=True)\nrunning ._test_pickling() . . . fail\nTraceback (most recent call last):\n  File \"/mnt/usb1/scratch/hivert/sage-4.3.4.alpha0-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/misc/sage_unittest.py\", line 268, in run\n    test_method(tester = tester)\n  File \"/mnt/usb1/scratch/hivert/sage-4.3.4.alpha0-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/misc/sage_unittest.py\", line 484, in _test_pickling\n    tester.assertEqual(loads(dumps(self._instance)), self._instance)\n  File \"sage_object.pyx\", line 792, in sage.structure.sage_object.dumps (sage/structure/sage_object.c:8367)\nPicklingError: Can't pickle <class 'sage.combinat.words.words._python_object_alphabet'>: attribute lookup sage.combinat.words.words._python_object_alphabet failed\n------------------------------------------------------------\nThe following tests failed: _test_pickling\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8475\n\n",
    "created_at": "2010-03-07T09:14:12Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "Pickling of _python_object_alphabet is broken.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8475",
    "user": "hivert"
}
```
Assignee: hivert

Keywords: pickling nested classes

Thanks to #7448 and #8452, on can trace unpicklable class throughout sage. Here is one:

```
sage: sage: W = Words()
sage: sage: A = W._python_object_alphabet()
sage: TestSuite(A).run(verbose=True)
running ._test_pickling() . . . fail
Traceback (most recent call last):
  File "/mnt/usb1/scratch/hivert/sage-4.3.4.alpha0-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/misc/sage_unittest.py", line 268, in run
    test_method(tester = tester)
  File "/mnt/usb1/scratch/hivert/sage-4.3.4.alpha0-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/misc/sage_unittest.py", line 484, in _test_pickling
    tester.assertEqual(loads(dumps(self._instance)), self._instance)
  File "sage_object.pyx", line 792, in sage.structure.sage_object.dumps (sage/structure/sage_object.c:8367)
PicklingError: Can't pickle <class 'sage.combinat.words.words._python_object_alphabet'>: attribute lookup sage.combinat.words.words._python_object_alphabet failed
------------------------------------------------------------
The following tests failed: _test_pickling
```


Issue created by migration from https://trac.sagemath.org/ticket/8475





---

archive/issue_comments_076379.json:
```json
{
    "body": "Again, this is the nested class problem. I uploaded a patch which fixes that.\nI also added UniqueRepresentation to _python_object_alphabet (there seems to\nbe only one), hence inheriting missing equality.\n\nShould be ready for review.",
    "created_at": "2010-03-07T09:37:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8475#issuecomment-76379",
    "user": "hivert"
}
```

Again, this is the nested class problem. I uploaded a patch which fixes that.
I also added UniqueRepresentation to _python_object_alphabet (there seems to
be only one), hence inheriting missing equality.

Should be ready for review.



---

archive/issue_comments_076380.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-07T09:37:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8475#issuecomment-76380",
    "user": "hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076381.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-09T09:33:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8475#issuecomment-76381",
    "user": "slabbe"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076382.json:
```json
{
    "body": "BEFORE:\n\n\n```\nsage: W = Words()\nsage: A = W.alphabet()\nsage: A\nPython objects\nsage: Z = loads(dumps(W))\nsage: B = Z.alphabet()\nsage: B\nPython objects\nsage: A is B\nTrue\nsage: W is Z\nFalse\nsage: W == Z\nTrue\nsage: loads(dumps(A))\nTraceback (most recent call last):\n...\nPicklingError: Can't pickle <class 'sage.combinat.words.words._python_object_alphabet'>: attribute lookup sage.combinat.words.words._python_object_alphabet failed\nsage: loads(dumps(B))\nTraceback (most recent call last):\n...\nPicklingError: Can't pickle <class 'sage.combinat.words.words._python_object_alphabet'>: attribute lookup sage.combinat.words.words._python_object_alphabet failed\n```\n\n\nAFTER with the patche applied:\n\n\n```\nsage: W = Words()\nsage: A = W.alphabet()\nsage: A\nPython objects\nsage: Z = loads(dumps(W))\nsage: B = Z.alphabet()\nsage: B\nPython objects\nsage: A is B\nTrue\nsage: W is Z\nFalse\nsage: W == Z\nTrue\nsage: loads(dumps(A))\nPython objects\nsage: loads(dumps(B))\nPython objects\n```\n\n\n\nHence, the problem described in this ticket is fixed by the patch. Moreover, all tests passed in the sage tree. Positive review.\n\nNote to the release manager : this patch commutes with the one at #8429.",
    "created_at": "2010-03-09T09:33:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8475#issuecomment-76382",
    "user": "slabbe"
}
```

BEFORE:


```
sage: W = Words()
sage: A = W.alphabet()
sage: A
Python objects
sage: Z = loads(dumps(W))
sage: B = Z.alphabet()
sage: B
Python objects
sage: A is B
True
sage: W is Z
False
sage: W == Z
True
sage: loads(dumps(A))
Traceback (most recent call last):
...
PicklingError: Can't pickle <class 'sage.combinat.words.words._python_object_alphabet'>: attribute lookup sage.combinat.words.words._python_object_alphabet failed
sage: loads(dumps(B))
Traceback (most recent call last):
...
PicklingError: Can't pickle <class 'sage.combinat.words.words._python_object_alphabet'>: attribute lookup sage.combinat.words.words._python_object_alphabet failed
```


AFTER with the patche applied:


```
sage: W = Words()
sage: A = W.alphabet()
sage: A
Python objects
sage: Z = loads(dumps(W))
sage: B = Z.alphabet()
sage: B
Python objects
sage: A is B
True
sage: W is Z
False
sage: W == Z
True
sage: loads(dumps(A))
Python objects
sage: loads(dumps(B))
Python objects
```



Hence, the problem described in this ticket is fixed by the patch. Moreover, all tests passed in the sage tree. Positive review.

Note to the release manager : this patch commutes with the one at #8429.



---

archive/issue_comments_076383.json:
```json
{
    "body": "In the \"TESTS:\" section, you should saying something like:\n\n```\nTESTS:\n\nTest that #8475 is fixed::\n\n    <put-your-tests-here>\n```\n\nThat way, you provide more context for why you are writing that test. Plus, it makes it easier to locate the relevant ticket number. I leave it up to you to modify the patch as appropriate.",
    "created_at": "2010-03-10T06:34:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8475#issuecomment-76383",
    "user": "mvngu"
}
```

In the "TESTS:" section, you should saying something like:

```
TESTS:

Test that #8475 is fixed::

    <put-your-tests-here>
```

That way, you provide more context for why you are writing that test. Plus, it makes it easier to locate the relevant ticket number. I leave it up to you to modify the patch as appropriate.



---

archive/issue_comments_076384.json:
```json
{
    "body": "Attachment [trac_8475-alphabet_pickling_fix-fh.patch](tarball://root/attachments/some-uuid/ticket8475/trac_8475-alphabet_pickling_fix-fh.patch) by hivert created at 2010-03-10 08:09:39\n\nReplying to [comment:3 mvngu]:\n> In the \"TESTS:\" section, you should saying something like:\n> {{{\n> TESTS:\n> \n> Test that #8475 is fixed::\n> \n>     <put-your-tests-here>\n> }}}\n> That way, you provide more context for why you are writing that test. Plus, it makes it easier to locate the relevant ticket number. I leave it up to you to modify the patch as appropriate.\n\nDone. Please re-review.",
    "created_at": "2010-03-10T08:09:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8475#issuecomment-76384",
    "user": "hivert"
}
```

Attachment [trac_8475-alphabet_pickling_fix-fh.patch](tarball://root/attachments/some-uuid/ticket8475/trac_8475-alphabet_pickling_fix-fh.patch) by hivert created at 2010-03-10 08:09:39

Replying to [comment:3 mvngu]:
> In the "TESTS:" section, you should saying something like:
> {{{
> TESTS:
> 
> Test that #8475 is fixed::
> 
>     <put-your-tests-here>
> }}}
> That way, you provide more context for why you are writing that test. Plus, it makes it easier to locate the relevant ticket number. I leave it up to you to modify the patch as appropriate.

Done. Please re-review.



---

archive/issue_comments_076385.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-03-10T08:09:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8475#issuecomment-76385",
    "user": "hivert"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_076386.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-10T08:09:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8475#issuecomment-76386",
    "user": "hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076387.json:
```json
{
    "body": "Minh's suggestion is done. To me the patch is good for a positive review.",
    "created_at": "2010-03-10T10:33:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8475#issuecomment-76387",
    "user": "slabbe"
}
```

Minh's suggestion is done. To me the patch is good for a positive review.



---

archive/issue_comments_076388.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-10T20:21:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8475#issuecomment-76388",
    "user": "mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076389.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-11T04:47:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8475#issuecomment-76389",
    "user": "mvngu"
}
```

Resolution: fixed
