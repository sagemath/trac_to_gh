# Issue 3970: MaximaElements should not coerce into SR.

archive/issues_003970.json:
```json
{
    "body": "Assignee: burcin\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3970\n\n",
    "created_at": "2008-08-27T22:48:14Z",
    "labels": [
        "calculus",
        "minor",
        "bug"
    ],
    "title": "MaximaElements should not coerce into SR.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3970",
    "user": "mhansen"
}
```
Assignee: burcin



Issue created by migration from https://trac.sagemath.org/ticket/3970





---

archive/issue_comments_028527.json:
```json
{
    "body": "After:\n\n\n```\nsage: f = maxima.function('x','sin(x)')\nsage: f+x\nsin(x)+x\nsage: x+f\nsin(x)+x\nsage: type(_)\n<class 'sage.interfaces.maxima.MaximaFunction'>\n```\n",
    "created_at": "2008-08-27T22:49:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3970",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3970#issuecomment-28527",
    "user": "mhansen"
}
```

After:


```
sage: f = maxima.function('x','sin(x)')
sage: f+x
sin(x)+x
sage: x+f
sin(x)+x
sage: type(_)
<class 'sage.interfaces.maxima.MaximaFunction'>
```




---

archive/issue_comments_028528.json:
```json
{
    "body": "Patch added which fixes the issue.  This depends on #132.",
    "created_at": "2008-08-27T22:51:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3970",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3970#issuecomment-28528",
    "user": "mhansen"
}
```

Patch added which fixes the issue.  This depends on #132.



---

archive/issue_comments_028529.json:
```json
{
    "body": "This patch actually breaks everything in calculus.py.  I must have ran the tests without having it actually applied.",
    "created_at": "2008-08-29T00:47:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3970",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3970#issuecomment-28529",
    "user": "mhansen"
}
```

This patch actually breaks everything in calculus.py.  I must have ran the tests without having it actually applied.



---

archive/issue_comments_028530.json:
```json
{
    "body": "What is the status of this now?  Apparently it still is a problem in 4.0:\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: f = maxima.function('x','sin(x)')\nsage: f + x  #correct\nsin(x)+x\nsage: x+f    #wrong\nsage0 + x\nsage: \n| Sage Version 4.0, Release Date: 2009-05-29                         |\n| Type notebook() for the GUI, and license() for information.        |\n```\n",
    "created_at": "2009-05-30T08:05:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3970",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3970#issuecomment-28530",
    "user": "jason"
}
```

What is the status of this now?  Apparently it still is a problem in 4.0:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: f = maxima.function('x','sin(x)')
sage: f + x  #correct
sin(x)+x
sage: x+f    #wrong
sage0 + x
sage: 
| Sage Version 4.0, Release Date: 2009-05-29                         |
| Type notebook() for the GUI, and license() for information.        |
```




---

archive/issue_comments_028531.json:
```json
{
    "body": "I get an error with sage -t -long sage/symbolic/ring.pyx. I am not sure that I understand the patch as it seems to apply for both maxima and pari. Is this by intention? \n\n\n```\nsage -t -long \"devel/sage-myver/sage/symbolic/ring.pyx\"\n**********************************************************************\nFile \"/home/adamwebb/local/sage/devel/sage-myver/sage/symbolic/ring.pyx\", line 97:\n    sage: SR.coerce(pari(2/5))\nException raised:\n    Traceback (most recent call last):\n      File \"/home/adamwebb/local/sage/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/adamwebb/local/sage/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/adamwebb/local/sage/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_7[3]>\", line 1, in <module>\n        SR.coerce(pari(Integer(2)/Integer(5)))###line 97:\n    sage: SR.coerce(pari(2/5))\n      File \"parent.pyx\", line 402, in sage.structure.parent.Parent.coerce (sage/structure/parent.c:4859)\n      File \"parent.pyx\", line 429, in sage.structure.parent.Parent.coerce (sage/structure/parent.c:4806)\n    TypeError: no canonical coercion from Interface to the PARI C library to Symbolic Ring\n**********************************************************************\n1 items had failures:\n   1 of  12 in __main__.example_7\n***Test Failed*** 1 failures.\n```\n\n\nif I put back the Pari stuff:\n\n```\nfrom sage.libs.pari.gen import PariInstance\n\nelif isinstance(R, (PariInstance)): \n    return True\n```\n\nThen everything works.\n\nCheers,\nAdam",
    "created_at": "2009-10-06T12:58:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3970",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3970#issuecomment-28531",
    "user": "awebb"
}
```

I get an error with sage -t -long sage/symbolic/ring.pyx. I am not sure that I understand the patch as it seems to apply for both maxima and pari. Is this by intention? 


```
sage -t -long "devel/sage-myver/sage/symbolic/ring.pyx"
**********************************************************************
File "/home/adamwebb/local/sage/devel/sage-myver/sage/symbolic/ring.pyx", line 97:
    sage: SR.coerce(pari(2/5))
Exception raised:
    Traceback (most recent call last):
      File "/home/adamwebb/local/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/adamwebb/local/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/adamwebb/local/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_7[3]>", line 1, in <module>
        SR.coerce(pari(Integer(2)/Integer(5)))###line 97:
    sage: SR.coerce(pari(2/5))
      File "parent.pyx", line 402, in sage.structure.parent.Parent.coerce (sage/structure/parent.c:4859)
      File "parent.pyx", line 429, in sage.structure.parent.Parent.coerce (sage/structure/parent.c:4806)
    TypeError: no canonical coercion from Interface to the PARI C library to Symbolic Ring
**********************************************************************
1 items had failures:
   1 of  12 in __main__.example_7
***Test Failed*** 1 failures.
```


if I put back the Pari stuff:

```
from sage.libs.pari.gen import PariInstance

elif isinstance(R, (PariInstance)): 
    return True
```

Then everything works.

Cheers,
Adam



---

archive/issue_comments_028532.json:
```json
{
    "body": "Attachment [trac_3970.patch](tarball://root/attachments/some-uuid/ticket3970/trac_3970.patch) by mhansen created at 2009-10-07 04:20:59\n\nI forgot to remove the pari doctest.  It should also be removed since these parents should not have coercions going in both directions.\n\nThis is taken care of in the new patch.",
    "created_at": "2009-10-07T04:20:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3970",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3970#issuecomment-28532",
    "user": "mhansen"
}
```

Attachment [trac_3970.patch](tarball://root/attachments/some-uuid/ticket3970/trac_3970.patch) by mhansen created at 2009-10-07 04:20:59

I forgot to remove the pari doctest.  It should also be removed since these parents should not have coercions going in both directions.

This is taken care of in the new patch.



---

archive/issue_comments_028533.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-07T08:25:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3970",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3970#issuecomment-28533",
    "user": "awebb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_028534.json:
```json
{
    "body": "In that case, everything looks good. A quick retest also passes. ~ Adam",
    "created_at": "2009-10-07T08:25:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3970",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3970#issuecomment-28534",
    "user": "awebb"
}
```

In that case, everything looks good. A quick retest also passes. ~ Adam



---

archive/issue_comments_028535.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T05:49:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3970",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3970#issuecomment-28535",
    "user": "mhansen"
}
```

Resolution: fixed
