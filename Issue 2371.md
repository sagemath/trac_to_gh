# Issue 2371: tut.tex failures for 2.10.3.rc0

archive/issues_002371.json:
```json
{
    "body": "Assignee: @wdjoyner\n\nExtracted from a recent sage -testall:\n\nTesting SAGE tutorial\n\nsage -t  tut.tex                                            \n\n\n```\n**********************************************************************\nFile \"tut.py\", line 2377:\n    : F.reduced_groebner_bases ()\nException raised:\n    Traceback (most recent call last):\n      File \"/home/wdj/wdj/sagefiles/sage-2.10.3.rc0/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_103[3]>\", line 1, in <module>\n        F.reduced_groebner_bases ()###line 2377:\n    : F.reduced_groebner_bases ()\n      File \"/home/wdj/wdj/sagefiles/sage-2.10.3.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.py\", line 272, in reduced_groebner_bases\n        G0 = self._gfan_reduced_groebner_bases()\n      File \"/home/wdj/wdj/sagefiles/sage-2.10.3.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.py\", line 230, in _gfan_reduced_groebner_bases\n        B = self.gfan()\n      File \"/home/wdj/wdj/sagefiles/sage-2.10.3.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.py\", line 310, in gfan\n        I = self._gfan_ideal()\n      File \"/home/wdj/wdj/sagefiles/sage-2.10.3.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.py\", line 214, in _gfan_ideal\n        J = to_gfan(self.__ideal)\n      File \"morphism.pyx\", line 116, in sage.categories.morphism.Morphism.__call__\n      File \"multi_polynomial_libsingular.pyx\", line 618, in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__\n      File \"multi_polynomial_libsingular.pyx\", line 525, in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__\n      File \"<string>\", line 1\n         Ideal (b**2 - a*c, c**2 - b*d, -b*c + a*d) of Multivariate Polynomial Ring in a, b, c, d over Rational Field\n                                                     ^\n     SyntaxError: invalid syntax\n**********************************************************************\nFile \"tut.py\", line 2386:\n    : F.fvector()\nException raised:\n    Traceback (most recent call last):\n      File \"/home/wdj/wdj/sagefiles/sage-2.10.3.rc0/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_103[4]>\", line 1, in <module>\n        F.fvector()###line 2386:\n    : F.fvector()\n      File \"/home/wdj/wdj/sagefiles/sage-2.10.3.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.py\", line 358, in fvector\n        f = self.gfan(cmd='fvector', I=self._gfan_reduced_groebner_bases().replace(' ',','))\n      File \"/home/wdj/wdj/sagefiles/sage-2.10.3.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.py\", line 230, in _gfan_reduced_groebner_bases\n        B = self.gfan()\n      File \"/home/wdj/wdj/sagefiles/sage-2.10.3.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.py\", line 310, in gfan\n        I = self._gfan_ideal()\n      File \"/home/wdj/wdj/sagefiles/sage-2.10.3.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.py\", line 214, in _gfan_ideal\n        J = to_gfan(self.__ideal)\n      File \"morphism.pyx\", line 116, in sage.categories.morphism.Morphism.__call__\n      File \"multi_polynomial_libsingular.pyx\", line 618, in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__\n      File \"multi_polynomial_libsingular.pyx\", line 525, in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__\n      File \"<string>\", line 1\n         Ideal (b**2 - a*c, c**2 - b*d, -b*c + a*d) of Multivariate Polynomial Ring in a, b, c, d over Rational Field\n                                                     ^\n     SyntaxError: invalid syntax\n**********************************************************************\nFile \"tut.py\", line 1453:\n    : eigvecs = g.eigenspaces()[0][1], g.eigenspaces()[1][1]; eigvecs\nExpected:\n    ([\n    (1, 5)\n    ], [\n    (1, 1)\n    ])\nGot:\n    (Vector space of degree 2 and dimension 1 over Finite Field of size 7\n    User basis matrix:\n    [1 5], Vector space of degree 2 and dimension 1 over Finite Field of size 7\n    User basis matrix:\n    [1 1])\n**********************************************************************\nFile \"tut.py\", line 1604:\n    : e.word_problem([b1,b2,b3,b4,b5],display=False)\nException raised:\n    Traceback (most recent call last):\n      File \"/home/wdj/wdj/sagefiles/sage-2.10.3.rc0/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_63[7]>\", line 1, in <module>\n        e.word_problem([b1,b2,b3,b4,b5],display=False)###line 1604:\n    : e.word_problem([b1,b2,b3,b4,b5],display=False)\n    TypeError: word_problem() got an unexpected keyword argument 'display'\n**********************************************************************\n3 items had failures:\n   2 of   5 in __main__.example_103\n   1 of   4 in __main__.example_57\n   1 of  16 in __main__.example_63\n***Test Failed*** 4 failures.\nFor whitespace errors, see the file .doctest_tut.tex\n         [22.2 s]\nexit code: 256\n\n----------------------------------------------------------------------\n```\n\nThe following tests failed:\n\n\n        sage -t  tut.tex\n\nTotal time for all tests: 22.2 seconds\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2371\n\n",
    "created_at": "2008-03-02T22:31:29Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "tut.tex failures for 2.10.3.rc0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2371",
    "user": "@wdjoyner"
}
```
Assignee: @wdjoyner

Extracted from a recent sage -testall:

Testing SAGE tutorial

sage -t  tut.tex                                            


```
**********************************************************************
File "tut.py", line 2377:
    : F.reduced_groebner_bases ()
Exception raised:
    Traceback (most recent call last):
      File "/home/wdj/wdj/sagefiles/sage-2.10.3.rc0/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_103[3]>", line 1, in <module>
        F.reduced_groebner_bases ()###line 2377:
    : F.reduced_groebner_bases ()
      File "/home/wdj/wdj/sagefiles/sage-2.10.3.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.py", line 272, in reduced_groebner_bases
        G0 = self._gfan_reduced_groebner_bases()
      File "/home/wdj/wdj/sagefiles/sage-2.10.3.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.py", line 230, in _gfan_reduced_groebner_bases
        B = self.gfan()
      File "/home/wdj/wdj/sagefiles/sage-2.10.3.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.py", line 310, in gfan
        I = self._gfan_ideal()
      File "/home/wdj/wdj/sagefiles/sage-2.10.3.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.py", line 214, in _gfan_ideal
        J = to_gfan(self.__ideal)
      File "morphism.pyx", line 116, in sage.categories.morphism.Morphism.__call__
      File "multi_polynomial_libsingular.pyx", line 618, in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__
      File "multi_polynomial_libsingular.pyx", line 525, in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__
      File "<string>", line 1
         Ideal (b**2 - a*c, c**2 - b*d, -b*c + a*d) of Multivariate Polynomial Ring in a, b, c, d over Rational Field
                                                     ^
     SyntaxError: invalid syntax
**********************************************************************
File "tut.py", line 2386:
    : F.fvector()
Exception raised:
    Traceback (most recent call last):
      File "/home/wdj/wdj/sagefiles/sage-2.10.3.rc0/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_103[4]>", line 1, in <module>
        F.fvector()###line 2386:
    : F.fvector()
      File "/home/wdj/wdj/sagefiles/sage-2.10.3.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.py", line 358, in fvector
        f = self.gfan(cmd='fvector', I=self._gfan_reduced_groebner_bases().replace(' ',','))
      File "/home/wdj/wdj/sagefiles/sage-2.10.3.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.py", line 230, in _gfan_reduced_groebner_bases
        B = self.gfan()
      File "/home/wdj/wdj/sagefiles/sage-2.10.3.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.py", line 310, in gfan
        I = self._gfan_ideal()
      File "/home/wdj/wdj/sagefiles/sage-2.10.3.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.py", line 214, in _gfan_ideal
        J = to_gfan(self.__ideal)
      File "morphism.pyx", line 116, in sage.categories.morphism.Morphism.__call__
      File "multi_polynomial_libsingular.pyx", line 618, in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__
      File "multi_polynomial_libsingular.pyx", line 525, in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__
      File "<string>", line 1
         Ideal (b**2 - a*c, c**2 - b*d, -b*c + a*d) of Multivariate Polynomial Ring in a, b, c, d over Rational Field
                                                     ^
     SyntaxError: invalid syntax
**********************************************************************
File "tut.py", line 1453:
    : eigvecs = g.eigenspaces()[0][1], g.eigenspaces()[1][1]; eigvecs
Expected:
    ([
    (1, 5)
    ], [
    (1, 1)
    ])
Got:
    (Vector space of degree 2 and dimension 1 over Finite Field of size 7
    User basis matrix:
    [1 5], Vector space of degree 2 and dimension 1 over Finite Field of size 7
    User basis matrix:
    [1 1])
**********************************************************************
File "tut.py", line 1604:
    : e.word_problem([b1,b2,b3,b4,b5],display=False)
Exception raised:
    Traceback (most recent call last):
      File "/home/wdj/wdj/sagefiles/sage-2.10.3.rc0/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_63[7]>", line 1, in <module>
        e.word_problem([b1,b2,b3,b4,b5],display=False)###line 1604:
    : e.word_problem([b1,b2,b3,b4,b5],display=False)
    TypeError: word_problem() got an unexpected keyword argument 'display'
**********************************************************************
3 items had failures:
   2 of   5 in __main__.example_103
   1 of   4 in __main__.example_57
   1 of  16 in __main__.example_63
***Test Failed*** 4 failures.
For whitespace errors, see the file .doctest_tut.tex
         [22.2 s]
exit code: 256

----------------------------------------------------------------------
```

The following tests failed:


        sage -t  tut.tex

Total time for all tests: 22.2 seconds


Issue created by migration from https://trac.sagemath.org/ticket/2371





---

archive/issue_comments_015997.json:
```json
{
    "body": "Changing priority from minor to blocker.",
    "created_at": "2008-03-02T22:36:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2371#issuecomment-15997",
    "user": "mabshoff"
}
```

Changing priority from minor to blocker.



---

archive/issue_comments_015998.json:
```json
{
    "body": "David, this is a *blocker* for the 2.10.3 release :)\n\nCheers,\n\nMichael",
    "created_at": "2008-03-02T22:36:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2371#issuecomment-15998",
    "user": "mabshoff"
}
```

David, this is a *blocker* for the 2.10.3 release :)

Cheers,

Michael



---

archive/issue_comments_015999.json:
```json
{
    "body": "Okay, it is a blocker, but some of the failures possibly are from patches\nnew to 2.10.3.rc0. Should I wait for 2.10.3.rc1 or try to fix it now?\n\nBTW, I would dearly love to include a new example based on the recent patches of\nSimon King. Would that be okay?",
    "created_at": "2008-03-02T22:46:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2371#issuecomment-15999",
    "user": "@wdjoyner"
}
```

Okay, it is a blocker, but some of the failures possibly are from patches
new to 2.10.3.rc0. Should I wait for 2.10.3.rc1 or try to fix it now?

BTW, I would dearly love to include a new example based on the recent patches of
Simon King. Would that be okay?



---

archive/issue_comments_016000.json:
```json
{
    "body": "I assume that there errors have not changed from rc0 to rc3?",
    "created_at": "2008-03-11T01:52:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2371#issuecomment-16000",
    "user": "@wdjoyner"
}
```

I assume that there errors have not changed from rc0 to rc3?



---

archive/issue_comments_016001.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-11T02:33:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2371#issuecomment-16001",
    "user": "@williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_016002.json:
```json
{
    "body": "Attachment [doc-2371.patch](tarball://root/attachments/some-uuid/ticket2371/doc-2371.patch) by @williamstein created at 2008-03-11 02:33:34",
    "created_at": "2008-03-11T02:33:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2371#issuecomment-16002",
    "user": "@williamstein"
}
```

Attachment [doc-2371.patch](tarball://root/attachments/some-uuid/ticket2371/doc-2371.patch) by @williamstein created at 2008-03-11 02:33:34



---

archive/issue_comments_016003.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc5",
    "created_at": "2008-03-11T02:37:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2371#issuecomment-16003",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.rc5
